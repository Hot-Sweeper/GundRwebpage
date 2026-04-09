with open('website/css/variables.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the nav white and text black
css = css.replace('--nav-bg:        #000000;', '--nav-bg:        #ffffff;')
css = css.replace('--nav-bg-scroll: rgba(0, 0, 0, 0.95);', '--nav-bg-scroll: #ffffff;')
css = css.replace('--text-nav:       #ffffff;', '--text-nav:       #000000;')

with open('website/css/variables.css', 'w', encoding='utf-8') as f:
    f.write(css)
