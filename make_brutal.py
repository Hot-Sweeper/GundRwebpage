with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace border-radius with 0
import re
# Make outlines thick
css = re.sub(r'border: 1px solid var\(--border\);', r'border: 3px solid var(--border);', css)
css = re.sub(r'border-radius: var\(--radius-[^\)]+\);', r'border-radius: 0;', css)
css = re.sub(r'box-shadow: var\(--shadow-[^\)]+\);', r'box-shadow: 6px 6px 0 var(--accent);', css)
css = re.sub(r'transform: translateY\(-6px\);', r'transform: translate(-4px, -4px);', css)

# Brutalist Buttons
# Find buttons and make them brutalist
css = css.replace('.btn {', '.btn {\n  text-transform: uppercase;\n  border: 3px solid #fff;\n  box-shadow: 4px 4px 0 var(--accent);\n')
css = css.replace('.btn:hover {', '.btn:hover {\n  box-shadow: 8px 8px 0 var(--accent);\n  transform: translate(-2px, -2px);\n')

css = css.replace('.btn--primary {', '.btn--primary {\n  background-color: var(--accent);\n  color: #000;\n  border-color: var(--accent);\n')
css = css.replace('.btn--secondary {', '.btn--secondary {\n  background-color: transparent;\n  color: var(--accent);\n  border-color: var(--accent);\n')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
