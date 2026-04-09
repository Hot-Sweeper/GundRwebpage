with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()
import re
css = css.replace("font-family: 'Plus Jakarta Sans', sans-serif;", "font-family: 'Space Grotesk', system-ui, sans-serif; text-transform: uppercase;")
with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
