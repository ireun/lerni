<%include file="top.mak"/>
<!--
#header {
	background: #1D3836 url(header_blue.png) repeat;
}
		-->
			<div id="main_page">
				<div id="center">
				% if not knows_password:
				lool
				% else:
					<div id="data"> Zastępstwa na dzień ${date_for} </div>
					<table  class="hovertable" id="substitutions_table" style="width: 100%;">
						<colgroup>
						   <col class="column_id"/>
						   <col class="column_teacher"/>
						   <col span="8" class="column_lesson"/>
						</colgroup>
						<thead>
						   <tr>
							  <td>LP</td>
							  <td>Imie i nazwisko nauczyciela nieobecnego</td>
							<!-- <td>Przyczyna nieobecności</td> -->
							  <td>1</td>
							  <td>2</td>
							  <td>3</td>
							  <td>4</td>
							  <td>5</td>
							  <td >6</td>
							  <td >7</td>
							  <td >8</td>
							</tr>
						</thead>
						<tbody>
						% for row in range(len(absent_list)):
						<tr>
							<td>${row+1}</td>
							<td>${absent_list[row][0]}</td>
							<!-- <td>${absent_list[row][1]}</td> -->
							<td >${absent_list[row][2][0]}</td>
							<td >${absent_list[row][2][1]}</td>
							<td >${absent_list[row][2][2]}</td>
							<td >${absent_list[row][2][3]}</td>
							<td >${absent_list[row][2][4]}</td>
							<td >${absent_list[row][2][5]}</td>
							<td >${absent_list[row][2][6]}</td>
							<td >${absent_list[row][2][7]}</td>
						</tr>
						% endfor
						</tbody>
						<thead>
   						<tr>
   							<td>LP</td>
   							<td>Imie i nazwisko nauczyciela zastępującego</td>
   							<!-- <td>Za klasę</td> -->
   							<td >1</td>
   							<td >2</td>
   							<td >3</td>
   							<td >4</td>
   							<td >5</td>
   							<td >6</td>
   							<td >7</td>
   							<td >8</td>
   						<tr>
						</thead>
						<tbody >
   						% for row in range(len(replace_list)):
   						<tr>
   							<td>${row+1}</td>
   							<td>${replace_list[row][0]}</td>
   							<!-- <td>${replace_list[row][1]}</td> -->
   							<td >${replace_list[row][2][0]}</td>
   							<td >${replace_list[row][2][1]}</td>
   							<td >${replace_list[row][2][2]}</td>
   							<td >${replace_list[row][2][3]}</td>
   							<td >${replace_list[row][2][4]}</td>
   							<td >${replace_list[row][2][5]}</td>
   							<td >${replace_list[row][2][6]}</td>
   							<td >${replace_list[row][2][7]}</td>
   						</tr>
   						% endfor
						</tbody>
   					<tr>
   							<td colspan="11">Uwagi:</td>
   					<tr>
					</table>
					<br /><div id="data"> Dyżury </div>
					<table id="duty_table" style="width: 100%;">
						<colgroup>
						   <col class="column_teacher"/>
						   <col class="column_place"/>
						   <col class="column_teacher"/>
						</colgroup>
						<thead>
							<td>Nauczyciel nieobecny</td>
							<td>Zmiana - miejsce</td>
							<td>Nauczyciel zastępujący</td>
						</thead>
						% for row in range(len(duty_list)):
						<tr>
							<td>${duty_list[row][0]}</td>
							<td>${duty_list[row][1]}</td>
							<td>${duty_list[row][2]}</td>
						</tr>
						% endfor
					</table>
				% endif
				</div>
			</div>	
<%include file="bottom.mak"/>
