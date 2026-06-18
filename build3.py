# -*- coding: utf-8 -*-
import os
DIR = r'D:\夸克\3'

js = '''
<script>
// ===== Global State =====
var SD = {
  do: {value:7.2,unit:"mg/L",label:"\u6eb6\u6c27\u91cf",status:"normal",min:5,max:10,icon:"droplets"},
  temp: {value:26.3,unit:"\u00b0C",label:"\u6c34\u6e29",status:"normal",min:15,max:35,icon:"thermometer"},
  ph: {value:7.4,unit:"",label:"pH\u503c",status:"normal",min:6.5,max:9,icon:"flask-conical"},
  nh3: {value:0.08,unit:"mg/L",label:"\u6c28\u6c2e",status:"warning",min:0,max:0.5,icon:"alert-triangle"},
  turb: {value:12.5,unit:"NTU",label:"\u6d4a\u5ea6",status:"normal",min:0,max:50,icon:"cloud"}
};
var H = {do:[],temp:[],ph:[],nh3:[],turb:[],labels:[]};
var showHeatmap=true,showPath=true,showSensor=true,robotAngle=0;
var twinInited=false;

// History
(function(){
  var now=new Date();
  for(var i=23;i>=0;i--){
    var t=new Date(now-i*3600000);
    H.labels.push(t.getHours()+":00");
    H.do.push(+(6.5+Math.random()*2).toFixed(1));
    H.temp.push(+(24+Math.random()*4).toFixed(1));
    H.ph.push(+(7+Math.random()*0.8).toFixed(1));
    H.nh3.push(+(0.05+Math.random()*0.1).toFixed(2));
    H.turb.push(+(8+Math.random()*10).toFixed(1));
  }
})();

// ===== Lucide =====
document.addEventListener("DOMContentLoaded",function(){lucide.createIcons();});

// ===== Navigation =====
var titles={dashboard:["\u6570\u636e\u770b\u677f","\u603b\u89c8 / \u6570\u636e\u770b\u677f"],ponds:["\u9c7c\u5858\u7ba1\u7406","\u7ba1\u7406 / \u9c7c\u5858\u7ba1\u7406"],monitor:["\u5b9e\u65f6\u76d1\u63a7","\u76d1\u63a7 / \u5b9e\u65f6\u76d1\u63a7"],twin:["\u6570\u5b57\u5b5a\u751f","\u6570\u5b57\u5b5a\u751f / 3D\u573a\u666f"],robot:["\u673a\u5668\u4eba\u7ba1\u7406","\u8bbe\u5907 / \u673a\u5668\u4eba\u7ba1\u7406"],report:["\u62a5\u544a\u4e2d\u5fc3","\u5206\u6790 / \u62a5\u544a\u4e2d\u5fc3"]};

function switchPage(page){
  document.querySelectorAll(".page").forEach(function(p){p.classList.remove("active");});
  document.querySelectorAll(".nav-item").forEach(function(n){n.classList.remove("active");});
  document.getElementById("page-"+page).classList.add("active");
  document.querySelector('[data-page="'+page+'"]').classList.add("active");
  document.getElementById("pageTitle").textContent=titles[page][0];
  document.getElementById("pageBreadcrumb").textContent=titles[page][1];
  if(page==="twin"&&!twinInited)setTimeout(initThreeScene,200);
  if(window._charts)Object.values(window._charts).forEach(function(c){c.resize();});
}

document.querySelectorAll(".nav-item").forEach(function(el){
  el.addEventListener("click",function(){switchPage(el.dataset.page);});
});

// ===== Clock =====
function updateClock(){
  var now=new Date();
  document.getElementById("headerTime").textContent=
    now.toLocaleDateString("zh-CN",{month:"2-digit",day:"2-digit"})+" "+
    now.toLocaleTimeString("zh-CN",{hour12:false});
}
setInterval(updateClock,1000);updateClock();

// ===== Sensor Cards =====
function renderSensorCards(){
  var c=document.getElementById("sensorCards");
  var cols={normal:"var(--accent-green)",warning:"var(--accent-orange)",danger:"var(--accent-red)"};
  var bg={normal:"var(--accent-green-dim)",warning:"var(--accent-orange-dim)",danger:"var(--accent-red-dim)"};
  var ics={normal:"check-circle",warning:"alert-circle",danger:"x-circle"};
  var stx={normal:"\u6b63\u5e38",warning:"\u504f\u9ad8",danger:"\u5f02\u5e38"};
  var html="";
  for(var k in SD){
    var d=SD[k];
    html+='<div class="data-card"><div class="data-card-header"><span class="data-card-label">'+d.label+'</span><div class="data-card-icon" style="background:'+bg[d.status]+'"><i data-lucide="'+d.icon+'" style="color:'+cols[d.status]+'"></i></div></div><div class="data-card-value" style="color:'+cols[d.status]+'">'+d.value+'<span class="data-card-unit">'+d.unit+'</span></div><div class="data-card-status '+d.status+'"><i data-lucide="'+ics[d.status]+'" style="width:14px;height:14px;"></i> '+stx[d.status]+' \u00b7 \u8303\u56f4 '+d.min+'-'+d.max+d.unit+'</div></div>';
  }
  c.innerHTML=html;lucide.createIcons();
}

// ===== Monitor Cards =====
function renderMonitorCards(){
  var c=document.getElementById("monitorCards");
  var html="";
  for(var k in SD){
    var d=SD[k];
    html+='<div class="data-card"><div class="data-card-header"><span class="data-card-label">'+d.label+' \u5b9e\u65f6</span><div class="data-card-icon" style="background:var(--accent-blue-dim)"><i data-lucide="radio" style="color:var(--accent-blue)"></i></div></div><div class="data-card-value" style="color:var(--accent-blue)">'+d.value+'<span class="data-card-unit">'+d.unit+'</span></div><div style="font-size:12px;color:var(--text-muted);margin-top:8px;">\u91c7\u96c6\u9891\u7387: 5s \u00b7 \u4e0a\u6b21\u66f4\u65b0: \u521a\u521a</div></div>';
  }
  c.innerHTML=html;lucide.createIcons();
}

// ===== Alerts =====
var alertsData=[
  {type:"danger",title:"3\u53f7\u9c7c\u5858\u6eb6\u6c27\u504f\u4f4e",desc:"\u6eb6\u6c27\u964d\u81f34.2mg/L\uff0c\u4f4e\u4e8e\u5b89\u5168\u9608\u503c5.0mg/L",time:"10:23:15"},
  {type:"warning",title:"2\u53f7\u9c7c\u5858\u6c28\u6c2e\u504f\u9ad8",desc:"\u6c28\u6c2e\u6d53\u5ea60.12mg/L\uff0c\u63a5\u8fd1\u9884\u8b66\u7ebf0.15mg/L",time:"09:45:02"},
  {type:"info",title:"1\u53f7\u9c7c\u5858\u673a\u5668\u4eba\u8fd4\u822a",desc:"AquaBot-01\u5b8c\u6210\u5de1\u822a\u4efb\u52a1\uff0c\u6b63\u5728\u8fd4\u822a\u5145\u7535",time:"09:12:38"},
  {type:"warning",title:"5\u53f7\u9c7c\u5858\u6c34\u6e29\u504f\u9ad8",desc:"\u6c34\u6e29\u8fbe\u523030.2\u00b0C\uff0c\u5efa\u8bae\u5f00\u542f\u589e\u6c27",time:"08:55:11"}
];

function renderAlerts(){
  var ics={danger:"alert-octagon",warning:"alert-triangle",info:"info"};
  var html="";
  alertsData.forEach(function(a){
    html+='<div class="alert-item '+a.type+'"><div class="alert-icon"><i data-lucide="'+ics[a.type]+'"></i></div><div class="alert-content"><div class="alert-title">'+a.title+'</div><div class="alert-desc">'+a.desc+'</div><div class="alert-time">'+a.time+'</div></div></div>';
  });
  document.getElementById("alertList").innerHTML=html;

  var rows=[
    {time:"10:23",pond:"3\u53f7\u9c7c\u5858",type:"\u6eb6\u6c27",level:"danger",status:"\u5904\u7406\u4e2d"},
    {time:"09:45",pond:"2\u53f7\u9c7c\u5858",type:"\u6c28\u6c2e",level:"warning",status:"\u5df2\u901a\u77e5"},
    {time:"09:12",pond:"1\u53f7\u9c7c\u5858",type:"\u673a\u5668\u4eba",level:"info",status:"\u5df2\u5904\u7406"},
    {time:"08:55",pond:"5\u53f7\u9c7c\u5858",type:"\u6c34\u6e29",level:"warning",status:"\u76d1\u63a7\u4e2d"},
    {time:"07:30",pond:"4\u53f7\u9c7c\u5858",type:"\u6d4a\u5ea6",level:"info",status:"\u5df2\u6062\u590d"}
  ];
  var lbc={danger:"red",warning:"orange",info:"blue"};
  var lt={danger:"\u4e25\u91cd",warning:"\u9884\u8b66",info:"\u4fe1\u606f"};
  var sbc={"\u5904\u7406\u4e2d":"orange","\u5df2\u901a\u77e5":"blue","\u5df2\u5904\u7406":"green","\u76d1\u63a7\u4e2d":"blue","\u5df2\u6062\u590d":"green"};
  var thtml="";
  rows.forEach(function(r){
    thtml+='<tr><td class="mono">'+r.time+'</td><td>'+r.pond+'</td><td>'+r.type+'</td><td><span class="badge badge-'+lbc[r.level]+'">'+lt[r.level]+'</span></td><td><span class="badge badge-'+sbc[r.status]+'">'+r.status+'</span></td></tr>';
  });
  document.getElementById("alertTable").innerHTML=thtml;
  lucide.createIcons();
}

// ===== Pond Grid =====
function renderPondGrid(){
  var ponds=[
    {name:"1\u53f7\u9c7c\u5858",area:"1200",depth:"2.5",species:"\u9c88\u9c7c",density:"800\u5c3e/\u4ea9",do:7.2,temp:26.3,status:"normal"},
    {name:"2\u53f7\u9c7c\u5858",area:"800",depth:"2.0",species:"\u8349\u9c7c",density:"1200\u5c3e/\u4ea9",do:6.8,temp:25.8,status:"warning"},
    {name:"3\u53f7\u9c7c\u5858",area:"1500",depth:"3.0",species:"\u9c88\u9c7c",density:"600\u5c3e/\u4ea9",do:4.2,temp:27.1,status:"danger"},
    {name:"4\u53f7\u9c7c\u5858",area:"600",depth:"1.8",species:"\u9cab\u9c7c",density:"1500\u5c3e/\u4ea9",do:7.5,temp:24.9,status:"normal"},
    {name:"5\u53f7\u9c7c\u5858",area:"1000",depth:"2.2",species:"\u9c88\u9c7c",density:"900\u5c3e/\u4ea9",do:6.1,temp:30.2,status:"warning"},
    {name:"6\u53f7\u9c7c\u5858",area:"900",depth:"2.0",species:"\u9ca4\u9c7c",density:"1000\u5c3e/\u4ea9",do:7.8,temp:25.5,status:"normal"}
  ];
  var sc={normal:"green",warning:"orange",danger:"red"};
  var st={normal:"\u5065\u5eb7",warning:"\u9884\u8b66",danger:"\u5f02\u5e38"};
  var html="";
  ponds.forEach(function(p,idx){
    html+='<div class="pond-card" data-idx="'+idx+'"><div class="pond-card-title"><i data-lucide="waves" style="width:18px;height:18px;color:var(--accent-cyan)"></i>'+p.name+'<span class="badge badge-'+sc[p.status]+'" style="margin-left:auto">'+st[p.status]+'</span></div><div class="pond-card-meta">\u54c1\u79cd: '+p.species+' \u00b7 \u9762\u79ef: '+p.area+'m\u00b2 \u00b7 \u6c34\u6df1: '+p.depth+'m \u00b7 \u5bc6\u5ea6: '+p.density+'</div><div class="pond-card-stats"><div class="pond-stat"><div class="pond-stat-label">\u6eb6\u6c27</div><div class="pond-stat-value">'+p.do+' mg/L</div></div><div class="pond-stat"><div class="pond-stat-label">\u6c34\u6e29</div><div class="pond-stat-value">'+p.temp+'\u00b0C</div></div></div></div>';
  });
  document.getElementById("pondGrid").innerHTML=html;
  document.querySelectorAll(".pond-card").forEach(function(card){
    card.addEventListener("click",function(){switchPage("twin");});
  });
  lucide.createIcons();
}

// ===== Robots =====
function renderRobots(){
  var robots=[
    {name:"AquaBot-01",status:"\u5de1\u822a\u4e2d",battery:78,task:"\u6eb6\u6c27\u8865\u6c27",pond:"1\u53f7\u9c7c\u5858",speed:"1.2 m/s"},
    {name:"AquaBot-02",status:"\u5145\u7535\u4e2d",battery:35,task:"\u5f85\u547d",pond:"\u5145\u7535\u7ad9",speed:"0 m/s"},
    {name:"AquaBot-03",status:"\u5de1\u822a\u4e2d",battery:92,task:"\u6c34\u8d28\u68c0\u6d4b",pond:"3\u53f7\u9c7c\u5858",speed:"0.8 m/s"}
  ];
  var html="";
  robots.forEach(function(r){
    html+='<div class="robot-card"><div class="robot-avatar"><i data-lucide="bot"></i></div><div class="robot-info"><div class="robot-name">'+r.name+' <span class="badge badge-'+(r.status==="\u5de1\u822a\u4e2d"?"green":"blue")+'" style="margin-left:8px">'+r.status+'</span></div><div class="robot-desc">\u4efb\u52a1: '+r.task+' \u00b7 \u4f4d\u7f6e: '+r.pond+' \u00b7 \u901f\u5ea6: '+r.speed+'</div></div><div class="robot-stats"><div class="robot-stat"><div class="robot-stat-val" style="color:'+(r.battery>50?"var(--accent-green)":"var(--accent-orange)")+'">'+r.battery+'%</div><div class="robot-stat-label">\u7535\u91cf</div></div></div></div>';
  });
  document.getElementById("robotList").innerHTML=html;

  var tasks=[
    {task:"\u6eb6\u6c27\u8865\u6c27",robot:"AquaBot-01",time:"10:00 - 12:00",status:"\u8fdb\u884c\u4e2d"},
    {task:"\u6c34\u8d28\u5de1\u68c0",robot:"AquaBot-03",time:"09:30 - 11:30",status:"\u8fdb\u884c\u4e2d"},
    {task:"\u5168\u9762\u5de1\u5858",robot:"AquaBot-01",time:"14:00 - 16:00",status:"\u5f85\u6267\u884c"},
    {task:"\u81ea\u52a8\u8fd4\u822a\u5145\u7535",robot:"AquaBot-02",time:"08:00 - 10:00",status:"\u5df2\u5b8c\u6210"}
  ];
  var sb={"\u8fdb\u884c\u4e2d":"orange","\u5f85\u6267\u884c":"blue","\u5df2\u5b8c\u6210":"green"};
  var thtml="";
  tasks.forEach(function(t){
    thtml+='<tr><td>'+t.task+'</td><td>'+t.robot+'</td><td class="mono">'+t.time+'</td><td><span class="badge badge-'+sb[t.status]+'">'+t.status+'</span></td></tr>';
  });
  document.getElementById("taskTable").innerHTML=thtml;
  lucide.createIcons();
}

// ===== Reports =====
function renderReports(){
  var reports=[
    {id:"RPT-20260617-001",type:"\u65e5\u62a5",pond:"\u5168\u90e8",time:"2026-06-17 08:00",score:87,risk:"\u4f4e"},
    {id:"RPT-20260616-001",type:"\u65e5\u62a5",pond:"\u5168\u90e8",time:"2026-06-16 08:00",score:82,risk:"\u4f4e"},
    {id:"RPT-20260609-001",type:"\u5468\u62a5",pond:"\u5168\u90e8",time:"2026-06-09 09:00",score:79,risk:"\u4e2d"},
    {id:"RPT-20260601-001",type:"\u6708\u62a5",pond:"\u5168\u90e8",time:"2026-06-01 09:00",score:84,risk:"\u4f4e"},
    {id:"RPT-20260526-001",type:"\u65e5\u62a5",pond:"3\u53f7\u9c7c\u5858",time:"2026-05-26 08:00",score:65,risk:"\u9ad8"}
  ];
  var rb={"\u4f4e":"green","\u4e2d":"orange","\u9ad8":"red"};
  var html="";
  reports.forEach(function(r){
    html+='<tr><td class="mono">'+r.id+'</td><td>'+r.type+'</td><td>'+r.pond+'</td><td class="mono">'+r.time+'</td><td><strong>'+r.score+'</strong></td><td><span class="badge badge-'+rb[r.risk]+'">'+r.risk+'\u98ce\u9669</span></td><td><button class="btn" style="padding:4px 10px;font-size:12px"><i data-lucide="download" style="width:12px;height:12px"></i> \u5bfc\u51fa</button></td></tr>';
  });
  document.getElementById("reportTable").innerHTML=html;
  lucide.createIcons();
}

document.getElementById("btnGenReport").addEventListener("click",function(){alert("\u62a5\u544a\u751f\u6210\u4e2d... \u5b8c\u6210\u540e\u5c06\u51fa\u73b0\u5728\u5217\u8868\u4e2d");});
'''

with open(os.path.join(DIR, 'index.html'), 'a', encoding='utf-8') as f:
    f.write(js)
print('Part 3 JS core written')
