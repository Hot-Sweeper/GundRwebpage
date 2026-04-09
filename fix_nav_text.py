with open('website/css/variables.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Swap text-nav globally
css = css.replace('--text-nav:       #ffffff;', '--text-nav:       #000000;')
css = css.replace('--text-nav:       #f0f2f8;', '--text-nav:       #000000;')

with open('website/css/variables.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('website/css/style.css', 'r', encoding='utf-8') as f:
    s = f.read()

# Make links black
s = s.replace('color: var(--text-nav);', 'color: #000000;\n  font-weight: bold;')
s = s.replace('.nav-toggle {\n  width: 32px;\n  height: 24px;\n  background: transparent;\n  border: none;\n  cursor: pointer;\n  display: none;\n  position: relative;\n  z-index: 1000;\n  color: #fff;', '.nav-toggle {\n  width: 32px;\n  height: 24px;\n  background: transparent;\n  border: none;\n  cursor: pointer;\n  display: none;\n  position: relative;\n  z-index: 1000;\n  color: #000;')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(s)
