var ground_level=8;
var h=0;
var x=0;
var move=false;
var x_v=0;
var h_v=0;
var t=0;
var g=10;
var h_begin=0;

var h_prev=0;
var x_prev=0;

var start_date=0;

var load = function(){
   var board = document.getElementById('board');
   var fly = document.getElementById('board');
   width = board.width;
   height = board.height;
   context = board.getContext('2d');
   return setInterval(draw, 20);
}
function draw() {	
	if(move){
		var h_max = h_v*h_v/20; 
		var t_max = Math.sqrt((2*h_begin+2*h_max)/g)+h_v/g;
		t=Math.min(parseFloat(new Date().getTime()-start_date)/1000,t_max);
		h=t*h_v+h_begin-(g*t*t)/2;
		x=x_v*t;
		if(h==0){
			move=false;
		}
	}
	if(clean2===0){
		var fly_context = fly.getContext('2d');
		fly_context.beginPath();
		fly_context.strokeStyle = '#0099FF'; 
   	fly_context.moveTo(x, height-h-5);
   	fly_context.lineTo(x_prev, height-h_prev-5);
   	fly_context.stroke();
   	fly_context.closePath();
	}
	h_prev=h;
	x_prev=x;
	document.getElementById('time').value=Math.round(t*100)/100;
	document.getElementById('height').value=Math.round(h)/100;
	document.getElementById('distance').value=Math.round(x)/100;
	context.clearRect(0,400,800,8);	
	draw_scale();
	context.clearRect(0,0,800,400);
	context.beginPath();
	context.strokeStyle = '#0099FF'; 
	context.fillStyle = '#0099FF'; 
	context.arc(x, height-h-ground_level, 10, 0, Math.PI*2, true); 
	context.closePath();
	context.fill();
	//if(x>800){
	//	alert(t);
	//	t=0;
	//}
}
function draw_scale(){
	context.beginPath();
	context.strokeStyle = '#0099FF'; 
   for(i=1; i<10; i++){
   	context.moveTo(100*i, 0);
   	context.lineTo(100*i, height);
   }
   context.stroke();
   context.closePath();
}
var clean2=0;
function tdo(){
	t=0;
	x=0;
	h=0;
	
	h_prev=0;
	x_prev=0;
	h_begin = parseInt(document.getElementById('height_begin').value);
	var v = parseInt(document.getElementById('velocity_begin').value);
	var a = parseInt(document.getElementById('angle_begin').value);
	h_v = v*Math.round(Math.sin(a*Math.PI/180)*100)/100;
	x_v = v*Math.round(Math.cos(a*Math.PI/180)*100)/100;
	//var delta = parseFloat(h_v*h_v-4*g*-2*h_begin); 
	//var t_max=(-h_v+Math.sqrt(delta))/(2*g) +(2*h_v)/g;
	var h_max = h_v*h_v/20; 
	var t_max = Math.sqrt((2*h_begin+2*h_max)/g)+h_v/g;
	document.getElementById('time_max').value=Math.round(t_max*100)/100;
	//var h_max =(t_max/2)*h_v+h_begin-(g*(t_max/2)*(t_max/2))/2;	
	document.getElementById('height_max').value=Math.round((h_max+h_begin))/100;
	document.getElementById('distance_max').value=Math.round(t_max*x_v)/100;
	start_date = new Date().getTime();
	move=true;
	clean2=0;
}
function clean(){
	var fly_context = fly.getContext('2d');
	fly_context.clearRect(0,0,800,500);	
	clean2=1;
}



