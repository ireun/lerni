<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>ZSO nr 15 w Sosnowcu</title>
		<link rel="shortcut icon" href="${request.static_url('main_page:static/favicon.ico')}" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/index.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/index2.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/index3.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/blip.css')}" type="text/css" media="screen" charset="utf-8" />
		<script type="text/javascript" src="${request.static_url('main_page:static/index.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/login.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/register.js')}"></script>
		
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js"></script>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js"></script>

	</head>
	<body>
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
		</script>
		<!-- END'S THERE -->
		<div class="topbar">
			% if logged_in:
				<li class="button_nav" style="float: right;"> <a href="${request.application_url}/logout">Wyloguj</a> </li>
			% else:
			<form id="login-form" action="javascript://" method="post" onsubmit="form_login();">
				<ul class="inline-login">
					<li>
						<label for="login" id="login_label" style="opacity: 1; ">Username or email</label>
						<input type="text" id="login" name="login" value="" autocomplete="on" onfocus="setLabelOpacity(this.id,0.5)"
						onblur="setLabelOpacity(this.id,1)" oninput="setLabelVisibility(this.id)">
					</li>
					<li>
						<label for="password" id="password_label" style="opacity: 1; ">Password</label>
						<input type="password" id="password" name="password" value="" autocomplete="on" onfocus="setLabelOpacity(this.id,0.5)"
						onblur="setLabelOpacity(this.id,1)" oninput="setLabelVisibility(this.id)">
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
		<div id="register_form">
			Witamy!<br /> Uzupełnij poniższe pola a następnie przesuń ${quest} do skrzynki.
			<div id="captcha">
				<div class="drop" style="position:absolute;bottom:0;left:189px;background-image:url(${request.application_url}/captcha/${captcha});height:72px;width:72px;background-position:-360px"></div>
				<div id="pic1" class="drag" style="background-image:url(${request.application_url}/captcha/${captcha});height:72px;width:72px;background-position:0;"></div>
				<div id="pic2" class="drag" style="background-image:url(${request.application_url}/captcha/${captcha});height:72px;width:72px;background-position:-72px;"></div>
				<div id="pic3" class="drag" style="background-image:url(${request.application_url}/captcha/${captcha});height:72px;width:72px;background-position:-144px"></div>
				<div id="pic4" class="drag" style="background-image:url(${request.application_url}/captcha/${captcha});height:72px;width:72px;background-position:-216px"></div>
				<div id="pic5" class="drag" style="background-image:url(${request.application_url}/captcha/${captcha});height:72px;width:72px;background-position:-288px"></div>
				
				
			</div>
			<div id="debug">nothing</div>
				
<!--				
<div id="post_message_2286338">
<div class="recaptcha_box" id="recaptcha_box_for_post_2286338" rel="2286338">
</div>
<script type="text/javascript">jQuery("#recaptcha_box_for_post_2286338").captcha({answer: '1', hash: '81d898ffe9b8e6172f04b66dee3a02ab'});</script>
</div>
-->
		</div>
		<footer>
			© ZSO nr 15, Sosnowiec 2008-2012			
		</footer>
	</body>
</html>
