import re

with open('website/team.html', 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(
    r'<div class="team-card (.*?)">\s*'
    r'<div class="team-card__photo-placeholder">(.*?)</div>\s*'
    r'<div class="team-card__body">\s*(.*?)\s*</div>\s*'
    r'</div>',
    re.DOTALL
)

def replacer(match):
    classes = match.group(1)
    placeholder = match.group(2)
    body = match.group(3)
    
    # Extract name for the back of the card
    name_match = re.search(r'<div class="team-card__name">(.*?)</div>', body)
    name = name_match.group(1) if name_match else "Team Member"
    
    # For the front, keep the picture and just the name & role.
    # The back will show the details.
    
    return f'''<div class="team-card {classes}">
        <div class="team-card-inner">
          <div class="team-card-front">
            <div class="team-card__photo-placeholder">{placeholder}</div>
            <div class="team-card__body">
              <div class="team-card__name">{name}</div>
              <div class="team-card__role">Mehr Infos (Hover)</div>
            </div>
          </div>
          <div class="team-card-back">
            {body}
          </div>
        </div>
      </div>'''

new_html = pattern.sub(replacer, html)

with open('website/team.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done updating team.html regex")
