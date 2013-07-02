/*
;(function( $ ){
	$.fn.captcha = function(options){
			
		
	var defaults = {  
	   borderColor: "",  
	   captchaDir: "http://peb.pl/js/captcha",  
	   url: "index.php?recaptcha_challenge=1",  
	   urlAnswer: "index.php?recaptcha=1&context="+ $(this).attr("id"), 
	   formId: "myForm",  
	   text: "Aby zobaczyć linki przeciągnij <span>nożyczki</span> do koła",
	   items: Array("ołówek", "nożyczki", "zegar", "serce", "nutę"),
	   itemsNames: Array("http://peb.pl/js/captcha/imgs/item-olowek.png", "http://peb.pl/js/captcha/imgs/item-nozyczki.png", "http://peb.pl/js/captcha/imgs/item-zegar.png", "http://peb.pl/js/captcha/imgs/item-serce.png", "http://peb.pl/js/captcha/imgs/item-nute.png") 
	  };	
	
	var options = $.extend(defaults, options); 
        var thisId = $(this).attr("id");
        var postid = $(this).attr("rel");

		
	$(this).html("<b class='ajax-fc-rtop'><b class='ajax-fc-r1'></b> <b class='ajax-fc-r2'></b> <b class='ajax-fc-r3'></b> <b class='ajax-fc-r4'></b></b><img class='ajax-fc-border' id='"+thisId+"-ajax-fc-left' src='" + options.captchaDir + "/imgs/border-left.png' /><img class='ajax-fc-border' id='"+thisId+"-ajax-fc-right' src='" + options.captchaDir + "/imgs/border-right.png' /><div id='"+thisId+"-ajax-fc-content' class='ajax-fc-content'><div id='"+thisId+"-ajax-fc-left' class='ajax-fc-left'><p id='"+thisId+"-ajax-fc-task' class='ajax-fc-task'>" + options.text + "</p><ul id='"+thisId+"-ajax-fc-task' class='ajax-fc-task'><li class='ajax-fc-0'><img src='" + options.captchaDir + "/imgs/item-none.png' alt='' /></li><li class='ajax-fc-1'><img src='" + options.captchaDir + "/imgs/item-none.png' alt='' /></li><li class='ajax-fc-2'><img src='" + options.captchaDir + "/imgs/item-none.png' alt='' /></li><li class='ajax-fc-3'><img src='" + options.captchaDir + "/imgs/item-none.png' alt='' /></li><li class='ajax-fc-4'><img src='" + options.captchaDir + "/imgs/item-none.png' alt='' /></li></ul></div><div id='"+thisId+"-ajax-fc-right' class='ajax-fc-right'><p id='"+thisId+"-ajax-fc-circle' class='ajax-fc-circle'></p></div></div><div id='"+thisId+"-ajax-fc-corner-spacer' class='ajax-fc-corner-spacer'></div><b class='ajax-fc-rbottom'><b class='ajax-fc-r4'></b> <b class='ajax-fc-r3'></b> <b class='ajax-fc-r2'></b> <b class='ajax-fc-r1'></b></b>");
	//var xml = $.ajax({ url: options.url,async: false }).responseXML;
        var rand = options.answer;//$(xml).find('answer').text();
        var hash = options.hash//$(xml).find('hash').text();

	var pic = randomNumber();
        $("#" + thisId).append("<input id=\""+thisId+"-hash-value\" type=\"hidden\" style=\"display: none;\" name=\"hash\" value=\"" + hash + "\">");
        $(this).addClass("ajax-fc-container");
	$("#"+thisId+" .ajax-fc-" + rand).html( "<img src=\"" + options.itemsNames[pic] + "\" alt=\"\" />");
	$("p#"+thisId+"-ajax-fc-task span").html(options.items[pic]);
	$("#"+thisId+" .ajax-fc-" + rand).addClass('ajax-fc-highlighted');
	$("#"+thisId+" .ajax-fc-" + rand).draggable();
	var used = Array();
	for(var i=0;i<5;i++){
		if(i != rand && i != pic)	
		{
			$("#"+thisId+" .ajax-fc-" +i).html( "<img src=\"" + options.itemsNames[i] + "\" alt=\"\" />");
			used[i] = options.items[i];
		}
	}
	$("#"+thisId+" .ajax-fc-container, #"+thisId+" .ajax-fc-rtop *, #"+thisId+" .ajax-fc-rbottom *").css("background-color", options.borderColor);
	$("#"+thisId+"-ajax-fc-circle").droppable({
                accept: "#"+thisId+" .ajax-fc-" + rand,
		drop: function(event, ui) {
			$("#"+thisId+" .ajax-fc-" + rand).draggable("disable");
			//$("#" + thisId).append("<input type=\"hidden\" style=\"display: none;\" name=\"captcha\" value=\"" + rand + "\">");
                        var response = $.ajax({ url: options.urlAnswer+ "&answer="+ rand +"&hash="+ $("#"+thisId+"-hash-value").val(),async: false }).responseText;
                        if(response != 'false') {
                              $("#post_message_" + postid).html(response); 
                        }
		},
		tolerance: 'touch'
	});	
	};

})( jQuery );

function randomNumber() {
	var chars = "01234";
	chars += ".";
	var size = 1;
	var i = 1;
	var ret = "";
		while ( i <= size ) {
			max = chars.length-1;
			num = Math.floor(Math.random()*max);
			temp = chars.substr(num, 1);
			ret += temp;
			i++;
		}
	return ret;
}





    function showRecaptcha(element) {
        $("#"+ element).captcha();
    }
    jQuery(function(){
        jQuery("input[name='recaptcha_response_field']").live("keydown",function(e){
            if(e.which == 13) {
                jQuery(this).parents("div.recaptcha_box").nextAll("input.submit_recaptcha:first").click();
                                e.preventDefault(); 
            }
        });
    }); 
    
    */
var _startX = 0;            // mouse starting positions
var _startY = 0;
var _offsetX = 0;           // current element offset
var _offsetY = 0;
var _dragElement;           // needs to be passed from OnMouseDown to OnMouseMove
var _oldZIndex = 0;         // we temporarily increase the z-index during drag
var _debug = document.getElementById("debug");    // makes life easier

InitDragDrop();

function InitDragDrop()
{
    document.onmousedown = OnMouseDown;
    document.onmouseup = OnMouseUp;
}
function OnMouseDown(e)
{
    var _debug = document.getElementById("debug");
    
    // IE uses srcElement, others use target
    var target = e.target != null ? e.target : e.srcElement;
    
    _debug.innerHTML = target.className == 'drag' 
        ? 'draggable element clicked' 
        : 'NON-draggable element clicked';

    // for IE, left click == 1
    // for Firefox, left click == 0
    if ((e.button == 1 && window.event != null || 
        e.button == 0) && 
        target.className == 'drag')
    {
        // grab the mouse position
        _startX = e.clientX;
        _startY = e.clientY;
        
        // grab the clicked element's position
        _offsetX = ExtractNumber(target.style.left);
        _offsetY = ExtractNumber(target.style.top);
        
        // bring the clicked element to the front while it is being dragged
        _oldZIndex = target.style.zIndex;
        target.style.zIndex = 10000;
        
        // we need to access the element in OnMouseMove
        _dragElement = target;

        // tell our code to start moving the element with the mouse
        document.onmousemove = OnMouseMove;
        
        // cancel out any text selections
        document.body.focus();

        // prevent text selection in IE
        document.onselectstart = function () { return false; };
        // prevent IE from trying to drag an image
        target.ondragstart = function() { return false; };
        
        // prevent text selection (except IE)
        return false;
    }
}
function OnMouseMove(e)
{
    var _debug = document.getElementById("debug");
    if (e == null) 
        var e = window.event; 

    // this is the actual "drag code"
    _dragElement.style.left = (_offsetX + e.clientX - _startX) + 'px';
    _dragElement.style.top = (_offsetY + e.clientY - _startY) + 'px';
    
    _debug.innerHTML = '(' + _dragElement.style.left + ', ' + 
        _dragElement.style.top + ')';   
}
function OnMouseUp(e)
{
    var _debug = document.getElementById("debug");
    chceck_for_colision(_dragElement.style.left,_dragElement.style.top,_dragElement.id);
    if (_dragElement != null)
    {
        _dragElement.style.zIndex = _oldZIndex;

        // we're done with these events until the next OnMouseDown
        document.onmousemove = null;
        document.onselectstart = null;
        _dragElement.ondragstart = null;

        // this is how we know we're not dragging      
        _dragElement = null;
        
        _debug.innerHTML = 'mouse up';
    }
}
/*
Ogarnac, bo narazie dziala tylko gdy serwer jest na localhoscie !!!
*/
function chceck_for_colision(x,y,id){
	if(parseInt(x)>135 && parseInt(x)<238 && parseInt(y)>82 && parseInt(y)<166){
		var http = new XMLHttpRequest();
		var hashcode = document.getElementById("pic1").style.backgroundImage;
		var url = "captcha/validate/"+id.substr(3,3)+hashcode.substr(34,hashcode.length-35);
		http.open("GET", url, true);
		http.onreadystatechange = function() {//Call a function when the state changes.
		if(http.readyState == 4 && http.status == 200) {
				alert(http.responseText);
			}
		}
		http.send();
	}
}
function ExtractNumber(value)
{
    var n = parseInt(value);
	
    return n == null || isNaN(n) ? 0 : n;
}

// this is simply a shortcut for the eyes and fingers
function $(id)
{
    return document.getElementById(id);
} 
    
  