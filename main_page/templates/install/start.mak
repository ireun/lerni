<%include file="../top_new.mak"/>
<%include file="../snippets/header.mak"/>
<div id="main" class="container">
	<div id="inner-wrapper" class="container">
        <div class="row">
            <div class="col-md-8">
                <h2>Witaj w procesie konfiguracji lerni.</h2>
                <h4>Aby móc kontynuować następujące wymagania muszą zostać spełnione.</h4>
                <table class="table table-bordered">
                    <tr>
                        %if internet_on:
                        <td class="success">Komputer jest podłączony do internetu.</td>
                        %else:
                        <td class="warning">Nie wykryto połączenia z internetem.
                            Jeśli jesteś pewien, że jest ono dostępne nie przejmuj się tym komunikatem.</td>
                        %endif
                    </tr>
                    <tr>
                        %if celery:
                        <td class="success">W sieci obecny jest prawidłowo skonfigurowany serwer Celery.</td>
                        %else:
                        <td class="danger">Połączenie z serwerem Celery nie powiodło się.
                            Instalacja nie może być kontynuowana.</td>
                        %endif
                    </tr>
                    <tr>
                      <td class="warning">Prawidłowo skonfigurowano wysyłkę maili. [niesprawdzono]</td>
                    </tr>
                    <tr>
                      <td class="warning">Wkhtmltopdf jest zainstalowany. [niesprawdzono]</td>
                    </tr>
                    <tr>
                      <td class="warning">Serwer cups jest dostępny. [niesprawdzono]</td>
                    </tr>
                    <tr>
                        %if gpg:
                        <td class="success">GnuPG jest zainstalowane.</td>
                        %else:
                        <td class="warning">GnuPG nie jest zainstalowane. Część funkcji może być niedostępna.</td>
                        %endif
                    </tr>
                    <tr>
                        %if update_available:
                        <td class="warning">Nowa wersja Lerni jest dostępna.</td>
                        %else:
                        <td class="success">Instalowana wersja jest najnowszą dostępną wersją Lerni.</td>
                        %endif
                    </tr>
                </table>
                <a href="?s=1" class="btn btn-default pull-right" role="button">Dalej <i class="icon-white icon-chevron-right"></i></a>

                <!--
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
                -->
            </div>
            <%include file="installation_progress.mak"/>
        </div>

    </div>
</div>
<%include file="../bottom_new.mak"/>