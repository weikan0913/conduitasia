#!/usr/bin/env python3
"""Emit HTML fragments for media archive from media-citations-canonical.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "media-citations-canonical.json").read_text(encoding="utf-8"))


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def item_html(row: dict, lang: str = "en") -> str:
    title = esc(row["title"])
    outlet = esc(row["outlet"])
    topic = esc(row.get("topic", ""))
    date = esc(row["date"])
    url = row.get("url")
    note = row.get("note")
    if url:
        title_block = f'<a class="ma-title" href="{esc(url)}" target="_blank" rel="noopener">{title}</a>'
    else:
        title_block = f'<span class="ma-title">{title}</span>'
    note_html = f'<p class="ma-note">{esc(note)}</p>' if note else ""
    topic_html = f'<p class="ma-topic">{topic}</p>' if topic else ""
    return f"""<li class="fade-in">
      <span class="ma-date">{date}</span>
      <span class="ma-outlet">{outlet}</span>
      {title_block}
      {topic_html}
      {note_html}
    </li>"""


en = "\n".join(item_html(r) for r in data["english_named"])
print("<!-- EN_ARCHIVE_START -->")
print(f'<ul class="media-archive-en" id="media-archive-en">')
print(en)
print("</ul>")
print("<!-- EN_ARCHIVE_END -->")