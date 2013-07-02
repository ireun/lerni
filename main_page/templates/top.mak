<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>ZSO nr 15 w Sosnowcu</title>
		<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.5.1/leaflet.css" />
		<script src="http://cdn.leafletjs.com/leaflet-0.5.1/leaflet.js"></script>
		
		<link rel="shortcut icon" href="${request.static_url('main_page:static/favicon.ico')}" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/index.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/index2.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/blip.css')}" type="text/css" media="screen" charset="utf-8" />
		% if admin:
		<link rel="stylesheet" href="${request.static_url('main_page:static/admin.css')}" type="text/css" media="screen" charset="utf-8" /></link>		
		<link rel="stylesheet" href="${request.static_url('main_page:static/substitutions.css')}" type="text/css" media="screen" charset="utf-8" />
		% endif
		<!--
		not compatibile with fancybox :/
		<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
		-->
		<script type="text/javascript" src="${request.static_url('main_page:static/jquery-1.8.0.min.js')}"></script>
		
		<script type="text/javascript" src="${request.static_url('main_page:static/index.js')}"></script>
		% if not logged_in:
		<script type="text/javascript" src="${request.static_url('main_page:static/login.js')}"></script>
		% endif
		<script type="text/javascript" src="${request.static_url('main_page:static/blip.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/admin.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/picnet.table.filter.min.js')}"></script>
		
		<script type="text/javascript" src="${request.static_url('main_page:static/blip.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/jquery.timeago.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/tinycon.js')}"></script>
		% if editor:
			<script type="text/javascript" src="${request.static_url('main_page:assets/mercury_loader.js')}"></script>
			<script type="text/javascript" src="${request.static_url('main_page:static/jquery.mousewheel.js')}"></script>
			<script type="text/javascript" src="${request.static_url('main_page:static/plugins.js')}"></script>
			<script type="text/javascript" src="${request.static_url('main_page:static/jquery.longpress.js')}"></script>
			<script>
			$(function(){
            	$('#center').first().longPress();
            });
            </script>
		% endif
		
		<script type="text/javascript" src="${request.static_url('main_page:static/jquery.picasagallery.js')}"></script>
		<link rel="stylesheet" href="${request.static_url('main_page:static/jquery.picasagallery.css')}" type="text/css" media="screen" charset="utf-8" />
		
        <link href="/static/fancyBox/jquery.fancybox.css?v=2.0.5" rel="stylesheet" type="text/css" media="screen" />
        <link href="/static/fancyBox/helpers/jquery.fancybox-thumbs.css?v=2.0.5" rel="stylesheet" type="text/css" media="screen" />
        <script src="/static/fancyBox/jquery.fancybox.pack.js?v=2.0.5" type="text/javascript"></script>
        <script src="/static/fancyBox/helpers/jquery.fancybox-thumbs.js?v=2.0.5" type="text/javascript"></script>
		
		
		<link rel="stylesheet" href="${request.static_url('main_page:static/substitutions.css')}" type="text/css" media="screen" charset="utf-8" />
		<script type="text/javascript" src="${request.static_url('main_page:static/subs_edit.js')}"></script>
		
		<!-- <link rel="stylesheet" href="${request.static_url('main_page:static/styles/Base.css')}" type="text/css"> -->
      <link rel="stylesheet" href="${request.static_url('main_page:static/styles/BreadCrumb.css')}" type="text/css">
      <script type="text/javascript" src="${request.static_url('main_page:static/js/jquery.easing.1.3.js')}"></script>
      <script type="text/javascript" src="${request.static_url('main_page:static/js/jquery.jBreadCrumb.1.1.js')}"></script>
      <script type="text/javascript" src="${request.static_url('main_page:static/jquery.qrcode.min.js')}"></script>
      <script type="text/javascript" src="${request.static_url('main_page:static/mailcheck.min.js')}"></script>
   
      <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jquery-noty/2.0.3/jquery.noty.js"></script>
      <script type="text/javascript" src="${request.static_url('main_page:static/topRight.js')}"></script>
      <script type="text/javascript" src="${request.static_url('main_page:static/top.js')}"></script>
      <script type="text/javascript" src="${request.static_url('main_page:static/default.js')}"></script>
      <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/select2/3.2/select2.min.js"></script> <!-- Formularze -->
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/select2/3.2/select2.css" type="text/css" >
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/leaflet/0.5.1/leaflet.css" type="text/css" />
      <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/leaflet/0.5.1/leaflet.js"></script>
      
      <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/wysihtml5/0.3.0/wysihtml5.min.js"></script>

      <script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>
      <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/2.3.1/css/bootstrap-responsive.min.css" type="text/css" />

      <script type="text/javascript" src="${request.static_url('main_page:static/bootstrap-wysihtml5.js')}"></script>
      <link rel="stylesheet" src="${request.static_url('main_page:static/styles/bootstrap-wysihtml5.css')}"></link>
      <script type="text/javascript" src="${request.static_url('main_page:static/list.min.js')}"></script>

     
		<script type="text/javascript" >
		$(document).ready(function(){
		%for row in allerts:
			setTimeout(function(){show_allerts("${row[0]}","${row[1]}","${row[2]}")},1500);
		% endfor
		});
		</script>
	</head>
	<body id="body" onload="start()" data-twttr-rendered="true">
		<!-- FACEBOOK PLUGIN START'S THERE -->
		<div id="fb-root"></div>
		<script>
			(function(d, s, id) {
			var js, fjs = d.getElementsByTagName(s)[0];
			if (d.getElementById(id)) return;
				js = d.createElement(s); js.id = id;
				js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1";
				fjs.parentNode.insertBefore(js, fjs);
			}(document, 'script', 'facebook-jssdk'));
		</script> <!-- ENDS THERE -->
		<div class="topbar">
            <div class="breadCrumbHolder module">
                <div id="breadCrumb" class="breadCrumb module">
                    <ul>
                        <li><a href="/">Home</a>
                        % for row in breadcrumbs:
                        	<li><a href="${row[0]}">${row[1]}</a></li>
                        % endfor
                    </ul>
                </div>
            </div>
			% if logged_in:
				<ul style="float: right;">
				    <!--
					<a href="google.pl"><li class="button_nav">${name}</li></a>
					<a href="google.pl"><li class="button_nav notification">2</li></a>
					<a href="google.pl"><li class="button_nav">Moje Oceny</li></a>
					<a href="google.pl"><li class="button_nav">Prace domowe</li></a>
					<a href="google.pl"><li class="button_nav">User content</li></a>
					-->
					<a href="/admin"><li class="button_nav">Panel administratora</li></a>
					<a href="${request.route_url('account')}"><li class="button_nav"><div class="cogwheel">&nbsp;</div></li></a>
					<!--
					<li class="button_nav"><a href="${request.application_url}/logout">Logout</a></li>
					-->
				</ul>
			% else:
			<form id="login-form" action="javascript://" method="post" onsubmit="form_login();">
				<ul class="inline-login">
					<li>
						<label for="login" id="login_label" style="opacity: 1; ">Username or email</label>
						<input type="text" id="login" name="login" value="" autocomplete="on" onfocus="setLabelOpacity(this.id,0.5)"
						onblur="setLabelOpacity(this.id,1)" oninput="setLabelVisibility(this.id)" onload="setLabelVisibility(this.id)">
					</li>
					<li>
						<label for="password" id="password_label" style="opacity: 1; ">Password</label>
						<input type="password" id="password" name="password" value="" autocomplete="on" onfocus="setLabelOpacity(this.id,0.5)"
						onblur="setLabelOpacity(this.id,1)" oninput="setLabelVisibility(this.id)" onload="setLabelVisibility(this.id)">
					</li>
					<li>
						<input id="login-button" class="btn dark" name="form.submitted" type="submit" value="Login">
					</li>
				</ul>
				<div id="login-message"></div>
				<div class="forgot-password">
					<a href="/forgot_password">Zapomniałeś hasła?</a>
				</div>
			</form>
			% endif
		</div>
		<div id="wrapper">		
			<div id="header">
			<!--
				<img src="${request.static_url('main_page:static/logo.png')}" style="height:80px;">
				<div style="font-size: 48px; color: #E6E6E6; float: right;">ZSO nr 15 w Sosnowcu</div>
			-->
				% if not admin:
				<div class="fb-like" data-href="https://www.facebook.com/sustaszic" data-send="false" data-layout="button_count"></div>
				% endif
			</div>			
				<div id="panel_nav">
					<ol style="padding: 0 9px;">
						% for row in menu_top_list:
							<li class="button_nav"> <a href="${row[0]}">${row[1]}</a> </li>
						% endfor
					</ol>
				</div>