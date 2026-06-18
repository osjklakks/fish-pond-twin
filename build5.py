# -*- coding: utf-8 -*-
import os
DIR = r'D:\夸克\3'

js3 = '''
// ===== Three.js Digital Twin =====
function initThreeScene(){
  twinInited=true;
  var canvas=document.getElementById("twinCanvas");
  var container=canvas.parentElement;
  var W=container.clientWidth,H=container.clientHeight;

  var scene=new THREE.Scene();
  scene.background=new THREE.Color(0x070b14);
  scene.fog=new THREE.FogExp2(0x070b14,0.015);

  var camera=new THREE.PerspectiveCamera(50,W/H,0.1,200);
  camera.position.set(18,14,18);
  camera.lookAt(0,0,0);

  var renderer=new THREE.WebGLRenderer({canvas:canvas,antialias:true});
  renderer.setSize(W,H);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));

  var controls=new THREE.OrbitControls(camera,renderer.domElement);
  controls.enableDamping=true;controls.dampingFactor=0.05;
  controls.maxPolarAngle=Math.PI/2.2;controls.minDistance=8;controls.maxDistance=40;

  scene.add(new THREE.AmbientLight(0x4488aa,0.6));
  var dl=new THREE.DirectionalLight(0xffffff,0.8);
  dl.position.set(10,20,10);scene.add(dl);
  var pl=new THREE.PointLight(0x22d3ee,0.5,30);
  pl.position.set(0,5,0);scene.add(pl);

  // Ground
  var gnd=new THREE.Mesh(new THREE.PlaneGeometry(60,60),new THREE.MeshStandardMaterial({color:0x1a2a1a,roughness:0.9}));
  gnd.rotation.x=-Math.PI/2;gnd.position.y=-0.5;scene.add(gnd);

  // Shore
  var sh=new THREE.Shape();
  sh.moveTo(-12,-8);sh.lineTo(12,-8);sh.lineTo(12,8);sh.lineTo(-12,8);sh.lineTo(-12,-8);
  var hole=new THREE.Path();
  hole.moveTo(-10,-6);hole.lineTo(10,-6);hole.lineTo(10,6);hole.lineTo(-10,6);hole.lineTo(-10,-6);
  sh.holes.push(hole);
  var shore=new THREE.Mesh(new THREE.ShapeGeometry(sh),new THREE.MeshStandardMaterial({color:0x3d2b1f,roughness:1}));
  shore.rotation.x=-Math.PI/2;shore.position.y=-0.3;scene.add(shore);

  // Water
  var waterGeo=new THREE.PlaneGeometry(20,12,80,48);
  var waterMat=new THREE.MeshPhongMaterial({color:0x0c4a6e,transparent:true,opacity:0.85,shininess:100,specular:0x22d3ee,side:THREE.DoubleSide});
  var water=new THREE.Mesh(waterGeo,waterMat);
  water.rotation.x=-Math.PI/2;water.position.y=0;scene.add(water);

  // Heatmap
  var heatGroup=new THREE.Group();scene.add(heatGroup);
  var hps=[];
  for(var x=-9;x<=9;x+=1.5){
    for(var z=-5;z<=5;z+=1.5){
      var v=Math.random();
      var c=new THREE.Color().setHSL(0.35-v*0.35,0.8,0.4+v*0.2);
      var sp=new THREE.Mesh(new THREE.SphereGeometry(0.2,8,8),new THREE.MeshBasicMaterial({color:c,transparent:true,opacity:0.6}));
      sp.position.set(x,0.3,z);heatGroup.add(sp);hps.push({m:sp,b:v});
    }
  }

  // Sensors
  var senGroup=new THREE.Group();scene.add(senGroup);
  [{x:-5,z:-3},{x:3,z:-2},{x:-2,z:3},{x:6,z:2}].forEach(function(s){
    var mk=new THREE.Mesh(new THREE.CylinderGeometry(0.15,0.15,1.5,8),new THREE.MeshStandardMaterial({color:0x22d3ee,emissive:0x22d3ee,emissiveIntensity:0.3}));
    mk.position.set(s.x,0.75,s.z);senGroup.add(mk);
    var tp=new THREE.Mesh(new THREE.SphereGeometry(0.2,8,8),new THREE.MeshBasicMaterial({color:0x22d3ee}));
    tp.position.set(s.x,1.5,s.z);senGroup.add(tp);
  });

  // Robot
  var rbt=new THREE.Group();
  rbt.add(new THREE.Mesh(new THREE.BoxGeometry(1,0.4,0.6),new THREE.MeshStandardMaterial({color:0x22c55e,emissive:0x22c55e,emissiveIntensity:0.2})));
  var cn=new THREE.Mesh(new THREE.BoxGeometry(0.5,0.3,0.4),new THREE.MeshStandardMaterial({color:0x16a34a}));
  cn.position.y=0.35;rbt.add(cn);
  var nz=new THREE.Mesh(new THREE.CylinderGeometry(0.05,0.05,0.4,8),new THREE.MeshStandardMaterial({color:0x94a3b8}));
  nz.position.set(0.4,0.4,0);rbt.add(nz);
  rbt.position.y=0.3;scene.add(rbt);

  // Path
  var pathGroup=new THREE.Group();scene.add(pathGroup);
  var pp=[];
  for(var t=0;t<Math.PI*2;t+=0.05)pp.push(new THREE.Vector3(Math.cos(t)*7+Math.sin(t*2)*1.5,0.15,Math.sin(t)*4+Math.cos(t*3)*0.8));
  var pathCurve=new THREE.CatmullRomCurve3(pp,true);
  pathGroup.add(new THREE.Mesh(new THREE.TubeGeometry(pathCurve,200,0.03,4,true),new THREE.MeshBasicMaterial({color:0x22c55e,transparent:true,opacity:0.3})));

  // Toggle buttons
  document.getElementById("btnHeatmap").addEventListener("click",function(){showHeatmap=!showHeatmap;});
  document.getElementById("btnPath").addEventListener("click",function(){showPath=!showPath;});
  document.getElementById("btnSensor").addEventListener("click",function(){showSensor=!showSensor;});
  document.getElementById("btnResetCam").addEventListener("click",function(){
    camera.position.set(18,14,18);controls.target.set(0,0,0);controls.update();
  });

  // Animate
  var clock=new THREE.Clock();
  function animate(){
    requestAnimationFrame(animate);
    var t=clock.getElapsedTime();
    var pos=waterGeo.attributes.position;
    for(var i=0;i<pos.count;i++){
      var px=pos.getX(i),pz=pos.getZ(i);
      pos.setY(i,Math.sin(px*0.5+t*1.5)*0.08+Math.cos(pz*0.8+t*1.2)*0.06);
    }
    pos.needsUpdate=true;waterGeo.computeVertexNormals();

    hps.forEach(function(p,idx){
      var v=p.b+Math.sin(t*0.5+idx)*0.1;
      v=Math.max(0,Math.min(1,v));
      p.m.material.color.setHSL(0.35-v*0.35,0.8,0.4+v*0.2);
      p.m.position.y=0.3+Math.sin(t+idx*0.3)*0.05;
    });
    heatGroup.visible=showHeatmap;
    senGroup.visible=showSensor;
    pathGroup.visible=showPath;

    robotAngle+=0.002;
    var rp=pathCurve.getPointAt(robotAngle%1);
    var la=pathCurve.getPointAt((robotAngle+0.01)%1);
    rbt.position.x=rp.x;rbt.position.z=rp.z;
    rbt.lookAt(la.x,rbt.position.y,la.z);
    rbt.position.y=0.3+Math.sin(t*3)*0.03;

    controls.update();renderer.render(scene,camera);
  }
  animate();

  window.addEventListener("resize",function(){
    var w=container.clientWidth,h=container.clientHeight;
    camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h);
  });
}

// ===== Data Simulation =====
function simulateData(){
  function jit(v,r){return +(v+(Math.random()-0.5)*r).toFixed(1);}
  SD.do.value=jit(SD.do.value,0.4);
  SD.temp.value=jit(SD.temp.value,0.3);
  SD.ph.value=+(SD.ph.value+(Math.random()-0.5)*0.1).toFixed(1);
  SD.nh3.value=+(SD.nh3.value+(Math.random()-0.5)*0.02).toFixed(2);
  SD.turb.value=jit(SD.turb.value,1);
  SD.do.status=SD.do.value<5?"danger":SD.do.value<6?"warning":"normal";
  SD.nh3.status=SD.nh3.value>0.15?"danger":SD.nh3.value>0.1?"warning":"normal";
  SD.temp.status=SD.temp.value>30?"warning":"normal";
  renderSensorCards();
}

// ===== Init =====
window.addEventListener("DOMContentLoaded",function(){
  renderSensorCards();renderMonitorCards();renderAlerts();
  renderPondGrid();renderRobots();renderReports();
  setTimeout(initCharts,300);
  setInterval(simulateData,5000);
});
</script>
</body>
</html>
'''

with open(os.path.join(DIR, 'index.html'), 'a', encoding='utf-8') as f:
    f.write(js3)

# Verify
sz = os.path.getsize(os.path.join(DIR, 'index.html'))
with open(os.path.join(DIR, 'index.html'), 'r', encoding='utf-8') as f:
    content = f.read()
print('Final size:', sz, 'bytes')
print('Lines:', content.count('\n'))
print('Starts:', content[:50])
print('Ends:', content[-50:])
print('Chinese check:', '鱼塘' in content, '数据看板' in content, '数字孪生' in content)
