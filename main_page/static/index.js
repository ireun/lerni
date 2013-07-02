var show_allerts = function(allerts_list,allert_type,allert_location){
	var n=noty({text: allerts_list,type: allert_type,layout: allert_location}); //callback:{afterClose: function(){nic=0} }});
}
$(document).ready(
function()
{
	Tinycon.setBubble(80);
	jQuery("abbr.timeago").timeago();
	jQuery("#breadCrumb").jBreadCrumb();
	


		  jQuery.timeago.settings.strings = {
		    prefixAgo: null,
		    prefixFromNow: "za",
		    suffixAgo: "temu",
		    suffixFromNow: null,
		    seconds: "mniej niż minutę",
		    minute: "minutę",
		    minutes: function(value) { return numpf(value, "%d minuty", "%d minut"); },
		    hour: "godzinę",
		    hours: function(value) { return numpf(value, "%d godziny", "%d godzin"); },
		    day: "dzień",
		    days: "%d dni",
		    month: "miesiąc",
		    months: function(value) { return numpf(value, "%d miesiące", "%d miesięcy"); },
		    year: "rok",
		    years: function(value) { return numpf(value, "%d lata", "%d lat"); }
		  };
   $(".shortable").toggleClass("content_short");
   $(".shortable img").load(function(){
   if( $(this).parent().height()>200){
      $(this).parent().toggleClass("content_short");
   }
   /*
   $(".content").each(function(index) {
      alert(index + ': ' + $(this).height());
   });
   */
   });
   
   
   
	$("table").delegate('td','mouseover mouseleave', function(e) {
		var table = $(this).parent().parent().parent();
		var col = $(this).parent().children().index($(this));
		var row = $(this).parent().parent().children().index($(this).parent());
		if (e.type == 'mouseover') {
			$(this).addClass("hover");
			$(this).parent().addClass("rowHover");
			$("tr td:nth-child("+(col+1)+")", table).addClass("columnHover");
		}
		else {
			$(this).removeClass("hover");
			$(this).parent().removeClass("rowHover");
			$("tr td:nth-child("+(col+1)+")", table).removeClass("columnHover");
		}
	});
});
var toggle_comments = function(x,y){
   var button_show_comments =  x.parentNode.parentNode.getElementsByTagName("div")[9];
   if (button_show_comments.innerHTML.substring(0,5)==="Pokaż"){
      show_comments(x,y);
   }else{
      hide_comments(x,y);
   }
}
var show_comments = function(x,y){
   var post_content = x.parentNode.parentNode.getElementsByTagName("div")[11];
   var button_show_comments =  x.parentNode.parentNode.getElementsByTagName("div")[9];
   var api_url = '/api/jsonp/post_comments?post_id='+y;
   $.post(api_url, {no_cache: "just_noo!"}, function(data) {
      $(post_content).html("");
      $.each(data, function(key, val) {
         for(var i=0; i<val.length; i++){
            $(post_content).html($(post_content).html()+'<div class="wrapper"><div class="avatar"></div><div class="comment"><div class="author">'+
            val[i][1]+'</div><div class="time">'+val[i][2]+'</div><div class="delete" onclick="rm_comment(this,'+y+','+val[i][0]+
            ')"></div><br /><div class="content">'+val[i][3]+'</div></div></div>');
         }
         $(post_content).html($(post_content).html()+'<div class="wrapper"><div class="avatar"></div>'+
         '<form action="javascript://" method="post" onsubmit="add_comment(this,'+y+');"><textarea></textarea><input type="submit"></input></form></div>');
         button_show_comments.innerHTML="Ukryj komentarze ("+i+")";
      });      
      $('.comments .wrapper').height(0);                                /*Można zrobić jakoś ładniej*/
      $('.comments .wrapper').each(function(x){
         $(this).height(function(){
            return $(this).children().height();
         });
      });/*
      alert("Refreshed");*/
   }, "json");
}
var hide_comments = function(x,y){
   var post_content = x.parentNode.parentNode.getElementsByTagName("div")[11];
   var button_show_comments =  x.parentNode.parentNode.getElementsByTagName("div")[9];
   var api_url = '/api/jsonp/post_comments?post_id='+y;
   $.post(api_url, {no_cache: "just_noo!"}, function(data) {
      $(post_content).html("");
      $.each(data, function(key, val) {
         for(var i=0; i<val.length; i++){
         }
      button_show_comments.innerHTML="Pokaż komentarze ("+i+")";
      });
   }, "json");
}
var add_comment = function(x,y){
   var add_comment_url = '/add_comment';
   $.post(add_comment_url, { id: y, content: x.getElementsByTagName("textarea")[0].value },
   function(data) {
      show_comments(x.parentNode,y);
   });
}
var rm_comment = function(x,y,z){
   var rm_comment_url = '/rm_comment';
   $.post(rm_comment_url, { comment_id: z},
   function(data) {
      show_comments(x.parentNode.parentNode,y);
   });
}

/*
$.getJSON('ajax/test.json', function(data) {
  var items = [];

  $.each(data, function(key, val) {
    items.push('<li id="' + key + '">' + val + '</li>');
  });

  $('<ul/>', {
    'class': 'my-new-list',
    html: items.join('')
  }).appendTo('body');
});
*/


var show_post = function(x){
   post_content = x.parentNode.parentNode.getElementsByTagName("div")[7];
   if(x.innerHTML==='Zwiń<img src="/static/shrink.png">' && $(post_content).height()>200){
      x.innerHTML='Rozwiń<img src="/static/expand.png">';
   }else{
      x.innerHTML='Zwiń<img src="/static/shrink.png">';
   }
   if($(post_content).height() || post_content.className.indexOf("content_short")!=-1){
      toggleclass(post_content,"content_short");
   }
}
function show_post_options(x)
{
   toggleclass(x.parentNode.getElementsByTagName("div")[2],"post_options_exp");
}
var toggleclass = function(x,y){
   if (x.className.indexOf(y)===-1){
      x.className += " "+y;   
   }else{
      x.className = x.className.replace(" "+y,"");
   }
}
var post_action = function(type,id){
   if (type == "delete"){
      alert(id);
   }else if (type == "edit"){
   }else if (type == "publish"){
   }
}





















function addRow(tableID,Array,Array2,Array3,Array4){
	var table = document.getElementById(tableID); 
	var rowCount = table.rows.length;
	var row = table.insertRow(rowCount);
	Array2 = typeof(Array2) != 'undefined' ? Array2 : "";
	for (var i2=Array.length-1; i2>=0; i2--) {
		if(Array2!=""){
			addCell(row,"text",Array[i2],"0",Array2[i2]);
		}		
		else{
			addCell(row,"text",Array[i2]);
		}
	}
}

function addRowX(tableID,Array,Array2){
	var table = document.getElementById(tableID); 
	var rowCount = table.rows.length;
	var row = table.insertRow(rowCount);
	for (var i2=Array.length-1; i2>=0; i2--) {
		if (Array2[i2] == ""){
			addCell(row,"text",Array[i2]);
		}else{
			var cell0 = row.insertCell(0);
			var element0 = document.createElement("a");
			element0.innerHTML = Array[i2];
			element0.setAttribute('href', Array2[i2]);		
			cell0.appendChild(element0);
		}
	}
}
function addCell(row,type,value,array,span){
	var cell0 = row.insertCell(0);
	span = typeof(span) != 'undefined' ? span : "";
	if(span!="") {
		cell0.colSpan=span;
	}
	if (type=="delete"){
		var element0 = document.createElement("button");
	}
	else{
		var element0 = document.createElement(type);
	}
	if (type == 'select') {
		AddItems(element0,array);	
		element0.value=value;
		element0.onchange=function(){refresh();};
	}
	else if (type == "text"){
		element0 = document.createTextNode(value);
	}
	else if (type == "delete"){
		element0.value="";
		element0.onclick=function(){removeRow(table,row);};
	}
	else{
		element0.value=value;
		element0.oninput=function(){refresh();};
	}
	cell0.appendChild(element0);
}

function show_qr(code){
	jQuery('#qrcode').html("");jQuery('#qrcode').qrcode({width: 256,height: 256,text : "http://staszic.edu.pl/app/"+code});
	jQuery('#qrtext').html(code.substr(0,33)+" "+code.substr(33,code.length));
}