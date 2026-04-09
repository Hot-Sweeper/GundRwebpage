with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Generic button fixes
css = re.sub(r'\.btn-primary \{\s*\n\s*background-color:[^;]+;\s*\n\s*color:[^;]+;', '.btn-primary {\n  background-color: var(--accent);\n  color: var(--accent-text);', css)
css = re.sub(r'\.btn-primary:hover \{\s*\n\s*background-color:[^;]+;\s*\n\s*color:[^;]+;', '.btn-primary:hover {\n  background-color: var(--accent-hover);\n  color: var(--accent-text);', css)

# Make sure outline button works
css = re.sub(r'\.btn-outline \{\s*\n\s*background-color: transparent;\s*\n\s*color: var\(--text-primary\);\s*\n\s*border: [^;]+;', '.btn-outline {\n  background-color: transparent;\n  color: var(--text-primary);\n  border: 3px solid var(--text-primary);', css)

# Inside CTA banner, buttons must contrast
# Because CTA banner is lime green (var(--accent)), buttons inside it should be inverted or dark.
if '.cta-banner .btn-primary' not in css:
    css += '''\n
.cta-banner .btn-primary {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  border-color: var(--bg-primary);
}
.cta-banner .btn-primary:hover {
  background-color: var(--bg-secondary);
  color: var(--text-primary);
  border-color: var(--bg-secondary);
}

.cta-banner .btn--secondary {
  background-color: transparent;
  color: var(--accent-text);
  border-color: var(--accent-text);
}
.cta-banner .btn--secondary:hover {
  background-color: var(--accent-text);
  color: var(--accent);
}
'''

with open('website/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
