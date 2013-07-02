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
						<div class="settings_header">Aplikacja na telefon
						<form class="icon_add" action="${request.route_url('phone_app')}" method="post">
							<input type="hidden" name="action" value="add_phone"></input>
							<input class="submit" type="submit" value="Send"></input>
						</form>
						</div>
						<table class="table_devices">
							<colgroup>
								<col style="width:400px;"></col>
								<col style="width:56px;"></col>
								<col style="width:56px;"></col>
							</colgroup>
							<thead>
								<tr>
									<th scope="col">Nazwa urządzenia</th>
									<th scope="col"></th>
									<th scope="col"></th>
								</tr>
							</thead>
							<tbody>
								% for row in phones:
								<tr>
									% if row[2]=="phone_id":
									<td>Kliknji pokaż aby podłączyć urządzenie.</td>
									% else:									
									<td>${row[0]}</td>
									% endif
									<td><a href="#" onclick="show_qr('${row[1]}')">Pokaż</a></td>
									<td>
									<form action="${request.route_url('phone_app')}" method="post">
										<input type="hidden" name="action" value="delete"></input>
										<input type="hidden" name="code" value="${row[1]}"></input>
										<input class="del" class="submit" type="submit" value="Usuń"></input>										
									</form>
								</tr>
								% endfor
							</tbody>
						</table>
						<div id="qrcontainer">
							<div id="qrcode"></div>
							<div id="qrtext"></div>
						</div>
					</div>
				</div>
			</div>	
<%include file="bottom.mak"/>