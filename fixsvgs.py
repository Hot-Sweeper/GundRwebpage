import os

target_a = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
target_b = 'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
sized = 'width="16" height="16" '

for fname in os.listdir('website'):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join('website', fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    orig = html

    # Replace only SVGs that do NOT already have width in that tag
    import re
    def add_size(m):
        tag = m.group(0)
        if 'width=' in tag:
            return tag
        return tag.replace('<svg ', '<svg width="16" height="16" ')

    # Match only SVG opening tags inside footer section
    footer_start = html.find('<footer')
    if footer_start == -1:
        footer_start = html.find('class="footer')
    if footer_start == -1:
        continue

    before = html[:footer_start]
    footer_part = html[footer_start:]

    footer_part = re.sub(r'<svg\b[^>]*>', add_size, footer_part)

    html = before + footer_part

    if html != orig:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Fixed: {fname}')

print('All done.')
