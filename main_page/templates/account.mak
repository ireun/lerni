<%include file="top_new.mak"/>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<div id="settings-wrapper">
   <ul id="settings_tab" class="tabs big">
   <li><a href="#basic" id="account_tab">Ogólne</a></li>
   <li><a href="#profile" id="profile_tab">Bezpieczeństwo</a></li>
   <li><a href="#password" id="password_tab">Prywatność</a></li>
   <li><a href="#notifications" id="notifications_tab">Powiadomienia</a></li>
   <li><a href="#applications" id="notifications_tab">Aplikacje</a></li>
   </ul>
   <div id="basic">
      <div class="settings_header">Informacje podstawowe</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Nazwa użytkownika:</td><td>
               <a href="#" id="username" data-type="text" data-original-title="Nazwa użytkownika" class="editable editable-click editable-empty">${name}</a>
            </td></tr>
            <tr><td>Pierwsze imię:</td><td>
               <a href="#" id="firstname" data-type="text" data-original-title="Pierwsze imię" class="editable editable-click">${first_name}</a>
            </td></tr><tr><td>Drugie imię:</td><td>
               <a href="#" id="secondname" data-type="text" data-original-title="drugie imię" class="editable editable-click editable-empty">${second_name}</a>
            </td></tr><tr><td>Nazwisko:</td><td>
               <a href="#" id="lastname" data-type="text" data-original-title="Nazwisko" class="editable editable-click editable-empty">${last_name}</a>
            </td></tr><tr><td>Wiek:</td><td>
               ${years}
            </td></tr><tr><td>Płeć:</td><td>
               ${gender}
            </td></tr><tr><td>Klasa:</td><td>
               ${group}
            </td></tr><tr><td>Lektorat:</td><td>
               ${language_group}
            </td></tr><tr><td>Rozszerzenie:</td><td>
               ${extension_group}
            </td></tr>
         </tbody>
      </table>
      <div class="settings_header">Miejsce zamieszkania</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Miejscowość:</td><td>
               Sosnowiec
            </td></tr><tr><td>Ulica:</td><td>
               Legionów
            </td></tr><tr><td>Numer</td><td>
               klatki: 5/II
            </td></tr><tr><td>Numer mieszkania:</td><td>
               9
            </td></tr>
         </tbody>
      </table>
      <div class="settings_header">Dane kontaktowe</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Numer telefonu:</td><td>
               518158009
            </td></tr><tr><td>Email:</td><td>
               kamilx3@gmail.com
            </td></tr><tr><td>XMPP:</td><td>
               kamilx3@gmail.com
            </td></tr>
         </tbody>
      </table>
      <div class="settings_header">Informacje dodatkowe</div>
      <table class="table table-bordered table-striped">
         <tbody>
            <tr><td>Adres bitcoin:</td><td>
               
            </td></tr><tr><td>Opeenstreetmap:</td><td>
               KD_
            </td></tr><tr><td>Minecraft:</td><td>
               KD_
            </td></tr><tr><td>Strona internetowa:</td><td>
               moja-strona.pl
            </td></tr>
         </tbody>
      </table>

   </div>
   <div id="profile" >
      <div class="settings_header">Informacje podstawowe</div>
      Nasdasdasd
   </div>
   <div id="notifications" >
      <div class="settings_header">Informacje podstawowe</div>
      Nasdasdasd
   </div>
   <div id="applications" >
      <div class="settings_header">Informacje podstawowe</div>
      Nasdasdasd
   </div>
   <div class="setting-bottom">
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