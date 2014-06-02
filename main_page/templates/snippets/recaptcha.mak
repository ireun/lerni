<script type="text/javascript">
  var RecaptchaOptions = {
      tabindex: 1,
      theme: 'custom',
      custom_theme_widget: 'recaptcha_widget'
  };
</script>
<div id="recaptcha_widget">
    <table id="recaptcha_table" class="recaptchatable recaptcha_theme_clean">
        <tbody>
            <tr height="73">
                <td style="padding: 0px 0px 3px ! important;" class="recaptcha_image_cell" width="302">
                    <div id="recaptcha_image"></div>
                </td>
                <td style="padding: 10px 7px 7px 7px;">
                    <a title="Get a new challenge" id="recaptcha_reload_btn" href="javascript:Recaptcha.reload()">
                        <img src="http://www.google.com/recaptcha/api/img/clean/refresh.png" id="recaptcha_reload" alt="Get a new challenge" height="18" width="25"></a><br>
                    <a title="Get an audio challenge" id="recaptcha_switch_audio_btn" class="recaptcha_only_if_image" href="javascript:Recaptcha.switch_type(&#39;audio&#39;)">
                        <img src="http://www.google.com/recaptcha/api/img/clean/audio.png" id="recaptcha_switch_audio" alt="Get an audio challenge" height="15" width="25"></a><br>
                    <a title="Get a visual challenge" id="recaptcha_switch_img_btn" class="recaptcha_only_if_audio" href="javascript:Recaptcha.switch_type(&#39;image&#39;)">
                        <img src="http://www.google.com/recaptcha/api/img/clean/text.png" id="recaptcha_switch_img" alt="Get a visual challenge" height="15" width="25"></a>
                    <a title="Help" id="recaptcha_whatsthis_btn" href="javascript:Recaptcha.showhelp()">
                        <img alt="Help" src="http://www.google.com/recaptcha/api/img/clean/help.png" id="recaptcha_whatsthis" height="16" width="25">
                    </a>
                </td>
                <td style="padding: 18px 7px 18px 7px;"> <img src="http://www.google.com/recaptcha/api/img/clean/logo.png" id="recaptcha_logo" alt="" height="36" width="71"> </td>
            </tr>
        </tbody>
    </table>
    <input type="text" id="recaptcha_response_field" name="recaptcha_response_field" style="display:none;"/>
    <script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=${recaptcha_public}"></script>
    <noscript><iframe src="http://www.google.com/recaptcha/api/noscript?k=${recaptcha_public}" height="300" width="500" frameborder="0"></iframe><br>
    <textarea name="recaptcha_challenge_field" rows="3" cols="40"></textarea>
    <input type="hidden" name="recaptcha_response_field" value="manual_challenge"></noscript>
    <style>
        body iframe{display: none;}
    </style>
</div>