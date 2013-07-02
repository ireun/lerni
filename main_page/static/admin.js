$(document).ready(function(){
   if (document.getElementById('mem_info') != null){
      var board = document.getElementById('mem_info');
      width = board.width;
      height = board.height;
      context = board.getContext('2d');
      draw_scale();/*
      return setInterval(draw, 20);*/ 
   }
   if (document.getElementById('people_list') != null){
   	refresh_table_people();
   }
})

function draw(){
   draw_scale();
}
function draw_scale(){
   diagram_padding = 10;
   line_distance=(width-2*diagram_padding)/9;
	context.beginPath();
	context.fillStyle = '#000';
	context.lineWidth   = 1; 
   for(i=0; i<10; i++){
   	context.moveTo(line_distance*i+diagram_padding, height);
   	context.lineTo(line_distance*i+diagram_padding, height-height/9);
   }
   context.stroke();
   context.closePath();
}

var refresh_table_people = function(x,y){
	
/*
   var post_content = x.parentNode.parentNode.getElementsByTagName("div")[11];
   var button_show_comments =  x.parentNode.parentNode.getElementsByTagName("div")[9];
*/
   var api_url = '/api/jsonp/people';
   $.post(api_url, {no_cache: "just_noo!"}, function(data) {
      /*$(post_content).html("");*/
      $.each(data, function(key, val) {
         for(var i=0; i<val.length; i++){
         	addRowX('people_list',[val[i][0],val[i][1],val[i][2],'Nauczyciel','Podgląd','Edytuj','Usuń'],["","","","","a","a","a"]);
         }
         /*
            $(post_content).html($(post_content).html()+'<div class="wrapper"><div class="avatar"></div><div class="comment"><div class="author">'+
            val[i][1]+'</div><div class="time">'+val[i][2]+'</div><div class="delete" onclick="rm_comment(this,'+y+','+val[i][0]+
            ')"></div><br /><div class="content">'+val[i][3]+'</div></div></div>');
         }/*
         $(post_content).html($(post_content).html()+'<div class="wrapper"><div class="avatar"></div>'+
         '<form action="javascript://" method="post" onsubmit="add_comment(this,'+y+');"><textarea></textarea><input type="submit"></input></form></div>');
         button_show_comments.innerHTML="Ukryj komentarze ("+i+")";*/
      });  
      /*    
      $('.comments .wrapper').height(0);                                /*Można zrobić jakoś ładniej*/
      $('.comments .wrapper').each(function(x){
         $(this).height(function(){
            return $(this).children().height();
         });
      });/*
      alert("Refreshed");*/
   }, "json");
}