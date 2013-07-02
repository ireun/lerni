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
						<div class="settings_header">Centrum supportu staszic.edu.pl</div>
						Witaj na stronie supportu staszic.edu.pl<br/>
						Dostaniesz tutaj odpowiedź na każde trapiące cię pytanie.<br/>
						Skorzystaj z menu po lewej i wybierz interesującą cię pozycję.<br/>
						Jeśli coś nie działa staraj się dokładnie opisać swój problem.<br/>
						Jeśli korzystasz z Internet Explorera - zainstaluj normalną przeglądarkę.<br/>
						Chcesz pomagać innym? <a href="/apply">kliknij tutaj</a><br/>
					</div>
				</div>
			</div>	
<%include file="bottom.mak"/>