#!/usr/bin/env python3
"""
normalize_docs.py

Copy all Markdown files from a nested directory tree into a *flat*
destination folder, renaming each file so its relative path components are
joined with underscores. Additionally:

- Extracts metadata (id, title, source, url, commit_sha, lang) for RAG system
- Strips Jekyll/Hugo front-matter but preserves code fences
- Normalizes whitespace and Unicode for better chunking and deduplication

Example
-------
data/raw/docs/guide/getting-started/intro.md
    ⟶ data/normalized/docs/guide_getting-started_intro.md

Basic usage
-----------
python normalize_docs.py --src data/raw/docs --dst data/normalized/docs

Flags
-----
--dry-run       Show what would be copied without doing it.
--overwrite     Overwrite if a filename collision happens. Otherwise, numeric
                suffixes are appended to keep both copies.
--manifest-file Path to save JSONL manifest with metadata for each document.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

def slugify_path(rel_path: Path) -> str:
    """Join path parts with underscores to make a flat filename."""
    return "_".join(rel_path.parts)

def strip_front_matter(content: str) -> tuple[str, dict]:
    """
    Strip Jekyll/Hugo front-matter from markdown content.
    Returns (content_without_frontmatter, frontmatter_dict).
    """
    frontmatter = {}
    
    # Check if content starts with front-matter (--- at the beginning)
    if content.startswith('---\n') or content.startswith('---\r\n'):
        # Find the closing ---
        lines = content.split('\n')
        end_idx = None
        
        for i, line in enumerate(lines[1:], 1):
            if line.strip() == '---':
                end_idx = i
                break
        
        if end_idx is not None:
            # Extract front-matter
            fm_lines = lines[1:end_idx]
            fm_content = '\n'.join(fm_lines)
            
            # Simple YAML parsing for common key: value pairs
            for line in fm_lines:
                if ':' in line and not line.strip().startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"\'')
                    if value and value.lower() not in ('null', '~'):
                        frontmatter[key] = value
            
            # Return content without front-matter
            remaining_lines = lines[end_idx + 1:]
            content = '\n'.join(remaining_lines)
    
    return content, frontmatter

def normalize_markdown(content: str) -> str:
    """Normalize markdown content for consistency."""
    # Unicode normalization
    content = unicodedata.normalize("NFKC", content)
    
    # Normalize line endings
    content = re.sub(r"\r\n?", "\n", content)
    
    # Collapse excessive whitespace (≤ 2 blank lines)
    content = re.sub(r"\n{3,}", "\n\n", content)
    
    # Normalize spaces within lines (but preserve code block formatting)
    lines = content.split('\n')
    normalized_lines = []
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            normalized_lines.append(line)
        elif in_code_block:
            # Preserve exact formatting in code blocks
            normalized_lines.append(line)
        else:
            # Normalize whitespace in regular text
            normalized_lines.append(re.sub(r'\s+', ' ', line).strip())
    
    return '\n'.join(normalized_lines)

def generate_metadata(md_file: Path, rel_path: Path, content: str, frontmatter: dict) -> dict:
    """Generate metadata for a documentation file."""
    # Extract title from front-matter or content
    title = frontmatter.get('title')
    if not title:
        # Try to extract from first H1 heading
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else rel_path.stem.replace("-", " ").replace("_", " ").title()
    
    # Generate content hash for ID
    content_id = hashlib.sha1(content.encode('utf-8')).hexdigest()[:12]
    
    # Generate commit_sha from normalized content (for version tracking)
    commit_sha = hashlib.sha1(content.encode('utf-8')).hexdigest()
    
    # Create documentation URL (assuming Telerik docs structure)
    url_path = str(rel_path.with_suffix('')).replace('\\', '/')
    doc_url = f"https://docs.telerik.com/blazor-ui/{url_path}"
    
    return {
        "id": f"docs_{content_id}",
        "title": title,
        "source": "telerik-docs", 
        "url": doc_url,
        "file_path": f"data/normalized/docs/{slugify_path(rel_path)}",
        "content_type": "documentation",
        "lang": "en",
        "commit_sha": commit_sha
    }

def copy_markdowns(src: Path, dst: Path, manifest_file: Path = None, dry_run=False, overwrite=False):
    if not src.exists():
        sys.exit(f"Source directory '{src}' does not exist.")
    dst.mkdir(parents=True, exist_ok=True)
    
    # Initialize manifest entries list
    manifest_entries = []
    
    # Ensure manifest directory exists
    if manifest_file:
        manifest_file.parent.mkdir(parents=True, exist_ok=True)

    for md in src.rglob("*.md"):
        rel = md.relative_to(src)
        new_name = slugify_path(rel)
        target = dst / new_name

        # avoid collisions
        if target.exists() and not overwrite:
            stem, ext = target.stem, target.suffix
            counter = 1
            while (dst / f"{stem}_{counter}{ext}").exists():
                counter += 1
            target = dst / f"{stem}_{counter}{ext}"
            # Update the filename in rel_path for metadata
            new_rel = Path(f"{rel.stem}_{counter}{rel.suffix}")
        else:
            new_rel = rel

        if dry_run:
            print(f"COPY {md} -> {target}")
        else:
            # Read and process the markdown file
            try:
                with open(md, 'r', encoding='utf-8') as f:
                    original_content = f.read()
                
                # Strip front-matter
                content_no_fm, frontmatter = strip_front_matter(original_content)
                
                # Normalize content
                normalized_content = normalize_markdown(content_no_fm)
                
                # Generate metadata
                if manifest_file:
                    metadata = generate_metadata(md, new_rel, normalized_content, frontmatter)
                    manifest_entries.append(metadata)
                
                # Write processed content
                with open(target, 'w', encoding='utf-8') as f:
                    f.write(normalized_content)
                
                print(f"Processed {md} -> {target}")
                if manifest_file:
                    print(f"  Generated metadata (ID: {metadata['id']})")
                    
            except Exception as e:
                print(f"Error processing {md}: {e}")
                continue
    
    # Write manifest file
    if manifest_file and manifest_entries and not dry_run:
        with open(manifest_file, 'w', encoding='utf-8') as f:
            for entry in manifest_entries:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')
        print(f"Generated manifest with {len(manifest_entries)} entries: {manifest_file}")
    
    return len(manifest_entries) if manifest_entries else 0

def main(argv=None):
    p = argparse.ArgumentParser(description="Flatten nested Markdown files and generate metadata.")
    p.add_argument("--src", default="data/raw/docs", help="Source root directory.")
    p.add_argument("--dst", default="data/normalized/docs", help="Destination directory.")
    p.add_argument("--manifest-file", default="data/manifests/docs.jsonl", help="Path to save manifest file")
    p.add_argument("--dry-run", action="store_true", help="Show operations without copying.")
    p.add_argument("--overwrite", action="store_true", help="Overwrite on filename collision.")
    args = p.parse_args(argv)

    src_path = Path(args.src).expanduser()
    dst_path = Path(args.dst).expanduser()
    manifest_path = Path(args.manifest_file).expanduser() if args.manifest_file else None

    count = copy_markdowns(src_path, dst_path, manifest_path, 
                          dry_run=args.dry_run, overwrite=args.overwrite)
    
    if not args.dry_run:
        print(f"Normalization complete! Processed {count} files.")

if __name__ == "__main__":
    main()
