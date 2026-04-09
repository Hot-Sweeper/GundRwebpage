with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Update nav background explicitly if it's forced elsewhere
css = re.sub(r'\.nav \{\n\s*background-color: var\(--nav-bg\);', '.nav {\n  background-color: var(--nav-bg);\n  border-bottom: 3px solid #000;', css)
# Ensure nav text color gets black explicitly, and hover effects stand out
css = re.sub(r'\.nav__link \{\n\s*color: var\(--text-nav\);', '.nav__link {\n  color: var(--text-nav);\n  font-weight: 700;', css)

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
