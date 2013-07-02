<%include file="top.mak"/>
			<div id="main_page">
			<div id="left"> 
				<div id="nav">
					<ul>
						% for row in menu_left_list:
							<li><a href="${row[0]}" class="indent${row[2]}" id="homenav">${row[1]}</a></li>
						% endfor
	    			</ul>
				</div>
			</div>
				<div id="right">

				</div>
				<div id="center">
					<div id="primary" data-mercury="full">
						default content
					</div>
				</div>
			</div>	
<%include file="bottom.mak"/>
