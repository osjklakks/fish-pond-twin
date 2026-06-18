# -*- coding: utf-8 -*-
import os
DIR = r'D:\夸克\3'

js2 = '''
// ===== ECharts =====
function initCharts(){
  var doChart=echarts.init(document.getElementById("chartDoTrend"));
  doChart.setOption({backgroundColor:"transparent",grid:{left:50,right:20,top:20,bottom:30},xAxis:{type:"category",data:H.labels,axisLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b",fontSize:11},axisTick:{show:false}},yAxis:{type:"value",min:4,max:10,splitLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b",fontSize:11},axisLine:{show:false}},series:[{type:"line",data:H.do,smooth:true,symbol:"none",lineStyle:{color:"#22c55e",width:2},areaStyle:{color:{type:"linear",x:0,y:0,x2:0,y2:1,colorStops:[{offset:0,color:"rgba(34,197,94,.25)"},{offset:1,color:"rgba(34,197,94,0)"}]}},markLine:{silent:true,lineStyle:{color:"#ef4444",type:"dashed"},data:[{yAxis:5,label:{formatter:"\u5b89\u5168\u7ebf 5.0",color:"#ef4444",fontSize:11}}]}}],tooltip:{trigger:"axis",backgroundColor:"#1e293b",borderColor:"#334155",textStyle:{color:"#f1f5f9",fontSize:12}}});

  var radarChart=echarts.init(document.getElementById("chartRadar"));
  radarChart.setOption({backgroundColor:"transparent",radar:{indicator:[{name:"\u6eb6\u6c27",max:10},{name:"pH",max:14},{name:"\u6c34\u6e29",max:40},{name:"\u6c28\u6c2e",max:0.5},{name:"\u6d4a\u5ea6",max:50}],axisName:{color:"#94a3b8",fontSize:12},splitArea:{areaStyle:{color:["rgba(30,41,59,.3)","rgba(30,41,59,.15)"]}},axisLine:{lineStyle:{color:"#1e293b"}},splitLine:{lineStyle:{color:"#1e293b"}}},series:[{type:"radar",data:[{value:[7.2,7.4,26.3,0.08,12.5],name:"\u5f53\u524d\u503c",areaStyle:{color:"rgba(34,197,94,.15)"},lineStyle:{color:"#22c55e"},itemStyle:{color:"#22c55e"}}]}],tooltip:{backgroundColor:"#1e293b",borderColor:"#334155",textStyle:{color:"#f1f5f9"}}});

  var barChart=echarts.init(document.getElementById("chartPondBar"));
  barChart.setOption({backgroundColor:"transparent",grid:{left:60,right:20,top:10,bottom:30},xAxis:{type:"category",data:["1\u53f7\u5858","2\u53f7\u5858","3\u53f7\u5858","4\u53f7\u5858","5\u53f7\u5858","6\u53f7\u5858"],axisLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b"},axisTick:{show:false}},yAxis:{type:"value",name:"\u6eb6\u6c27 mg/L",nameTextStyle:{color:"#64748b"},splitLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b"},axisLine:{show:false}},series:[{type:"bar",barWidth:28,data:[{value:7.2,itemStyle:{color:"#22c55e"}},{value:6.8,itemStyle:{color:"#22c55e"}},{value:4.2,itemStyle:{color:"#ef4444"}},{value:7.5,itemStyle:{color:"#22c55e"}},{value:6.1,itemStyle:{color:"#f59e0b"}},{value:7.8,itemStyle:{color:"#22c55e"}}],markLine:{silent:true,lineStyle:{color:"#ef4444",type:"dashed"},data:[{yAxis:5}]}}],tooltip:{trigger:"axis",backgroundColor:"#1e293b",borderColor:"#334155",textStyle:{color:"#f1f5f9"}}});

  var multiChart=echarts.init(document.getElementById("chartMultiTrend"));
  multiChart.setOption({backgroundColor:"transparent",grid:{left:50,right:50,top:30,bottom:30},legend:{data:["\u6eb6\u6c27","\u6c34\u6e29","pH"],textStyle:{color:"#94a3b8",fontSize:12},top:0},xAxis:{type:"category",data:H.labels,axisLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b",fontSize:11},axisTick:{show:false}},yAxis:[{type:"value",name:"mg/L / pH",splitLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b"},axisLine:{show:false}},{type:"value",name:"\u00b0C",splitLine:{show:false},axisLabel:{color:"#64748b"},axisLine:{show:false}}],series:[{name:"\u6eb6\u6c27",type:"line",data:H.do,smooth:true,symbol:"none",lineStyle:{color:"#22c55e",width:2},itemStyle:{color:"#22c55e"}},{name:"pH",type:"line",data:H.ph,smooth:true,symbol:"none",lineStyle:{color:"#a78bfa",width:2},itemStyle:{color:"#a78bfa"}},{name:"\u6c34\u6e29",type:"line",yAxisIndex:1,data:H.temp,smooth:true,symbol:"none",lineStyle:{color:"#f59e0b",width:2},itemStyle:{color:"#f59e0b"}}],tooltip:{trigger:"axis",backgroundColor:"#1e293b",borderColor:"#334155",textStyle:{color:"#f1f5f9",fontSize:12}}});

  var robotChart=echarts.init(document.getElementById("chartRobot"));
  var rh=[];
  for(var i=0;i<12;i++)rh.push((8+i)+":00");
  robotChart.setOption({backgroundColor:"transparent",grid:{left:50,right:50,top:30,bottom:30},legend:{data:["AquaBot-01","AquaBot-02","AquaBot-03"],textStyle:{color:"#94a3b8",fontSize:12},top:0},xAxis:{type:"category",data:rh,axisLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b"},axisTick:{show:false}},yAxis:{type:"value",max:100,name:"\u7535\u91cf %",nameTextStyle:{color:"#64748b"},splitLine:{lineStyle:{color:"#1e293b"}},axisLabel:{color:"#64748b"},axisLine:{show:false}},series:[{name:"AquaBot-01",type:"line",data:[100,95,88,82,78,75,70,65,60,55,50,45],smooth:true,symbol:"none",lineStyle:{color:"#22d3ee",width:2},itemStyle:{color:"#22d3ee"}},{name:"AquaBot-02",type:"line",data:[20,25,30,35,40,50,60,70,80,85,90,95],smooth:true,symbol:"none",lineStyle:{color:"#a78bfa",width:2},itemStyle:{color:"#a78bfa"}},{name:"AquaBot-03",type:"line",data:[100,98,96,94,92,90,88,86,84,82,80,78],smooth:true,symbol:"none",lineStyle:{color:"#22c55e",width:2},itemStyle:{color:"#22c55e"}}],tooltip:{trigger:"axis",backgroundColor:"#1e293b",borderColor:"#334155",textStyle:{color:"#f1f5f9"}}});

  renderTwinSensors();
  window.addEventListener("resize",function(){doChart.resize();radarChart.resize();barChart.resize();multiChart.resize();robotChart.resize();});
  window._charts={doChart:doChart,radarChart:radarChart,barChart:barChart,multiChart:multiChart,robotChart:robotChart};
}

function renderTwinSensors(){
  var sensors=[
    {name:"\u6eb6\u6c27 DO",value:"7.2 mg/L",color:"var(--accent-green)"},
    {name:"\u6c34\u6e29",value:"26.3\u00b0C",color:"var(--accent-orange)"},
    {name:"pH\u503c",value:"7.4",color:"var(--accent-purple)"},
    {name:"\u6c28\u6c2e",value:"0.08 mg/L",color:"var(--accent-orange)"},
    {name:"\u6d4a\u5ea6",value:"12.5 NTU",color:"var(--accent-blue)"}
  ];
  var html="";
  sensors.forEach(function(s){
    html+='<div style="display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--border)"><span style="font-size:13px;color:var(--text-secondary)">'+s.name+'</span><span style="font-family:var(--font-data);font-size:14px;font-weight:600;color:'+s.color+'">'+s.value+'</span></div>';
  });
  document.getElementById("twinSensorList").innerHTML=html;
  document.getElementById("twinRobotInfo").innerHTML='<div style="font-size:13px;color:var(--text-secondary);line-height:1.8"><div style="display:flex;justify-content:space-between"><span>\u8bbe\u5907</span><span style="color:var(--text-primary);font-weight:500">AquaBot-01</span></div><div style="display:flex;justify-content:space-between"><span>\u72b6\u6001</span><span class="badge badge-green">\u5de1\u822a\u4e2d</span></div><div style="display:flex;justify-content:space-between"><span>\u7535\u91cf</span><span style="color:var(--accent-green);font-family:var(--font-data)">78%</span></div><div style="display:flex;justify-content:space-between"><span>\u901f\u5ea6</span><span style="font-family:var(--font-data)">1.2 m/s</span></div><div style="display:flex;justify-content:space-between"><span>\u4efb\u52a1</span><span>\u6eb6\u6c27\u8865\u6c27</span></div></div>';
}
'''

with open(os.path.join(DIR, 'index.html'), 'a', encoding='utf-8') as f:
    f.write(js2)
print('Part 4 ECharts written')
