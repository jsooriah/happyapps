# Front-End Revamp

## Overview

This branch introduces an editorial/magazine CSS theme (`editorial.css`) alongside the existing default theme. Both can coexist — you switch per-page via frontmatter, with no rebuild or code change required.

---

## File locations

| What | Path |
|---|---|
| New CSS | `src/themes/default/assets/css/editorial.css` |
| Base layout template | `src/themes/default/templates/html.mustache` |
| Existing variables | `src/themes/default/assets/css/variables.css` |
| Existing main styles | `src/themes/default/assets/css/style.css` |

---

## How to switch themes per page

Toucan exposes a `css` frontmatter key that injects an extra `<link>` tag into the page `<head>`. Use it to opt a page into the editorial theme.

### Use the editorial theme on a page

Add `css` to the post's frontmatter:

```yaml
---
type: post
title: My Post
css: /happyapps/css/editorial.css
---
```

### Revert to the default theme

Remove (or comment out) the `css` line:

```yaml
---
type: post
title: My Post
# css: /happyapps/css/editorial.css
---
```

That's it — no other files are touched.

---

## Making editorial the sitewide default

When you're happy with the new theme and want it on every page, add one line to `html.mustache` after the existing `style.css` link:

```html
<link rel="stylesheet" href="/happyapps/css/style.css">
<link rel="stylesheet" href="/happyapps/css/editorial.css">   <!-- add this -->
```

Then you no longer need the `css` frontmatter key on individual pages.

---

## What editorial.css adds

The file is self-contained — it imports its own Google Fonts (`Playfair Display`, `Source Serif 4`, `JetBrains Mono`) and defines its own CSS custom properties under non-conflicting names (`--ink`, `--cream`, `--accent`, `--gold`, etc.). It does not override or depend on the existing `variables.css` values.

### Components available

| Class | Description |
|---|---|
| `.masthead` | Dark header bar with publication name and issue line |
| `.pub-name` / `.issue-line` | Masthead text elements |
| `.hero` | Article title area with constrained width |
| `.kicker` | Category label above the headline |
| `.deck` | Subtitle / standfirst paragraph |
| `.byline-block` | Author + date row with border rules |
| `.article-body` | Main prose container (680px max-width) |
| `.pull-quote` | Full-bleed dark quote block with large opening mark |
| `.taxonomy-block` | Two-column definition table with dark header |
| `.callout` | Highlighted aside box with gold left border |
| `.section-break` | `<hr>` with centred diamond ornament |
| `.endnotes` | Footnotes section in monospace |
| `sup.cite` | Inline citation superscript |
