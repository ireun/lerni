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
						<div class="settings_header">Formularz kontatktowy.</div>
							<form id="ask_form" method="post">
								Poniżej widzisz formularz, dzięki któremu możesz zadać pytanie.</br>
								<div class="label"><label>Temat:</label></div><input name="topic" type="text"></input></br>
								% if not logged_in:
								<div class="label"><label>Email:</label></div><input id="email" name="email" type="text" /></input></br>
								<div class="label"><label>Hasło:</label></div><input id="password" name="password" type="text" /></input>
								% endif
								<div style="display:inline-block;position:relative;top:5px;" id="email_help"></div></br>
								<div class="label"><label>Sekcja:</label></div>
									<select name="section_select" id="section_select" style="width:300px">
									<option></option>
									% for row in sections:
										<optgroup label="${row[0]}">
											% for row2 in row[1]:
											<option value="${row2[1]}">${row2[0]}</option>
											% endfor
										</optgroup>
									% endfor
									</select>
								</br>
								<label>Treść pytania:</label></br><textarea name="question"></textarea></br>
								<div id="importance">
									<input name="importance" type="text" value="40" class="dial"></br>
								</div>
								<div id="captcha">
									Pokaż siłę swojego umysłu - ile to jest 2x+2=6?<input name="captcha" type="text"></input></br>
									<input type="submit"></input>
								</div>
							</form>
						<div id="ask_list">
							<table>
								<colgroup>
									<col style="width:220px;"></col>
									<col style="width:70px;"></col>
								<colgroup>
								<thead>
									<tr>
										<th scope="col">Temat ticketu</th>
										<th scope="col">Otwórz</th>
									</tr>
								</thead>
							</table>
						</div>
					<script type="text/javascript" src="${request.static_url('main_page:static/jquery.knob.js')}"></script>
					<script type="text/javascript" >
						$(document).ready(function(){
							$("#captcha :submit").attr("disabled", true);
							$('#captcha :text').change(function(){
								if($('#captcha :text').val()!="2"){
									$("#captcha :submit").attr("disabled", true);
								}else{
									$(":submit").removeAttr("disabled");
								}
							});
  							$(function() {
							    $(".dial").knob({width:"120",angleOffset:"-125",angleArc:"250",displayPrevious:true,displayInput:false,step:"10",
							    'release':function(v){
							    	if(v>70){
										var n=noty({text: "Czy jesteś pewień, że problem jest tak ważny?\
										W celu poprawy jakości obsługi staraj się obiektywnie oceniać wagę problemu.",type: "warning",layout: "topRight"});
							    	}
							    	if(v<40){
										var n=noty({text: "Brawo. Dobrze jest zmniejszyć wagę problemu,\
										dzięki temu, gdy do zrobienia będzie coś bardzo ważnego\
										możliwe będzie oznaczenie tego jako coś ważnego.",type: "success",layout: "topRight"});
							    	}
							    } });
							});
							$("#section_select").select2({placeholder:"Wybierz sekcję"});
							$("#section_select").select2('data', null)							
						});
						var domains = ['hotmail.com', 'gmail.com', 'o2.pl'];
						var topLevelDomains = ["com", "net", "org", "pl"];
						$('#email').on('blur', function() {
						  $(this).mailcheck({
						    //domains: domains,                       // optional
						    topLevelDomains: topLevelDomains,       // optional
						    suggested: function(element, suggestion) {
						    	$("#email_help").html("Czy chodziło ci o:</br><a href=\"#\")\">"+suggestion.full+"</a>");
						    	$("#email_help a").click( function(){$('#email').val(suggestion.full);$("#email_help").html("");} );
						    },
						    empty: function(element) {
						    	$("#email_help").html("");
						    }
						  });
						});
					</script>
					</div>
				</div>
			</div>	
<%include file="bottom.mak"/>