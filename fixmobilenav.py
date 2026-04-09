import os, re

for fname in os.listdir('website'):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join('website', fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    orig = html

    # Remove inline white color style from mobile theme toggle button
    html = re.sub(
        r'(<button[^>]*theme-toggle[^>]*)\s+style="[^"]*color:rgba\(255,255,255[^"]*"',
        r'\1',
        html
    )
    # Remove inline white color from the Farbschema span inside mobile nav
    html = re.sub(
        r'(<span)\s+style="[^"]*color:rgba\(255,255,255[^"]*"',
        r'\1',
        html
    )

    if html != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print('Fixed:', fname)

print('Done.')
