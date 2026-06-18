# -*- coding: utf-8 -*-
"""
将界面配色从暗色青绿主题改为浅色白橙主题
"""
import os, re

DIR = r'D:\夸克\3'
OUT = os.path.join(DIR, 'index.html')

with open(OUT, 'r', encoding='utf-8') as f:
    c = f.read()

# ============================================================
# 1. CSS 变量 — 浅色白橙主题
# ============================================================
old_vars = """:root {
  --bg-deep:#070b14;--bg-base:#0c1220;--bg-card:#111827;--bg-card-hover:#1a2332;
  --bg-surface:#1e293b;--border:#1e293b;--border-light:#2d3a4d;
  --text-primary:#f1f5f9;--text-secondary:#94a3b8;--text-muted:#64748b;
  --accent-green:#22c55e;--accent-green-dim:rgba(34,197,94,.12);
  --accent-blue:#38bdf8;--accent-blue-dim:rgba(56,189,248,.12);
  --accent-orange:#f59e0b;--accent-orange-dim:rgba(245,158,11,.12);
  --accent-red:#ef4444;--accent-red-dim:rgba(239,68,68,.12);
  --accent-cyan:#22d3ee;--accent-cyan-dim:rgba(34,211,238,.12);
  --accent-purple:#a78bfa;
  --sidebar-w:220px;--header-h:56px;--radius:8px;--radius-lg:12px;
  --font-data:"Fira Code","Noto Sans SC",monospace;
  --font-ui:"Noto Sans SC",-apple-system,sans-serif;
  --transition:.2s ease;
}"""

new_vars = """:root {
  --bg-deep:#fafafa;--bg-base:#ffffff;--bg-card:#ffffff;--bg-card-hover:#fff7ed;
  --bg-surface:#f3f4f6;--border:#e5e7eb;--border-light:#d1d5db;
  --text-primary:#1a1a2e;--text-secondary:#6b7280;--text-muted:#9ca3af;
  --accent-green:#16a34a;--accent-green-dim:rgba(22,163,74,.10);
  --accent-blue:#2563eb;--accent-blue-dim:rgba(37,99,235,.10);
  --accent-orange:#f59e0b;--accent-orange-dim:rgba(245,158,11,.10);
  --accent-red:#ef4444;--accent-red-dim:rgba(239,68,68,.10);
  --accent-cyan:#f59e0b;--accent-cyan-dim:rgba(245,158,11,.10);
  --accent-purple:#8b5cf6;
  --sidebar-w:220px;--header-h:56px;--radius:8px;--radius-lg:12px;
  --font-data:"Fira Code","Noto Sans SC",monospace;
  --font-ui:"Noto Sans SC",-apple-system,sans-serif;
  --transition:.2s ease;
}"""

c = c.replace(old_vars, new_vars)

# ============================================================
# 2. CSS 组件样式调整
# ============================================================

# 侧边栏 — 白色底部栏 + 橙色阴影
c = c.replace(
    '.sidebar{width:100%;height:56px;background:var(--bg-base);border-top:1px solid var(--border)',
    '.sidebar{width:100%;height:56px;background:#fff;border-top:1px solid var(--border);box-shadow:0 -2px 12px rgba(0,0,0,.06)'
)
# nav active → orange
c = c.replace('.nav-item.active{color:var(--accent-green)}', '.nav-item.active{color:var(--accent-orange)}')
c = c.replace('.nav-item.active::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:20px;height:2px;background:var(--accent-green)',
              '.nav-item.active::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:20px;height:2px;background:var(--accent-orange)')

# Header — 白底
c = c.replace(
    '.header{height:var(--header-h);background:var(--bg-base);border-bottom:1px solid var(--border)',
    '.header{height:var(--header-h);background:#fff;border-bottom:1px solid var(--border);box-shadow:0 1px 4px rgba(0,0,0,.04)'
)
# Header status → orange
c = c.replace('.header-status{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--accent-green)}',
              '.header-status{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--accent-orange)}')
c = c.replace('.header-status .dot{width:8px;height:8px;background:var(--accent-green)',
              '.header-status .dot{width:8px;height:8px;background:var(--accent-orange)')

# Card hover shadow
c = c.replace(
    '.data-card:hover{border-color:var(--border-light);transform:translateY(-1px)}',
    '.data-card:hover{border-color:var(--accent-orange);transform:translateY(-2px);box-shadow:0 4px 16px rgba(245,158,11,.10)}'
)

# Section hover
c = c.replace(
    '.section{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px;margin-bottom:20px}',
    '.section{background:#fff;border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px;margin-bottom:20px;box-shadow:0 1px 3px rgba(0,0,0,.04)}'
)

# Buttons — primary → orange
c = c.replace('.btn-primary{background:var(--accent-green);color:#000;border-color:var(--accent-green);font-weight:600}',
              '.btn-primary{background:var(--accent-orange);color:#fff;border-color:var(--accent-orange);font-weight:600}')
c = c.replace('.btn-primary:hover{background:#16a34a}', '.btn-primary:hover{background:#d97706}')
c = c.replace('.btn:hover{background:var(--bg-card-hover);color:var(--text-primary);border-color:var(--border-light)}',
              '.btn:hover{background:#fff7ed;color:var(--accent-orange);border-color:var(--accent-orange)}')

# Form focus → orange
c = c.replace('.form-input:focus{outline:none;border-color:var(--accent-green)}',
              '.form-input:focus{outline:none;border-color:var(--accent-orange)}')

# WQI ring → orange
c = c.replace('.wqi-ring{width:100px;height:100px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;border:3px solid var(--accent-green)',
              '.wqi-ring{width:100px;height:100px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;border:3px solid var(--accent-orange)')
c = c.replace('.wqi-score{font-family:var(--font-data);font-size:28px;font-weight:700;color:var(--accent-green)}',
              '.wqi-score{font-family:var(--font-data);font-size:28px;font-weight:700;color:var(--accent-orange)}')

# Heatmap bar
c = c.replace('background:linear-gradient(90deg,#22c55e,#eab308,#ef4444)',
              'background:linear-gradient(90deg,#f59e0b,#ef4444)')

# Pond card hover → orange
c = c.replace('.pond-card:hover{border-color:var(--accent-cyan)',
              '.pond-card:hover{border-color:var(--accent-orange)')

# Robot avatar → orange
c = c.replace('.robot-avatar{width:56px;height:56px;border-radius:var(--radius-lg);background:var(--accent-cyan-dim)',
              '.robot-avatar{width:56px;height:56px;border-radius:var(--radius-lg);background:var(--accent-orange-dim)')
c = c.replace('.robot-avatar i{width:28px;height:28px;color:var(--accent-cyan)}',
              '.robot-avatar i{width:28px;height:28px;color:var(--accent-orange)}')

# Report card hover
c = c.replace('.report-card:hover{border-color:var(--accent-cyan)',
              '.report-card:hover{border-color:var(--accent-orange)')

# Hero accent → orange
c = c.replace('.hero-title .accent{color:var(--accent-cyan)}',
              '.hero-title .accent{color:var(--accent-orange)}')

# Table hover
c = c.replace('.data-table tr:hover td{background:rgba(255,255,255,.02)}',
              '.data-table tr:hover td{background:#fff7ed}')

# Tabs active
c = c.replace('.tab.active{background:var(--bg-card);color:var(--text-primary)}',
              '.tab.active{background:#fff;color:var(--accent-orange);font-weight:600}')

# Scrollbar
c = c.replace('::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:var(--border)',
              '::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:#f3f4f6}::-webkit-scrollbar-thumb{background:#d1d5db')

# Glass card
c = c.replace('.glass-card{background:rgba(17,24,39,.85)',
              '.glass-card{background:rgba(255,255,255,.90)')

# ============================================================
# 3. JS 硬编码颜色 — ECharts 图表
# ============================================================

# ECharts 背景和文字
c = c.replace('backgroundColor:"transparent"', 'backgroundColor:"transparent"')

# ECharts 坐标轴颜色 (dark → light)
c = c.replace('axisLine:{lineStyle:{color:"#1e293b"}}', 'axisLine:{lineStyle:{color:"#e5e7eb"}}')
c = c.replace('splitLine:{lineStyle:{color:"#1e293b"}}', 'splitLine:{lineStyle:{color:"#f3f4f6"}}')
c = c.replace('axisLabel:{color:"#64748b"', 'axisLabel:{color:"#9ca3af"')
c = c.replace('axisName:{color:"#94a3b8"', 'axisName:{color:"#6b7280"')
c = c.replace('splitArea:{areaStyle:{color:["rgba(30,41,59,.3)","rgba(30,41,59,.15)"]}}',
              'splitArea:{areaStyle:{color:["rgba(245,158,11,.05)","rgba(245,158,11,.02)"]}}')
c = c.replace('splitLine:{lineStyle:{color:"#1e293b"}}', 'splitLine:{lineStyle:{color:"#f3f4f6"}}')

# ECharts tooltip — light style
c = c.replace('tooltip:{trigger:"axis",backgroundColor:"#1e293b",borderColor:"#334155",textStyle:{color:"#f1f5f9"',
              'tooltip:{trigger:"axis",backgroundColor:"#fff",borderColor:"#e5e7eb",textStyle:{color:"#1a1a2e"')
c = c.replace('tooltip:{backgroundColor:"#1e293b",borderColor:"#334155",textStyle:{color:"#f1f5f9"',
              'tooltip:{backgroundColor:"#fff",borderColor:"#e5e7eb",textStyle:{color:"#1a1a2e"')

# ECharts legend text
c = c.replace('textStyle:{color:"#94a3b8"', 'textStyle:{color:"#6b7280"')

# 溶氧趋势线 — green → orange
c = c.replace('lineStyle:{color:"#22c55e",width:2}', 'lineStyle:{color:"#f59e0b",width:2}')
c = c.replace('areaStyle:{color:{type:"linear",x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:"rgba(34,197,94,.25)"},{offset:1,color:"rgba(34,197,94,0)"}]}}',
              'areaStyle:{color:{type:"linear",x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:"rgba(245,158,11,.20)"},{offset:1,color:"rgba(245,158,11,0)"}]}}')

# 安全线 — red stays red
# (no change needed)

# 雷达图
c = c.replace('areaStyle:{color:"rgba(34,197,94,.15)"', 'areaStyle:{color:"rgba(245,158,11,.12)"')
c = c.replace('lineStyle:{color:"#22c55e"}', 'lineStyle:{color:"#f59e0b"}')
c = c.replace('itemStyle:{color:"#22c55e"', 'itemStyle:{color:"#f59e0b"')

# 柱状图 — 各鱼塘溶氧对比
c = c.replace('itemStyle:{color:"#22c55e"}', 'itemStyle:{color:"#f59e0b"}')

# 多参数曲线
c = c.replace('name:"溶氧",type:"line"', 'name:"溶氧",type:"line"')  # no change
# pH 紫色保持
# 水温橙色保持

# 机器人电量趋势 — 青色→橙色
c = c.replace('name:"AquaBot-01",type:"line"', 'name:"AquaBot-01",type:"line"')
c = c.replace('lineStyle:{color:"#22d3ee",width:2}', 'lineStyle:{color:"#f59e0b",width:2}')
c = c.replace('itemStyle:{color:"#22d3ee"', 'itemStyle:{color:"#f59e0b"')

# ============================================================
# 4. JS 硬编码颜色 — Three.js 场景
# ============================================================

# 场景背景 — dark → light blue-white
c = c.replace('scene.background=new THREE.Color(0x070b14)', 'scene.background=new THREE.Color(0xf0f4f8)')
c = c.replace('scene.fog=new THREE.FogExp2(0x070b14,0.015)', 'scene.fog=new THREE.FogExp2(0xf0f4f8,0.012)')

# 环境光 — 更亮
c = c.replace('new THREE.AmbientLight(0x4488aa,0.6)', 'new THREE.AmbientLight(0xffffff,0.7)')

# 地面 — 深绿 → 浅绿
c = c.replace('new THREE.MeshStandardMaterial({color:0x1a2a1a,roughness:0.9})',
              'new THREE.MeshStandardMaterial({color:0x8bc34a,roughness:0.8})')

# 岸边 — 深棕 → 浅棕
c = c.replace('new THREE.MeshStandardMaterial({color:0x3d2b1f,roughness:1})',
              'new THREE.MeshStandardMaterial({color:0xd7ccc8,roughness:0.9})')

# 水面 — 深蓝 → 浅蓝
c = c.replace('new THREE.MeshPhongMaterial({color:0x0c4a6e,transparent:true,opacity:0.85,shininess:100,specular:0x22d3ee',
              'new THREE.MeshPhongMaterial({color:0x4fc3f7,transparent:true,opacity:0.75,shininess:80,specular:0xffffff')

# 传感器柱 — 青色 → 橙色
c = c.replace('new THREE.MeshStandardMaterial({color:0x22d3ee,emissive:0x22d3ee,emissiveIntensity:0.3})',
              'new THREE.MeshStandardMaterial({color:0xf59e0b,emissive:0xf59e0b,emissiveIntensity:0.3})')
c = c.replace('new THREE.MeshBasicMaterial({color:0x22d3ee})', 'new THREE.MeshBasicMaterial({color:0xf59e0b})')

# 机器人 — 绿色 → 橙色
c = c.replace('new THREE.MeshStandardMaterial({color:0x22c55e,emissive:0x22c55e,emissiveIntensity:0.2})',
              'new THREE.MeshStandardMaterial({color:0xf59e0b,emissive:0xf59e0b,emissiveIntensity:0.2})')
c = c.replace('new THREE.MeshStandardMaterial({color:0x16a34a})', 'new THREE.MeshStandardMaterial({color:0xe65100})')

# 巡游路径 — 绿色 → 橙色
c = c.replace('new THREE.MeshBasicMaterial({color:0x22c55e,transparent:true,opacity:0.3})',
              'new THREE.MeshBasicMaterial({color:0xf59e0b,transparent:true,opacity:0.25})')

# 热力图色相 — 从绿色系(0.35)改为橙色系(0.08)
c = c.replace('new THREE.Color().setHSL(0.35-v*0.35,0.8,0.4+v*0.2)',
              'new THREE.Color().setHSL(0.08-v*0.08,0.9,0.5+v*0.2)')
c = c.replace('p.m.material.color.setHSL(0.35-v*0.35,0.8,0.4+v*0.2)',
              'p.m.material.color.setHSL(0.08-v*0.08,0.9,0.5+v*0.2)')

# 顶灯 — 青色 → 暖白
c = c.replace('new THREE.PointLight(0x22d3ee,0.5,30)', 'new THREE.PointLight(0xffcc80,0.4,30)')

# ============================================================
# 5. JS 渲染函数中的颜色映射
# ============================================================

# renderSensorCards / renderMonitorCards 中的 normal 状态颜色 → orange
c = c.replace('normal:"var(--accent-green)"', 'normal:"var(--accent-orange)"')
# 但保留 green 用于 normal status 的 badge

# renderRobots 中的电池颜色
c = c.replace('(r.battery>50?"var(--accent-green)":"var(--accent-orange)")',
              '(r.battery>50?"var(--accent-orange)":"var(--accent-red)")')

# ============================================================
# 6. HTML 内联样式中的颜色
# ============================================================

# Hero stats 颜色
c = c.replace('style="color:var(--accent-green)">12+', 'style="color:var(--accent-orange)">12+')
c = c.replace('style="color:var(--accent-cyan)">24/7', 'style="color:var(--accent-orange)">24/7')

# SVG logo 颜色
c = c.replace('.sidebar-logo svg{width:28px;height:28px;color:var(--accent-cyan)}',
              '.sidebar-logo svg{width:28px;height:28px;color:var(--accent-orange)}')
c = c.replace('.footer-brand svg{width:24px;height:24px;color:var(--accent-cyan)}',
              '.footer-brand svg{width:24px;height:24px;color:var(--accent-orange)}')

# ============================================================
# Write
# ============================================================
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(c)

print(f'Done. File size: {len(c)} bytes')

# Verify key changes
checks = [
    ('Light background', '--bg-deep:#fafafa' in c),
    ('White cards', '--bg-card:#ffffff' in c),
    ('Orange accent', '--accent-orange:#f59e0b' in c),
    ('No dark bg', '#070b14' not in c),
    ('No dark card', '#111827' not in c),
    ('Orange nav active', 'nav-item.active{color:var(--accent-orange)}' in c),
    ('Orange btn-primary', 'btn-primary{background:var(--accent-orange)' in c),
    ('Orange Three bg', '0xf0f4f8' in c),
    ('Orange robot', '0xf59e0b' in c),
    ('Light ground', '0x8bc34a' in c),
    ('Light water', '0x4fc3f7' in c),
]
print('\nVerification:')
for label, ok in checks:
    print(f'  {"OK" if ok else "FAIL"}: {label}')
