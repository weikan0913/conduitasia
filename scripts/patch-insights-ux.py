#!/usr/bin/env python3
"""Patch insights.html: dual-lane UX + full media archive."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INSIGHTS = ROOT / "insights.html"
ARCHIVE = ROOT / "_generated-media-archive-en.html"

archive_ul = ARCHIVE.read_text(encoding="utf-8")
# strip comment markers
for marker in ("<!-- EN_ARCHIVE_START -->\n", "<!-- EN_ARCHIVE_END -->\n"):
    archive_ul = archive_ul.replace(marker, "")

html = INSIGHTS.read_text(encoding="utf-8")

css_addition = """
        .insights-hero-lede { max-width: 720px; font-size: 16px; line-height: 1.85; color: var(--mid-gray); margin-bottom: 8px; }
        .insights-fork { display: grid; grid-template-columns: 1fr 1fr; gap: 2px; max-width: 1200px; margin: 0 auto; padding: 8px 48px 40px; }
        .fork-card {
            display: block; background: var(--card-dark); padding: 40px 36px;
            text-decoration: none; color: inherit;
            border: 1px solid rgba(136, 136, 128, 0.18);
            transition: border-color 0.35s ease, background 0.35s ease;
        }
        .fork-card:hover { border-color: rgba(125, 107, 138, 0.65); background: rgba(26, 26, 26, 0.85); }
        .fork-card h2 { font-family: 'Playfair Display', serif; font-weight: 400; font-size: clamp(22px, 2.6vw, 30px); line-height: 1.3; color: var(--text-light); margin-bottom: 14px; }
        .fork-card p { font-size: 15px; line-height: 1.8; color: var(--mid-gray); }
        .fork-card .fork-cta { display: inline-block; margin-top: 18px; font-size: 11px; letter-spacing: 2px; text-transform: uppercase; color: var(--dusty-violet); }
        .insights-subnav {
            position: sticky; top: 70px; z-index: 90;
            background: rgba(15, 15, 15, 0.94); backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(136, 136, 128, 0.12);
        }
        .insights-subnav-inner { max-width: 1200px; margin: 0 auto; padding: 14px 48px; display: flex; flex-wrap: wrap; gap: 12px 28px; }
        .insights-subnav a { font-size: 12px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--mid-gray); text-decoration: none; transition: color 0.3s ease; }
        .insights-subnav a:hover { color: var(--text-light); }
        .insights-lane { max-width: 1200px; margin: 0 auto; padding: 56px 48px 0; }
        .lane-header { margin-bottom: 32px; max-width: 760px; }
        .lane-header .divider { margin-bottom: 24px; }
        .lane-header h2 { font-family: 'Playfair Display', serif; font-weight: 400; font-size: clamp(28px, 3.5vw, 40px); line-height: 1.25; color: var(--text-light); margin-bottom: 16px; }
        .lane-header p { font-size: 15px; line-height: 1.85; color: var(--mid-gray); }
        .lane-header a { color: var(--text-light); text-decoration: none; border-bottom: 1px solid rgba(136, 136, 128, 0.4); }
        .lane-header a:hover { color: var(--dusty-violet); border-bottom-color: var(--dusty-violet); }
        .media-archive-en { list-style: none; max-width: 860px; }
        .media-archive-en li { padding: 22px 0; border-bottom: 1px solid rgba(136, 136, 128, 0.15); }
        .media-archive-en li:first-child { border-top: 1px solid rgba(136, 136, 128, 0.15); }
        .ma-date { display: block; font-size: 10px; letter-spacing: 2.5px; text-transform: uppercase; color: var(--dusty-violet); margin-bottom: 8px; }
        .ma-outlet { display: block; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: rgba(136, 136, 128, 0.9); margin-bottom: 8px; }
        .media-archive-en .ma-title { font-family: 'Playfair Display', serif; font-weight: 400; font-size: 19px; line-height: 1.4; color: var(--text-light); text-decoration: none; border-bottom: none; }
        a.ma-title:hover { color: var(--dusty-violet); }
        .ma-topic { margin-top: 10px; font-size: 14px; line-height: 1.7; color: var(--mid-gray); max-width: 720px; }
        .ma-note { margin-top: 8px; font-size: 13px; line-height: 1.65; color: rgba(136, 136, 128, 0.9); }
        .lane-separator { max-width: 1200px; margin: 72px auto 0; padding: 0 48px; }
        .lane-separator .line { height: 1px; background: rgba(136, 136, 128, 0.2); }
        .operator-callout { margin-top: 48px; padding: 36px 32px; border: 1px solid rgba(136, 136, 128, 0.2); max-width: 760px; }
        @media (max-width: 768px) {
            .insights-fork { grid-template-columns: 1fr; padding: 8px 24px 32px; }
            .fork-card { padding: 32px 24px; }
            .insights-subnav-inner { padding: 12px 24px; }
            .insights-lane { padding: 48px 24px 0; }
            .lane-separator { padding: 0 24px; margin-top: 56px; }
        }
"""

if ".insights-fork" not in html:
    html = html.replace(
        "        .fade-in { opacity: 0; transform: translateY(20px);",
        css_addition + "\n        .fade-in { opacity: 0; transform: translateY(20px);",
    )

new_hero_block = """    <section class="hero">
        <h1>Insights</h1>
        <p class="insights-hero-lede">Client work stays confidential. What you can read on this site is our published judgment: third-party press quotes and our own analysis.</p>
    </section>

    <div class="insights-fork fade-in">
        <a class="fork-card" href="#in-the-media">
            <h2>In the Media</h2>
            <p>Named quotations in the <em>Financial Times</em>, <em>Bloomberg</em>, <em>Reuters</em>, <em>CNBC</em>, <em>WSJ</em>, <em>Nikkei Asia</em>, the <em>BBC</em>, and other outlets. Full archive, updated from our public record.</p>
            <span class="fork-cta">Open media archive &rarr;</span>
        </a>
        <a class="fork-card" href="#our-writing">
            <h2>Our Writing</h2>
            <p><em>From the Inside</em> on Substack, frameworks on Medium, and shorter reads on LinkedIn. This is how we show commercial thinking without client names on the site.</p>
            <span class="fork-cta">Open writing archive &rarr;</span>
        </a>
    </div>

    <nav class="insights-subnav" aria-label="Insights sections">
        <div class="insights-subnav-inner">
            <a href="#in-the-media">In the Media</a>
            <a href="#our-writing">Our Writing</a>
            <a href="#operator-read">The Operator Read</a>
            <a href="#newsletter">From the Inside</a>
            <a href="#enquiries">Enquiries</a>
        </div>
    </nav>

    <section class="insights-lane" id="in-the-media">
        <div class="lane-header fade-in">
            <div class="divider"></div>
            <div class="section-label">Press Archive</div>
            <h2>In the Media</h2>
            <p><strong>19 named English-language citations</strong> (newest first), verified against our internal media log. Chinese-language citations: <a href="/cn-insights.html#media">see 观点与媒体</a>.</p>
        </div>
"""
new_hero_block += "        " + archive_ul.strip().replace("\n", "\n        ") + "\n"
new_hero_block += """        <p class="selected-intro fade-in" style="margin-top:32px;max-width:720px">For interviews or background, <a href="mailto:wei.kan@conduitasia.com?subject=Press%20enquiry%20via%20conduitasia.com">email press</a>. We do not list client mandates on this site.</p>
    </section>

    <div class="lane-separator"><div class="line"></div></div>
"""

import re

pattern = re.compile(
    r"    <section class=\"hero\">.*?</section>\n\n    <section class=\"content-section\" id=\"operator-read\".*?</section>\n\n    <div class=\"inquiry-strip",
    re.DOTALL,
)
if not pattern.search(html):
    raise SystemExit("insights.html hero/operator block not found")
html = pattern.sub(
    new_hero_block
    + "\n    <div class=\"inquiry-strip",
    html,
    count=1,
)

# Wrap writing: add id our-writing before content-section (first one after fork)
html = html.replace(
    '    <section class="content-section">\n        <div class="content-section-header fade-in">\n            <div class="divider"></div>\n            <div class="section-label">Selected</div>',
    '    <section class="insights-lane content-section" id="our-writing">\n        <div class="content-section-header fade-in">\n            <div class="divider"></div>\n            <div class="section-label">Our Writing</div>\n            <h2 style="font-family:\'Playfair Display\',serif;font-weight:400;font-size:clamp(26px,3.2vw,36px);line-height:1.3;color:var(--text-light);margin:0 0 16px;max-width:760px">Published analysis</h2>',
)

html = html.replace(
    '<p class="selected-intro">A short front window, not the full archive. <strong>Recent</strong> pulls from the last month on LinkedIn and Substack, including the weekday digest. <strong>Standouts</strong> keeps the longer frameworks and posts that still earn the read. Press quotes live under Media and on the home page.</p>',
    '<p class="selected-intro"><strong>Recent</strong> pulls from the last month on LinkedIn and Substack. <strong>Standouts</strong> keeps longer frameworks. The full list of published pieces is below. Press citations are in <a href="#in-the-media">In the Media</a>.</p>',
)

# Remove old also-on Media paragraph section
html = re.sub(
    r"\n    <section class=\"also-on\">.*?</section>\n",
    "\n",
    html,
    count=1,
    flags=re.DOTALL,
)

# Operator read: move into our-writing lane before newsletter - find old operator section was removed; add callout before newsletter
operator_block = """    <div class="operator-callout fade-in" id="operator-read">
            <div class="section-label">Institutional Subscription</div>
            <h2 style="font-family:'Playfair Display',serif;font-weight:400;font-size:clamp(22px,2.6vw,28px);line-height:1.3;color:var(--text-light);margin:12px 0 14px">The Operator Read</h2>
            <p class="selected-intro" style="margin-bottom:12px"><em>The Operator Read</em> is Conduit Asia&rsquo;s periodic paid publication for investment and research teams. Separate from public <em>From the Inside</em> analysis.</p>
            <p class="selected-intro">Institutional subscription: <a href="mailto:wei.kan@conduitasia.com?subject=The%20Operator%20Read%20inquiry">wei.kan@conduitasia.com</a></p>
        </div>

"""
if 'id="operator-read"' not in html:
    html = html.replace(
        '    <section class="newsletter" id="newsletter">',
        operator_block + '    <section class="newsletter" id="newsletter">',
    )

INSIGHTS.write_text(html, encoding="utf-8")
print("patched", INSIGHTS)