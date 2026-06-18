# -*- coding: utf-8 -*-
import os
DIR = r'D:\夸克\3'
OUT = os.path.join(DIR, 'index.html')
with open(OUT, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Three.js version r160 -> r149 (r160 removed examples/js)
content = content.replace('three@0.160.0', 'three@0.149.0')

# Fix 2: Unicode encoding errors in titles
content = content.replace('\u6570\u5b57\u5b5a\u751f', '\u6570\u5b57\u5b5a\u751f')
content = content.replace('\u6570\u5b57\u5b5a\u751f', '\u6570\u5b57\u5b5a\u751f')
# Try fixing the literal characters too
content = content.replace('\u5b5a', '\u5b6a')

# Fix 3: Fix twin page HTML - add proper closing divs
# The twin page section needs proper closing
old_twin = '<div class="twin-container"><div class="twin-canvas-wrap"><canvas id="twinCanvas"></canvas><div class="twin-overlay">'
new_twin = '<div class="twin-container">\n<div class="twin-canvas-wrap">\n<canvas id="twinCanvas"></canvas>\n<div class="twin-overlay">'
content = content.replace(old_twin, new_twin)

# Fix 4: Make sure page-twin is properly closed before page-robot
# Find the page-twin section and fix its closing
twin_marker = 'id="page-twin"'
if twin_marker in content:
    # Find the twin page start
    twin_start = content.index(twin_marker)
    # Find the next page start (page-robot)
    robot_marker = 'id="page-robot"'
    if robot_marker in content:
        robot_start = content.index(robot_marker)
        # Extract the twin section
        twin_section = content[twin_start:robot_start]
        
        # Count open/close divs
        opens = twin_section.count('<div')
        closes = twin_section.count('</div>')
        print(f'Twin section: {opens} opens, {closes} closes, diff={opens-closes}')
        
        # If there are unclosed divs, add closing divs before page-robot
        if opens > closes:
            missing = opens - closes
            print(f'Adding {missing} closing divs')
            # Find the line just before page-robot
            before_robot = content[:robot_start]
            # Add closing divs
            closers = '</div>' * missing
            content = before_robot + closers + '\n' + content[robot_start:]

# Fix 5: Ensure proper script placement - move inline script before </body>
# Check if script is in the right place
body_close = '</body>'
script_tag = '<script>'
last_script = content.rfind(script_tag)
last_body = content.rfind(body_close)

if last_script > 0 and last_body > 0:
    if last_script > last_body:
        print('WARNING: Script is after </body>!')
    else:
        print('Script placement OK')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed. Size:', os.path.getsize(OUT), 'bytes')
