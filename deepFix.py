import re

with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Nav Links invisible issue
css = re.sub(r'color: rgba\(255, \s*255, \s*255, \s*0\.85\);', 'color: var(--text-nav);', css)
css = re.sub(r'color: rgba\(255, \s*255, \s*255, \s*0\.7\);', 'color: var(--text-nav);', css)
css = re.sub(r'color: rgba\(255, \s*255, \s*255, \s*0\.75\);', 'color: var(--text-nav);', css)
# If hover was rgba white, let's use a subtle text-nav border or something, or background-color text-nav with opacity
css = css.replace('background-color: rgba(255, 255, 255, 0.12);', 'background-color: transparent;\n    border-bottom: 2px solid var(--text-nav);')
css = css.replace('background-color: rgba(255,255,255,0.1);', 'background-color: transparent;\n    border-left: 2px solid var(--text-nav);')

# 2. CTA Banner Ass Gradient -> Solid Brutalist Accent
css = re.sub(r'background: linear-gradient\(135deg, var\(--accent\) 0%, [^)]+\);', 'background-color: var(--accent);', css)
# Make CTA banner text black and button black
css = re.sub(r'\.cta-banner__title \{\n[^{]* color: #ffffff;', '.cta-banner__title {\n  font-size: 2.5rem;\n  font-weight: 800;\n  margin-bottom: 0.5rem;\n  color: var(--accent-text);', css)
css = css.replace('.cta-banner__desc {\n  font-size: 1.1rem;\n  color: rgba(255, 255, 255, 0.85);', '.cta-banner__desc {\n  font-size: 1.1rem;\n  color: var(--accent-text);')
# Replace CTA text
css = css.replace('.cta-banner__title {\n  font-size: 2rem;\n  font-weight: 800;\n  margin-bottom: 0.5rem;\n  color: #ffffff;\n}', '.cta-banner__title {\n  font-size: 2rem;\n  font-weight: 800;\n  margin-bottom: 0.5rem;\n  color: var(--accent-text);\n}')

# 3. About Badge (35+ Jahre) white text on lime green
css = css.replace('.about__badge {\n    position: absolute;\n    bottom: 1.5rem;\n    left: 1.5rem;\n    background-color: var(--accent);\n    color: var(--text-primary);', '.about__badge {\n    position: absolute;\n    bottom: 1.5rem;\n    left: 1.5rem;\n    background-color: var(--accent);\n    color: var(--accent-text);')

# Force cta banner buttons to have black text
css = css.replace('.btn--secondary {\n  background-color: var(--bg-primary);\n  color: var(--text-primary);\n  border-color: var(--border);\n', '.btn--secondary {\n  background-color: var(--bg-primary);\n  color: var(--text-primary);\n  border-color: var(--border);\n')

css = css.replace('.cta-banner .btn--secondary {\n  background-color: transparent;\n  color: #fff;\n  border-color: #fff;\n}', '.cta-banner .btn--secondary {\n  background-color: transparent;\n  color: var(--accent-text);\n  border-color: var(--accent-text);\n}')
css = css.replace('.cta-banner .btn--secondary:hover {\n  background-color: #fff;\n  color: var(--accent);\n}', '.cta-banner .btn--secondary:hover {\n  background-color: var(--accent-text);\n  color: var(--accent);\n}')

# 4. Erste hilfe box
css = re.sub(r'\.erste-hilfe-box \{\n\s*background: linear-gradient[^;]+;', '.erste-hilfe-box {\n    background: var(--bg-secondary);', css)


with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
