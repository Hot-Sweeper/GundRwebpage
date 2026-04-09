with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure buttons use proper accent-text
css = css.replace('.btn--primary {\n  background-color: var(--accent);\n  color: #000;\n  border-color: var(--accent);\n', '.btn--primary {\n  background-color: var(--accent);\n  color: var(--accent-text);\n  border-color: var(--border);\n')
css = css.replace('.btn {\n  text-transform: uppercase;\n  border: 3px solid #fff;\n', '.btn {\n  text-transform: uppercase;\n  border: 3px solid var(--border);\n  color: var(--text-primary);\n')
css = css.replace('.btn {\n  text-transform: uppercase;\n  border: 3px solid var(--border);\n', '.btn {\n  text-transform: uppercase;\n  border: 3px solid var(--border);\n  color: var(--text-primary);\n')
css = css.replace('color: var(--bg-primary);', 'color: var(--text-primary);')

# The nav links
css = css.replace('.nav__link {\n  color: var(--bg-primary);\n  font-weight: 700;', '.nav__link {\n  color: var(--text-nav);\n  font-weight: 700;')

# The nav background 
css = css.replace('background-color: #ffffff;\n  border-bottom: 3px solid var(--text-nav);', 'background-color: var(--nav-bg);\n  border-bottom: 3px solid var(--border-nav);')
css = css.replace('.nav {\n  position: fixed;\n  top: 0;\n  width: 100%;\n  z-index: 1000;\n  transition: background-color var(--transition-base), padding var(--transition-base), box-shadow var(--transition-base);\n  padding: 1.25rem 0;\n  border-bottom: 3px solid var(--border);\n}', '.nav {\n  position: fixed;\n  top: 0;\n  width: 100%;\n  z-index: 1000;\n  transition: background-color var(--transition-base), padding var(--transition-base), box-shadow var(--transition-base);\n  padding: 1.25rem 0;\n  background-color: var(--nav-bg);\n  border-bottom: 3px solid var(--border-nav);\n}')

# General background colors
css = css.replace('background-color: transparent;\n  color: var(--accent);\n  border-color: var(--accent);\n', 'background-color: var(--bg-primary);\n  color: var(--text-primary);\n  border-color: var(--border);\n')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
