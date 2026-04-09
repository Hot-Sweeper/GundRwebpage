with open('website/css/variables.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = '''/* ===================================================
   Fahrschule G&R — CSS Custom Properties (Brutalist)
   =================================================== */

:root {
  /* === 60% Dominant (surfaces) === */
  --bg-primary:   #090909;
  --bg-secondary: #000000;
  --bg-card:      #111111;

  /* === 30% Secondary (structural) === */
  --nav-bg:        #000000;
  --nav-bg-scroll: rgba(0, 0, 0, 0.95);
  --footer-bg:     #000000;
  --footer-surface:#0a0a0a;

  /* === 10% Accent (brand) === */
  --accent:       #bcee00;
  --accent-hover: #ccff00;
  --accent-dark:  #a6db00;
  --accent-light: rgba(188, 238, 0, 0.15);

  /* === Typography === */
  /* For brutalist try uppercase and thick */
  --text-primary:   #ffffff;
  --text-secondary: #cccccc;
  --text-muted:     #888888;
  --text-nav:       #ffffff;
  --text-footer:    #dddddd;

  /* === Borders & Shadows === */
  --border:        #333333;
  --border-focus:  var(--accent);
  
  /* Hard brutalist shadows */
  --shadow-sm:     3px 3px 0 var(--accent);
  --shadow-md:     5px 5px 0 var(--accent);
  --shadow-lg:     8px 8px 0 var(--accent);
  --shadow-card:   6px 6px 0 var(--accent);
  --shadow-card-hover: 12px 12px 0 var(--accent-hover);

  /* === Spacing === */
  --space-xs:  0.5rem;
  --space-sm:  1rem;
  --space-md:  1.5rem;
  --space-lg:  2.5rem;
  --space-xl:  4rem;
  --space-2xl: 6rem;

  /* === Radius === */
  --radius-sm:   0px;
  --radius-md:   0px;
  --radius-lg:   0px;
  --radius-full: 0px;

  /* === Transitions === */
  --transition-fast:   100ms linear;
  --transition-base:   150ms linear;
  --transition-slow:   200ms linear;
}

[data-theme="dark"] {
  --bg-primary:   #000000;
  --bg-secondary: #0a0a0a;
  --bg-card:      #111111;

  --text-primary:   #ffffff;
  --text-secondary: #dddddd;
  --text-muted:     #999999;

  --border:        #444444;
  --shadow-sm:     3px 3px 0 var(--accent);
  --shadow-md:     5px 5px 0 var(--accent);
  --shadow-lg:     8px 8px 0 var(--accent);
  --shadow-card:   6px 6px 0 var(--accent);
  --shadow-card-hover: 12px 12px 0 var(--accent-hover);
}
'''

# We'll just overwrite it to keep it clean.
import re
# Keep the fonts if they are there
fonts = ""
if "/* === Fonts" in css:
    pass # we can assume there are no other blocks, wait, let's just write the whole file.

with open('website/css/variables.css', 'w', encoding='utf-8') as f:
    f.write(new_css)
