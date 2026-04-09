with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Force header to be white, with a hard border
import re
css = css.replace('background-color: var(--nav-bg);', 'background-color: #ffffff;\n  border-bottom: 3px solid #000;')
css = css.replace('background-color: var(--nav-bg-scroll);', 'background-color: #ffffff;\n  border-bottom: 3px solid #000;\n  box-shadow: 4px 4px 0 var(--accent);')
css = css.replace('.nav__link {\n  color: #fff;', '.nav__link {\n  color: #000;\n  font-weight: 700;')

# Ensure sub-page hero is consistent dark
css = re.sub(r'background: linear-gradient\(135deg, [^\)]+\);', 'background: #000000;', css)

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

