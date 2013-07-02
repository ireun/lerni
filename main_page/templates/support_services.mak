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
						<div class="settings_header">Status serwisów</div>
<div id="service_status">
  <div id="news_container"></div>
  <ul>
    <li class="green checked"><h4>Minecraft.net</h4><span>This service is healthy. All is good!</span></li>
    <li class="green checked"><h4>Mojang accounts website</h4><span>This service is healthy. All is good!</span></li>
    <li class="green checked"><h4>Minecraft logins</h4><span>This service is healthy. All is good!</span></li>
    <li class="green checked"><h4>Mojang accounts login</h4><span>This service is healthy. All is good!</span></li>
    <li class="green checked"><h4>Minecraft multiplayer sessions</h4><span>This service is healthy. All is good!</span></li>
    <li class="green checked"><h4>Minecraft skins</h4><span>This service is healthy. All is good!</span></li>
  </ul>
</div>

					</div>
				</div>
			</div>	
<%include file="bottom.mak"/>