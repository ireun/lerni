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
				<div id="center" style="width:820px;">
					<div class="settings_container" style="width:800px;">
						<div class="settings_header">Kontakt</div>

Zespół Szkół Ogólnokształcących nr15</br>
41-206 Sosnowiec, Plac Zillingera 1</br>
tel.032 2913784, 032 2911659</br>
</br>
dyrektor@staszic.edu.pl	dyrektor szkoły	mgr Tomasz Szyjkowski</br>
dyrektor2@staszic.edu.pl	z-ca dyrektora szkoły	mgr Dorota Gawron</br>
lo4@sosnowiec.edu.pl	sekretariat szkoły	pracownicy sekretariatu</br>
samorzad@staszic.edu.pl	samorzad szkolny	</br>
</br>
Jeśli wiesz cokolwiek na temat rozprowadzania narkotyków w naszej szkole, lub innych spraw związanych z narkotykami pisz anonimowo na adres: narkotyki@staszic.edu.pl
					</div>
				</div>
			</div>
<%include file="bottom.mak"/>