with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Force solid CTA banner and black text
import re
css = re.sub(r'\.cta-banner \{\n\s*background: linear-gradient[^;]+;', '.cta-banner {\n    background-color: var(--accent);', css)

# title
css = re.sub(r'\.cta-banner__title \{\n\s*color: var\(--text-primary\);', '.cta-banner__title {\n    color: var(--accent-text);', css)

# sub
css = re.sub(r'\.cta-banner__sub \{\n\s*color: rgba\(255,255,255,0\.85\);', '.cta-banner__sub {\n    color: var(--accent-text);', css)

# Any other rgba
css = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*[0-9.]+\s*\);', 'color: var(--text-nav);', css)

# Look at .about__badge just in case my replace didn't hit
css = re.sub(r'\.about__badge \{\s*\n[^{]*color: var\(--text-primary\);', '.about__badge {\n    position: absolute;\n    bottom: 1.5rem;\n    left: 1.5rem;\n    background-color: var(--accent);\n    color: var(--accent-text);', css)

# The about stat label, maybe they are green too? 
# Wait, .about__stat is background-color: var(--bg-secondary) so it's fine.

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
