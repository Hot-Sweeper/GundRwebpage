import re

with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('background-color: #ffffff;\n  border-bottom: 3px solid #000;', 'background-color: var(--nav-bg);\n  border-bottom: 3px solid var(--border-nav);')
css = css.replace('color: #000;\n  font-weight: 700;', 'color: var(--text-nav);\n  font-weight: 700;')
css = css.replace('.hamburger {\n  display: none;\n  background: none;\n  border: none;\n  color: #000;', '.hamburger {\n  display: none;\n  background: none;\n  border: none;\n  color: var(--text-nav);')
css = css.replace('background-color: #000;', 'background-color: var(--text-nav);')
css = css.replace('color: #000;', 'color: var(--text-nav);')
css = css.replace('border: 3px solid #000;', 'border: 3px solid var(--border);')
css = css.replace('border-bottom: 3px solid #000;', 'border-bottom: 3px solid var(--border);')
css = css.replace('border: 3px solid #fff;', 'border: 3px solid var(--border);')
css = css.replace('color: #fff;', 'color: var(--bg-primary);') # wait, button text on primary usually text, but let's use text-primary

css = css.replace('.btn--primary {\n  background-color: var(--accent);\n  color: var(--text-nav);\n  border-color: var(--accent);\n', '.btn--primary {\n  background-color: var(--accent);\n  color: var(--accent-text);\n  border-color: var(--border);\n')
css = css.replace('.btn--primary:hover {\n  background-color: var(--accent-hover);', '.btn--primary:hover {\n  background-color: var(--accent-hover);\n  color: var(--accent-text);')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
