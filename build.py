# -*- coding: utf-8 -*-
import os

DIR = r'D:\夸克\3'
os.makedirs(DIR, exist_ok=True)

css = r"""
:root {
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
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;font-family:var(--font-ui);background:var(--bg-deep);color:var(--text-primary);overflow:hidden}
body{display:flex}

.sidebar{width:var(--sidebar-w);height:100vh;background:var(--bg-base);border-right:1px solid var(--border);display:flex;flex-direction:column;position:fixed;left:0;top:0;z-index:100}
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
.nav-badge{margin-left:auto;background:var(--accent-red);color:#fff;font-size:11px;padding:1px 7px;border-radius:10px;font-weight:600}

.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;height:100vh}
.header{height:var(--header-h);background:var(--bg-base);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 24px;flex-shrink:0}
.header-left{display:flex;align-items:center;gap:16px}
.header-title{font-size:16px;font-weight:600}
.header-breadcrumb{font-size:13px;color:var(--text-muted)}
.header-right{display:flex;align-items:center;gap:16px}
.header-time{font-family:var(--font-data);font-size:13px;color:var(--text-secondary);background:var(--bg-card);padding:5px 12px;border-radius:var(--radius)}
.header-status{display:flex;align-items:center;gap:6px;font-size:13px;color:var(--accent-green)}
.header-status .dot{width:8px;height:8px;background:var(--accent-green);border-radius:50%;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.content{flex:1;overflow-y:auto;padding:24px;background:var(--bg-deep)}
.page{display:none}.page.active{display:block}

.cards-row{display:grid;gap:16px;margin-bottom:20px}
.cards-4{grid-template-columns:repeat(4,1fr)}
.cards-3{grid-template-columns:repeat(3,1fr)}
.cards-2{grid-template-columns:repeat(2,1fr)}
.data-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px;position:relative;transition:all var(--transition);overflow:hidden}
.data-card:hover{border-color:var(--border-light);transform:translateY(-1px)}
.data-card-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px}
.data-card-label{font-size:13px;color:var(--text-muted);font-weight:500}
.data-card-icon{width:36px;height:36px;border-radius:var(--radius);display:flex;align-items:center;justify-content:center}
.data-card-icon i{width:20px;height:20px}
.data-card-value{font-family:var(--font-data);font-size:28px;font-weight:700;line-height:1;margin-bottom:4px}
.data-card-unit{font-size:13px;color:var(--text-muted);margin-left:4px;font-weight:400}
.data-card-status{display:flex;align-items:center;gap:4px;font-size:12px;margin-top:8px}
.data-card-status.normal{color:var(--accent-green)}.data-card-status.warning{color:var(--accent-orange)}.data-card-status.danger{color:var(--accent-red)}

.section{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px;margin-bottom:20px}
.section-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.section-title{font-size:15px;font-weight:600}
.chart-container{width:100%;height:280px}
.chart-container-lg{width:100%;height:360px}

.btn{padding:6px 14px;border-radius:var(--radius);border:1px solid var(--border);background:var(--bg-surface);color:var(--text-secondary);font-size:13px;cursor:pointer;transition:all var(--transition);font-family:var(--font-ui);display:inline-flex;align-items:center;gap:6px}
.btn:hover{background:var(--bg-card-hover);color:var(--text-primary);border-color:var(--border-light)}
.btn-primary{background:var(--accent-green);color:#000;border-color:var(--accent-green);font-weight:600}
.btn-primary:hover{background:#16a34a}
.btn i{width:14px;height:14px}
.tabs{display:flex;gap:4px;background:var(--bg-surface);padding:3px;border-radius:var(--radius)}
.tab{padding:6px 14px;border-radius:6px;font-size:13px;color:var(--text-muted);cursor:pointer;transition:all var(--transition)}
.tab.active{background:var(--bg-card);color:var(--text-primary)}
.tab:hover:not(.active){color:var(--text-secondary)}

.data-table{width:100%;border-collapse:collapse}
.data-table th{text-align:left;padding:10px 14px;font-size:12px;font-weight:600;color:var(--text-muted);text-transform:uppercase;letter-spacing:.5px;border-bottom:1px solid var(--border);background:var(--bg-surface)}
.data-table td{padding:12px 14px;font-size:13px;border-bottom:1px solid var(--border);color:var(--text-secondary)}
.data-table tr:hover td{background:rgba(255,255,255,.02)}
.data-table .mono{font-family:var(--font-data);font-size:12px}

.badge{padding:3px 10px;border-radius:20px;font-size:12px;font-weight:500;display:inline-flex;align-items:center;gap:4px}
.badge-green{background:var(--accent-green-dim);color:var(--accent-green)}
.badge-orange{background:var(--accent-orange-dim);color:var(--accent-orange)}
.badge-red{background:var(--accent-red-dim);color:var(--accent-red)}
.badge-blue{background:var(--accent-blue-dim);color:var(--accent-blue)}

.alert-item{display:flex;align-items:flex-start;gap:12px;padding:12px 14px;border-radius:var(--radius);margin-bottom:8px;border:1px solid var(--border)}
.alert-item.warning{background:var(--accent-orange-dim);border-color:rgba(245,158,11,.2)}
.alert-item.danger{background:var(--accent-red-dim);border-color:rgba(239,68,68,.2)}
.alert-item.info{background:var(--accent-blue-dim);border-color:rgba(56,189,248,.2)}
.alert-icon{flex-shrink:0;margin-top:2px}
.alert-icon i{width:18px;height:18px}
.alert-item.warning .alert-icon{color:var(--accent-orange)}
.alert-item.danger .alert-icon{color:var(--accent-red)}
.alert-item.info .alert-icon{color:var(--accent-blue)}
.alert-content{flex:1}
.alert-title{font-size:13px;font-weight:600;margin-bottom:2px}
.alert-desc{font-size:12px;color:var(--text-muted)}
.alert-time{font-size:11px;color:var(--text-muted);font-family:var(--font-data);margin-top:4px}

.twin-container{display:grid;grid-template-columns:1fr 320px;gap:16px;height:calc(100vh - var(--header-h) - 48px - 80px)}
.twin-canvas-wrap{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;position:relative}
.twin-canvas-wrap canvas{display:block;width:100%;height:100%}
.twin-overlay{position:absolute;top:12px;left:12px;display:flex;gap:6px}
.twin-sidebar{display:flex;flex-direction:column;gap:12px}

.pond-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.pond-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px;cursor:pointer;transition:all var(--transition)}
.pond-card:hover{border-color:var(--accent-cyan);transform:translateY(-2px)}
.pond-card-title{font-size:15px;font-weight:600;margin-bottom:8px;display:flex;align-items:center;gap:8px}
.pond-card-meta{font-size:12px;color:var(--text-muted);margin-bottom:12px}
.pond-card-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}
.pond-stat{background:var(--bg-surface);border-radius:6px;padding:8px 10px}
.pond-stat-label{font-size:11px;color:var(--text-muted)}
.pond-stat-value{font-family:var(--font-data);font-size:15px;font-weight:600}

.robot-card{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius-lg);padding:20px;display:flex;align-items:center;gap:16px;transition:all var(--transition)}
.robot-card:hover{border-color:var(--border-light)}
.robot-avatar{width:56px;height:56px;border-radius:var(--radius-lg);background:var(--accent-cyan-dim);display:flex;align-items:center;justify-content:center}
.robot-avatar i{width:28px;height:28px;color:var(--accent-cyan)}
.robot-info{flex:1}
.robot-name{font-size:15px;font-weight:600;margin-bottom:4px}
.robot-desc{font-size:12px;color:var(--text-muted)}
.robot-stats{display:flex;gap:16px}
.robot-stat{text-align:center}
.robot-stat-val{font-family:var(--font-data);font-size:16px;font-weight:600}
.robot-stat-label{font-size:11px;color:var(--text-muted)}

.report-filters{display:flex;gap:12px;margin-bottom:20px;align-items:flex-end}
.form-group{margin-bottom:16px}
.form-label{font-size:13px;color:var(--text-secondary);margin-bottom:6px;display:block;font-weight:500}
.form-input{width:100%;padding:8px 12px;background:var(--bg-surface);border:1px solid var(--border);border-radius:var(--radius);color:var(--text-primary);font-size:14px;font-family:var(--font-ui);transition:border-color var(--transition)}
.form-input:focus{outline:none;border-color:var(--accent-green)}
select.form-input{cursor:pointer}

.wqi-ring{width:100px;height:100px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-direction:column;border:3px solid var(--accent-green);margin:0 auto 8px}
.wqi-score{font-family:var(--font-data);font-size:28px;font-weight:700;color:var(--accent-green)}
.heatmap-legend{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--text-muted)}
.heatmap-bar{width:120px;height:10px;border-radius:5px;background:linear-gradient(90deg,#22c55e,#eab308,#ef4444)}

::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}::-webkit-scrollbar-thumb:hover{background:var(--border-light)}

@media(max-width:1200px){.cards-4{grid-template-columns:repeat(2,1fr)}.pond-grid{grid-template-columns:repeat(2,1fr)}.twin-container{grid-template-columns:1fr}.twin-sidebar{flex-direction:row;overflow-x:auto}}
@media(max-width:768px){.sidebar{width:60px}.sidebar-logo span,.nav-item span,.nav-group-label{display:none}.nav-item{justify-content:center;padding:12px}.main{margin-left:60px}.cards-4,.cards-3{grid-template-columns:1fr}.pond-grid{grid-template-columns:1fr}}
"""

with open(os.path.join(DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n')
    f.write('<meta charset="UTF-8">\n')
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>鱼塘智慧管理平台</title>\n')
    f.write('<link rel="preconnect" href="https://fonts.googleapis.com">\n')
    f.write('<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n')
    f.write('<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>\n')
    f.write('<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>\n')
    f.write('<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/examples/js/controls/OrbitControls.js"></script>\n')
    f.write('<script src="https://unpkg.com/lucide@latest"></script>\n')
    f.write('<style>\n' + css + '\n</style>\n')
    f.write('</head>\n')
    print('Part 1 OK')

print('Done:', os.path.getsize(os.path.join(DIR, 'index.html')), 'bytes')
