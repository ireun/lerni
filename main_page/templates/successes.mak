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
            <div class="settings_header">${title}</div>
            Wybierz z listy po lewej interesującą cię listę sukcesów. :D	
				  </div>
				</div>
			</div>
<%include file="bottom.mak"/>