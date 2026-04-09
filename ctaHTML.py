import glob
import re

for file in glob.glob('website/*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # The inline style for Beratungsgespräch in CTA banner
    html = re.sub(r'class="btn" style="background:rgba\(255,255,255,0\.2\);color:#fff;border:2px solid rgba\(255,255,255,0\.4\);"', 'class="btn btn--secondary"', html)
    html = re.sub(r'class="btn btn-outline"', 'class="btn btn--primary"', html) # Wait, typically "jetzt anmelden" should be primary, but it might be outline. Let's make it primary.
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
