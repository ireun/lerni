# -*- coding: utf-8 -*-
<%include file="top_new.mak"/>
    <div class="container">
		<div id="form_wrapper" class="form_wrapper">
            <form action="/forgot-password" method="post" class="forgot_password active">
                <h2 class="form-signin-heading"> Ustaw nowe hasło </h2>
                <input name="new_password" type="password" class="input-block-level" placeholder="Nowe hasło">
                <input name="new_password_repeat" type="password" class="input-block-level" placeholder="Powtórz hasło">
                <input type="hidden" name="token" value="${token}">
                <div class="custom_container"></div>
                <div class="settings-bottom" style="margin: 16px -30px 0 -30px;">
                    <button id="submit_button" name="form.submitted" type="submit" class="btn large primary pull-right" >Wyślij</button>
                   <a href="/login" rel="login" class="linkform">Pamiętam!</a><br>
                </div>
            </form>
		</div>
    </div>

    <script type="text/javascript">
        head.js(jquery, jquery_noty, jquery_noty_b_c, jquery_noty_b_l, jquery_noty_b_r,
                        jquery_noty_c, jquery_noty_c_l, jquery_noty_c_r,
                        jquery_noty_i, jquery_noty_t, jquery_noty_t_d, jquery_noty_t_l, jquery_noty_t_r, function () {
            function setWrapperWidth(){
                $form_wrapper.css({
                    'max-width'	: ($currentForm.data('max-width')+60) + 'px',
                    'min-width'	: ($currentForm.data('max-width')+60) + 'px',
                    height	: ($currentForm.data('height')+25) + 'px'
                });
            }
            var show_alert = function (message, type) {
                var n = $('.custom_container').noty({text: message, type: type, callback: {
                    afterShow: function() {setWrapperWidth();},
                    onClose: function() {setTimeout(function() {setWrapperWidth();}, 2000);}}
                });
                $form_wrapper= $('#form_wrapper');
                $currentForm= $form_wrapper.children('form.active');
            };
            %for row in alerts:
                %if len(row) == 3:
                    show_alert('${row[0]}','${row[1]}','${row[2]}');
                %else:
                    show_alert('${row[0]}','${row[1]}');
                %endif
            % endfor
        });
    </script>
    <script src="/static/js/form_login.min.js"></script>
<style>
    #space{height: 200px;}
</style>
<%include file="bottom_new.mak"/>
