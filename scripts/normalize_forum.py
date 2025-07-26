#!/usr/bin/env python3
"""
normalize_forum.py
Convert scraped HTML forum files to Markdown and generate metadata for RAG systems.

Usage
-----
pip install beautifulsoup4 markdownify tqdm
python scripts/normalize_forum.py \
       --html-dir data/raw/forum \
       --md-dir   data/normalized/forum \
       --verbose
"""
from __future__ import annotations
import argparse, os, re, sys, hashlib, json, unicodedata
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm

###############################################################################
# Helpers
###############################################################################
def ensure_dir(p: Path) -> None:
    """Ensure directory exists."""
    p.mkdir(exist_ok=True, parents=True)

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

def generate_metadata(html_file: Path, md_content: str, html_content: str) -> dict:
    """Generate metadata for a forum post."""
    # Extract title from markdown content
    title_match = re.search(r'^# (.+)$', md_content, re.MULTILINE)
    title = title_match.group(1) if title_match else html_file.stem.replace("-", " ").title()
    
    # Generate content hash for ID
    content_id = hashlib.sha1(md_content.encode('utf-8')).hexdigest()[:12]
    
    # Generate commit_sha from original HTML content (for version tracking)
    commit_sha = hashlib.sha1(html_content.encode('utf-8')).hexdigest()
    
    # Create forum URL (corrected format)
    forum_url = f"https://www.telerik.com/forums/{html_file.stem}"
    
    return {
        "id": f"forum_{content_id}",
        "title": title,
        "source": "telerik-forum",
        "url": forum_url,
        "file_path": f"data/normalized/forum/{html_file.stem}.md",
        "content_type": "forum_post",
        "lang": "en",
        "commit_sha": commit_sha
    }

###############################################################################
# HTML to Markdown conversion
###############################################################################
def html_to_md(html: str) -> str:
    """Extract and convert forum thread content to markdown with proper structure."""
    soup = BeautifulSoup(html, "lxml")
    
    # Extract the thread title
    title = soup.find('h1')
    title_text = title.get_text(strip=True) if title else "Forum Thread"
    
    # Start building the markdown content
    markdown_parts = [f"# {title_text}\n"]
    
    # Find all message content elements (questions and answers)
    msg_contents = soup.select('.msg-content')
    
    # Find all comment elements (responses to questions and answers)
    comment_contents = soup.select('.comment-text')
    
    # Combine and sort all content by their position in the document
    all_contents = []
    
    # Add main messages
    for msg in msg_contents:
        all_contents.append({
            'element': msg,
            'type': 'message',
            'position': get_element_position(msg)
        })
    
    # Add comments
    for comment in comment_contents:
        all_contents.append({
            'element': comment,
            'type': 'comment', 
            'position': get_element_position(comment)
        })
    
    # Sort by position to maintain chronological order
    all_contents.sort(key=lambda x: x['position'])
    
    question_posted = False
    answer_count = 0
    
    for item in all_contents:
        content_elem = item['element']
        content_type = item['type']
        
        # Get the message text - preserve spacing between elements
        msg_text = ""
        for elem in content_elem.descendants:
            if elem.name is None:  # Text node
                text = elem.strip()
                if text:
                    # Add space before text if needed (unless it's the first text or starts with punctuation)
                    if msg_text and not msg_text.endswith(' ') and not text.startswith(('.', ',', '!', '?', ';', ':')):
                        msg_text += " "
                    msg_text += text
            elif elem.name in ['br', 'div', 'p']:
                # Add space/newline for block elements
                if msg_text and not msg_text.endswith((' ', '\n')):
                    msg_text += " "
        
        msg_text = msg_text.strip()
        
        # Filter out promotional content
        promo_phrases = [
            "Love the Telerik and Kendo UI products",
            "Invite a fellow developer to become a Progress customer",
            "$50 Amazon gift voucher",
            "referral-program",
            "Stay tuned by visiting our",
            "public roadmap",
            "feedback portal",
            "getting started resources",
            "Progress Telerik",
            "Virtual Classroom, the free self-paced technical training"
        ]
        
        # Remove promotional text
        for phrase in promo_phrases:
            if phrase in msg_text:
                # Find where the promotional content starts and cut it off
                promo_start = msg_text.find(phrase)
                if promo_start > 0:
                    msg_text = msg_text[:promo_start].strip()
                break
        
        # Skip if message is too short (likely not real content)
        if len(msg_text) < 10:
            continue
        
        # Clean and format the message text
        msg_text = clean_and_format_text(msg_text)
            
        # Find author information
        author_info = ""
        current = content_elem
        
        # Go up hierarchy to find author
        for level in range(10):
            current = current.parent
            if current:
                # Look for author elements
                author_elem = current.select_one('[class*="username"], [class*="author"], [class*="by"]')
                if author_elem:
                    author_text = author_elem.get_text(strip=True)
                    
                    # Extract author info based on content type
                    if content_type == 'comment':
                        # Comments use "commented on" format
                        if "commented on" in author_text:
                            parts = author_text.split("commented on")
                            if len(parts) >= 2:
                                author_name = parts[0].strip()
                                date_part = parts[1].strip()
                                # Clean up author name
                                author_clean = clean_author_name(author_name)
                                author_info = f"**{author_clean}** commented on {date_part.split(',')[0]}"
                    else:
                        # Messages use "asked on" or "answered on" format
                        if "asked on" in author_text or "answered on" in author_text:
                            parts = author_text.split("asked on") if "asked on" in author_text else author_text.split("answered on")
                            if len(parts) >= 2:
                                author_name = parts[0].strip()
                                date_part = parts[1].strip()
                                # Clean up author name
                                author_clean = clean_author_name(author_name)
                                action = "asked" if "asked on" in author_text else "answered"
                                author_info = f"**{author_clean}** {action} on {date_part.split(',')[0]}"
                    break
            else:
                break
        
        # Determine the message type and header level
        if content_type == 'message':
            # Check if this is a question or answer
            current = content_elem
            is_question = False
            
            for level in range(10):
                current = current.parent
                if current:
                    classes = current.get('class', [])
                    class_str = ' '.join(classes) if classes else ''
                    
                    if 'thread-question' in class_str:
                        is_question = True
                        break
                    elif 'answer-container' in class_str:
                        break
                else:
                    break
            
            if is_question and not question_posted:
                header = "## Question"
                question_posted = True
            elif not is_question:
                if answer_count == 0:
                    answer_count += 1
                    header = "## Answer"
                else:
                    header = "### Response"
            else:
                header = "## Message"
                
        else:  # content_type == 'comment'
            # Comments are always responses (H3)
            header = "### Response"
        
        # Add the message to markdown
        message_md = f"\n{header}\n\n"
        if author_info:
            message_md += f"{author_info}\n\n"
        message_md += f"{msg_text}\n"
        
        markdown_parts.append(message_md)
    
    # If no content found, fallback to original method
    if len(all_contents) == 0:
        # Look for any content in the main areas
        main_content = soup.select('main, .main-content, .page-content')
        if main_content:
            for main in main_content:
                # Remove navigation and unwanted elements
                for unwanted in main.select('nav, header, footer, .navbar, .top-nav, .breadcrumb, .menu, script, style'):
                    unwanted.decompose()
                content_text = main.get_text(strip=True)
                if content_text:
                    content_text = clean_and_format_text(content_text)
                    markdown_parts.append(f"\n## Content\n\n{content_text}\n")
    
    # Consolidate adjacent code blocks before returning
    final_markdown = "\n".join(markdown_parts)
    return consolidate_code_blocks(final_markdown)

def consolidate_code_blocks(markdown_content: str) -> str:
    """Post-process markdown to consolidate adjacent code blocks of the same language."""
    import re
    
    # Pattern to match code blocks
    code_block_pattern = re.compile(r'^```(\w+)\n(.*?)\n```\s*$', re.MULTILINE | re.DOTALL)
    
    lines = markdown_content.split('\n')
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts a code block
        if line.startswith('```') and not line.endswith('```'):
            language = line[3:].strip()
            code_lines = []
            i += 1
            
            # Collect code lines until we hit the closing ```
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i])
                i += 1
            
            # Skip the closing ```
            if i < len(lines):
                i += 1
            
            # Look ahead for adjacent code blocks of the same language
            while i < len(lines):
                # Skip empty lines
                while i < len(lines) and lines[i].strip() == '':
                    i += 1
                
                # Check if next non-empty line starts another code block of same language
                if (i < len(lines) and 
                    lines[i].startswith('```') and 
                    lines[i][3:].strip() == language):
                    
                    i += 1  # Skip opening ```
                    
                    # Collect more code lines
                    while i < len(lines) and not lines[i].startswith('```'):
                        code_lines.append(lines[i])
                        i += 1
                    
                    # Skip closing ```
                    if i < len(lines):
                        i += 1
                else:
                    break
            
            # Add the consolidated code block
            result_lines.append(f'```{language}')
            result_lines.extend(code_lines)
            result_lines.append('```')
            
        else:
            result_lines.append(line)
            i += 1
    
    return '\n'.join(result_lines)

def clean_author_name(author_name: str) -> str:
    """Clean author name by removing achievement badges and junk text."""
    # Remove common junk patterns
    junk_patterns = [
        r"Top achievements[^a-zA-Z]*",
        r"Telerik team[^a-zA-Z]*",
        r"Rank\s+\d+[^a-zA-Z]*",
        r"(Iron|Bronze|Silver|Gold|Platinum)[^a-zA-Z]*",
        r"Level\s+\d+[^a-zA-Z]*"
    ]
    
    cleaned = author_name
    for pattern in junk_patterns:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)
    
    # Handle concatenated usernames like "khashayarVeterankhashayar"
    # Look for patterns where someone's name is repeated or has status words
    status_words = ['veteran', 'expert', 'pro', 'admin', 'moderator', 'developer']
    for status in status_words:
        # Remove status words from usernames
        pattern = rf'{status}'
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
    
    # Handle specific case like "khashayarVeterankhashayar" -> extract first part
    if len(cleaned) > 6:
        # Look for a repeated pattern where the name appears twice with something in between
        for i in range(3, len(cleaned) // 2 + 1):
            first_part = cleaned[:i]
            # Check if this name appears again later in the string
            rest_of_string = cleaned[i:]
            if first_part.lower() in rest_of_string.lower():
                # Found repetition, use the first part
                cleaned = first_part
                break
    
    # Remove duplicated names (e.g., "RobRob" -> "Rob")
    # Split by common separators and check for duplicates
    words = cleaned.split()
    if len(words) >= 2:
        # Check if the name is repeated (like "RobRob" or "Rob Rob")
        if words[0].lower() == words[1].lower():
            cleaned = words[0]
        # Check if it's the same name with different cases
        elif words[0].lower() == words[1].lower().rstrip('s'):  # Handle cases like "Rob Robs"
            cleaned = words[0]
    
    # Handle cases where the name is concatenated (like "RobRob")
    if len(cleaned) > 6:  # Only process if name is reasonably long
        # Check if the first half equals the second half
        mid = len(cleaned) // 2
        if cleaned[:mid].lower() == cleaned[mid:].lower():
            cleaned = cleaned[:mid]
    
    return cleaned.strip()

def clean_and_format_text(text: str) -> str:
    """Clean and format text content for better markdown output."""
    import re
    
    # Basic cleanup only - preserve original layout
    # Just normalize excessive whitespace but preserve line structure
    text = re.sub(r'[ \t]+', ' ', text)  # Normalize spaces and tabs to single spaces
    text = re.sub(r'\n{3,}', '\n\n', text)  # Limit to max 2 consecutive newlines
    
    # Fix component name spacing issues (common Telerik component names)
    component_fixes = [
        (r'\bCombo Box\b', 'ComboBox'),
        (r'\bTab Strip\b', 'TabStrip'),
        (r'\bGrid Layout\b', 'GridLayout'),
        (r'\bTile Layout\b', 'TileLayout'),
        (r'\bDate Picker\b', 'DatePicker'),
        (r'\bDate Input\b', 'DateInput'),
        (r'\bTime Picker\b', 'TimePicker'),
        (r'\bAllow Custom\b', 'AllowCustom'),
        (r'\bFilter Operator\b', 'FilterOperator'),
        (r'\bString Filter Operator\b', 'StringFilterOperator'),
        (r'\bText Field\b', 'TextField'),
        (r'\bValue Field\b', 'ValueField'),
        (r'\bItems Field\b', 'ItemsField'),
        (r'\bUrl Field\b', 'UrlField'),
        (r'\bData Source\b', 'DataSource'),
        (r'\bOn Change\b', 'OnChange'),
        (r'\bOn Click\b', 'OnClick'),
        (r'\bOn Read\b', 'OnRead'),
        (r'\bEdit Context\b', 'EditContext'),
        (r'\bForm Update Event Args\b', 'FormUpdateEventArgs'),
        (r'\bValidation Event\b', 'ValidationEvent'),
        (r'\bDebounce Delay\b', 'DebounceDelay'),
        (r'\bRow Span\b', 'RowSpan'),
        (r'\bCol Span\b', 'ColSpan')
    ]
    
    for pattern, replacement in component_fixes:
        text = re.sub(pattern, replacement, text)
    
    # Fix HTML/XML tag spacing issues
    # Remove spaces around = in HTML attributes: < tag attr = "value" > -> <tag attr="value">
    text = re.sub(r'<\s+', '<', text)  # < tag -> <tag
    text = re.sub(r'\s+>', '>', text)  # tag > -> tag>
    text = re.sub(r'<\s*/\s*', '</', text)  # < / tag -> </tag
    text = re.sub(r'\s*=\s*', '=', text)  # attr = "value" -> attr="value"
    
    # Fix spaces around @ symbols: @ bind -> @bind
    text = re.sub(r'@\s+', '@', text)
    
    # Check for numbered code lines pattern (01. 02. etc.)
    # Only handle very obvious numbered code lines pattern from HTML scraping
    numbered_lines_pattern = r'^(\d{2}\.\s*)'
    lines = text.split('\n')
    
    # Check if this looks like numbered code from HTML scraping (multiple consecutive numbered lines)
    numbered_line_count = sum(1 for line in lines if re.match(numbered_lines_pattern, line.strip()))
    
    if numbered_line_count >= 3 and numbered_line_count >= len(lines) * 0.5:
        # This looks like numbered code from HTML scraping - clean it up
        cleaned_lines = []
        for line in lines:
            cleaned_line = re.sub(numbered_lines_pattern, '', line).strip()
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
        
        cleaned_text = '\n'.join(cleaned_lines)
        
        # Simple language detection for numbered code
        if re.search(r'@[a-zA-Z]|@\(|@{|\.razor|@bind|@onclick', cleaned_text):
            language = "razor"
        elif re.search(r'<[^>]+>', cleaned_text) and not re.search(r'(public|private|protected|namespace|class)', cleaned_text):
            language = "html"
        elif re.search(r'\b(var|new|if|for|while|return|using|await|async|public|private|protected|class|namespace)\b', cleaned_text):
            language = "csharp"
        else:
            language = "text"
        
        formatted_code = format_code_segment(cleaned_text)
        return f"\n\n```{language}\n{formatted_code}\n```\n"
    
    # Very minimal text processing - preserve original formatting
    # Only format URLs as markdown links
    text = re.sub(r'(https?://[^\s]+)', r'[\1](\1)', text)
    
    return text.strip()

def format_code_segment(code: str) -> str:
    """Format a code segment for better readability."""
    # Add line breaks after common patterns
    code = re.sub(r'(\>)(\s*)(\<)', r'\1\n\3', code)  # Between XML/HTML tags
    code = re.sub(r'(\{)(\s*)', r'\1\n    ', code)    # After opening braces
    code = re.sub(r'(\s*)(\})', r'\n\2', code)        # Before closing braces
    code = re.sub(r'(;)(\s*)([a-zA-Z])', r'\1\n\3', code)  # After semicolons
    
    # Clean up excessive whitespace
    lines = [line.strip() for line in code.split('\n') if line.strip()]
    return '\n'.join(lines)

def get_element_position(element):
    """Get the position of an element in the document for sorting."""
    position = 0
    for sibling in element.parent.parent.find_all_previous():
        position += 1
    return position

def convert_html_file(html_file: Path, md_dir: Path, manifest_entries: list, verbose: bool = False) -> None:
    """Convert a single HTML file to Markdown and generate metadata."""
    try:
        # Read HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert to Markdown
        md_content = html_to_md(html_content)
        
        # Normalize the markdown content
        md_content = normalize_markdown(md_content)
        
        # Generate metadata
        metadata = generate_metadata(html_file, md_content, html_content)
        
        # Add to manifest (without content - content stays in the .md file)
        manifest_entries.append(metadata)
        
        # Write Markdown file
        md_file = md_dir / f"{html_file.stem}.md"
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        if verbose:
            print(f"Converted {html_file.name} -> {md_file.name} (ID: {metadata['id']})")
            
    except Exception as e:
        print(f"Error converting {html_file}: {e}")

###############################################################################
# CLI
###############################################################################
def main(argv=None):
    p = argparse.ArgumentParser(description="Convert scraped forum HTML files to Markdown")
    p.add_argument("--html-dir", default="data/raw/forum", help="Directory containing HTML files")
    p.add_argument("--md-dir",   default="data/normalized/forum", help="Directory to save Markdown files")
    p.add_argument("--manifest-file", default="data/manifests/forum.jsonl", help="Path to save manifest file")
    p.add_argument("--pattern",  default="*.html", help="File pattern to match (default: *.html)")
    p.add_argument("--single-file", type=str, help="Convert only a specific file (filename without extension)")
    p.add_argument("--limit", type=int, help="Limit the number of files to process (useful for testing)")
    p.add_argument("--force", action="store_true", help="Overwrite existing Markdown files")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args(argv)

    html_dir = Path(args.html_dir)
    md_dir = Path(args.md_dir)
    manifest_file = Path(args.manifest_file)
    
    if not html_dir.exists():
        print(f"HTML directory {html_dir} does not exist")
        return 1
    
    ensure_dir(md_dir)
    ensure_dir(manifest_file.parent)
    
    # Initialize manifest entries list
    manifest_entries = []
    
    # Handle single file conversion
    if args.single_file:
        html_file = html_dir / f"{args.single_file}.html"
        if not html_file.exists():
            print(f"File {html_file} does not exist")
            return 1
        
        md_file = md_dir / f"{args.single_file}.md"
        if md_file.exists() and not args.force:
            print(f"Markdown file {md_file} already exists. Use --force to overwrite.")
            return 1
        
        print(f"Converting single file: {html_file.name}")
        convert_html_file(html_file, md_dir, manifest_entries, verbose=True)
        
        # Write manifest for single file
        with open(manifest_file, 'w', encoding='utf-8') as f:
            for entry in manifest_entries:
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')
        
        print(f"Generated manifest with {len(manifest_entries)} entry")
        return 0
    
    # Get all HTML files
    html_files = list(html_dir.glob(args.pattern))
    if not html_files:
        print(f"No HTML files found in {html_dir} matching pattern {args.pattern}")
        return 1
    
    # Filter out files that already have corresponding Markdown files (unless --force)
    if not args.force:
        files_to_convert = []
        for html_file in html_files:
            md_file = md_dir / f"{html_file.stem}.md"
            if not md_file.exists():
                files_to_convert.append(html_file)
            elif args.verbose:
                print(f"Skipping {html_file.name} (MD file exists)")
        html_files = files_to_convert
    
    if not html_files:
        print("No files to convert (all have existing Markdown files). Use --force to overwrite.")
        return 0
    
    # Apply limit if specified
    if args.limit:
        html_files = html_files[:args.limit]
        print(f"Limited to first {len(html_files)} files")
    
    print(f"Converting {len(html_files)} HTML files to Markdown...")
    
    # Convert files with progress bar and batch writing
    batch_size = 50  # Write manifest every 50 files
    
    for i, html_file in enumerate(tqdm(html_files, desc="Converting", disable=not sys.stdout.isatty())):
        convert_html_file(html_file, md_dir, manifest_entries, verbose=args.verbose)
        
        # Write manifest every batch_size files (or at the end)
        if (i + 1) % batch_size == 0 or i == len(html_files) - 1:
            with open(manifest_file, 'w', encoding='utf-8') as f:
                for entry in manifest_entries:
                    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
            
            if args.verbose:
                print(f"Saved manifest with {len(manifest_entries)} entries (batch {(i + 1) // batch_size + 1})")
    
    # Final manifest write (redundant but safe)
    with open(manifest_file, 'w', encoding='utf-8') as f:
        for entry in manifest_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    
    print(f"Conversion complete! Markdown files saved to {md_dir}")
    print(f"Generated manifest with {len(manifest_entries)} entries: {manifest_file}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
