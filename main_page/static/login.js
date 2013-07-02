function setLabelOpacity(x,value)
{
	document.getElementById(x+"_label").style.opacity=value;
}
function setLabelVisibility(x)
{
	if(document.getElementById(x).value!=""){
		document.getElementById(x+"_label").style.visibility="hidden";
	}else{
		document.getElementById(x+"_label").style.visibility="visible";
	}
}
var form_login = function()
{
	var http = new XMLHttpRequest();
	var url = "/login";
	var params = "login="+document.getElementById("login").value+"&password="+document.getElementById("password").value+"&form.submitted=yea";
	http.open("POST", url, true);
	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http.setRequestHeader("Content-length", params.length);
	http.setRequestHeader("Connection", "close");
	http.onreadystatechange = function() {//Call a function when the state changes.
	if(http.readyState == 4 && http.status == 200) {
			if(http.responseText=="OK"){
				location.reload(true);
			}else{
				document.getElementById("login-message").innerHTML=http.responseText;
			}
		}
	}
	http.send(params);
}