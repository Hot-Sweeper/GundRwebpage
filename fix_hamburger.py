with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Hamburger is white initially, make it black
css = css.replace('.hamburger {\n  display: none;\n  background: none;\n  border: none;\n  color: #fff;', '.hamburger {\n  display: none;\n  background: none;\n  border: none;\n  color: #000;')

# Theme toggle
css = css.replace('.theme-toggle {\n  background: none;\n  border: none;\n  cursor: pointer;\n  color: rgba(255, 255, 255, 0.7);', '.theme-toggle {\n  background: none;\n  border: none;\n  cursor: pointer;\n  color: #000;')
css = css.replace('.theme-toggle:hover {\n  color: #fff;\n  background-color: rgba(255,255,255,0.12);', '.theme-toggle:hover {\n  color: #000;\n  background-color: rgba(0,0,0,0.12);')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
