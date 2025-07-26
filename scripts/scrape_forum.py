#!/usr/bin/env python3
"""
scrape_forum.py
Incremental crawler for https://www.telerik.com/forums/blazor - HTML only

Usage
-----
pip install requests beautifulsoup4 tqdm
python scripts/scrape_forum.py \
       --html-dir data/raw/forum \
       --delay    1 \
       --verbose
"""
from __future__ import annotations
import argparse, os, re, sys, time, json
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlencode

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

BASE = "https://www.telerik.com"
FORUM_ROOT = f"{BASE}/forums/blazor"
LISTING_QS  = {"page": 1}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (+https://github.com/your-handle/blazor-scraper)"
}

THREAD_RE = re.compile(r"^/forums/(?P<slug>[^/?#]+)$")     # /forums/thread-slug
PAGE_RE   = re.compile(r"[?&]page=(\d+)")

# Category pages to exclude (these are forum sections, not individual threads)
EXCLUDED_CATEGORIES = {
    'blazor', 'ui-for-blazor', 'aspnet-core', 'aspnet-mvc', 'aspnet-ajax',
    'winforms', 'wpf', 'reporting', 'test-studio', 'mobile', 'web', 'desktop'
}

###############################################################################
# Helpers
###############################################################################
def norm_slug(s: str) -> str:
    """Turn a thread slug into a safe filename stem."""
    return re.sub(r"[^\w\-]", "_", s)

def ensure_dir(p: Path) -> None:
    """Ensure directory exists."""
    p.mkdir(exist_ok=True, parents=True)

def fetch(url: str, sess: requests.Session, delay: float = 1.0, verbose: bool = False) -> requests.Response:
    """Fetch a URL with delay and headers."""
    if verbose:
        print(f"GET {url}")
    resp = sess.get(url, headers=HEADERS)
    resp.raise_for_status()
    time.sleep(delay)
    return resp

###############################################################################
# Main scraping logic
###############################################################################
def listing_iter(start_page: int = 1):
    """Generate listing page URLs."""
    page = start_page
    while True:
        qs = LISTING_QS.copy()
        qs["page"] = page
        url = f"{FORUM_ROOT}?" + urlencode(qs)
        yield url
        page += 1

def extract_threads(listing_html: str) -> list[str]:
    """Extract thread URLs from a listing page."""
    soup = BeautifulSoup(listing_html, "lxml")
    threads = []
    for a in soup.select('a[href]'):
        href = a.get('href', '')
        m = THREAD_RE.match(href)
        if m:
            slug = m.group('slug')
            # Skip known category pages
            if slug.lower() not in EXCLUDED_CATEGORIES:
                # Additional heuristics: real threads usually have longer, more descriptive slugs
                if len(slug) > 6 and ('-' in slug or len(slug) > 15):
                    threads.append(f"{BASE}/forums/{slug}")
    return threads

def crawl_thread(thread_url: str, html_dir: Path, 
                 sess: requests.Session, delay: float, 
                 verbose: bool = False) -> None:
    """Crawl a single thread and save HTML."""
    parsed = urlparse(thread_url)
    slug = parsed.path.split('/')[-1]
    safe_slug = norm_slug(slug)
    
    # Handle filename collisions by adding a counter
    html_file = html_dir / f"{safe_slug}.html"
    counter = 1
    original_safe_slug = safe_slug
    
    while html_file.exists():
        # Check if the existing file contains the same URL to avoid re-downloading
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                existing_content = f.read()
                # Check if this is the same thread by looking for the URL in the content
                if thread_url in existing_content or slug in existing_content:
                    if verbose:
                        print(f"Skipping {thread_url} (already exists)")
                    return
        except:
            pass  # If we can't read the file, continue with collision handling
        
        # File exists but contains different content, handle collision
        safe_slug = f"{original_safe_slug}_{counter:02d}"
        html_file = html_dir / f"{safe_slug}.html"
        counter += 1
        
        # Prevent infinite loop
        if counter > 99:
            print(f"Warning: Too many filename collisions for {thread_url}, using {safe_slug}")
            break
    
    try:
        resp = fetch(thread_url, sess, delay, verbose)
        
        # Save HTML
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(resp.text)
        
    except Exception as e:
        print(f"Error crawling {thread_url}: {e}")

###############################################################################
# CLI
###############################################################################
def main(argv=None):
    p = argparse.ArgumentParser(description="Incremental Telerik Blazor forum scraper - HTML only")
    p.add_argument("--html-dir", default="data/raw/forum/html")
    p.add_argument("--delay",    type=float, default=1.0, help="seconds between HTTP requests")
    p.add_argument("--max-threads", type=int, default=None, help="stop after N threads")
    p.add_argument("--max-pages",   type=int, default=None, help="stop after N listing pages")
    p.add_argument("--start-page",  type=int, default=1, help="listing page number to start from (default: 1)")
    p.add_argument("--rescrape", type=str, help="re-scrape specific file by slug (e.g., 'thread-slug')")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args(argv)

    html_dir = Path(args.html_dir)
    ensure_dir(html_dir)

    sess = requests.Session()
    
    # Handle single file re-scraping
    if args.rescrape:
        slug = args.rescrape
        thread_url = f"{BASE}/forums/{slug}"
        print(f"Re-scraping single thread: {thread_url}")
        crawl_thread(thread_url, html_dir, sess, args.delay, verbose=True)
        sess.close()
        return

    crawled = 0
    listing_bar = tqdm(disable= not sys.stdout.isatty(),
                       unit="list_page", desc="Listing pages",
                       total=args.max_pages)
    try:
        for lp_i, list_url in enumerate(listing_iter(start_page=args.start_page), start=args.start_page):
            if args.max_pages and lp_i > (args.start_page + args.max_pages - 1):
                break
            listing_resp = fetch(list_url, sess, args.delay, args.verbose)
            threads = extract_threads(listing_resp.text)
            if not threads:
                listing_bar.write(f"No threads found @ page {lp_i}; assuming end.")
                break
            thread_bar = tqdm(threads, unit="thread",
                              desc=f"Threads p{lp_i}",
                              leave=False,
                              disable= not sys.stdout.isatty())
            for t_url in thread_bar:
                crawl_thread(t_url, html_dir, sess, args.delay, verbose=args.verbose)
                crawled += 1
                if args.max_threads and crawled >= args.max_threads:
                    raise KeyboardInterrupt
            listing_bar.update(1)
    except KeyboardInterrupt:
        listing_bar.write("Interrupted. Saving progress and exiting.")
    finally:
        listing_bar.close()
        sess.close()

if __name__ == "__main__":
    main()
