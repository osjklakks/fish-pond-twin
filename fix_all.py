# -*- coding: utf-8 -*-
"""
完整修复数字孪生及整个 HTML 结构问题
根本原因: 多个 build 脚本追加写入导致 div 嵌套错乱
修复方案: 保留 CSS/JS，重建正确的 HTML body 结构
"""
import os, re

DIR = r'D:\夸克\3'
OUT = os.path.join(DIR, 'index.html')

with open(OUT, 'r', encoding='utf-8') as f:
    content = f.read()

# === Step 1: 提取 CSS (从 <style> 到 </style>) ===
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
css = css_match.group(1) if css_match else ''

# === Step 2: 提取 JS (从最后一个 <script> 到 </script>) ===
js_match = re.search(r'<script>(.*?)</script>\s*</body>\s*</html>', content, re.DOTALL)
js = js_match.group(1) if js_match else ''

print(f'CSS: {len(css)} bytes')
print(f'JS: {len(js)} bytes')

# === Step 3: 重建完整 HTML ===
new_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>智氧兴渔 - 智能鱼塘监控系统</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<script src="https://unpkg.com/three@0.128.0/build/three.min.js"></script>
<script src="https://unpkg.com/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script src="https://unpkg.com/lucide@latest"></script>
<style>
''' + css + '''
</style>
</head>
<body>

<!-- Sidebar -->
<nav class="sidebar">
  <div class="sidebar-logo">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12c2-4 6-6 10-6s8 2 10 6c-2 4-6 6-10 6s-8-2-10-6z"/><path d="M12 6v12"/><path d="M6 9c2 1 4 2 6 2s4-1 6-2"/></svg>
    <span>智氧兴渔</span>
  </div>
  <div class="sidebar-nav">
    <div class="nav-group-label">概览</div>
    <a class="nav-item active" data-page="home"><i data-lucide="home"></i><span>首页</span></a>
    <a class="nav-item" data-page="dashboard"><i data-lucide="layout-dashboard"></i><span>数据看板</span></a>
    <div class="nav-group-label">管理</div>
    <a class="nav-item" data-page="ponds"><i data-lucide="waves"></i><span>鱼塘管理</span></a>
    <a class="nav-item" data-page="monitor"><i data-lucide="activity"></i><span>实时监控</span><span class="nav-badge" id="alertCount">3</span></a>
    <a class="nav-item" data-page="twin"><i data-lucide="box"></i><span>数字孪生</span></a>
    <div class="nav-group-label">设备</div>
    <a class="nav-item" data-page="robot"><i data-lucide="bot"></i><span>机器人管理</span></a>
    <div class="nav-group-label">分析</div>
    <a class="nav-item" data-page="report"><i data-lucide="file-text"></i><span>报告中心</span></a>
  </div>
</nav>

<!-- Main Content -->
<div class="main">
  <header class="header">
    <div class="header-left">
      <h1 class="header-title" id="pageTitle">首页</h1>
      <span class="header-breadcrumb" id="pageBreadcrumb">智氧兴渔 / 智能鱼塘监控系统</span>
    </div>
    <div class="header-right">
      <div class="header-status"><span class="dot"></span> 系统在线</div>
      <div class="header-time" id="headerTime">--:--:--</div>
    </div>
  </header>

  <div class="content">

    <!-- Page: 首页 -->
    <div class="page active" id="page-home">
      <div class="hero-section">
        <div style="max-width:800px;margin:0 auto;">
          <div style="margin-bottom:12px;">
            <span class="badge badge-green" style="font-size:13px;padding:5px 16px;">喷泉式智能增氧机器人</span>
          </div>
          <h1 class="hero-title">智氧<span class="accent">兴渔</span></h1>
          <p class="hero-subtitle">基于数字孪生技术的智能鱼塘监控系统，实时监测水质参数，智能调控增氧设备</p>
          <div class="hero-actions">
            <button class="btn btn-primary" style="padding:12px 28px;font-size:15px;" onclick="switchPage('dashboard')"><i data-lucide="bar-chart-3"></i> 查看实时数据</button>
            <button class="btn" style="padding:12px 28px;font-size:15px;" onclick="switchPage('twin')"><i data-lucide="box"></i> 数字孪生演示</button>
          </div>
          <div class="hero-stats">
            <div class="hero-stat"><div class="hero-stat-val" style="color:var(--accent-green)">12+</div><div class="hero-stat-label">监测参数</div></div>
            <div class="hero-stat"><div class="hero-stat-val" style="color:var(--accent-orange)">99.9%</div><div class="hero-stat-label">数据准确率</div></div>
            <div class="hero-stat"><div class="hero-stat-val" style="color:var(--accent-cyan)">24/7</div><div class="hero-stat-label">实时监控</div></div>
            <div class="hero-stat"><div class="hero-stat-val" style="color:var(--accent-purple)">3D</div><div class="hero-stat-label">数字孪生</div></div>
          </div>
        </div>
      </div>
      <div class="footer">
        <div class="footer-inner">
          <div class="footer-grid">
            <div>
              <div class="footer-brand"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12c2-4 6-6 10-6s8 2 10 6c-2 4-6 6-10 6s-8-2-10-6z"/><path d="M12 6v12"/></svg><span>智氧兴渔</span></div>
              <p class="footer-desc">基于数字孪生技术的智能鱼塘监控系统</p>
            </div>
            <div><h4 class="footer-col-title">产品功能</h4><a class="footer-link" onclick="switchPage('dashboard')">实时监控</a><a class="footer-link" onclick="switchPage('twin')">数字孪生</a><a class="footer-link" onclick="switchPage('report')">报告生成</a></div>
            <div><h4 class="footer-col-title">技术支持</h4><a class="footer-link">使用文档</a><a class="footer-link">API接口</a><a class="footer-link">常见问题</a></div>
            <div><h4 class="footer-col-title">联系我们</h4><span class="footer-link">邮箱: contact@zhiyaoxingyu.com</span><br><span class="footer-link">电话: 400-XXX-XXXX</span></div>
          </div>
          <div class="footer-bottom">&copy; 2024 智氧兴渔. 保留所有权利.</div>
        </div>
      </div>
    </div>

    <!-- Page: 数据看板 -->
    <div class="page" id="page-dashboard">
      <div class="cards-row cards-4" id="sensorCards"></div>
      <div class="cards-row cards-2">
        <div class="section">
          <div class="section-header"><span class="section-title">溶氧趋势 (24h)</span><div class="tabs"><span class="tab active">24h</span><span class="tab">7d</span><span class="tab">30d</span></div></div>
          <div class="chart-container" id="chartDoTrend"></div>
        </div>
        <div class="section">
          <div class="section-header"><span class="section-title">水质综合评分</span></div>
          <div style="display:flex;justify-content:center;align-items:center;gap:40px;height:280px;">
            <div><div class="wqi-ring"><span class="wqi-score">87</span></div><div style="text-align:center;font-size:13px;color:var(--text-secondary)">综合评分</div></div>
            <div class="chart-container" id="chartRadar" style="width:280px;height:260px;"></div>
          </div>
        </div>
      </div>
      <div class="cards-row cards-2">
        <div class="section">
          <div class="section-header"><span class="section-title">实时告警</span></div>
          <div id="alertList"></div>
        </div>
        <div class="section">
          <div class="section-header"><span class="section-title">各鱼塘溶氧对比</span></div>
          <div class="chart-container" id="chartPondBar"></div>
        </div>
      </div>
    </div>

    <!-- Page: 鱼塘管理 -->
    <div class="page" id="page-ponds">
      <div class="section" style="margin-bottom:20px;">
        <div class="section-header"><span class="section-title">鱼塘列表</span><button class="btn btn-primary"><i data-lucide="plus"></i> 新增鱼塘</button></div>
      </div>
      <div class="pond-grid" id="pondGrid"></div>
    </div>

    <!-- Page: 实时监控 -->
    <div class="page" id="page-monitor">
      <div class="cards-row cards-4" id="monitorCards"></div>
      <div class="cards-row cards-2">
        <div class="section">
          <div class="section-header"><span class="section-title">多参数实时曲线</span></div>
          <div class="chart-container-lg" id="chartMultiTrend"></div>
        </div>
        <div class="section">
          <div class="section-header"><span class="section-title">报警记录</span></div>
          <table class="data-table">
            <thead><tr><th>时间</th><th>鱼塘</th><th>类型</th><th>等级</th><th>状态</th></tr></thead>
            <tbody id="alertTable"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Page: 数字孪生 -->
    <div class="page" id="page-twin">
      <div class="section" style="padding:12px 16px;margin-bottom:16px;display:flex;align-items:center;justify-content:space-between;">
        <div style="display:flex;align-items:center;gap:12px;">
          <span class="section-title">数字孪生 — 1号鱼塘</span>
          <span class="badge badge-green">实时同步</span>
        </div>
        <div style="display:flex;gap:8px;align-items:center;">
          <div class="heatmap-legend"><span>低</span><div class="heatmap-bar"></div><span>高</span><span style="margin-left:8px;">溶氧热力图 (mg/L)</span></div>
          <button class="btn" id="btnResetCam"><i data-lucide="maximize-2"></i> 重置视角</button>
        </div>
      </div>
      <div class="twin-container">
        <div class="twin-canvas-wrap">
          <canvas id="twinCanvas"></canvas>
          <div class="twin-overlay">
            <button class="btn" id="btnHeatmap"><i data-lucide="flame"></i> 热力图</button>
            <button class="btn" id="btnPath"><i data-lucide="route"></i> 轨迹</button>
            <button class="btn" id="btnSensor"><i data-lucide="radio"></i> 传感器</button>
          </div>
        </div>
        <div class="twin-sidebar">
          <div class="section" style="margin-bottom:0;">
            <div class="section-title" style="margin-bottom:12px;">实时传感数据</div>
            <div id="twinSensorList"></div>
          </div>
          <div class="section" style="margin-bottom:0;">
            <div class="section-title" style="margin-bottom:12px;">机器人状态</div>
            <div id="twinRobotInfo"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- Page: 机器人管理 -->
    <div class="page" id="page-robot">
      <div class="cards-row cards-2" style="margin-bottom:20px;">
        <div class="section" style="margin-bottom:0;">
          <div class="section-header"><span class="section-title">设备列表</span></div>
          <div id="robotList" style="display:flex;flex-direction:column;gap:12px;"></div>
        </div>
        <div class="section" style="margin-bottom:0;">
          <div class="section-header"><span class="section-title">任务调度</span></div>
          <table class="data-table">
            <thead><tr><th>任务</th><th>机器人</th><th>时间</th><th>状态</th></tr></thead>
            <tbody id="taskTable"></tbody>
          </table>
        </div>
      </div>
      <div class="section">
        <div class="section-header"><span class="section-title">机器人电量趋势</span></div>
        <div class="chart-container" id="chartRobot"></div>
      </div>
    </div>

    <!-- Page: 报告中心 -->
    <div class="page" id="page-report">
      <div class="section">
        <div class="section-header">
          <span class="section-title">报告中心</span>
          <button class="btn btn-primary" id="btnGenReport"><i data-lucide="file-plus"></i> 生成报告</button>
        </div>
        <div class="report-filters">
          <div class="form-group" style="margin-bottom:0;"><label class="form-label">报告类型</label><select class="form-input" style="width:140px;"><option>日报</option><option>周报</option><option>月报</option></select></div>
          <div class="form-group" style="margin-bottom:0;"><label class="form-label">鱼塘</label><select class="form-input" style="width:140px;"><option>全部</option><option>1号鱼塘</option><option>2号鱼塘</option><option>3号鱼塘</option></select></div>
          <div class="form-group" style="margin-bottom:0;"><label class="form-label">日期范围</label><input type="date" class="form-input" style="width:160px;" value="2026-06-17"></div>
        </div>
        <table class="data-table">
          <thead><tr><th>报告编号</th><th>类型</th><th>鱼塘</th><th>生成时间</th><th>水质评分</th><th>风险等级</th><th>操作</th></tr></thead>
          <tbody id="reportTable"></tbody>
        </table>
      </div>
    </div>

  </div><!-- /content -->
</div><!-- /main -->

<script>
''' + js + '''
</script>
</body>
</html>'''

# === Step 4: 写入 ===
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f'Written: {os.path.getsize(OUT)} bytes')

# === Step 5: 验证 ===
with open(OUT, 'r', encoding='utf-8') as f:
    verify = f.read()

depth = 0
for ch in verify:
    idx = verify.index(ch) if False else 0  # skip
# Simple check
opens = verify.count('<div')
closes = verify.count('</div>')
print(f'DIV balance: {opens} opens, {closes} closes, diff={opens-closes}')
print(f'Has </html>: {"</html>" in verify}')
print(f'Has </script>: {"</script>" in verify}')
print(f'Has </body>: {"</body>" in verify}')
print(f'Has Three.js: {"three@0.128.0" in verify}')
print(f'Has initThreeScene: {"initThreeScene" in verify}')
print(f'Has twinCanvas: {"twinCanvas" in verify}')
print(f'Has OrbitControls: {"OrbitControls" in verify}')
