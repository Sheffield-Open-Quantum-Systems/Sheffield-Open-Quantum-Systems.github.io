# Code Citations

## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ccbuzzell/ccbuzzell.github.io/blob/6adb776e10f6fdeb0e81413826c98aad9dba9e0a/amend/data-story-02.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ccbuzzell/ccbuzzell.github.io/blob/6adb776e10f6fdeb0e81413826c98aad9dba9e0a/amend/data-story-02.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ccbuzzell/ccbuzzell.github.io/blob/6adb776e10f6fdeb0e81413826c98aad9dba9e0a/amend/data-story-02.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ccbuzzell/ccbuzzell.github.io/blob/6adb776e10f6fdeb0e81413826c98aad9dba9e0a/amend/data-story-02.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">
```


## License: unknown
https://github.com/ccbuzzell/ccbuzzell.github.io/blob/6adb776e10f6fdeb0e81413826c98aad9dba9e0a/amend/data-story-02.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/ccbuzzell/ccbuzzell.github.io/blob/6adb776e10f6fdeb0e81413826c98aad9dba9e0a/amend/data-story-02.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/kiyo-masui/kiyo-masui.github.io/blob/e785ef8b4e502153d55b3c9844c1084c2a5b6009/about.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/mlangill/mlangill.github.com/blob/b9d74e873652691aa3083dab5807ae6fda382447/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/ging/ging.github.com/blob/8f67cb74537cc38f8d1353ea50a9ee086d5a04fe/v2/index.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/Anitya/stavam/blob/a346f6eb35770152bd009bede409142eef97a367/WebContent/projects.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/ccbuzzell/ccbuzzell.github.io/blob/6adb776e10f6fdeb0e81413826c98aad9dba9e0a/amend/data-story-02.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```


## License: unknown
https://github.com/hugo-ribeiro/hugo-ribeiro.github.io/blob/896b26d51e86a23c82cf1405e387947064aba831/contact.html

```
I'm in read-only mode so I can't create files directly, but here's everything you need. Create these files:

---

### 1. `scripts/fetch_papers.py`

```python
"""
Fetch publications from Semantic Scholar API and write to data/papers.json.
"""

import json
import time
import urllib.request
import urllib.error
from pathlib import Path

# === CONFIGURATION ===
# Find your ID: search your name on semanticscholar.org
# Profile URL is https://www.semanticscholar.org/author/NAME/AUTHOR_ID
AUTHOR_IDS = [
    "2055661938",  # Jake Iles-Smith — update this if incorrect
]

MAX_PAPERS_PER_AUTHOR = 50
PAPER_FIELDS = "title,authors,year,venue,externalIds,url,publicationDate"
BASE_URL = "https://api.semanticscholar.org/graph/v1"


def fetch_author_papers(author_id):
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
    return {
        "title": paper.get("title") or "Untitled",
        "authors": authors,
        "year": paper.get("year"),
        "venue": paper.get("venue") or "",
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
```

---

### 2. `.github/workflows/update-papers.yml`

```yaml
name: Update Papers

on:
  schedule:
    - cron: '0 6 * * 1'  # Every Monday at 6:00 UTC
  workflow_dispatch:       # Manual trigger

permissions:
  contents: write

jobs:
  fetch-papers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Fetch papers from Semantic Scholar
        run: python scripts/fetch_papers.py

      - name: Commit updated papers
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/papers.json
          git diff --staged --quiet || git commit -m "Update papers from Semantic Scholar"
          git push
```

---

### 3. `data/papers.json` (initial placeholder)

```json
[]
```

---

### 4. Replace `papers.html` with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Papers – SOQS</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <header>
    <div class="container">
      <div class="logo">
        <h1><span>SOQS</span> | Sheffield Open Quantum Systems</h1>
      </div>
      <nav>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="research.html">Research</a></li>
          <li><a href="team.html">Team</a></li>
          <li><a href="funding.html">Funding</a></li>
          <li><a href="papers.html" class="active">Papers
```

