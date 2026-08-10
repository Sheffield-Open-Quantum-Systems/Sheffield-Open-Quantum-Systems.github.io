"""
Fetch publications from Semantic Scholar API and write to data/papers.json.

Usage:
    python scripts/fetch_papers.py

Configure AUTHOR_IDS below with Semantic Scholar author IDs for group members.
Find your ID at: https://www.semanticscholar.org/ (search your name, copy the ID from the URL)
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# To find your ID: search your name on semanticscholar.org, your profile URL will be
# https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "1393697239",  # Jake Iles-Smith
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate,journal"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
    """Fetch papers for a given Semantic Scholar author ID."""
    url = (
        f"{BASE_URL}/author/{author_id}/papers"
        f"?fields={PAPER_FIELDS}&limit={MAX_PAPERS_PER_AUTHOR}"
    )
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "SOQS-Website-PaperFetcher/1.0")
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
            return data.get("data", [])
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print(f"  Error for author {author_id}: {e}")
        return []


def build_paper_entry(paper):
    """Convert a Semantic Scholar paper object into our display format."""
    external_ids = paper.get("externalIds") or {}
    links = {}
    if external_ids.get("DOI"):
        links["doi"] = f"https://doi.org/{external_ids['DOI']}"
    if external_ids.get("ArXiv"):
        links["arxiv"] = f"https://arxiv.org/abs/{external_ids['ArXiv']}"
    if paper.get("url"):
        links["semantic_scholar"] = paper["url"]

    authors = ", ".join(
        a.get("name", "Unknown") for a in (paper.get("authors") or [])
    )

    # Build full reference string
    journal_info = paper.get("journal") or {}
    journal_name = journal_info.get("name", "") or paper.get("venue", "") or ""
    volume = (journal_info.get("volume") or "").strip()
    pages = (journal_info.get("pages") or "").strip()

    reference_parts = []
    if journal_name:
        reference_parts.append(journal_name)
    if volume:
        reference_parts.append(volume)
    if pages:
        reference_parts.append(pages)

    reference = ", ".join(reference_parts)
    year = paper.get("year")
    if reference and year:
        reference += f" ({year})"
    elif year:
        reference = f"({year})"

    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": year,
        "venue": journal_name,
        "volume": volume,
        "pages": pages,
        "reference": reference,
        "date": paper.get("publicationDate") or "",
        "links": links,
    }


def main():
    all_papers = {}
    for author_id in AUTHOR_IDS:
        print(f"Fetching papers for author ID: {author_id}")
        papers = fetch_author_papers(author_id)
        print(f"  Found {len(papers)} papers")
        for paper in papers:
            paper_id = paper.get("paperId")
            if paper_id and paper_id not in all_papers:
                entry = build_paper_entry(paper)
                if entry["title"] != "Untitled":
                    all_papers[paper_id] = entry
        time.sleep(1)

    # Sort by date (newest first)
    paper_list = sorted(
        all_papers.values(),
        key=lambda p: (p.get("date") or f"{p.get('year') or 0}-01-01"),
        reverse=True,
    )

    output_dir = Path(__file__).parent.parent / "data"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "papers.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(paper_list, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {len(paper_list)} papers to {output_file}")


if __name__ == "__main__":
    main()
