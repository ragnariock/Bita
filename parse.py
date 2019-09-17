import re
with open('site.html') as html:
    content = html.read()
    matches = re.findall(r'\ssrc="([^"]+)"', content)
    matches = ' '.join(matches)

print(matches)