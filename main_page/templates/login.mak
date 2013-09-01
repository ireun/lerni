# -*- coding: utf-8 -*-
<%include file="top_new.mak"/>
    <div class="container">
		<div id="form_wrapper" class="form_wrapper">
	      <form action="/login" method="post" class="login 
	      %if active=='login':
	      active
	      %endif
	      ">
				<h2 class="form-signin-heading">Zaloguj się</h2>
				<input name="login" type="text" class="input-block-level" placeholder="Adres email">
				<input name="password" type="password" class="input-block-level" placeholder="Hasło">
				<label class="checkbox"><input type="checkbox" name="remember_me" value="true"> Pamiętaj mnie </label>
				%if active=="login":
				<div class="custom_container"></div>
				%endif
			   <div class="settings-bottom" style="margin: 0px -30px;">
			   	<button id="submit_button" name="form.submitted" type="submit" class="btn large primary pull-right" >Zaloguj</button>
				   <a href="/register" rel="register" class="linkform">Rejestracja</a><br>
				   <a href="/forgot-password" rel="forgot_password" class="linkform">Zapomniałem hasła</a>      
			   </div>
	      </form>
	      
	      <form enctype="multipart/form-data" action="/register" method="post" id="registerform" class="register 
	      %if active=='register':
	      active
	      %endif
	      ">
				<script type="text/javascript">
				  var RecaptchaOptions = {
				      tabindex: 1,
				      theme: 'custom',
				      custom_theme_widget: 'recaptcha_widget'
				  };
				</script>
				<h2 class="form-signin-heading">Rejestracja (nieaktywna)</h2>
				<p class="column"><input data-progression="" name="name" type="text" class="input-block-level" placeholder="Imię" data-helper="Wprowadź imię i nazwisko, abyśmy wiedzieli, jak się nazywasz."></p>
				<p class="column" style="float: right"><input data-progression="" name="secondname" type="text" class="input-block-level" placeholder="Drugie Imię" data-helper="Wprowadź imię i nazwisko, abyśmy wiedzieli, jak się nazywasz."></p>
				<p class="column"><input data-progression="" name="surname" type="text" class="input-block-level" placeholder="Nazwisko" data-helper="Wprowadź imię i nazwisko, abyśmy wiedzieli, jak się nazywasz."></p>
				<p class="column" style="float: right"><input id="pesel" data-progression="" name="pesel" type="text" class="input-block-level" placeholder="PESEL" data-helper="Numer pesel będzie twoim identyfikatorem w systemie. Upewnij się, że jest poprawny."></p>
				<p class="column"><input id="birthdate" data-progression="" name="birthdate" type="text" class="input-block-level" placeholder="Data urodzenia" data-helper="Podaj swoją datę urodzenia. (dd-mm-yyyy)"></p>
				<p class="column" style="float: right"><input data-progression="" name="phonenumber" type="text" class="input-block-level" placeholder="Telefon komórkowy" data-helper="Podaj swój numer telefonu komórkowego."></p>
				<p><input id="email" data-progression="" name="email" type="text" class="input-block-level" placeholder="Adres email" data-helper="Adres email, na który zostanie przysłany link aktywacyjny."></p>
				<div class="email-suggestion" style="position:relative; top: -10px; display: none;">Czy miałeś na myśli <a class="suggested-email"></span></a>?</div>	    	  
				<p class="column"><input data-progression="" name="password" type="password" class="input-block-level" placeholder="Hasło" data-helper="Wpisz hasło dwukrotnie, aby uniknąć pomyłki."></p>
				<p class="column" style="float: right"><input data-progression="" name="repeat-password" type="password" class="input-block-level" placeholder="Powtórz hasło" data-helper="Wpisz hasło dwukrotnie, aby uniknąć pomyłki."></p>
				<div style="height: 78px; display: block;">
			   <div id="recaptcha_widget" >
					<table id="recaptcha_table" class="recaptchatable recaptcha_theme_clean"><tbody><tr height="73">
					<td style="padding: 0px 0px 3px ! important;" class="recaptcha_image_cell" width="302"><div id="recaptcha_image"></div></td>					
					<td style="padding: 10px 7px 7px 7px;">
					<a title="Get a new challenge" id="recaptcha_reload_btn" href="javascript:Recaptcha.reload()"><img src="http://www.google.com/recaptcha/api/img/clean/refresh.png" id="recaptcha_reload" alt="Get a new challenge" height="18" width="25"></a><br>
					<a title="Get an audio challenge" id="recaptcha_switch_audio_btn" class="recaptcha_only_if_image" href="javascript:Recaptcha.switch_type(&#39;audio&#39;)"><img src="http://www.google.com/recaptcha/api/img/clean/audio.png" id="recaptcha_switch_audio" alt="Get an audio challenge" height="15" width="25"></a><br>
					<a title="Get a visual challenge" id="recaptcha_switch_img_btn" class="recaptcha_only_if_audio" href="javascript:Recaptcha.switch_type(&#39;image&#39;)"><img src="http://www.google.com/recaptcha/api/img/clean/text.png" id="recaptcha_switch_img" alt="Get a visual challenge" height="15" width="25"></a>
					<a title="Help" id="recaptcha_whatsthis_btn" href="javascript:Recaptcha.showhelp()"><img alt="Help" src="http://www.google.com/recaptcha/api/img/clean/help.png" id="recaptcha_whatsthis" height="16" width="25"></a>
					</td>
					<td style="padding: 18px 7px 18px 7px;"> <img src="http://www.google.com/recaptcha/api/img/clean/logo.png" id="recaptcha_logo" alt="" height="36" width="71"> </td>
					</tr> </tbody></table>					
					<input type="text" id="recaptcha_response_field" name="recaptcha_response_field" style="display:none;">
					<script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=${recaptcha_public}"></script>
					<noscript><iframe src="http://www.google.com/recaptcha/api/noscript?k=${recaptcha_public}" height="300" width="500" frameborder="0"></iframe><br>
					<textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>
					<input type="hidden" name="recaptcha_response_field" value="manual_challenge"></noscript>
				</div>
				</div>
				<p><input id="recaptcha_response_field2" data-progression="" name="recaptcha_response_field2" type="text" class="input-block-level" placeholder="Przepisz tekst widoczny powyżej" data-helper="Przepisz oba słowa z obrazka aby udowodnić, że nie jesteś robotem."></p>
				<p>Klucz publiczny GPG (Pole nieobowiązkowe):<input value="" id="gpg" data-progression="" name="gpg" type="file" class="input-block-level" placeholder="Klucz publiczny GPG" data-helper="Dołącz swój klucz GPG, który będzie używany do bezpiecznego kontaktu ze szkołą."></p>
				%if active=="register":
				<div class="custom_container"></div>
				%endif
			   <div class="settings-bottom" style="margin: 0 -30px -10px -30px; height: 50px;">
			   	<button id="submit_button" name="form.submitted" type="submit" class="btn large primary pull-right" >Wyślij</button>
				   <a href="/login" rel="login" class="linkform">Zaloguj</a><br>
				   <a href="/forgot-password" rel="forgot_password" class="linkform">Zapomniałem hasła</a>      
				</div>
	      </form>
	      
			<form action="/forgot-password" method="post" class="forgot_password
			%if active=='forgot_password':
	      active
	      %endif
	      ">
	      	<h2 class="form-signin-heading">Zapomniałem hasła</h2>
	        	<input name="login" type="text" class="input-block-level" placeholder="Adres email">	        
	        	%if active=="forgot_password":
				<div class="custom_container"></div>
				%endif
			  	<div class="settings-bottom" style="margin: 0px -30px;">
			  		<button id="submit_button" name="form.submitted" type="submit" class="btn large primary pull-right" >Wyślij</button>
				   <a href="/login" rel="login" class="linkform">Pamiętam!</a><br>	   
			  	</div>
	      </form>
		</div>
    </div>
    <script type="text/javascript">
		   %for row in allerts:
            show_allert('${row[0]}','${row[1]}','${row[2]}')
		   % endfor
    </script>
    <script src="/static/js/form_login.min.js"></script>
    <div id="space" style="height: 200px;"></div>
<%include file="bottom_new.mak"/>
