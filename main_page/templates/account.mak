<%include file="top_new.mak"/>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<div id="settings-wrapper">
   <ul id="settings_tab" class="tabs big">
   <li><a href="#basic" id="account_tab">Ogólne</a></li>
   <li><a href="#courses" id="profile_tab">Kursy</a></li>
   <li><a href="#profile" id="profile_tab">Bezpieczeństwo</a></li>
   <li><a href="#notifications" id="notifications_tab">Powiadomienia</a></li>
   <li><a href="#applications" id="notifications_tab">Aplikacje</a></li>
   </ul>
   <div id="basic">
      <div class="settings_header">Informacje podstawowe</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Pierwsze imię:</td><td>
               <a href="#" id="firstname" data-original-title="Pierwsze imię">${first_name}</a>
            </td></tr><tr><td>Drugie imię:</td><td>
               <a href="#" id="secondname" data-original-title="drugie imię">${second_name}</a>
            </td></tr><tr><td>Nazwisko:</td><td>
               <a href="#" id="lastname" data-original-title="Nazwisko">${last_name}</a>
            </td></tr><tr><td>Tytuł:</td><td>
               <a href="#" id="lastname" data-original-title="Tytuł">${last_name}</a>
            </td></tr><tr><td>Miejsce urodzenia:</td><td> <!-- miejscowość -->
               <a href="#" id="lastname" data-original-title="Tytuł">${last_name}</a>
            </td></tr><tr><td>Data urodzenia:</td><td>
               <a href="#" id="age" data-original-title="Wiek">${birthdate}</a>
            </td></tr><tr><td>Płeć:</td><td>
               <a href="#" id="sex" data-type="select" data-original-title="Płeć">Male</a>
            </td></tr><!--
            <tr><td>Klasa:</td><td>
               ${group}
            </td></tr><tr><td>Lektorat:</td><td>
               ${language_group}
            </td></tr><tr><td>Rozszerzenie:</td><td>
               ${extension_group}
            </td></tr>
            -->
         </tbody>
      </table>
      <div class="settings_header">Miejsce zamieszkania</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Kraj:</td><td>
               <a href="#" id="country" data-original-title="Kraj">Polska</a>
            </td></tr><tr><td>Miejscowość:</td><td>
               <a href="#" id="city" data-original-title="Miasto">Sosnowiec</a>
            </td></tr><tr><td>Adres:</td><td>
            <a href="#" id="street" data-original-title="Miasto">ul. Legionów 5/II/9</a>
            </td></tr>
         </tbody>
      </table>
      <div class="settings_header">Dane kontaktowe</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Numer telefonu:</td><td>
               <a href="#" id="country" data-original-title="Kraj">518158009</a>
            </td></tr><tr><td>Email:</td><td>
               <a href="#" id="country" data-original-title="Kraj">kamilx3@gmail.com</a>
            </td></tr><tr><td>XMPP:</td><td>
               <a href="#" id="country" data-original-title="Kraj">kamilx3@gmail.com</a>
            </td></tr>
         </tbody>
      </table>
      <div class="settings_header">Informacje dodatkowe</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Adres bitcoin:</td><td>
               <a href="#" id="country" data-original-title="Kraj"></a>
            </td></tr><tr><td>Strona internetowa:</td><td>
               <a href="#" id="country" data-original-title="Kraj">moja-strona.pl</a>
            </td></tr>
         </tbody>
      </table>

   </div>
   <div id="courses" >
      <div class="settings_header">Aktywne kursy</div>
      <table class="table table-bordered table-condensed table-striped">
         <tbody>
            <tr><td>Adres bitcoin:</td><td>
               <a href="#" id="country" data-original-title="Kraj"></a>
            </td></tr><tr><td>Opeenstreetmap:</td><td>
               <a href="#" id="country" data-original-title="Kraj">KD_</a>
            </td></tr><tr><td>Minecraft:</td><td>
               <a href="#" id="country" data-original-title="Kraj">KD_</a>
            </td></tr><tr><td>Strona internetowa:</td><td>
               <a href="#" id="country" data-original-title="Kraj">moja-strona.pl</a>
            </td></tr>
         </tbody>
      </table>
      <div class="settings_header">Ukończone kursy</div>
   </div>
   <div id="profile" >
      <div class="settings_header">Hasło</div>
      Nasdasdasd
      <div class="settings_header">Ustawienia prywatności</div>
   </div>
   <div id="notifications" >
      <div class="settings_header">Informacje podstawowe</div>
      Nasdasdasd
   </div>
   <div id="applications" >
      <div class="settings_header">Informacje podstawowe</div>
      Nasdasdasd
   </div>
   <div class="settings-bottom">
      <button id="submit_button" type="submit" class="btn large primary right" disabled="">Save changes</button>
      <!-- <button id="cancel_button" type="reset" class="btn large right">Cancel</button> -->
      <div id="confirmation-message" class="hidden save-message">Saved!</div>
      <div id="error-message" class="hidden save-message">Error</div></div>
   </div>
</div>  

<div id="space"></div>
<script>   
$( "#settings-wrapper" ).tabs();
</script>
<%include file="bottom_new.mak"/>