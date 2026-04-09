with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make hamburger bar black
css = css.replace('.hamburger__bar {\n  width: 24px;\n  height: 2px;\n  background-color: #fff;', '.hamburger__bar {\n  width: 24px;\n  height: 2px;\n  background-color: #000;')

# Make theme toggle black explicitly
css = css.replace('color: rgba(255, 255, 255, 0.7);', 'color: #000;')

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
