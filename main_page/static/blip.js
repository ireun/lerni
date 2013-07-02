var start = function (){
	var blipblock = document.getElementById('blip');
	blipblock.innerHTML = "Ładowanie blipa...";	
	var data_src = 'http://api.blip.pl/users/staszic/statuses.json?callback=show_blip&limit=5&nocache='+Math.round(Math.random()*(1<<30));
	blip_load_data(data_src);
}

var blip_load_data = function(src) {
	if ((t = document.getElementById('blip-data')) != null)
		t.parentNode.removeChild(t)
	s=doc_create_element('script');
	s.setAttribute('src', src);
	s.setAttribute('type', 'text/javascript');
	s.setAttribute('id', 'blip-data');

	document.getElementsByTagName('head')[0].appendChild(s);
}
doc_create_element = function(e) {
	return document.createElement(e);
};
var show_blip = function(b){
	var blipblock=document.getElementById('blip');
	var bliptext="";
	var pictures=["","","","",""];
	for (var i=0; i < b.length; i++) {
		bliptext=bliptext+'<div class="blip_post" id="blip_'+i+'">'+b[i].body+'</div>';
		if (typeof b[i].pictures_path != "undefined") {
			pictures[i]=b[i].pictures_path;
		}
	}	
	blipblock.innerHTML=bliptext;
	for (var i=0; i < b.length; i++) {
		if (pictures[i] != ""){
			loadimages(pictures[i],i)
		}		
	}
	
}
var loadimages = function (aaa,i){
	var img_src="http://blip.pl"+aaa+"?callback=add_pict_"+i;
	
	if ((t = document.getElementById('blip-data2')) != null)
		t.parentNode.removeChild(t)
	s=doc_create_element('script');
	s.setAttribute('src', img_src);
	s.setAttribute('type', 'text/javascript');
	s.setAttribute('id', 'blip-data2');
	document.getElementsByTagName('head')[0].appendChild(s);
}

var add_pict_0 = function(b){add_pict(0,b)}
var add_pict_1 = function(b){add_pict(1,b)}
var add_pict_2 = function(b){add_pict(2,b)}
var add_pict_3 = function(b){add_pict(3,b)}
var add_pict_4 = function(b){add_pict(4,b)}
var add_pict = function(b,c){
	var block = document.getElementById('blip_'+b)
	block.innerHTML=block.innerHTML+"<br />"+'<img class="blip_img" src="'+c[0].url.replace(".jpg","_inmsg.jpg")+'"/>'+"<br />";
				// _inmsg.jpg _moze_ robic problemy (?)
}


