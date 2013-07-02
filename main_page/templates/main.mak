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
					% for row in articles:
						<div class="article">
							<div class="titlebar">
                        <div class="title">
                        	% if editor:
                        	<div id="primary" data-mercury="simple">${row[1]}</div>
                        	% else:
                        	${row[1]}
                        	% endif
                        </div>
							</div>
							<div class="time"><abbr class="timeago" title="${row[2]}">${row[2]}</abbr><br /></div>	
							<div class="author">${row[3]}<br /></div>	
								% if editor:
								<div class="content">
								<div id="primary" data-mercury="full">
									<% context.write(row[4]) %>
								</div>
								% else:
								<div class="content shortable">
								<% context.write(row[4]) %><br />
								% endif
							</div>
							<div class="post_options2">
								% if editor:
								</br>
								% else:
								    <!--
									<div onclick="toggle_comments(this,${row[0]})" class="show_comments">Pokaż komentarze (${row[5]})</div>
									  -->
									<div onclick="show_post(this)" class="expand_content">Rozwiń<img src="/static/expand.png"></div>
								% endif
							</div>
							<div class="comments">
							</div>
						</div>
					% endfor
				</div>
				<div id="right">
					<div id="blip"></div>
				</div>
			</div>
<%include file="bottom.mak"/>
