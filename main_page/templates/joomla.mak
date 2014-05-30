<%include file="top_new.mak"/>
<%include file="snippets/header.mak"/>
<link type='text/css' rel='stylesheet' href='/static/libs/raptor/raptor-front-end.min.css'/>

<script>
    var NWave = function () {
        this.css = function (p) {
            var path_len = $(document).width() - 300;
            var s = Math.abs(Math.sin(p * 60));
            var x = path_len - p * path_len;
            var y = s * 50 - 50;
            var o = 0;
            /*((s+2)/4+0.1)*/
            return {bottom: y + "px", left: x + "px", opacity: 1}
        }
    };
    var NWave2 = function () {
        this.css = function (p) {
            var path_len = $(document).width() - 300;
            var s = Math.abs(Math.sin(p * 60));
            var x = path_len - p * path_len;
            var y = s * 50 - 50;
            var o = 0;
            /*((s+2)/4+0.1)*/
            return {top: y + "px", right: x + "px", opacity: 1}
        }
    };

    head.js(jquery, ion_sound, jwerty, function () {
        $().ready(function () {
            (function ($) {
                $.path = {};
                $.fx.step.path = function (fx) {
                    var css = fx.end.css(1 - fx.pos);
                    if (css.bottom) {
                        fx.elem.style.bottom = css.bottom;
                    }
                    if (css.top) {
                        fx.elem.style.top = css.top;
                    }
                    if (css.right) {
                        fx.elem.style.right = css.right;
                    }
                    if (css.left) {
                        fx.elem.style.left = css.left;
                    }
                };
            })(jQuery);
            $.ionSound({sounds: ["rasputin"]});
            jwerty.key('↑,↑,↓,↓,←,→,←,→,B,A', function () {
                var natalia = $("#natalia");
                var natalia2 = $("#natalia2");
                natalia.width($(document).width() / 6);
                natalia2.width($(document).width() / 6);
                natalia.delay(200).show();
                natalia.delay(200).animate({path: new NWave}, 7800, "linear", function () {
                    natalia.hide();
                    natalia2.show()
                    natalia2.animate({path: new NWave2}, 8300, "linear", function () {
                        natalia2.hide()
                    });

                });
                $.ionSound.play("rasputin");
            });
        });
    });

    head.js(jquery, readmore, function(){
        $().ready(function () {
        $('.article > .panel-body').readmore();
        })
    });
    head.js(jquery, jquery_ui, function(){
        $().ready(function () {
            $('#button_add_article').click(function() {
            $('#button_add_article').hide();
            var a = $("<div class='article panel panel-default'>\
                        <div class='panel-heading' style='padding: 4px 4px 10px 4px;'>\
                            <h4 id=\"add_title\" class='title editable'>Wpisz tytuł tutaj.</h4>\
                            <div id=\"add_email\" class='author editable'>Tutaj adres email (nie będzie publicznie widoczny)</div>\
                        </div>\
                        <div class='panel-body'>\
                            <div id=\"add_content\"> A tutaj text artykułu.</div>\
                        </div>\
                    </div>");
            $('.articles').prepend(a);

            $(function($){
            $(a).raptor({partialEdit: $(".editable"),
                                           layouts: {
                                               toolbar: {
                                                   uiOrder: [
                                                            ['historyUndo', 'historyRedo','cancel','save'],
                                                            ['tagMenu','classMenu','alignLeft', 'alignCenter', 'alignJustify', 'alignRight','textBold', 'textItalic', 'textUnderline', 'textStrike'],
                                                            ['textSuper', 'textSub'],
                                                            /*['colorMenuBasic'],*/
                                                            ['snippetMenu', 'specialCharacters'],
                                                            ['listUnordered', 'listOrdered'],
                                                            ['hrCreate', 'textBlockQuote'],
                                                            /*['textSizeDecrease', 'textSizeIncrease'],*/
                                                            ['floatLeft', 'floatNone', 'floatRight'],
                                                            ['tableCreate', 'tableInsertRow', 'tableDeleteRow', 'tableInsertColumn', 'tableDeleteColumn'],
                                                            ['linkCreate', 'linkRemove', 'embed', 'insertFile'],
                                                            ['guides','viewSource']
                                                   ]
                                               },
                                               hoverPanel: {
                                                  uiOrder: [['clickButtonToEdit']]
                                               }
                                           },
                                           enablePlugins: true,
                                           reloadOnDisable: true,
                                           plugins:{
                                                    dock: { docked: true, dockToScreen: true,persist: false},
                                                    save: { plugin: 'saveJson'},
                                                    saveJson: {url: '/api?format=jsonp&method=lerni.articles.raptor.propose',
                                                               postName: 'raptor-content',
                                                               id: function() { return 1 }},
                                                    textBlockQuote: false
                                           }
                                        });
            });
        });
    });
});
</script>

<style>
    .raptor-layout-toolbar-group .ui-button {
        height: 20px;
    }
    .raptor-layout-toolbar-group .ui-button-text-icon-primary .ui-button-text {
        padding: 0 16px 0 32px;
    }
    .raptor-layout-toolbar-group .ui-button-text-only .ui-button-text {
        padding: 1px 16px 10px;
    }
    .ui-dialog{
        z-index: 13002;
    }
    .natalia {
        position: fixed;
        display: none;
    }

    #header {
        max-width: 1050px;
        border: none;
        background: #FFF;
        max-height: 335px;
    }

    #header img {
        max-width: 1050px;
    }

    #main {
        max-width: 1050px;
        border: none;
        background: #FFF
    }

    #footer {
        background: #FFF
    }

    #wrapper {
        background: #E0DEDF;
    }

    #masthead a {
        padding: 4px;
        color: #707070;
    }

    #masthead .active a {
        text-decoration: none;
        color: black;
    }

    #masthead {
        position: relative;
        top: -7px;
        border-bottom: solid 1px lightgrey;
    }

    .navbar {
        display: none;
    }

    #header {
        margin-top: 0;
    }

    .nav-stacked > li > a {
        padding: 4px;
        color: #606060;
        border-bottom: solid 1px #E0E0E0;
    }

    .article .title {
        font-size: 1.4em;
        font-weight: normal;
        color: #555;
        font-family: Arial;
        text-align: left;
        line-height: 20px;
    }

    .article {
        background: #FFF
    }

    .readmore-js-toggle{
        font-weight: bold;
        padding: 2px 5px 2px 10px;
        margin-top: 5px;
        text-decoration: none;
        color: #095197;
        border: 1px solid #DDD;
        background: #EEE;
        display: inline-block;
        width: 100%;
    }

    .readmore-js-toggle:hover {
        background: #444;
        color: #FFF
    }

    .readmore-js-expanded {
        height: 100% !important;
    }

    .published {
        font-size: 12px;
    }

    #login-form li {
        list-style: none;
        margin-left: -40px;
        font-size: 13px;
    }

    @media (min-width: 992px) {
        #menu {
            width: 23%;
        }

        #article_main {
            width: 52%;
        }
    }

    .timeago, .author {
        font-size: 13px !important;
        color: #888;
        margin-top: -10px;
        min-width: 10px;
    }

    span {
        font-size: inherit !important;
    }

    p {
        margin: 0 !important;
    }

    .article .panel-heading {
        background: #DEDEDE;
    }

    .lucky_number {
        font-size: 140px;
        border: none !important;
        width: 100% !important;
        color: #444;
        margin-top: -30px;
    }

    .lucky_number_date {
        margin-top: -50px;
        text-align: center;
        color: #BBB;
    }
</style>
<div id="main" class="container">
    <div class="row">
        <div id="masthead">
            <ul class="nav nav-justified">
                <li class="item current active"><a href="/strona-glowna">Strona Główna</a></li>
                <li><a href="/zastepstwa">Zastępstwa</a></li>
                <li><a href="/p/dla-kandydatow">Dla Kandydatów</a></li>
                <li><a href="/education">Dla Rodziców</a></li>
                <li><a href="/about">Poznaj Staszica!</a></li>
                <li><a href="http://staszic.edu.pl/support">Support</a></li>
                <li><a href="http://pirc.pl/bramka/staszic/kandydat/ajax">Czat (${int(irc_users)-1})</a></li>
            </ul>
        </div>
    </div>
    <div class="row">
        <div id="menu" class="col-sm-3 hidden-xs">
            <h4>O Szkole</h4>
            <ul class="nav nav-stacked">
                <li><a href="http://www.120.ab.staszic.edu.pl">120-lecie Staszica</a></li>
                <li><a href="http://staszic.edu.pl/historia">Historia i Patroni</a></li>
                <li><a href="http://staszic.edu.pl/entry/8">Szkolne muzeum</a></li>
                <li><a href="http://staszic.edu.pl/graduates">Absolwenci</a></li>
                <li><a href="/fundacja">Fundacja</a></li>
                <li><a href="/towarzystwo-szkol-tworczych">Towarzystwo Szkół Twórczych</a></li>
                <li><a href="http://staszic.edu.pl/dokumenty">Statuty i Regulaminy</a></li>
                <li><a href="/galeria">Galeria</a></li>
                <li><a href="/kontakt">Kontakt</a></li>
                <li><a href="/dojazd">Dojazd</a></li>
                <li><a href="http://sis.staszic.edu.pl/schedule">Plan lekcji</a></li>
                <li><a href="/pliki/kalendarium2013-14.pdf">Kalendarium</a></li>
                <li><a href="http://www.facebook.com/sustaszic">Staszic na Facebooku</a></li>
            </ul>
            <h3>Edukacja</h3>
            <ul class="nav nav-stacked">
                <li><a href="/podreczniki">Podręczniki i Programy</a></li>
                <li><a href="/pliki/matura2014.doc">Tematy maturalne</a></li>
                <li><a href="/pliki/bibl.pdf">Bibliografia</a></li>
                <li><a href="/comenius">Comenius</a></li>
                <li><a href="http://www.ab.staszic.edu.pl">Informatyka</a></li>
            </ul>
            <h3>Strefa uczniowska</h3>
            <ul class="nav nav-stacked">
                <li><a href="http://staszic.edu.pl/lucky">Szczęśliwy numerek</a></li>
                <li><a href="/su">Samorząd Uczniowski</a></li>
                <li><a href="/staszictv">StaszicTV</a></li>
                <li><a href="/poczta/">Poczta</a></li>
                <li><a href="/p/dla-kandydatow">Serwis dla Kandydatów</a></li>
                <li><a href="/sport">Sport</a></li>
                <li><a href="/pliki/KONSULTACJE.pdf">Konsultacje</a></li>
                <li><a href="/pliki/dyżury.pdf">Dyżury klas</a></li>
                <li><a href="/dzwonki">Dzwonki</a></li>
            </ul>
            <h3>Na skróty</h3>
            <ul class="nav nav-stacked">
                <li><a href="http://staszic.edu.pl/competitions">Konkursy</a></li>
                <li><a href="/klub-podroznika">Klub Podróżnika</a></li>
                <li><a href="/">PO DRUGIEJ STRONIE LUSTRA</a></li>
            </ul>
        </div>
        <div id="article_main" class="col-sm-6">
            <div class="row">
                    <button id="button_add_article" type="button" class="btn btn-default btn-lg btn-block">Dodaj artykuł</button>
            </div>
            <br/>

            <div class="articles">
                % for x in articles:
                    <div class="article panel panel-default">
                        <div class="panel-heading" style="padding: 4px 4px 10px 4px;">
                            <h4 class="title">${x['title']}</h4>

                            <div class='author'>Administrator</div>
                            <div class='timeago' title="${x['time']}">${x['created']}</div>
                        </div>
                        <div class='panel-body'>
                            ${x['introtext'] |n}
                        </div>
                    </div>
                % endfor
            </div>
            <div id="pagination" class="container">
                <ul class="pagination pagination-sm">
                    <li class="disabled"><a href="#">&laquo;</a></li>
                    % for x in range(max(1, page_id-5),max(1, page_id-5)+10):
                        <li
                            %if x==page_id:
                                class="active"
                            %endif
                                ><a title="${x}" href="?page=${x}" class="pagenav">${x}</a></li>
                    % endfor
                    <li><a href="#">&raquo;</a></li>
                </ul>
            </div>
        </div>
        <!-- end wrapper -->

        <div id="right" class="col-sm-3  hidden-xs">
            <div class="panel panel-default">
                <div class="panel-heading">Nasze sukcesy (<a href="/nasze-sukcesy">więcej</a>)</div>
                <table class="table">
                    <tr>
                        <td class="editable">Łukasz Nawaro z klasy 3mat1 uzyskał tytuł laureata Olimpiady Wiedzy o Polsce i Świecie
                            Współczesnym.
                        </td>
                    </tr>
                    <tr>
                        <td>Justyna Motyka z klasy 3mat1 zdobyła tytuł finalistki Olimpiady Języka Francuskiego.</td>
                    </tr>
                </table>
            </div>
            <!--
            <h4>Logowanie</h4>
            <form action="https://staszic.edu.pl/strona-glowna" id="login-form" method="post" name="login-form">
                <fieldset class="userdata">
                    <div class="input-group">
                      <span class="input-group-addon">@</span>
                      <input id="modlgn-username" name="username" type="text" class="form-control" placeholder="Użytkownik">
                    </div>
                   <div class="input-group">
                      <span class="input-group-addon">***</span>
                      <input id="modlgn-passwd" name="password" type="password" class="form-control" placeholder="Hasło">
                    </div>
                    <div class="checkbox pull-right">
                        <label>
                          <input class="inputbox pull-left" id="modlgn-remember" name="remember" type="checkbox" value="yes">Zapamiętaj
                        </label>
                    </div>
                    <button type="submit" name="Submit" value="Zaloguj" class="btn btn-default pull-left">Zaloguj</button>
                    <input name="option" type="hidden" value="com_users"> <input name="task" type="hidden" value="user.login">
                    <input name="return" type="hidden" value="aW5kZXgucGhwP0l0ZW1pZD0z">
                    <input name="f99f4e842d3454782ffb695eeb5fb978" type="hidden" value="1">
                </fieldset>
                <ul>
                    <li><a href="/component/users/?view=reset">Nie pamiętasz hasła?</a></li>
                    <li><a href="/component/users/?view=remind">Nie pamiętasz nazwy?</a></li>
                    <li><a href="/component/users/?view=registration">Załóż swoje konto!</a></li>
                </ul>
            </form>
            <!--
            <a href="/administrator">Panel administratora</a>
            <a href="/admin">Panel Lerni</a>
            -->
            <div class="panel panel-default">
                <div class="panel-heading">Facebook</div>
                <div id="fb-root"></div>
                <script>(function (d, s, id) {
                    var js, fjs = d.getElementsByTagName(s)[0];
                    if (d.getElementById(id)) return;
                    js = d.createElement(s);
                    js.id = id;
                    js.src = "//connect.facebook.net/en_GB/all.js#xfbml=1&appId=231650380180066";
                    fjs.parentNode.insertBefore(js, fjs);
                }(document, 'script', 'facebook-jssdk'));</script>
                <div style="overflow: hidden; width: 220px; margin: auto;">
                    <div class="fb-like-box" data-href="https://www.facebook.com/sustaszic" data-width="280"
                         data-colorscheme="light" data-show-faces="false" data-header="false" data-stream="true"
                         data-show-border="false" style="margin-left: -60px;"></div>
                </div>

            </div>

            <div class="panel panel-default">
                <div class="panel-heading">Szczęśliwy numerek</div>
                <div class="lucky_number">${lucky_number}</div>
                <div class="lucky_number_date">${lucky_number_date}&nbsp;</div>
            </div>
        </div>
        <!-- end right -->
    </div>
    <!-- end row -->
    <div id="space"></div>
</div>
<img class="natalia" id="natalia" src="/static/images/natalia_poklonskaya.png"/>
<img class="natalia" id="natalia2" src="/static/images/natalia_poklonskaya2.png"/>
<%include file="bottom_new.mak"/>
