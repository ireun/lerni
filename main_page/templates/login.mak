<%include file="top_new.mak"/>
  <body>
    <div class="container">
      <form class="form-signin" action="/login" method="post">
        <h2 class="form-signin-heading">Zaloguj się</h2>
        <input name="login" type="text" class="input-block-level" placeholder="Adres email">
        <input name="password" type="password" class="input-block-level" placeholder="Hasło">
        <label><a href="">Rejestracja</a></label>
        <!--
        <label class="checkbox">
          <input type="checkbox" value="remember-me"> Pamiętaj mnie
        </label>
        -->
        <div class="custom_container"></div>
        <button class="btn btn-large btn-primary" name="form.submitted" type="submit">Sign in</button>
      </form>
      
    </div> <!-- /container -->
    <script type="text/javascript">
		   %for row in allerts:
            show_allert('${row[0]}','${row[1]}','${row[2]}')
		   % endfor
    </script>
<%include file="bottom_new.mak"/>