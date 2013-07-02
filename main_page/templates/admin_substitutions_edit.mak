<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>ZSO nr 15 w Sosnowcu</title>
		<link rel="shortcut icon" href="${request.static_url('main_page:static/favicon.ico')}" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/index.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/index2.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/blip.css')}" type="text/css" media="screen" charset="utf-8" />
		<link rel="stylesheet" href="${request.static_url('main_page:static/admin.css')}" type="text/css" media="screen" charset="utf-8" />
		<script type="text/javascript" src="${request.static_url('main_page:static/jquery-1.8.0.min.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/jquery-ui-1.8.23.custom.min.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/refresh.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/kreator.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/substitutions_create.js')}"></script>
		
		
		<script type="text/javascript" src="${request.static_url('main_page:static/index.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/login.js')}"></script>
		<script type="text/javascript" src="${request.static_url('main_page:static/admin.js')}"></script>
	</head>
	<body>
		<div class="topbar">
			% if logged_in:
				<li class="button_nav" style="float: right;"> <a href="${request.application_url}/logout">Wyloguj</a> </li>
			% else:
			<form id="login-form" action="javascript://" method="post" onsubmit="form_login();">
				<ul class="inline-login">
					<li>
						<label for="login" id="login_label" style="opacity: 1; ">Username or email</label>
						<input type="text" id="login" name="login" value="" autocomplete="on" onfocus="setLabelOpacity(this.id,0.5)"
						onblur="setLabelOpacity(this.id,1)" oninput="setLabelVisibility(this.id)" onload="setLabelVisibility(this.id)">
					</li>
					<li>
						<label for="password" id="password_label" style="opacity: 1; ">Password</label>
						<input type="password" id="password" name="password" value="" autocomplete="on" onfocus="setLabelOpacity(this.id,0.5)"
						onblur="setLabelOpacity(this.id,1)" oninput="setLabelVisibility(this.id)" onload="setLabelVisibility(this.id)">
					</li>
					<li>
						<input id="login-button" class="btn dark" name="form.submitted" type="submit" value="Login">
					</li>
				</ul>
				<div id="login-message"></div>
				<div class="forgot-password">
					<a href="/forgot_password">Zapomniałeś hasła?</a>
				</div>
			</form>
			% endif
		</div>
		<div id="wrapper">		
			<div id="header">
				<img src="${request.static_url('main_page:static/logo.png')}" style="height:80px;">
				<div style="font-size: 48px; color: #E6E6E6; float: right;">ZSO nr 15 w Sosnowcu</div>
			</div>			
			<div id="panel_nav">
				<ol style="padding: 0 9px;">
					% for row in menu_top_list:
						<li class="button_nav"> <a href="${row[0]}">${row[1]}</a> </li>
					% endfor
				</ol>
			</div>
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
				  <!-- Nauczyciele nieobecni -->
               <table id="absent_table_edit">
						<colgroup>
						   <col class="column_teacher"/><col class="column_reason"/><col span="8" class="column_lesson"/><col class="column_delete"/>
						</colgroup>
                  <thead>
                     <tr>
                        <th>Nauczyciel</th><th>Przyczyna</th><th>Lekcja 1</th><th>Lekcja 2</th><th>Lekcja 3</th><th>Lekcja 4</th>
                        <th>Lekcja 5</th><th>Lekcja 6</th><th>Lekcja 7</th><th>Lekcja 8</th><th>Usuń</th>
                     </tr>
                  </thead>
                  <tbody>
                  </tbody>
               </table>
               <table id="absent_table_edit2">
						<colgroup>
						   <col class="column_teacher"/><col class="column_reason"/><col span="8" class="column_lesson"/><col class="column_delete"/>
						</colgroup>
                  <tbody>
                  </tbody>
               </table>
	           <button onclick="addToTable1(absent_table_edit2)">Dodaj</button>

					<!-- Nauczyciele zastępujący -->
               <table id="replace_table_edit">
                  <col class="column_teacher"/><col class="column_reason"/><col span="8" class="column_lesson"/><col class="column_delete"/>
                  <thead>
                     <tr>
                        <th>Nauczyciel</th><th>Za klasę</th><th>Lekcja 1</th><th>Lekcja 2</th><th>Lekcja 3</th>
                        <th>Lekcja 4</th><th>Lekcja 5</th><th>Lekcja 6</th><th>Lekcja 7</th><th>Lekcja 8</th><th>Usuń</th>
                     </tr>
                  </thead>
               </table>
               <table id="replace_table_edit2">
						<colgroup>
						   <col class="column_teacher"/><col class="column_reason"/><col span="8" class="column_lesson"/><col class="column_delete"/>
						</colgroup>
                  <tbody>
                  </tbody>
               </table>
	           <button onclick="addToTable4(replace_table_edit2)">Dodaj</button>
	           
					<!-- Dyżury -->
               <table id="duty_table_edit">
                  <col class="column_teacher"/><col class="column_reason"/><col class="column_teacher"/><col class="column_delete"/>
                  <thead>
                     <tr>
								<th>Nauczyciel nieobecny</th><th>Zmiana - miejsce</th><th>Nauczyciel zastępujący</th><th>Usuń</th>
                     </tr>
                  </thead>
               </table>
               <table id="duty_table_edit2">
                  <col class="column_teacher"/><col class="column_reason"/><col class="column_teacher"/><col class="column_delete"/>
                  <tbody>
                  </body>
               </table>
               <button onclick="addToTable2(duty_table_edit2)">Dodaj</button>
               <!--
               <div id="content" >
                  Zwolnione klasy.
                     <table style="width:182px;" id="table_exemption_edit">
                        <col style="width: 82px;"/><col style="width: 50px;"/><col style="width: 30px;"/>
                        <thead>
                           <tr>
                              <th>Klasa</th><th>Lekcja</th><th>Usuń</th>
                           </tr>
                        </thead>
                     </table>
                     <table style="width:182px;" id="table_exemption_edit2">
                        <col style="width: 82px;"/><col style="width: 50px;"/><col style="width: 30px;"/>
                        <tbody>
                        </tbody>
                     </table>
                     <button onclick="addToTable5(table_exemption_edit2)">Dodaj</button>
               </div>
               <div id="content2">
                  <b>Lektorat/klasa</b>--&gt;Lektorat/klasa
                  <table style="width:182px" ;="">
                     <thead>
                        <tr>
                           <th style="width: 82px;">Klasa</th>
                           <th style="width: 50px;">Lekcja</th>
                           <th style="width: 30px;">Usuń</th>
                        </tr>
                     </thead>
                     <tbody>
                     </tbody>
                  </table>
                  <table>
						   <thead>
                        <tr>
                           <th tabindex="0" id="span1" onclick="addToTable6(table_ltc)"><button>Dodaj</button></th>
                        </tr>
                     </thead>
                     <tbody>
                     </tbody>
                  </table>
               </div>
               <div id="content3">
                  Lektorat/klasa--&gt;<b>Lektorat/klasa</b>
                  <table>
                     <thead>
                        <tr>
                        <th style="width: 82px;">Klasa</th>
                        <th style="width: 50px;">Lekcja</th>
                        <th style="width: 30px;">Usuń</th>
                        </tr>
                     </thead>
                     <tbody>
                     </tbody>
                  </table>
                  <div>
                  <table class="class_table_ltc2" id="table_ltc2">
                     <thead>
                     </thead>
                     <tbody>
                     </tbody>
                     </table>
                  </div>
                  <table>
                     <thead>
                        <tr>
                           <th tabindex="0" id="span1" onclick="addToTable7(table_ltc2)"><button>Dodaj</button></th>
                        </tr>
                     </thead>
                     <tbody>
                     </tbody>
                  </table>					
               </div>
               -->
               <div id="released">L1: <br>L2: <br>L3: <br>L4: <br>L5: <br>L6: <br>L7: <br>L8: </div>
               Zastępstwa na dzień: <input type="text" id="datepicker" onchange="refresh()">
               <br />Uwagi:<br /><input type="text" id="comments" onchange="refresh()">
               <br />Minimalna ilość wierszy (zastępstwa):
               <input type="number" id="row_min" value="5" min="0" max="20" step="1" onchange="refresh()"/>
               <br />Minimalna ilość wierszy (dyżury):
               <input type="number" id="row2_min" value="4" min="0" max="20" step="1" onchange="refresh()"/>
               <br /><input type="checkbox" name="galowy" id="dzien_galowy" onchange="refresh()"/> Dzień galowy<br />
               <div id="errors"></div>
            </div>				
         </div>	
      </div><!-- wrapper close -->
		<footer>
			© ZSO nr 15, Sosnowiec 2008-2012			
		</footer>
		
		<script>
		window.onload=show() ; 
		</script>
		
	</body>
</html>
