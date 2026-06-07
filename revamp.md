# UX Revamp — Implementation Log

## Overview

Full front-end redesign of the happyapps blog. The design system (templates + CSS) was replaced with an editorial/magazine aesthetic based on the reference files in `ux-revamp/`. All old code is commented out in-place — nothing was deleted.

**Design reference files:**
- `ux-revamp/home.html` — home page layout
- `ux-revamp/article-template.html` — article layout
- `ux-revamp/article.css` — design tokens and article styles

---

## Design System

### Font stack
| Role | Family | Usage |
|---|---|---|
| Display | Libre Baskerville | Headlines, post titles, pull quotes |
| Body | Lora | Prose, deck, excerpt |
| Mono | DM Mono | Nav, labels, dates, tags, metadata |

### Colour palette
| Token | Value | Usage |
|---|---|---|
| `--bg` | `#f8f7f5` | Page background (warm off-white) |
| `--surface` | `#ffffff` | Cards, hero sections, footer |
| `--ink` | `#1a1814` | Near-black for headings and strong text |
| `--ink-mid` | `#3d3a35` | Body prose |
| `--ink-light` | `#6b6760` | Dates, captions, secondary metadata |
| `--accent` | `#2d4a7a` | Night blue — links, tags, rules, CTAs |
| `--accent-light` | `#e8edf5` | Tag backgrounds, pull quote fill |
| `--rule` | `#dedad4` | Borders and dividers |

---

## Files Changed

### New file
| Path | Description |
|---|---|
| `src/themes/default/assets/css/revamp.css` | Single unified stylesheet replacing all 8 old CSS files |

### Updated templates
| Path | Change |
|---|---|
| `src/themes/default/templates/html.mustache` | New font stack (Libre Baskerville + Lora + DM Mono); single `revamp.css` load |
| `src/themes/default/templates/partials/navigation.mustache` | Sticky frosted-glass nav with text logo |
| `src/themes/default/templates/partials/footer.mustache` | Minimal 2-line footer |
| `src/themes/default/templates/partials/blog/post.mustache` | `.post-item` row layout (date col + body col) |
| `src/themes/default/templates/pages/home.mustache` | Hero + topic chips + post list + about strip |
| `src/themes/default/templates/blog/post/default.mustache` | Full-width article hero + article body |
| `src/themes/default/templates/blog/posts.mustache` | Clean paginated archive |
| `src/themes/default/templates/blog/home.mustache` | Clean blog index (removed duplicate sections) |

### Updated content/config
| Path | Change |
|---|---|
| `src/contents/index.yaml` | `dateFormat` changed from `"yyyy.MM.dd."` to `"MMM d, yyyy"` |
| `src/contents/blog/posts/sdd-the-spec-as-a-new-social-contract/index.md` | Commented out `css: editorial.css` frontmatter (now handled by `revamp.css`) |

### Old CSS files (still on disk, no longer loaded)
`modern-normalize.css`, `modern-base.css`, `variables.css`, `base.css`, `grid.css`, `navigation.css`, `footer.css`, `style.css`, `editorial.css`

---

## CSS Architecture

`revamp.css` is structured in sections:

1. **Custom properties** — design tokens (colours, type scale, spacing, layout widths)
2. **Reset** — minimal box-sizing + base element styles
3. **Site header** — `.site-header`, `.site-nav`, `.site-logo`, `.nav-links`
4. **Home: hero** — `.home-hero`, `.home-hero-inner`, `.hero-copy`, `.hero-feature`, `.hero-label`, `.hero-deck`, `.hero-actions`, `.btn`, `.read-link`
5. **Home: topics bar** — `.topics-bar`, `.topics-inner`, `.topic-label`, `.topic-chip`
6. **Post list** — `.posts-section`, `.section-head`, `.post-list`, `.post-item`, `.post-meta-col`, `.post-date`, `.post-readtime`, `.post-tag`, `.post-body-col`, `.post-title`, `.post-excerpt`
7. **Pagination** — `.pagination-bar`, `.current-page`
8. **Home: about strip** — `.about-strip`, `.about-inner`, `.about-avatar`, `.about-name`, `.about-bio`, `.about-links`
9. **Article hero** — `.article-hero`, `.hero-inner`, `.kicker`, `.kicker-tag`, `.kicker-date`, `.deck`, `.byline-block`, `.byline-meta`, `.byline-name`, `.byline-role`, `.byline-reading`
10. **Article body** — `.article-body` + prose elements (`h2`, `h3`, `h4`, `code`, `pre`, `blockquote.pull-quote`, `aside.callout`, `.footnotes`, `.fn-back`)
11. **Footer** — `.site-footer`, `.footer-copy`
12. **Responsive** — breakpoints at 720px and 480px
13. **Print** — hides nav/footer, resets colours

---

## Template Architecture

### Home page (`pages/home.mustache`)
```
<section class="home-hero">          ← 2-col grid: copy + featured card
<div class="topics-bar">             ← horizontal chip strip (static, update manually)
<div class="posts-section">          ← {{site.context.posts}} → post-item rows
<section class="about-strip">        ← static author bio block
```

### Article page (`blog/post/default.mustache`)
```
<header class="article-hero">        ← kicker tags + h1 + deck + byline
<div class="article-body">           ← {{& page.contents}} (Markdown-rendered HTML)
```

### Post list partial (`partials/blog/post.mustache`)
Renders a `.post-item` anchor with:
- Left col: date, read time, tag pill(s)
- Right col: title, 2-line excerpt

Used on home, archive (`blog/posts.mustache`), and blog index (`blog/home.mustache`).

---

## Manual Maintenance Notes

### Updating the featured post card
The hero feature card on the home page is hardcoded. When you publish a new featured post, update the block marked with the `<!-- UPDATE this card -->` comment in `pages/home.mustache`:

```html
<!-- UPDATE this card when a new post becomes the featured one -->
<div class="hero-feature">
  <p class="hero-feature-tag">Series label here</p>
  <h2>Post title here</h2>
  <p>Short excerpt here...</p>
  <a href="/happyapps/blog/posts/your-post-slug/" class="read-link">Read article</a>
</div>
```

### Adding topic chips
The topic chips bar in `pages/home.mustache` is static. Add or remove `<a class="topic-chip">` elements to reflect the current content focus.

### Adding article-specific styles
The `revamp.css` article body section handles standard Markdown output: `h2`, `h3`, `h4`, `p`, `ul`, `ol`, `blockquote`, `code`, `pre`, `hr`. If you add new custom components (e.g. `aside.callout`, `blockquote.pull-quote`), write them directly into `revamp.css` under the Article Body section.

---

## Build Commands

```bash
make dev     # generate with localhost:3000 base URL
make serve   # serve docs/ on port 3000
make watch   # live-reload generation
make dist    # production build (uses live base URL from toucan.yml)
```

---

## Reverting

Every changed template has the old markup commented out directly below the new code. To revert a specific file:
1. Delete the new markup block
2. Uncomment the old block

To revert the CSS entirely, update `html.mustache` to comment out the `revamp.css` link and uncomment the 8 old CSS file links.
