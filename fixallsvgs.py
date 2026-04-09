"""
Adds width/height attributes to every <svg> tag that's missing them.
Context-aware sizing:
  - Footer contact icons  → 16x16
  - Social icons          → 18x18 (already done, but safe to re-check)
  - Service/class icons   → 24x24
  - Arrow/link icons      → 16x16 (inside <a> or link elements)
  - Nav theme-toggle      → 20x20
  - All others            → 20x20 (safe default)

Technique: regex-replace on full file text, using lookbehind to detect context.
"""
import os
import re

HTML_DIR = "website"

# Groups of patterns we look for in the lines BEFORE the svg tag
CONTEXT_PATTERNS = [
    # (search string in preceding ~300 chars, width, height)
    ("footer__contact-item", 16, 16),
    ("footer__social",       18, 18),
    ("service-card__icon",   24, 24),
    ("class-group__icon",    24, 24),
    ("feature-card__icon",   24, 24),
    ("contact-card__icon",   24, 24),
    ("hero-scroll",          24, 24),
    ("service-card__link",   16, 16),
    ("btn-link",             16, 16),
    ("icon-sun",             20, 20),
    ("icon-moon",            20, 20),
]
DEFAULT_SIZE = (20, 20)

SVG_TAG_RE = re.compile(r'<svg\b([^>]*)>', re.DOTALL)

import re as _re
_DIM_RE = _re.compile(r'(?<![a-z-])width=|(?<![a-z-])height=')

def has_dim(attrs):
    return bool(_DIM_RE.search(attrs))

def get_size(preceding_text):
    for pattern, w, h in CONTEXT_PATTERNS:
        if pattern in preceding_text:
            return w, h
    return DEFAULT_SIZE

def process_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    changed = 0
    result = []
    pos = 0
    
    for m in SVG_TAG_RE.finditer(html):
        attrs = m.group(1)
        start = m.start()
        end = m.end()
        
        # Append everything before this match
        result.append(html[pos:start])
        
        if has_dim(attrs):
            # Already has dimensions, keep as-is
            result.append(m.group(0))
        else:
            # Determine size from context (up to 300 chars before the tag)
            preceding = html[max(0, start-300):start]
            w, h = get_size(preceding)
            new_tag = f'<svg width="{w}" height="{h}"{attrs}>'
            result.append(new_tag)
            changed += 1
        
        pos = end
    
    result.append(html[pos:])
    new_html = ''.join(result)
    
    if changed:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_html)
    
    return changed

total = 0
for fname in sorted(os.listdir(HTML_DIR)):
    if fname.endswith('.html'):
        fpath = os.path.join(HTML_DIR, fname)
        n = process_file(fpath)
        if n:
            print(f"  {fname}: {n} SVGs fixed")
        total += n

print(f"\nTotal: {total} SVGs updated across all pages")
