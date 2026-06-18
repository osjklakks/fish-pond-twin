# -*- coding: utf-8 -*-
import os, json
DIR = r'D:\夸克\3'
OUT = os.path.join(DIR, 'index.html')

# Build JS as Python list of strings, then join
js_lines = []

def add(s):
    js_lines.append(s)

add('<script>')
add('var SD = {')
add('  do:{value:7.2,unit:"mg/L",label:"\u6eb6\u6c27\u91cf",status:"normal",min:5,max:10,icon:"droplets"},')
add('  temp:{value:26.3,unit:"\u00b0C",label:"\u6c34\u6e29",status:"normal",min:15,max:35,icon:"thermometer"},')
add('  ph:{value:7.4,unit:"",label:"pH\u503c",status:"normal",min:6.5,max:9,icon:"flask-conical"},')
add('  nh3:{value:0.08,unit:"mg/L",label:"\u6c28\u6c2e",status:"warning",min:0,max:0.5,icon:"alert-triangle"},')
add('  turb:{value:12.5,unit:"NTU",label:"\u6d4a\u5ea6",status:"normal",min:0,max:50,icon:"cloud"}')
add('};')
add('var H={do:[],temp:[],ph:[],nh3:[],turb:[],labels:[]};')
add('var showHeatmap=true,showPath=true,showSensor=true,robotAngle=0,twinInited=false;')
add('(function(){var now=new Date();for(var i=23;i>=0;i--){var t=new Date(now-i*3600000);H.labels.push(t.getHours()+":00");H.do.push(+(6.5+Math.random()*2).toFixed(1));H.temp.push(+(24+Math.random()*4).toFixed(1));H.ph.push(+(7+Math.random()*0.8).toFixed(1));H.nh3.push(+(0.05+Math.random()*0.1).toFixed(2));H.turb.push(+(8+Math.random()*10).toFixed(1));}})();')
add('document.addEventListener("DOMContentLoaded",function(){lucide.createIcons();});')
add('var titles={home:["\u9996\u9875","\u667a\u6c27\u5174\u6e14 / \u667a\u80fd\u9c7c\u5858\u76d1\u63a7\u7cfb\u7edf"],dashboard:["\u6570\u636e\u770b\u677f","\u603b\u89c8 / \u6570\u636e\u770b\u677f"],ponds:["\u9c7c\u5858\u7ba1\u7406","\u7ba1\u7406 / \u9c7c\u5858\u7ba1\u7406"],monitor:["\u5b9e\u65f6\u76d1\u63a7","\u76d1\u63a7 / \u5b9e\u65f6\u76d1\u63a7"],twin:["\u6570\u5b57\u5b5a\u751f","\u6570\u5b57\u5b5a\u751f / 3D\u573a\u666f"],robot:["\u673a\u5668\u4eba\u7ba1\u7406","\u8bbe\u5907 / \u673a\u5668\u4eba\u7ba1\u7406"],report:["\u62a5\u544a\u4e2d\u5fc3","\u5206\u6790 / \u62a5\u544a\u4e2d\u5fc3"]};')
add('function switchPage(page){')
add('  document.querySelectorAll(".page").forEach(function(p){p.classList.remove("active");});')
add('  document.querySelectorAll(".nav-item").forEach(function(n){n.classList.remove("active");});')
add('  document.getElementById("page-"+page).classList.add("active");')
add('  var el=document.querySelector("[data-page=\x22"+page+"\x22]");if(el)el.classList.add("active");')
add('  document.getElementById("pageTitle").textContent=titles[page][0];')
add('  document.getElementById("pageBreadcrumb").textContent=titles[page][1];')
add('  if(page==="twin"&&!twinInited)setTimeout(initThreeScene,200);')
add('  if(window._charts)Object.values(window._charts).forEach(function(c){c.resize();});')
add('}')
add('document.querySelectorAll(".nav-item").forEach(function(el){el.addEventListener("click",function(){switchPage(el.dataset.page);});});')
add('function updateClock(){var now=new Date();document.getElementById("headerTime").textContent=now.toLocaleDateString("zh-CN",{month:"2-digit",day:"2-digit"})+" "+now.toLocaleTimeString("zh-CN",{hour12:false});}')
add('setInterval(updateClock,1000);updateClock();')

# renderSensorCards using JSON for safe quoting
add('function renderSensorCards(){')
add('  var c=document.getElementById("sensorCards");')
add('  var cols={normal:"var(--accent-green)",warning:"var(--accent-orange)",danger:"var(--accent-red)"};')
add('  var bg={normal:"var(--accent-green-dim)",warning:"var(--accent-orange-dim)",danger:"var(--accent-red-dim)"};')
add('  var ics={normal:"check-circle",warning:"alert-circle",danger:"x-circle"};')
add('  var stx={normal:"\u6b63\u5e38",warning:"\u504f\u9ad8",danger:"\u5f02\u5e38"};')
add('  var html="";for(var k in SD){var d=SD[k];')
add('    html+="<div class=\\"data-card\\"><div class=\\"data-card-header\\"><span class=\\"data-card-label\\">"+d.label+"</span><div class=\\"data-card-icon\\" style=\\"background:"+bg[d.status]+"\\"><i data-lucide=\\""+d.icon+"\\" style=\\"color:"+cols[d.status]+"\\"></i></div></div><div class=\\"data-card-value\\" style=\\"color:"+cols[d.status]+"\\">"+d.value+"<span class=\\"data-card-unit\\">"+d.unit+"</span></div><div class=\\"data-card-status "+d.status+"\\"><i data-lucide=\\""+ics[d.status]+"\\" style=\\"width:14px;height:14px;\\"></i> "+stx[d.status]+" \u00b7 \u8303\u56f4 "+d.min+"-"+d.max+d.unit+"</div></div>";')
add('  }')
add('  c.innerHTML=html;lucide.createIcons();')
add('}')

add('function renderMonitorCards(){')
add('  var c=document.getElementById("monitorCards");var html="";for(var k in SD){var d=SD[k];')
add('    html+="<div class=\\"data-card\\"><div class=\\"data-card-header\\"><span class=\\"data-card-label\\">"+d.label+" \u5b9e\u65f6</span><div class=\\"data-card-icon\\" style=\\"background:var(--accent-blue-dim)\\"><i data-lucide=\\"radio\\" style=\\"color:var(--accent-blue)\\"></i></div></div><div class=\\"data-card-value\\" style=\\"color:var(--accent-blue)\\">"+d.value+"<span class=\\"data-card-unit\\">"+d.unit+"</span></div><div style=\\"font-size:12px;color:var(--text-muted);margin-top:8px;\\">\u91c7\u96c6\u9891\u7387: 5s \u00b7 \u4e0a\u6b21\u66f4\u65b0: \u521a\u521a</div></div>";')
add('  }')
add('  c.innerHTML=html;lucide.createIcons();')
add('}')

add('var alertsData=[')
add('  {type:"danger",title:"3\u53f7\u9c7c\u5858\u6eb6\u6c27\u504f\u4f4e",desc:"\u6eb6\u6c27\u964d\u81f34.2mg/L\uff0c\u4f4e\u4e8e\u5b89\u5168\u9608\u503c5.0mg/L",time:"10:23:15"},')
add('  {type:"warning",title:"2\u53f7\u9c7c\u5858\u6c28\u6c2e\u504f\u9ad8",desc:"\u6c28\u6c2e\u6d53\u5ea60.12mg/L\uff0c\u63a5\u8fd1\u9884\u8b66\u7ebf0.15mg/L",time:"09:45:02"},')
add('  {type:"info",title:"1\u53f7\u9c7c\u5858\u673a\u5668\u4eba\u8fd4\u822a",desc:"AquaBot-01\u5b8c\u6210\u5de1\u822a\u4efb\u52a1\uff0c\u6b63\u5728\u8fd4\u822a\u5145\u7535",time:"09:12:38"},')
add('  {type:"warning",title:"5\u53f7\u9c7c\u5858\u6c34\u6e29\u504f\u9ad8",desc:"\u6c34\u6e29\u8fbe\u523030.2\u00b0C\uff0c\u5efa\u8bae\u5f00\u542f\u589e\u6c27",time:"08:55:11"}')
add('];')

add('function renderAlerts(){')
add('  var ics={danger:"alert-octagon",warning:"alert-triangle",info:"info"};var html="";')
add('  alertsData.forEach(function(a){html+="<div class=\\"alert-item "+a.type+"\\"><div class=\\"alert-icon\\"><i data-lucide=\\""+ics[a.type]+"\\"></i></div><div class=\\"alert-content\\"><div class=\\"alert-title\\">"+a.title+"</div><div class=\\"alert-desc\\">"+a.desc+"</div><div class=\\"alert-time\\">"+a.time+"</div></div></div>";});')
add('  document.getElementById("alertList").innerHTML=html;')
add('  var rows=[{time:"10:23",pond:"3\u53f7\u9c7c\u5858",type:"\u6eb6\u6c27",level:"danger",status:"\u5904\u7406\u4e2d"},{time:"09:45",pond:"2\u53f7\u9c7c\u5858",type:"\u6c28\u6c2e",level:"warning",status:"\u5df2\u901a\u77e5"},{time:"09:12",pond:"1\u53f7\u9c7c\u5858",type:"\u673a\u5668\u4eba",level:"info",status:"\u5df2\u5904\u7406"},{time:"08:55",pond:"5\u53f7\u9c7c\u5858",type:"\u6c34\u6e29",level:"warning",status:"\u76d1\u63a7\u4e2d"},{time:"07:30",pond:"4\u53f7\u9c7c\u5858",type:"\u6d4a\u5ea6",level:"info",status:"\u5df2\u6062\u590d"}];')
add('  var lbc={danger:"red",warning:"orange",info:"blue"};var lt={danger:"\u4e25\u91cd",warning:"\u9884\u8b66",info:"\u4fe1\u606f"};var sbc={"\u5904\u7406\u4e2d":"orange","\u5df2\u901a\u77e5":"blue","\u5df2\u5904\u7406":"green","\u76d1\u63a7\u4e2d":"blue","\u5df2\u6062\u590d":"green"};')
add('  var thtml="";rows.forEach(function(r){thtml+="<tr><td class=\\"mono\\">"+r.time+"</td><td>"+r.pond+"</td><td>"+r.type+"</td><td><span class=\\"badge badge-"+lbc[r.level]+"\\">"+lt[r.level]+"</span></td><td><span class=\\"badge badge-"+sbc[r.status]+"\\">"+r.status+"</span></td></tr>";});')
add('  document.getElementById("alertTable").innerHTML=thtml;lucide.createIcons();')
add('}')

with open(OUT, 'a', encoding='utf-8') as f:
    f.write('\n'.join(js_lines))
print('JS Part 1 written. Total:', os.path.getsize(OUT), 'bytes')
