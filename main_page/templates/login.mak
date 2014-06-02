# -*- coding: utf-8 -*-
<%include file="top_new.mak"/>
    <div class="container">
		<div id="form_wrapper" class="form_wrapper">

            <form action="/login" method="post" class="login ${active['login']}">
                <h2 class="form-signin-heading">Zaloguj się</h2>
                <input name="login" type="text" class="input-block-level" placeholder="Adres email">
                <input name="password" type="password" class="input-block-level" placeholder="Hasło">
                <label class="checkbox"><input type="checkbox" name="remember_me" value="true"> Pamiętaj mnie </label>
                %if active['login']:
                <div class="custom_container"></div>
                %endif
               <div class="settings-bottom" style="margin: 25px -30px -10px -30px;">
                <button id="submit_button" name="form.submitted" type="submit" class="btn large primary pull-right" >Zaloguj</button>
                   <a href="/register" rel="register" class="linkform">Rejestracja</a><br>
                   <a href="/forgot-password" rel="forgot_password" class="linkform">Zapomniałem hasła</a>
               </div>
            </form>

            <form enctype="multipart/form-data" action="/register" method="post" id="registerform"  class="register ${active['register']}">
                <script type="text/javascript">
                  var RecaptchaOptions = {
                      tabindex: 1,
                      theme: 'custom',
                      custom_theme_widget: 'recaptcha_widget'
                  };
                </script>
                <h2 class="form-signin-heading">Rejestracja</h2>
                <p class="column">
                    <input data-progression="" name="name" type="text" class="input-block-level" placeholder="Imię"
                    data-helper="Wprowadź imię i nazwisko, abyśmy wiedzieli, jak się nazywasz.">
                </p>
                <p class="column" style="float: right">
                    <input data-progression="" name="secondname" type="text" class="input-block-level" placeholder="Drugie Imię"
                    data-helper="Wprowadź imię i nazwisko, abyśmy wiedzieli, jak się nazywasz.">
                </p>
                <p class="column">
                    <input data-progression="" name="surname" type="text" class="input-block-level" placeholder="Nazwisko"
                    data-helper="Wprowadź imię i nazwisko, abyśmy wiedzieli, jak się nazywasz.">
                </p>
                <p class="column" style="float: right">
                    <input id="pesel" data-progression="" name="pesel" type="text" class="input-block-level" placeholder="PESEL"
                    data-helper="Numer pesel będzie twoim identyfikatorem w systemie. Upewnij się, że jest poprawny.">
                </p>
                <p class="column">
                    <input id="birthdate" data-progression="" name="birthdate" type="text" class="input-block-level" placeholder="Data urodzenia"
                    data-helper="Podaj swoją datę urodzenia. (dd-mm-yyyy)">
                </p>
                <p class="column" style="float: right">
                    <input data-progression="" name="phonenumber" type="text" class="input-block-level" placeholder="Telefon komórkowy"
                    data-helper="Podaj swój numer telefonu komórkowego.">
                </p>
                <p>
                    <input id="email" data-progression="" name="email" type="text" class="input-block-level" placeholder="Adres email"
                    data-helper="Adres email, na który zostanie przysłany link aktywacyjny.">
                </p>
                <div class="email-suggestion" style="position:relative; top: -10px; display: none;">
                    Czy miałeś na myśli <a class="suggested-email"></span></a>?
                </div>
                <p class="column">
                    <input data-progression="" name="password" type="password" class="input-block-level" placeholder="Hasło"
                    data-helper="Wpisz hasło dwukrotnie, aby uniknąć pomyłki.">
                </p>
                <p class="column" style="float: right"><input data-progression="" name="repeat-password" type="password" class="input-block-level" placeholder="Powtórz hasło" data-helper="Wpisz hasło dwukrotnie, aby uniknąć pomyłki."></p>
                <label class="checkbox"><input id="skip_captcha" type="checkbox" name="skip_captcha" value="true">
                    Pomiń weryfikację captcha (może być wymagana weryfikacja kodem sms).
                </label>
                <div id="captcha" style="height: 78px; display: block;">
                <%include file="snippets/recaptcha.mak"/>
                </div>
                <p><input id="recaptcha_response_field2" data-progression="" name="recaptcha_response_field2" type="text" class="input-block-level" placeholder="Przepisz tekst widoczny powyżej" data-helper="Przepisz oba słowa z obrazka aby udowodnić, że nie jesteś robotem."></p>
                <!--
                <p>Klucz publiczny GPG (Pole nieobowiązkowe):<input value="" id="gpg" data-progression="" name="gpg" type="file" class="input-block-level" placeholder="Klucz publiczny GPG" data-helper="Dołącz swój klucz GPG, który będzie używany do bezpiecznego kontaktu ze szkołą."></p>
                -->
                %if active['register']:
                <div class="custom_container"></div>
                %endif
               <div class="settings-bottom" style="margin: 0 -30px -10px -30px; position: relative; top: 24px;">
                <button id="submit_button" name="form.submitted" type="submit" class="btn large primary pull-right" >Wyślij</button>
                   <a href="/login" rel="login" class="linkform">Zaloguj</a><br>
                   <a href="/forgot-password" rel="forgot_password" class="linkform">Zapomniałem hasła</a>
                </div>
            </form>

            <form action="/forgot-password" method="post" class="forgot_password ${active['forgot_password']}">
                <h2 class="form-signin-heading"> Zapomniałem hasła </h2>
                <input name="email" type="text" class="input-block-level" placeholder="Adres email">
                %if active['forgot_password']:
                <div class="custom_container"></div>
                %endif
                <div class="settings-bottom" style="margin: 36px -30px 0 -30px;">
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
<style>
    #space{height: 200px;}
</style>
<%include file="bottom_new.mak"/>
