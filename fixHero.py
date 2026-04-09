import re

with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Force hero text to be always white since it is on a dark image
css = css.replace('.hero__title {\n  color: var(--text-primary);', '.hero__title {\n  color: #ffffff;')
css = re.sub(r'\.hero__subtitle \{\n  font-size: 1\.15rem;\n  color: var\(--text-secondary\);', '.hero__subtitle {\n  font-size: 1.15rem;\n  color: rgba(255, 255, 255, 0.9);', css)
css = re.sub(r'\.page-hero__title \{\n  color: var\(--text-primary\);', '.page-hero__title {\n  color: #ffffff;', css)
css = re.sub(r'\.page-hero \{\n  .*', '.page-hero {\n  background: #111111;', css) # Always dark for page hero background
css = css.replace('.page-hero__sub {\n  color: var(--text-secondary);', '.page-hero__sub {\n  color: rgba(255, 255, 255, 0.85);')

# Also revert paragraphs floating around the hero if any
css = css.replace('color: var(--text-primary);\n    margin-bottom: 0.75rem;\n  }\n  \n  .page-hero__sub', 'color: #ffffff;\n    margin-bottom: 0.75rem;\n  }\n  \n  .page-hero__sub')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
