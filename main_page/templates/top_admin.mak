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
  <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">
  <script src="//cdnjs.cloudflare.com/ajax/libs/headjs/0.99/head.min.js"></script>
  <script src="/static/js/libs.min.js"></script>
  <script src="/static/js/admin.min.js"></script>
  <link href="/static/css/admin.min.css" rel="stylesheet">
  <link href="/static/libs/bootstrap/bootstrap.min.css"  rel="stylesheet">
  <link href="/static/libs/typeahead/typeahead.js-bootstrap.min.css"  rel="stylesheet">
  <link href="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/css/base/jquery.ui.all.min.css"  rel="stylesheet">
  <link href="/static/libs/jtable/jtable_metro_base.min.css"  rel="stylesheet">
  <link href="/static/libs/jtable/blue/jtable.min.css"  rel="stylesheet">
  <link href="//cdnjs.cloudflare.com/ajax/libs/select2/3.4.1/select2.min.css"  rel="stylesheet">
</head>
<body>
  <div id="wrapper" class="">
    <header id="header">
      <div class="navbar navbar-medium navbar-inverse navbar-static-top">
        <div class="navbar-inner">
          <div class="container">
            <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse"> <span class="icon-bar"></span></button>
            <a class="brand" href="/">ZSO nr 15 w Sosnowcu</a>
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li> <a href="/about">Szkoła</a></li>
                <li> <a href="/education">Edukacja</a></li>
                <li> <a href="/">Konkursy</a></li>
                <li> <a href="/">Strefa ucznia</a></li>
                <li> <a href="/support">Support</a></li>
                <li> <a href="/login">Login</a></li>
              </ul>
              <div class="pull-right">
                <ul class="nav">
                  <li> <a href="/admin">Panel administratora</a></li>
                  <li style="float:right;height:40px;">
					<li style="font-size: 22px;"><a href="/account" class="icon-cog"></a></li>
                  </li>
                </ul>
              </div>
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
            <nav id="nav" class="accordion">
              <ul id="navigation">
                <li class="divider">Główne menu</li>
                <li class="accordion-group active">
                  <a href="/admin/overview"> <span class="icon icon-dashboard"></span>
                    <span class="text">Kokpit</span><span class="label label-inverse">10</span>
                  </a>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation" href="#submenu2"> <span class="icon icon-user"></span>
                    <span class="text">Ludzie</span><span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu2" class="collapse ">
                    <li class=""><a href="/admin/users"> <span class="icon icon-angle-right"></span>Lista użytkowników</a></li>
                    <li class=""><a href="/admin/teachers"> <span class="icon icon-angle-right"></span>Nauczyciele</a></li>
                    <li class=""><a href="/admin/personel"> <span class="icon icon-angle-right"></span>Personel</a></li>
                    <li class=""><a href="/admin/studnets"> <span class="icon icon-angle-right"></span>Uczniowie</a></li>
                  </ul>
                </li>

                <!--
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation" href="#submenu3"> <span class="icon icon-th-list"></span>
                    <span class="text">Dziennik</span><span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu3" class="collapse ">
                    <li class=""><a href="/admin/log/years"> <span class="icon icon-angle-right"></span>Lata Szkolne</a></li>
                    <li class=""><a href="/admin/log/groups"> <span class="icon icon-angle-right"></span>Klasy</a></li>
                    <li class=""><a href="/admin/log/groups"> <span class="icon icon-angle-right"></span>Sale lekcyjne</a></li>
                    <li class=""><a href="/admin/log/timetables"> <span class="icon icon-angle-right"></span>Plan lekcji</a></li>
                    <li class=""><a href="/admin/log/extra"> <span class="icon icon-angle-right"></span>Zajęcia pozalekcyjne</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation" href="#submenu4"> <span class="icon icon-cogs"></span>
                    <span class="text">Rekrutacja</span> <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu4" class="collapse ">
                    <li class=""><a href="jquery-ui.html"> <span class="icon icon-angle-right"></span>Jquery UI</a></li>
                    <li class=""><a href="calendar.html"> <span class="icon icon-angle-right"></span>Calendar</a></li>
                    <li class=""><a href="media.html"> <span class="icon icon-angle-right"></span>Media</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu5"> <span class="icon icon-sitemap"></span>
                    <span class="text">Budowa strony</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu5" class="collapse ">
                    <li>
                      <a href="page-login.html"> <span class="icon icon-angle-right"></span>
                        <span class="text">Rejestracja</span>
                      </a>
                    </li>
                    <li>
                      <a data-toggle="collapse" data-parent="#level3"
                      href="#submenu6"> <span class="icon icon-angle-right"></span>
                        <span class="text">Error</span>
                        <span class="label label-inverse">4</span>
                      </a>
                      <ul id="submenu6" class="collapse">
                        <li>
                          <a href="page-error403.html"> <span class="icon icon-angle-right"></span>403
                            page
                          </a>
                        </li>
                        <li>
                          <a href="page-error404.html"> <span class="icon icon-angle-right"></span>404
                            page
                          </a>
                        </li>
                        <li>
                          <a href="page-error500.html"> <span class="icon icon-angle-right"></span>500
                            page
                          </a>
                        </li>
                        <li>
                          <a href="page-error503.html"> <span class="icon icon-angle-right"></span>503
                            page
                          </a>
                        </li>
                      </ul>
                    </li>
                    <li class="">
                      <a href="page-blank.html"> <span class="icon icon-angle-right"></span>
                        <span class="text">Blank                                                                                                                                                                        </span>
                      </a>
                    </li>
                  </ul>
                </li>
                -->
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu7"> <span class="icon icon-list-alt"></span>
                    <span class="text">Ustawienia strony</span>                                                                                                                                                                             </span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu7" class="collapse ">
                    <li class="">
                      <a href="widget-default.html"> <span class="icon icon-angle-right"></span>Strona główna</a>
                    </li>
                    <li class="">
                      <a href="widget-default.html"> <span class="icon icon-angle-right"></span>Galeria</a>
                    </li>
                    <li class="">
                      <a href="widget-draggable.html"> <span class="icon icon-angle-right"></span>Ostatnie video</a>
                    </li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu8"> <span class="icon icon-cloud"></span>
                    <span class="text">Chmura</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu8" class="collapse ">
                    <li class=""><a href="chart.html"> <span class="icon icon-angle-right"></span>Moje pliki</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Moje programy</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Pliki do wydrukowania</a></li>
                  </ul>
                </li>
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu9"> <span class="icon icon-cloud"></span>
                    <span class="text">Moje konto</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu9" class="collapse ">
                    <li class=""><a href="chart.html"> <span class="icon icon-angle-right"></span>Dane personalne</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Kursy</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Bezpieczeństwo</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Powiadomienia</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Aplikacje</a></li>                    
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
                  <ul id="submenu10" class="collapse ">
                    <li class=""><a href="chart.html"> <span class="icon icon-angle-right"></span>Dodaj konkurs</a></li>
                    <li class=""><a href="statistic.html"> <span class="icon icon-angle-right"></span>Zobacz dostępne konkursy</a></li>
                  </ul>
                </li>
                -->
                <li class="accordion-group ">
                  <a data-toggle="collapse" data-parent="#navigation"
                  href="#submenu11"> <span class="icon icon-folder-open"></span>
                    <span class="text">Moja praca</span>
                    <span class="arrow icon-caret-down"></span>
                  </a>
                  <ul id="submenu11" class="collapse ">
                    <li class=""><a href="/account/folders"> <span class="icon icon-angle-right"></span>Foldery</a></li>
                    <li class=""><a href="/account/entries"> <span class="icon icon-angle-right"></span>Wpisy</a></li>
                    <li class=""><a href="/account/presentations"> <span class="icon icon-angle-right"></span>Prezentacje</a></li>
                    <li class=""><a href="/account/tasks-set"> <span class="icon icon-angle-right"></span>Zestawy zadań</a></li>
                    <li class=""><a href="/account/questions-set"> <span class="icon icon-angle-right"></span>Zestawy pytań</a></li>
                    <li class=""><a href="/account/other"> <span class="icon icon-angle-right"></span>Inne</a></li>
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