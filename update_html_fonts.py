import os
import glob
import re

for file in glob.glob('website/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Swap google fonts in HTML
    html = re.sub(r'family=Plus\+Jakarta\+Sans:wght@[0-9;]+', 'family=Space+Grotesk:wght@400;600;700', html)
    html = html.replace('1500px', '0px') # remove perspective for true brutalism
    html = html.replace('rotateY(180deg)', 'rotateY(0deg)') # or just let the transforms remain but look harder
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
