#!/usr/bin/env python3
"""
new-post.py — wizard to scaffold a new blog post.

Usage:
    python new-post.py
"""

import re
import sys
from datetime import datetime
from pathlib import Path

POSTS_DIR = Path(__file__).parent / "src/contents/blog/posts"
AUTHOR = "joel-sooriah"


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def ask(prompt: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{prompt}{suffix}: ").strip()
    return value if value else default


def ask_required(prompt: str) -> str:
    while True:
        value = input(f"{prompt}: ").strip()
        if value:
            return value
        print("  This field is required.")


def main():
    print("\n=== New Post Wizard ===\n")

    # Title
    title = ask_required("Title")

    # Slug
    suggested_slug = slugify(title)
    print(f"  -> suggested slug: {suggested_slug}")
    slug = ask("Slug (press enter to accept)", default=suggested_slug)

    # Check for collision
    target_dir = POSTS_DIR / slug
    if target_dir.exists():
        print(f"\nError: '{target_dir}' already exists. Pick a different slug.")
        sys.exit(1)

    # Description
    description = ask_required("Description (used in previews and meta)")

    # Tags (comma-separated)
    tags_input = ask("Tags (comma-separated, e.g. aiengineering, productmanagement)", default="")
    tags = [t.strip() for t in tags_input.split(",") if t.strip()]

    # Featured
    featured_input = ask("Featured? (y/n)", default="n")
    featured = featured_input.lower() in ("y", "yes")

    # Publication date
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pub_date = ask("Publication date", default=now)

    # Build frontmatter
    tags_yaml = "\n".join(f"  - {t}" for t in tags) if tags else "  - "
    frontmatter = f"""---
type: post
title: {title}
description: {description}
publication: {pub_date}
tags:
{tags_yaml}
authors:
  - {AUTHOR}
featured: {str(featured).lower()}
redirects:
    - from: {slug}
---

"""

    # Confirm
    print(f"\n--- Preview ---")
    print(frontmatter)
    print(f"Location: {target_dir}/index.md")
    confirm = ask("Create this post? (y/n)", default="y")
    if confirm.lower() not in ("y", "yes"):
        print("Aborted.")
        sys.exit(0)

    # Write
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "index.md").write_text(frontmatter)

    print(f"\nCreated: {target_dir}/index.md")


if __name__ == "__main__":
    main()
