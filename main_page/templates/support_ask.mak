<%include file="top_new.mak"/>
<%include file="snippets/header.mak"/>
<div id="main" class="container">
	<div id="inner-wrapper" class="container">
    <script type="text/javascript">
      var RecaptchaOptions = {
          tabindex: 1,
          theme: 'custom',
          custom_theme_widget: 'recaptcha_widget'
      };
    </script>
	<form class="grid-form">
		<fieldset>
			<legend>Formularz kontatktowy</legend>
			<div data-row-span="2">
				<div data-field-span="1">
					<label>Temat</label>
					<input type="text" autofocus>
				</div>
                <div data-field-span="1">
                    <label>Dział</label>
					<select>
                        % for row in sections:
                            % for row2 in row[1]:
						        <option value="${row2[1]}">${row2[0]}</option>
                            % endfor
                        % endfor
					</select>
                </div>
			</div>
			<div data-row-span="1">
				<div data-field-span="1">
					<label>Treść pytania</label>
					<textarea style="resize: vertical;"></textarea>
				</div>
            </div>
		</fieldset>
		<br>
		<fieldset>
			<legend>Dane kontaktowe</legend>
			<div data-row-span="4">
				<div data-field-span="1">
					<label>Tytuł</label>
					<label><input type="radio" name="customer-title[]"> Pan</label> &nbsp;
					<label><input type="radio" name="customer-title[]"> Pani</label> &nbsp;
				</div>
				<div data-field-span="3">
					<label>Imię i nazwisko</label>
					<input type="text">
				</div>
			</div>
			<div data-row-span="2">
				<div data-field-span="1">
					<label>Adres e-mail (wymagany)</label>
					<input type="text">
				</div>
				<div data-field-span="1">
					<label>Numer telefonu</label>
                    <input type="text">
				</div>
			</div>
		</fieldset>
		<br>
		<fieldset>
            <div data-row-span="3">
               <legend>Captcha</legend>
               <div style="height: 78px; display: block; padding: 0;" data-field-span="2">
			   <div id="recaptcha_widget" >
					<table id="recaptcha_table" class="recaptchatable recaptcha_theme_clean"><tbody><tr height="73">
					<td style="padding: 0px 0px 3px ! important;" class="recaptcha_image_cell" width="302"><div id="recaptcha_image"></div></td>
					<td style="padding: 10px 7px 7px 7px;">
					<a title="Get a new challenge" id="recaptcha_reload_btn" href="javascript:Recaptcha.reload()"><img src="http://www.google.com/recaptcha/api/img/clean/refresh.png" id="recaptcha_reload" alt="Get a new challenge" height="18" width="25"></a><br>
					<a title="Get an audio challenge" id="recaptcha_switch_audio_btn" class="recaptcha_only_if_image" href="javascript:Recaptcha.switch_type(&#39;audio&#39;)"><img src="http://www.google.com/recaptcha/api/img/clean/audio.png" id="recaptcha_switch_audio" alt="Get an audio challenge" height="15" width="25"></a><br>
					<a title="Get a visual challenge" id="recaptcha_switch_img_btn" class="recaptcha_only_if_audio" href="javascript:Recaptcha.switch_type(&#39;image&#39;)"><img src="http://www.google.com/recaptcha/api/img/clean/text.png" id="recaptcha_switch_img" alt="Get a visual challenge" height="15" width="25"></a>
					<a title="Help" id="recaptcha_whatsthis_btn" href="javascript:Recaptcha.showhelp()"><img alt="Help" src="http://www.google.com/recaptcha/api/img/clean/help.png" id="recaptcha_whatsthis" height="16" width="25"></a>
					</td>
					<td style="padding: 18px 7px 18px 7px;"> <img src="http://www.google.com/recaptcha/api/img/clean/logo.png" id="recaptcha_logo" alt="" height="36" width="71"> </td>
					</tr> </tbody></table>
					<input type="text" id="recaptcha_response_field" name="recaptcha_response_field" style="display:none;">
					<script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=${recaptcha_public}"></script>
					<noscript><iframe src="http://www.google.com/recaptcha/api/noscript?k=${recaptcha_public}" height="300" width="500" frameborder="0"></iframe><br>
					<textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>
					<input type="hidden" name="recaptcha_response_field" value="manual_challenge"></noscript>
				</div>
				</div>
				<div data-field-span="1">
					<label>Kod z obrazka</label>
					<input type="text">
				</div>
			</div>
		</fieldset>
	</form>




<!--
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
					-->
    </div>
</div>
<%include file="bottom_new.mak"/>