import os

old = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/>'
new = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/>'

fixed = []
for fname in os.listdir('website'):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join('website', fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    if old in html:
        html = html.replace(old, new)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        fixed.append(fname)

print('Fixed:', fixed)
