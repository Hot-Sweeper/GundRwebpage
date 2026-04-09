import re

with open('website/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix borders everywhere
css = re.sub(r'border: [0-9]+px solid #[0-9a-fA-F]{3,6};', 'border: 3px solid var(--border);', css)
css = css.replace('border-bottom: 3px solid var(--border);', 'border-bottom: 3px solid var(--border-nav);')
css = css.replace('border-bottom: 3px solid #000;', 'border-bottom: 3px solid var(--border-nav);')

# Fix text colors hardcoded to black or white
css = re.sub(r'color: #000(?:000)?;', 'color: var(--text-primary);', css)
css = re.sub(r'color: #fff(?:fff)?;', 'color: var(--bg-primary);', css) # usually #fff meant white bg equivalent, but wait: if they wanted white text in dark mode... better to use var(--text-primary)
# Let's be smart. 

# Re-read and apply specific fixes
