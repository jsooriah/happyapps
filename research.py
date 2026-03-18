#!/usr/bin/env python3
"""
research.py — generate a "Voices from the Field" section for a blog post using Lenny's dataset.

Usage:
    python research.py path/to/your/post/index.md           # dry run — preview only
    python research.py path/to/your/post/index.md --write   # append section to the article
"""

import os
import sys
import json
from pathlib import Path

def load_env():
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

def load_dataset(dataset_dir: Path) -> list[dict]:
    index_path = dataset_dir / "index.json"
    if not index_path.exists():
        print(f"Error: index.json not found in {dataset_dir}")
        sys.exit(1)

    index = json.loads(index_path.read_text())
    items = []

    for entry in index.get("podcasts", []) + index.get("newsletters", []):
        file_path = dataset_dir / entry["filename"]
        if file_path.exists():
            content = file_path.read_text()
            # Trim very long transcripts to first 8000 chars to stay within limits
            items.append({
                "title": entry["title"],
                "type": "podcast" if "podcasts" in entry["filename"] else "newsletter",
                "date": entry.get("date", ""),
                "guest": entry.get("guest", ""),
                "description": entry.get("description", ""),
                "content": content[:8000],
            })

    return items

def prefilter(article: str, dataset: list[dict], top_n: int = 8) -> list[dict]:
    """Score each dataset item by keyword overlap with the article and return top_n."""
    import re
    # Extract meaningful words from article (4+ chars, ignore markdown/frontmatter)
    words = set(re.findall(r'\b[a-zA-Z]{4,}\b', article.lower()))
    stopwords = {'that', 'this', 'with', 'from', 'they', 'have', 'what', 'when',
                 'their', 'more', 'will', 'been', 'than', 'into', 'each', 'also',
                 'about', 'which', 'there', 'would', 'rather', 'where', 'these',
                 'those', 'while', 'after', 'before', 'through', 'product', 'customer'}
    keywords = words - stopwords

    scored = []
    for item in dataset:
        text = (item['title'] + ' ' + item['description'] + ' ' + item['content']).lower()
        score = sum(1 for kw in keywords if kw in text)
        scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scored[:top_n]]

def build_prompt(article: str, dataset: list[dict]) -> str:
    relevant = prefilter(article, dataset)
    dataset_text = ""
    for i, item in enumerate(relevant, 1):
        label = f"[{i}] {item['type'].upper()}: {item['title']} ({item['date']})"
        if item["guest"]:
            label += f" — Guest: {item['guest']}"
        dataset_text += f"\n\n{label}\n{item['content'][:2000]}"

    return f"""You are a research assistant helping a product management blogger enrich their writing.

Below is a blog article, followed by a dataset of podcast transcripts and newsletter posts from Lenny's Newsletter/Podcast.

Your job: write a standalone markdown section titled "## Voices from the Field" to be appended at the end of the article.

This section should:
- Synthesise the 3–5 most interesting and relevant insights from the dataset that complement the article's themes
- Use direct quotes from practitioners where possible (clearly attributed)
- Add genuine value — new angles, concrete examples, or real-world validation of the article's arguments
- Feel cohesive and curated, not like a bullet dump
- Be written in a tone consistent with the article (analytical, thoughtful, practitioner-focused)
- Include a brief intro sentence before the individual entries

For each entry use this format:
**[Guest/Source name]** ([podcast/newsletter], [year]) — brief framing sentence, then the insight or quote.

Do not include research notes, meta-commentary, or instructions. Output only the markdown section, ready to paste.

---

ARTICLE:
{article}

---

DATASET:
{dataset_text}
"""

def main():
    load_env()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set. Add it to your .env file.")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python research.py path/to/article.md [--write]")
        sys.exit(1)

    article_path = Path(sys.argv[1])
    dry_run = "--write" not in sys.argv or "--dry-run" in sys.argv

    if not article_path.exists():
        print(f"Error: Article not found at {article_path}")
        sys.exit(1)

    article = article_path.read_text()
    dataset_dir = Path(__file__).parent / "lennys-newsletterpodcastdata"
    dataset = load_dataset(dataset_dir)

    print(f"Loaded {len(dataset)} items from dataset.")
    print(f"Article: {article_path}")
    print(f"Mode: {'DRY RUN — preview only' if dry_run else 'WRITE — will append to article'}\n")
    print("=" * 60)

    try:
        import anthropic
    except ImportError:
        print("Error: anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    prompt = build_prompt(article[:6000], dataset)

    generated = []
    with client.messages.stream(
        model="claude-opus-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            generated.append(text)

    print("\n" + "=" * 60)

    section = "".join(generated)

    if dry_run:
        print("\nDry run complete. Run with --write to append this section to the article.")
    else:
        with open(article_path, "a") as f:
            f.write(f"\n\n{section.strip()}\n")
        print(f"\nSection appended to {article_path}")

if __name__ == "__main__":
    main()
