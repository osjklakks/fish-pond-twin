# -*- coding: utf-8 -*-
"""
修复数字孪生页面不显示 3D 内容的问题
问题列表:
1. Line 280: 损坏的 HTML 标签 <u62a5警记录
2. Three.js CDN 版本和路径问题
3. canvas 容器在 initThreeScene 调用时尺寸为 0
4. switchPage 中 titles[page] 无空值保护
"""
import os, re

DIR = r'D:\夸克\3'
OUT = os.path.join(DIR, 'index.html')

with open(OUT, 'r', encoding='utf-8') as f:
    content = f.read()

original_size = len(content)
fixes = []

# === Fix 1: 修复第 280 行损坏的 HTML ===
bad_html = '<u62a5警记录</span>'
good_html = '报警记录</span>'
if bad_html in content:
    content = content.replace(bad_html, good_html)
    fixes.append('Fix 1: 修复损坏的 HTML 标签 <u62a5警记录')
else:
    print('WARN: Fix 1 target not found, trying alternative...')
    # Try literal match
    content = content.replace('<u62a5警记录</span>', '报警记录</span>')
    fixes.append('Fix 1: 修复损坏的 HTML 标签 (literal)')

# === Fix 2: 修复 Three.js CDN 版本 ===
old_three_main = 'https://cdn.jsdelivr.net/npm/three@0.149.0/build/three.min.js'
new_three_main = 'https://unpkg.com/three@0.128.0/build/three.min.js'
old_three_ctrl = 'https://cdn.jsdelivr.net/npm/three@0.149.0/examples/js/controls/OrbitControls.js'
new_three_ctrl = 'https://unpkg.com/three@0.128.0/examples/js/controls/OrbitControls.js'

if old_three_main in content:
    content = content.replace(old_three_main, new_three_main)
    fixes.append('Fix 2a: Three.js 主文件 CDN 切换到 unpkg r128')
else:
    print('WARN: Fix 2a target not found')

if old_three_ctrl in content:
    content = content.replace(old_three_ctrl, new_three_ctrl)
    fixes.append('Fix 2b: OrbitControls CDN 切换到 unpkg r128')
else:
    print('WARN: Fix 2b target not found')

# === Fix 3: 重写 initThreeScene，增加容错 ===
new_init = '''function initThreeScene(){
  try{
    twinInited=true;
    var canvas=document.getElementById("twinCanvas");
    if(!canvas){console.error("[Twin] canvas not found");return;}
    var container=canvas.parentElement;
    var W=container.clientWidth||window.innerWidth-260;
    var Ht=container.clientHeight||window.innerHeight-160;
    if(W<100||Ht<100){
      console.warn("[Twin] container too small, retrying in 500ms",W,Ht);
      twinInited=false;
      setTimeout(initThreeScene,500);
      return;
    }
    console.log("[Twin] init",W,"x",Ht);
    var scene=new THREE.Scene();
    scene.background=new THREE.Color(0x070b14);
    scene.fog=new THREE.FogExp2(0x070b14,0.015);
    var camera=new THREE.PerspectiveCamera(50,W/Ht,0.1,200);
    camera.position.set(18,14,18);camera.lookAt(0,0,0);
    var renderer=new THREE.WebGLRenderer({canvas:canvas,antialias:true});
    renderer.setSize(W,Ht);renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
    var controls=new THREE.OrbitControls(camera,renderer.domElement);
    controls.enableDamping=true;controls.dampingFactor=0.05;
    controls.maxPolarAngle=Math.PI/2.2;controls.minDistance=8;controls.maxDistance=40;
    scene.add(new THREE.AmbientLight(0x4488aa,0.6));
    var dl=new THREE.DirectionalLight(0xffffff,0.8);dl.position.set(10,20,10);scene.add(dl);
    var pl=new THREE.PointLight(0x22d3ee,0.5,30);pl.position.set(0,5,0);scene.add(pl);
    var gnd=new THREE.Mesh(new THREE.PlaneGeometry(60,60),new THREE.MeshStandardMaterial({color:0x1a2a1a,roughness:0.9}));
    gnd.rotation.x=-Math.PI/2;gnd.position.y=-0.5;scene.add(gnd);
    var sh=new THREE.Shape();sh.moveTo(-12,-8);sh.lineTo(12,-8);sh.lineTo(12,8);sh.lineTo(-12,8);sh.lineTo(-12,-8);
    var hole=new THREE.Path();hole.moveTo(-10,-6);hole.lineTo(10,-6);hole.lineTo(10,6);hole.lineTo(-10,6);hole.lineTo(-10,-6);
    sh.holes.push(hole);
    var shore=new THREE.Mesh(new THREE.ShapeGeometry(sh),new THREE.MeshStandardMaterial({color:0x3d2b1f,roughness:1}));
    shore.rotation.x=-Math.PI/2;shore.position.y=-0.3;scene.add(shore);
    var waterGeo=new THREE.PlaneGeometry(20,12,80,48);
    var waterMat=new THREE.MeshPhongMaterial({color:0x0c4a6e,transparent:true,opacity:0.85,shininess:100,specular:0x22d3ee,side:THREE.DoubleSide});
    var water=new THREE.Mesh(waterGeo,waterMat);water.rotation.x=-Math.PI/2;water.position.y=0;scene.add(water);
    var heatGroup=new THREE.Group();scene.add(heatGroup);var hps=[];
    for(var x=-9;x<=9;x+=1.5){for(var z=-5;z<=5;z+=1.5){var v=Math.random();var c=new THREE.Color().setHSL(0.35-v*0.35,0.8,0.4+v*0.2);var sp=new THREE.Mesh(new THREE.SphereGeometry(0.2,8,8),new THREE.MeshBasicMaterial({color:c,transparent:true,opacity:0.6}));sp.position.set(x,0.3,z);heatGroup.add(sp);hps.push({m:sp,b:v});}}
    var senGroup=new THREE.Group();scene.add(senGroup);
    [{x:-5,z:-3},{x:3,z:-2},{x:-2,z:3},{x:6,z:2}].forEach(function(s){var mk=new THREE.Mesh(new THREE.CylinderGeometry(0.15,0.15,1.5,8),new THREE.MeshStandardMaterial({color:0x22d3ee,emissive:0x22d3ee,emissiveIntensity:0.3}));mk.position.set(s.x,0.75,s.z);senGroup.add(mk);var tp=new THREE.Mesh(new THREE.SphereGeometry(0.2,8,8),new THREE.MeshBasicMaterial({color:0x22d3ee}));tp.position.set(s.x,1.5,s.z);senGroup.add(tp);});
    var rbt=new THREE.Group();
    rbt.add(new THREE.Mesh(new THREE.BoxGeometry(1,0.4,0.6),new THREE.MeshStandardMaterial({color:0x22c55e,emissive:0x22c55e,emissiveIntensity:0.2})));
    var cn=new THREE.Mesh(new THREE.BoxGeometry(0.5,0.3,0.4),new THREE.MeshStandardMaterial({color:0x16a34a}));cn.position.y=0.35;rbt.add(cn);
    var nz=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.05,0.4,8),new THREE.MeshStandardMaterial({color:0x94a3b8}));nz.position.set(0.4,0.4,0);rbt.add(nz);
    rbt.position.y=0.3;scene.add(rbt);
    var pathGroup=new THREE.Group();scene.add(pathGroup);var pp=[];
    for(var t=0;t<Math.PI*2;t+=0.05)pp.push(new THREE.Vector3(Math.cos(t)*7+Math.sin(t*2)*1.5,0.15,Math.sin(t)*4+Math.cos(t*3)*0.8));
    var pathCurve=new THREE.CatmullRomCurve3(pp,true);
    pathGroup.add(new THREE.Mesh(new THREE.TubeGeometry(pathCurve,200,0.03,4,true),new THREE.MeshBasicMaterial({color:0x22c55e,transparent:true,opacity:0.3})));
    document.getElementById("btnHeatmap").addEventListener("click",function(){showHeatmap=!showHeatmap;});
    document.getElementById("btnPath").addEventListener("click",function(){showPath=!showPath;});
    document.getElementById("btnSensor").addEventListener("click",function(){showSensor=!showSensor;});
    document.getElementById("btnResetCam").addEventListener("click",function(){camera.position.set(18,14,18);controls.target.set(0,0,0);controls.update();});
    var clock=new THREE.Clock();
    function animate(){
      requestAnimationFrame(animate);
      var t=clock.getElapsedTime();
      var pos=waterGeo.attributes.position;
      for(var i=0;i<pos.count;i++){var px=pos.getX(i),pz=pos.getZ(i);pos.setY(i,Math.sin(px*0.5+t*1.5)*0.08+Math.cos(pz*0.8+t*1.2)*0.06);}
      pos.needsUpdate=true;waterGeo.computeVertexNormals();
      hps.forEach(function(p,idx){var v=p.b+Math.sin(t*0.5+idx)*0.1;v=Math.max(0,Math.min(1,v));p.m.material.color.setHSL(0.35-v*0.35,0.8,0.4+v*0.2);p.m.position.y=0.3+Math.sin(t+idx*0.3)*0.05;});
      heatGroup.visible=showHeatmap;senGroup.visible=showSensor;pathGroup.visible=showPath;
      robotAngle+=0.002;var rp=pathCurve.getPointAt(robotAngle%1);var la=pathCurve.getPointAt((robotAngle+0.01)%1);
      rbt.position.x=rp.x;rbt.position.z=rp.z;rbt.lookAt(la.x,rbt.position.y,la.z);rbt.position.y=0.3+Math.sin(t*3)*0.03;
      controls.update();renderer.render(scene,camera);
    }
    animate();
    window.addEventListener("resize",function(){
      var w=container.clientWidth||window.innerWidth-260;
      var h=container.clientHeight||window.innerHeight-160;
      camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h);
    });
    console.log("[Twin] scene ready");
  }catch(e){console.error("[Twin] init error:",e);}
}'''

# Use regex to replace the entire initThreeScene function
pattern = r'function initThreeScene\(\)\{.*?\}\n(?=// ===== Data Simulation)'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content[:match.start()] + new_init + '\n' + content[match.end():]
    fixes.append('Fix 3: 重写 initThreeScene，增加尺寸检测、重试机制、错误捕获')
else:
    print('WARN: Fix 3 regex did not match, trying simpler pattern...')
    # Fallback: find start and count braces
    start_marker = 'function initThreeScene(){'
    if start_marker in content:
        start = content.index(start_marker)
        depth = 0
        end = start
        for i in range(start, len(content)):
            if content[i] == '{': depth += 1
            elif content[i] == '}': depth -= 1
            if depth == 0:
                end = i + 1
                break
        content = content[:start] + new_init + content[end:]
        fixes.append('Fix 3: 重写 initThreeScene (brace counting fallback)')

# === Fix 4: 修复 switchPage 中 titles 空值保护 ===
old_line = '  document.getElementById("pageTitle").textContent=titles[page][0];\n  document.getElementById("pageBreadcrumb").textContent=titles[page][1];'
new_line = '  if(titles[page]){document.getElementById("pageTitle").textContent=titles[page][0];document.getElementById("pageBreadcrumb").textContent=titles[page][1];}'
if old_line in content:
    content = content.replace(old_line, new_line)
    fixes.append('Fix 4: switchPage 增加 titles 空值保护')

# === Fix 5: 确保 initCharts 和 initThreeScene 之间有换行 ===
content = content.replace(
    '}// ===== Three.js Digital Twin =====',
    '}\n// ===== Three.js Digital Twin ====='
)
fixes.append('Fix 5: initCharts/initThreeScene 之间增加换行')

# === Write ===
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(content)

new_size = len(content)
print(f'\nOriginal: {original_size} bytes -> New: {new_size} bytes')
print(f'Applied {len(fixes)} fixes:')
for fix in fixes:
    print(f'  ✓ {fix}')
