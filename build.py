"""Build the website from the Markdown files in content/.

Run it locally with:   python build.py
The finished site is written to the _site/ folder (open _site/index.html).
On GitHub, the workflow in .github/workflows/build.yml runs this same script
every time you commit, and publishes _site/ to your GitHub Pages address.
"""
import pathlib
import re
import shutil
import sys

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

ROOT = pathlib.Path(__file__).resolve().parent
CONTENT = ROOT / "content"
OUT = ROOT / "_site"

FRONT = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.S)


def fail(msg):
    print(f"\nBUILD FAILED: {msg}\n", file=sys.stderr)
    sys.exit(1)


def to_html(text):
    return Markup(markdown.markdown(text or "", extensions=["extra", "sane_lists"]))


def to_inline_html(text):
    html = markdown.markdown(str(text or ""), extensions=["extra"])
    return Markup(re.sub(r"^<p>(.*)</p>$", r"\1", html.strip(), flags=re.S))


def read(path):
    """Read one Markdown file: the settings between the --- lines, then the text."""
    raw = path.read_text(encoding="utf-8")
    m = FRONT.match(raw)
    if not m:
        fail(f"{path.relative_to(ROOT)} must start with a line of three dashes (---), "
             "then its settings, then another --- line.")
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        fail(f"{path.relative_to(ROOT)} has a formatting problem in its settings:\n{e}\n"
             "Tip: put a value in quotes if it starts with * or contains ': '.")
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)}: the settings must be 'name: value' lines.")
    data["body"] = to_html(m.group(2).strip())
    data["file"] = path.name
    return data


def shown(item):
    return item.get("show", True) is not False


def load_section(name):
    path = CONTENT / f"{name}.md"
    if not path.exists():
        fail(f"content/site.md lists the section '{name}', but content/{name}.md does not exist.")
    sec = read(path)
    sec["id"] = name
    folder = CONTENT / name
    if folder.is_dir():
        sec["entries"] = [d for d in (read(p) for p in sorted(folder.glob("*.md"))) if shown(d)]
    return sec


def main():
    site = read(CONTENT / "site.md")
    sections = [s for s in (load_section(n) for n in site.get("sections", [])) if shown(s)]
    for s in sections:
        if not (ROOT / "templates" / "sections" / f"{s['id']}.html").exists():
            fail(f"There is no design template for the section '{s['id']}' "
                 f"(templates/sections/{s['id']}.html).")

    env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                      autoescape=select_autoescape(["html"]),
                      trim_blocks=True, lstrip_blocks=True)
    env.filters["md"] = to_html
    env.filters["mdi"] = to_inline_html
    html = env.get_template("page.html").render(site=site, sections=sections)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / "index.html").write_text(html, encoding="utf-8")
    shutil.copytree(ROOT / "assets", OUT / "assets")
    if (ROOT / "images").is_dir():
        shutil.copytree(ROOT / "images", OUT / "images")
    photo = site.get("photo")
    if photo and (ROOT / photo).is_file():
        shutil.copy(ROOT / photo, OUT / photo)
    elif photo:
        print(f"Note: the photo '{photo}' was not found next to build.py, so no photo is shown.")
    print(f"Built {OUT / 'index.html'} with {len(sections)} sections.")


if __name__ == "__main__":
    main()
