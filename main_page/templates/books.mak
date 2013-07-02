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
						<div class="settings_header">Podręczniki</div>
Poniżej przedstawiamy wykaz podręczników obowiązujących w roku szkolnym 2012/2013 dla poszczególnych klas.</br>

Gimnazjum</br>
Klasa 1 liceum</br>
Klasa 2 liceum</br>
Klasa 3 liceum</br>

					</div>
				</div>
			</div>
<%include file="bottom.mak"/>
