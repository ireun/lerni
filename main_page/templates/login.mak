<%include file="top_new.mak"/>
  <body>
    <div class="container">
      <form class="form-signin" action="/login">
        <h2 class="form-signin-heading">Zaloguj się</h2>
        <input name="login" type="text" class="input-block-level" placeholder="Adres email">
        <input name="password" type="password" class="input-block-level" placeholder="Hasło">
        <label><a href="">Rejestracja</a></label>
        <!--
        <label class="checkbox">
          <input type="checkbox" value="remember-me"> Pamiętaj mnie
        </label>
        -->
        <button class="btn btn-large btn-primary" name="form.submitted" type="submit">Sign in</button>
      </form>
      <span id="login-error" class="runner" data-layout="inline" data-custom=".custom_container" data-type="alert">Alert <i class="icon-caret-right"></i></span>
    </div> <!-- /container -->
    <script type="text/javascript">
        var noty = noty({text: 'noty - a jquery notification library!',type: 'warning',layout: 'topRight'});
        var noty2 = $('#login-error').noty({text: 'noty - a jquery notification library!'});
    </script>
<%include file="bottom_new.mak"/>