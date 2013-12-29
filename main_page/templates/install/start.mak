<%include file="../top_new.mak"/>
<%include file="../snippets/header.mak"/>
<div id="main" class="container">
	<div id="inner-wrapper" class="container">
        <h2>Witaj w procesie konfiguracji lerni.</h2>
        <h4>Jeśli robiłeś to już wcześniej możesz chcieć wczytać starą <a href="/uploaddb">bazę danych.</a></h4>
        <h4>W przeciwnym wypadku uzupełnij poniższy formularz.</h4>
        <form role="form">
          <div class="form-group">
            <label for="pageTitle">Tytuł strony</label>
            <input type="text" class="form-control" id="pageTitle" placeholder="Tytuł strony">
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">Adres email</label>
            <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Adres email">
          </div>
          <button type="submit" class="btn btn-default">Wyślij</button>
        </form>
    </div>
</div>
<%include file="../bottom_new.mak"/>