# mozhfarahani.github.io

My personal website. All the words live in Markdown files in the `content/` folder.
Edit a file on GitHub, click **Commit changes**, and the site rebuilds itself in about a minute.

## Where things are

| To change… | Edit this file |
|---|---|
| Name, photo, sidebar lines and links, footer, **section order** | `content/site.md` |
| Top line, headline, intro paragraph | `content/about.md` |
| One project | `content/projects/<project>.md` |
| Project filter buttons | `content/projects.md` |
| One job | `content/experience/<job>.md` |
| Education | `content/experience.md` |
| One recommendation | `content/recommendations/<name>.md` |
| Skills and certifications | `content/skills.md` |
| Publications | `content/publications.md` |
| Code repositories | `content/code.md` |
| Personal section | `content/personal.md` |
| Email and contact links | `content/contact.md` |

You only need `templates/` (page structure) and `assets/` (colors, fonts, behavior) to change the design.

## How a content file works

Every file has two parts. Between the two `---` lines are **settings** (`name: value`).
Below the second `---` is the **text**, written in Markdown.

```markdown
---
title: pyTIER
when: 2022
filters: [tools, hpc]
tags: [Python, Open source]
links:
  - label: GitHub
    url: https://github.com/NCAR/pyTIER
---

A Python port of the TIER station-interpolation model…
```

Markdown basics: `*italic*`, `**bold**`, `[link text](https://…)`, a blank line starts a new paragraph,
and `- ` at the start of a line makes a bullet.

## Common tasks

- **Add a project:** copy an existing file in `content/projects/`, rename it, and edit it.
  Files appear in name order, so the number at the front (`03-…`) sets the position.
  `filters` uses the keys defined in `content/projects.md` (`ml`, `hpc`, `it`, `tools`, `community`).
- **Hide something without deleting it:** add `show: false` to its settings.
  It works for a project, a job, a recommendation, or a whole section file.
- **Hide or reorder a whole section:** edit the `sections:` list in `content/site.md`.
- **Add a publication:** add a block at the top of the list in `content/publications.md`.
  `doi` and `code` are optional.
- **Add images:** upload them to an `images/` folder and use `![description](images/file.jpg)` in any text.

## Formatting tips

- Indentation matters in the settings. Use spaces, never tabs, and line items up under each other.
- Put a value in quotes if it starts with `*` or contains a colon followed by a space,
  for example `title: 'Information flows: characterizing…'`.
- If the site does not update, open the **Actions** tab. A red ✗ means the build stopped;
  click it to see which file has the problem and why. The live site keeps the last good version until you fix it.

## Preview on your own computer (optional)

```bash
pip install -r requirements.txt
python build.py
```

Then open `_site/index.html` in a browser.
