with open('website/team.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_sig = '<div class="team-grid">'
end_sig = '</section>'
start_idx = html.find(start_sig)
end_idx = html.find(end_sig, start_idx)

new_grid = '''<div class="team-grid">
      <!-- Peter Rothmeier -->
      <div class="team-card reveal stagger-1">
        <div class="team-card-inner">
          <div class="team-card-front">
            <div class="team-card__photo-placeholder">
              <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>
            </div>
            <div class="team-card__body">
              <div class="team-card__name">Peter Rothmeier</div>
              <div class="team-card__role">Mehr Infos (Hover)</div>
            </div>
          </div>
          <div class="team-card-back">
              <div class="team-card__name">Peter Rothmeier</div>
              <div class="team-card__role" style="margin-top:0.25rem;">Inhaber &amp; Fahrlehrer</div>
              <p class="team-card__classes" style="margin-top:1rem;">Klassen:<br> B, B96, BE, Mofa, AM, A1, B196, A2, A, L</p>
              <p class="team-card__since">Seit April 1990</p>
              <a href="tel:016090860033" class="team-card__phone">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.15 13 19.79 19.79 0 0 1 1.07 4.4 2 2 0 0 1 3 2.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 21 16z"/></svg>
                0160 90860033
              </a>
          </div>
        </div>
      </div>

      <!-- Dennis Rothmeier -->
      <div class="team-card reveal stagger-2">
        <div class="team-card-inner">
          <div class="team-card-front">
            <div class="team-card__photo-placeholder">
              <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>
            </div>
            <div class="team-card__body">
              <div class="team-card__name">Dennis Rothmeier</div>
              <div class="team-card__role">Mehr Infos (Hover)</div>
            </div>
          </div>
          <div class="team-card-back">
              <div class="team-card__name">Dennis Rothmeier</div>
              <div class="team-card__role" style="margin-top:0.25rem;">Fahrlehrer</div>
              <p class="team-card__classes" style="margin-top:1rem;">Klassen:<br> B, B96, BE, Mofa, AM, A1, B196, A2, A, L</p>
              <p class="team-card__since">Seit September 2009</p>
              <a href="tel:017662659792" class="team-card__phone">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.15 13 19.79 19.79 0 0 1 1.07 4.4 2 2 0 0 1 3 2.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 21 16z"/></svg>
                0176 62659792
              </a>
          </div>
        </div>
      </div>

      <!-- Claus Altzweig -->
      <div class="team-card reveal stagger-3">
        <div class="team-card-inner">
          <div class="team-card-front">
            <div class="team-card__photo-placeholder">
              <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>
            </div>
            <div class="team-card__body">
              <div class="team-card__name">Claus Altzweig</div>
              <div class="team-card__role">Mehr Infos (Hover)</div>
            </div>
          </div>
          <div class="team-card-back">
              <div class="team-card__name">Claus Altzweig</div>
              <div class="team-card__role" style="margin-top:0.25rem;">Fahrlehrer</div>
              <p class="team-card__classes" style="margin-top:1rem;">Klassen:<br> B, BE</p>
              <p class="team-card__since">Seit November 1989</p>
              <a href="tel:01773315254" class="team-card__phone">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.15 13 19.79 19.79 0 0 1 1.07 4.4 2 2 0 0 1 3 2.18h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L7.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 21 16z"/></svg>
                0177 3315254
              </a>
          </div>
        </div>
      </div>

      <!-- Sascha Dorst -->
      <div class="team-card reveal stagger-4">
        <div class="team-card-inner">
          <div class="team-card-front">
            <div class="team-card__photo-placeholder">
              <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 1 0-16 0"/></svg>
            </div>
            <div class="team-card__body">
              <div class="team-card__name">Sascha Dorst</div>
              <div class="team-card__role">Mehr Infos (Hover)</div>
            </div>
          </div>
          <div class="team-card-back">
              <div class="team-card__name">Sascha Dorst</div>
              <div class="team-card__role" style="margin-top:0.25rem;">Fahrlehrer</div>
              <p class="team-card__classes" style="margin-top:1rem;">Klassen:<br> B, BE, Mofa, AM, A1, B196, A2, A</p>
              <p class="team-card__since">Info folgt</p>
          </div>
        </div>
      </div>
    </div>
  '''

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_grid + "\n" + html[end_idx:]
    with open('website/team.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Restored and updated team.html safely.")
else:
    print("Could not find start/end")
