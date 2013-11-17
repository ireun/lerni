<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>ZSO nr 15 w Sosnowcu</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="">
  <meta name="author" content="Kamil Danak" >

  <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css"  rel="stylesheet">
  <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/assets/ico/apple-touch-icon-144-precomposed.png">
  <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/assets/ico/apple-touch-icon-72-precomposed.png">
                  <link rel="apple-touch-icon-precomposed" href="/assets/ico/apple-touch-icon-57-precomposed.png">
                                 <link rel="shortcut icon" href="/assets/ico/favicon.png">
  <link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/normalize/2.1.0/normalize.css" />
  <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
  <script src="//cdnjs.cloudflare.com/ajax/libs/headjs/0.99/head.min.js"></script>
  <script src="/static/js/libs.min.js"></script>
  <script src="/static/js/admin.min.js"></script>
  <link href="/static/css/admin.min.css" rel="stylesheet">
  <link href="/static/libs/bootstrap/bootstrap.min.css"  rel="stylesheet">
  <link href="/static/libs/typeahead/typeahead.js-bootstrap.min.css"  rel="stylesheet">
  <link href="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/css/base/jquery.ui.all.min.css"  rel="stylesheet">
  <link href="/static/libs/jtable/jtable_metro_base.min.css"  rel="stylesheet">
  <link href="/static/libs/jtable/blue/jtable.min.css"  rel="stylesheet">
  <link href="/static/libs/gridster/jquery.gridster.min.css" rel="stylesheet">
  <link href="//cdnjs.cloudflare.com/ajax/libs/select2/3.4.1/select2.min.css"  rel="stylesheet">
</head>
<body>
  <div id="wrapper" class="">
    <header id="header">
      <div class="navbar navbar-inverse navbar-static-top" role="navigation">
        <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">ZSO nr 15 w Sosnowcu</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="/about">Szkoła</a></li>
            <li><a href="/education">Edukacja</a></li>
            <li><a href="/competitions">Konkursy</a></li>
            <li><a href="/student_zone">Strefa ucznia</a></li>
            <li><a href="/support">Support</a></li>
            %if not logged_in:
            <li><a href="/login">Login</a></li>
            %endif
          </ul>
            %if logged_in:
            <div class="pull-right">
              <ul class="nav navbar-nav">
                <li><a href="/logout">Logout</a></li>
                <li style="font-size: 22px;"><a href="/admin" class="icon-cog"></a></li>
              </ul>
            </div>
            %endif
        </div>
        </div>
      </div>
    </header>

    <aside id="sidebar">
      <div class="sidebar-content">
        <ul class="nav nav-tabs">
          <li class="active"> <a href="#tab-menu" data-toggle="tab"> <span class="icon icon-list"></span> </a> </li>
          <li class=""> <a href="#tab-overview" data-toggle="tab"> <span class="icon icon-bar-chart"></span> </a> </li>
          <li class=""> <a href="#tab-email" data-toggle="tab"> <span class="icon icon-envelope"></span> </a> </li>
        </ul>
        <div class="tab-content">
          <div class="tab-pane active" id="tab-menu">
            <nav id="nav" class="accordion panel-group">
              <ul id="navigation">
                <li class="divider">Główne menu</li>
                <li class="accordion-group active">
                  <a href="/admin/overview"> <span class="icon icon-dashboard"></span>
                    <span class="text">Kokpit</span><span class="label label-inverse">10</span>
                  </a>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation" href="#submenu1"> <span class="icon icon-user"></span>
                    <span class="text">Ludzie</span><span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu1" style="height: 0px;">
                    <li class=""><a href="/admin/users"> <span class="icon icon-angle-right"></span>Lista użytkowników</a></li>
                    <li class=""><a href="/admin/teachers"> <span class="icon icon-angle-right"></span>Nauczyciele</a></li>
                    <li class=""><a href="/admin/personel"> <span class="icon icon-angle-right"></span>Personel</a></li>
                    <li class=""><a href="/admin/studnets"> <span class="icon icon-angle-right"></span>Uczniowie</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation" href="#submenu2"> <span class="icon icon-th-list"></span>
                    <span class="text">Dziennik</span><span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu2" style="height: 0px;">
                    <li class=""><a href="/admin/log/subjects"> <span class="icon icon-angle-right"></span>Przedmioty</a></li>
                    <li class=""><a href="/admin/log/divisions"> <span class="icon icon-angle-right"></span>Kategorie klas</a></li>
                    <li class=""><a href="/admin/log/years"> <span class="icon icon-angle-right"></span>Lata Szkolne</a></li>
                    <li class=""><a href="/admin/log/rooms"> <span class="icon icon-angle-right"></span>Sale lekcyjne</a></li>
                    <li class=""><a href="/admin/log/timetables"> <span class="icon icon-angle-right"></span>Plan lekcji</a></li>
                    <li class=""><a href="/admin/log/lucky"> <span class="icon icon-angle-right"></span>Szczęśliwy numerek</a></li>
                    <li class=""><a href="/admin/log/extra"> <span class="icon icon-angle-right"></span>Zajęcia pozalekcyjne</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation" href="#submenu3"> <span class="icon icon-paperclip "></span>
                    <span class="text">Dekretacja</span><span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu3" style="height: 0px;">
                    <li class=""><a href="/admin/dec/tweets"> <span class="icon icon-angle-right"></span>Tweety</a></li>
                    <li class=""><a href="/admin/dec/registrations"> <span class="icon icon-angle-right"></span>Rejestracja</a></li>
                    <li class=""><a href="/admin/dec/petitions"> <span class="icon icon-angle-right"></span>Wnioski</a></li>
                    <li class=""><a href="/admin/dec/competitions"> <span class="icon icon-angle-right"></span>Konkursy</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation" href="#submenu4"> <span class="icon icon-folder-open"></span>
                    <span class="text">Wszystkie Treści</span><span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu4" style="height: 0px;">
                    <li class=""><a href="/admin/all/tweets"> <span class="icon icon-angle-right"></span>Tweety</a></li>
                    <li class=""><a href="/admin/all/folders"> <span class="icon icon-angle-right"></span>Foldery</a></li>
                    <li class=""><a href="/admin/all/petitions"> <span class="icon icon-angle-right"></span>Wnioski</a></li>
                    <li class=""><a href="/admin/all/competitions"> <span class="icon icon-angle-right"></span>Konkursy</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu5"> <span class="icon icon-list-alt"></span>
                    <span class="text">Ustawienia strony</span>                                                                                                                                                                             </span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu5" style="height: 0px;">
                    <li class="">
                      <a href="/admin/layouts"> <span class="icon icon-angle-right"></span>Layout</a>
                    </li>
                    <li class="">
                      <a href="widget-default.html"> <span class="icon icon-angle-right"></span>Galeria</a>
                    </li>
                    <li class="">
                      <a href="widget-draggable.html"> <span class="icon icon-angle-right"></span>Ostatnie video</a>
                    </li>
                  </ul>
                </li>
                <li class="divider">Nauka</li>
                  <!--
                <li class="accordion-group ">
                  <a href="/admin/overview"> <span class="icon icon-file-text"></span>
                    <span class="text">Do przczytania</span>
                  </a>
                </li>
                <li class="accordion-group ">
                  <a href="/admin/overview"> <span class="icon icon-compass"></span>
                    <span class="text">Oceny</span>
                  </a>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu10"> <span class="icon icon-folder-open"></span>
                    <span class="text">Konkursy</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu10" style="height: 0px;">
                    <li class=""><a href="chart.html"> <span class="icon icon-angle-right"></span>Dodaj konkurs</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Zobacz dostępne konkursy</a></li>
                  </ul>
                </li>
                -->
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu6"> <span class="icon icon-folder-open"></span>
                    <span class="text">Moja praca</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu6" style="height: 0px;">
                    <li class=""><a href="/account/folders"> <span class="icon icon-angle-right"></span>Foldery</a></li>
                    <li class=""><a href="/account/entries"> <span class="icon icon-angle-right"></span>Wpisy</a></li>
                    <li class=""><a href="/account/presentations"> <span class="icon icon-angle-right"></span>Prezentacje</a></li>
                    <li class=""><a href="/account/tasks-set"> <span class="icon icon-angle-right"></span>Zestawy zadań</a></li>
                    <li class=""><a href="/account/questions-set"> <span class="icon icon-angle-right"></span>Zestawy pytań</a></li>
                    <li class=""><a href="/account/other"> <span class="icon icon-angle-right"></span>Inne</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu7"> <span class="icon icon-cloud"></span>
                    <span class="text">Chmura</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu7" style="height: 0px;">
                    <li class=""><a href="chart.html"> <span class="icon icon-angle-right"></span>Moje pliki</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Moje programy</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Pliki do wydrukowania</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu8"> <span class="icon icon-cloud"></span>
                    <span class="text">Moje konto</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu8" style="height: 0px;">
                    <li class=""><a href="chart.html"> <span class="icon icon-angle-right"></span>Dane personalne</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Kursy</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Bezpieczeństwo</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Powiadomienia</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Aplikacje</a></li>
                  </ul>
                </li>
              </ul>
            </nav>
          </div>
          <div class="tab-pane" id="tab-overview">
            <div class="divider">Informacje podstawowe</div>
            <figure class="stats sparkline"> <span class="chart sparkline-bar" sparkBarColor="#dc143c">${balance_history}</span>
              <figcaption>
                <h4><small>Stan konta</small>${balance} <span class="icon icon-leaf"></span></h4>
              </figcaption>
            </figure>
            <figure class="stats sparkline"> <span class="chart sparkline-bar" sparkBarColor="#2E8DEF">${likes_history}</span>
              <figcaption>
                <h4><small>Liczba polubień</small>${likes} <span class="icon icon-thumbs-up"></span></h4>
              </figcaption>
            </figure>
            <figure class="stats sparkline"> <span class="chart sparkline-bar" sparkBarColor="#2E8DEF">${subscribers_history}</span>
              <figcaption>
                <h4><small>Subskrybujący</small>${subscribers} <span class="icon icon-eye-open"></span></h4>
              </figcaption>
            </figure>
            <figure class="stats sparkline"> <span class="chart sparkline-bar" sparkBarColor="#8CBF26">${preparation_history}</span>
              <figcaption>
                <h4><small>Przygotowanie</small>${preparation}% <span class="icon icon-check"></span></h4>
              </figcaption>
            </figure>
            <div class="divider">Nauka</div>
            <figure class="stats summary stacked">
              <div class="up"> <span class="icon icon-caret-up"></span> </div>
              <div class="icon circle red"> <span class="icon-book"></span>
              </div>
              <figcaption>
                <h3>+230<small>Prace domowe</small></h3>
              </figcaption>
            </figure>
            <figure class="stats summary stacked">
              <div class="down"> <span class="icon icon-caret-down"></span> </div>
              <div class="icon circle lime"> <span class="icon-smile"></span> </div>
              <figcaption>
                <h3>+20<small>Przygotowanie</small></h3>
              </figcaption>
            </figure>
            <figure class="stats summary stacked">
              <div class="icon circle teal"> <span class="icon-trophy"></span> </div>
              <figcaption>
                <h3>1,432<small>Osiągnięcia</small></h3>
              </figcaption>
            </figure>
          </div>
        </div>
      </div>
    </aside>