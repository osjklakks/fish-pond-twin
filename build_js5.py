# -*- coding: utf-8 -*-
import os
DIR = r'D:\夸克\3'
OUT = os.path.join(DIR, 'index.html')

js = []
def add(s):
    js.append(s)

add('// ===== Data Simulation =====')
add('function simulateData(){')
add('  function jit(v,r){return +(v+(Math.random()-0.5)*r).toFixed(1);}')
add('  SD.do.value=jit(SD.do.value,0.4);')
add('  SD.temp.value=jit(SD.temp.value,0.3);')
add('  SD.ph.value=+(SD.ph.value+(Math.random()-0.5)*0.1).toFixed(1);')
add('  SD.nh3.value=+(SD.nh3.value+(Math.random()-0.5)*0.02).toFixed(2);')
add('  SD.turb.value=jit(SD.turb.value,1);')
add('  SD.do.status=SD.do.value<5?"danger":SD.do.value<6?"warning":"normal";')
add('  SD.nh3.status=SD.nh3.value>0.15?"danger":SD.nh3.value>0.1?"warning":"normal";')
add('  SD.temp.status=SD.temp.value>30?"warning":"normal";')
add('  renderSensorCards();')
add('}')

add('// ===== Init =====')
add('window.addEventListener("DOMContentLoaded",function(){')
add('  renderSensorCards();renderMonitorCards();renderAlerts();')
add('  renderPondGrid();renderRobots();renderReports();')
add('  setTimeout(initCharts,300);')
add('  setInterval(simulateData,5000);')
add('});')
add('</script>')
add('</body>')
add('</html>')

with open(OUT, 'a', encoding='utf-8') as f:
    f.write('\n'.join(js))

sz = os.path.getsize(OUT)
with open(OUT, 'r', encoding='utf-8') as f:
    content = f.read()
lines = content.count('\n')
has_html_close = '</html>' in content
has_script_close = '</script>' in content
has_body_close = '</body>' in content
has_init = 'DOMContentLoaded' in content
has_three = 'THREE.Scene' in content
has_echarts = 'echarts.init' in content

print(f'Final size: {sz} bytes, {lines} lines')
print(f'</html>: {has_html_close}')
print(f'</script>: {has_script_close}')
print(f'</body>: {has_body_close}')
print(f'Init: {has_init}')
print(f'Three.js: {has_three}')
print(f'ECharts: {has_echarts}')
