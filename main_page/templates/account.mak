<%include file="top.mak"/>
			<div id="main_page">
			<div id="left"> 
				<div id="nav">
					<ul>
						% for row in menu_left_list:
							<li><a href="${row[0]}" id="homenav">${row[1]}</a></li>
						% endfor
	    			</ul>
			 </div>
			</div>
				<div id="center">
					<div class="settings_container">
						<div class="settings_header">Informacje podstawowe</div>
						Nazwa użytkownika: ${name}</br>
						Pierwsze imię: ${first_name}</br>
						Drugie imię: ${second_name}</br>
						Nazwisko: ${last_name}</br>
						Wiek: ${years}</br>
						Płeć: ${gender}</br>
						Klasa: ${group}</br>
						Lektorat: ${language_group}</br>
						Rozszerzenie: ${extension_group}</br>
						<div class="settings_header">Miejsce zamieszkania</div>
						Miejscowość: Sosnowiec</br>
						Ulica: Legionów</br>
						Numer klatki: 5/II</br>
						Numer mieszkania: 9</br>
						<div class="settings_header">Dane kontaktowe</div>
						Numer telefonu: 518158009</br>
						Email: kamilx3@gmail.com </br>
						XMPP: kamilx3@gmail.com </br>
						<div class="settings_header">Informacje dodatkowe</div>
						Adres bitcoin:</br>
						Opeenstreetmap: KD_</br>
						Minecraft: KD_</br>
						Skype: kamil__196</br>
						Strona internetowa: moja-strona.pl</br>
					</div>
				</div>
			</div>	
<%include file="bottom.mak"/>