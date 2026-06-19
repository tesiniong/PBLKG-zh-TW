# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A translation project, not a software project. It renders a Lithuanian grammar book —
*Praktinė bendrinės lietuvių kalbos gramatika* (Vilnius University Press, 2024) — translated
into **Traditional Chinese (Taiwan usage / 臺灣用語)**, published as a static Docsify site on
GitHub Pages. Almost all "work" is editing Markdown prose; treat it accordingly (faithful
translation, terminology consistency, correct linguistic notation) rather than as code.

The output language is 繁體中文（臺灣用語）. Lithuanian source terms are normally kept in
parentheses or italics alongside the Chinese translation.

## Structure

- `part1/`–`part4/` — the book's four parts: **1 語音學 (Phonetics)**, **2 形態學
  (Morphology)**, **3 構詞學 (Word formation)**, **4 句法學 (Syntax)**. Each part is a flat
  folder of chapter files named `<n>-<中文標題>.md` (e.g. `part2/9-動詞.md`). Numbering
  follows the original book's chapter order; `0-` is the part's intro, `99-`/`9-` is references.
- `_sidebar.md` — the entire navigation tree. **Manually maintained.** Any new/renamed/removed
  chapter file must be reflected here or it won't appear on the site.
- `index.html` — the Docsify app: all config, CSS, and three custom render plugins live here
  (there is no separate config file).
- `README.md` — serves as the site's home page (`/`); it holds the book's front matter and 前言.
- `pdf/` — the Lithuanian source. `Praktinė_gramatika_fixed.pdf` is the whole book;
  `pdf/ilovepdf_split-range/` and the `*-<from>-<to>.pdf` files are page-range splits, used to
  hand portions to other AIs for translation. These are reference material, **not** published.
- `.nojekyll` — required so GitHub Pages serves Docsify's `_`-prefixed files.

## Running / previewing

No build, bundler, or test step exists — Docsify renders Markdown in the browser at runtime,
loading everything from CDNs. To preview locally, serve the repo root as static files, e.g.:

```sh
python3 -m http.server 8000   # then open http://localhost:8000
```

Opening `index.html` via `file://` will not work (Docsify fetches `.md` files over HTTP).
Deployment is just pushing to the GitHub Pages branch; there is nothing to compile.

## Authoring conventions (important — these are enforced by the custom plugins in `index.html`)

- **Phonetic / IPA notation** is written in square brackets, escaped as `\[ … ]` in the
  Markdown source (e.g. `\[ɑː]`, `\[²ˈʃɑːkɑː]`). The escape stops Markdown from treating it as a
  link/footnote; `ipaPlugin` then wraps `[…]` in `<span class="ipa">` and styles it with the
  Charis SIL font. Brackets containing Han characters, plain numbers, or `<>` are left alone.
- **Footnotes are custom, not standard Markdown.** Reference with `[^name]` inline (often
  escaped `\[^name]`) and define with `[^name]: text` in its own paragraph. `footnotePlugin`
  numbers them in order of appearance and renders a popover; names are arbitrary slugs
  (`fn70`, `footnote3`) and only need to be unique within a file. Do not rely on Markdown's
  native footnote syntax — it is intentionally bypassed.
- **Lithuanian example words** are typeset in italics (`*žodis*`); accent/length diacritics on
  them are significant and must be preserved exactly.
- **Translator's notes / editorial insertions** use lenticular brackets 〔…〕 (e.g. a supplied
  title: `〔原檔缺標題，暫擬〕`).
- `subMaxLevel: 3` — only `#`/`##`/`###` headings appear in the auto-generated per-page TOC.
- Full-text search is enabled across the whole book, so keep headings meaningful.

When translating a chapter, the source of truth is the matching page range in `pdf/`. Keep
terminology consistent with already-translated chapters and with the established renderings.

**Translation workflow / terminology authority:** `翻譯提示詞.md` (repo root) is the prompt the
user hands to a translating AI together with a PDF split. It holds the full formatting spec
(example format `原文「譯文」` with no space and 直角引號; first-occurrence terms followed by the
Lithuanian in 全形括號; italic terms become bold, italic examples stay italic; standard `[^fn1]`
footnotes; no spaces between Latin/digits and Han) and the canonical Lithuanian→繁中 glossary.
Treat that glossary as the authoritative term mapping and reuse it; when a chapter needs a term
that isn't listed, surface it for confirmation rather than inventing silently.
