import re

with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix body background
css = css.replace('background-color: var(--text-primary);\n  color: var(--text-primary);', 'background-color: var(--bg-primary);\n  color: var(--text-primary);')
css = css.replace('background-color: var(--text-nav);\n  color: var(--text-primary);', 'background-color: var(--bg-primary);\n  color: var(--text-primary);')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
