# -*- coding: utf-8 -*-
import os

DIR = r'D:\夸克\3'
f = os.path.join(DIR, 'index.html')

with open(f, 'r', encoding='utf-8') as fh:
    html = fh.read()

# 1. Replace sidebar CSS: left -> bottom
old_sidebar_css = """.sidebar{width:var(--sidebar-w);height:100vh;background:var(--bg-base);border-right:1px solid var(--border);display:flex;flex-direction:column;position:fixed;left:0;top:0;z-index:100}
.sidebar-logo{height:var(--header-h);display:flex;align-items:center;gap:10px;padding:0 20px;border-bottom:1px solid var(--border)}
.sidebar-logo svg{width:28px;height:28px;color:var(--accent-cyan)}
.sidebar-logo span{font-size:15px;font-weight:600;letter-spacing:.5px}
.sidebar-nav{flex:1;padding:12px 10px;overflow-y:auto}
.nav-group-label{font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px;padding:16px 12px 6px;font-weight:600}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:var(--radius);cursor:pointer;transition:all var(--transition);color:var(--text-secondary);font-size:14px;margin-bottom:2px;text-decoration:none;position:relative}
.nav-item:hover{background:var(--bg-surface);color:var(--text-primary)}
.nav-item.active{background:var(--accent-green-dim);color:var(--accent-green)}
.nav-item.active::before{content:"";position:absolute;left:0;top:8px;bottom:8px;width:3px;background:var(--accent-green);border-radius:2px}
.nav-item i{width:20px;height:20px;flex-shrink:0}
.nav-badge{margin-left:auto;background:var(--accent-red);color:#fff;font-size:11px;padding:1px 7px;border-radius:10px;font-weight:600}"""

new_sidebar_css = """.sidebar{width:100%;height:56px;background:var(--bg-base);border-top:1px solid var(--border);display:flex;align-items:center;justify-content:center;position:fixed;bottom:0;left:0;z-index:100}
.sidebar-logo{display:none}
.sidebar-nav{display:flex;align-items:center;gap:4px;padding:0 12px;overflow-x:auto}
.nav-group-label{display:none}
.nav-item{display:flex;flex-direction:column;align-items:center;gap:2px;padding:8px 16px;border-radius:var(--radius);cursor:pointer;transition:all var(--transition);color:var(--text-muted);font-size:11px;text-decoration:none;position:relative;white-space:nowrap}
.nav-item:hover{background:var(--bg-surface);color:var(--text-primary)}
.nav-item.active{color:var(--accent-green)}
.nav-item.active::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:20px;height:2px;background:var(--accent-green);border-radius:2px}
.nav-item i{width:20px;height:20px;flex-shrink:0}
.nav-item span{font-size:10px}
.nav-badge{position:absolute;top:2px;right:8px;background:var(--accent-red);color:#fff;font-size:9px;padding:0 5px;border-radius:8px;font-weight:600}"""

html = html.replace(old_sidebar_css, new_sidebar_css)

# 2. Replace main margin
html = html.replace('.main{margin-left:var(--sidebar-w)', '.main{margin-bottom:56px;margin-left:0')

# 3. Update responsive media queries
old_responsive = """@media(max-width:1200px){.cards-4{grid-template-columns:repeat(2,1fr)}.pond-grid{grid-template-columns:repeat(2,1fr)}.twin-container{grid-template-columns:1fr}.twin-sidebar{flex-direction:row;overflow-x:auto}}
@media(max-width:768px){.sidebar{width:60px}.sidebar-logo span,.nav-item span,.nav-group-label{display:none}.nav-item{justify-content:center;padding:12px}.main{margin-left:60px}.cards-4,.cards-3{grid-template-columns:1fr}.pond-grid,.report-card-grid{grid-template-columns:1fr}.hero-title{font-size:36px}.hero-stats{grid-template-columns:1fr 1fr}.footer-grid{grid-template-columns:1fr}}"""

new_responsive = """@media(max-width:1200px){.cards-4{grid-template-columns:repeat(2,1fr)}.pond-grid{grid-template-columns:repeat(2,1fr)}.twin-container{grid-template-columns:1fr}.twin-sidebar{flex-direction:row;overflow-x:auto}}
@media(max-width:768px){.sidebar{height:52px}.nav-item{padding:6px 10px}.nav-item span{display:none}.nav-item i{width:22px;height:22px}.main{margin-bottom:52px}.cards-4,.cards-3{grid-template-columns:1fr}.pond-grid,.report-card-grid{grid-template-columns:1fr}.hero-title{font-size:36px}.hero-stats{grid-template-columns:1fr 1fr}.footer-grid{grid-template-columns:1fr}}"""

html = html.replace(old_responsive, new_responsive)

# 4. Remove nav-group-label divs from HTML
import re
html = re.sub(r'<div class="nav-group-label">[^<]*</div>\n?', '', html)

with open(f, 'w', encoding='utf-8') as fh:
    fh.write(html)

print('Done. Size:', os.path.getsize(f), 'bytes')
