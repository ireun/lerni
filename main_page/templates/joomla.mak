<%include file="top_new.mak"/>
<%include file="snippets/header.mak"/>
<script>
    head.js(jquery, readmore, function(){
        $().ready(function () {
        $('.article > .panel-body.read_more').readmore();
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
                            <div id=\"add_content\" class='editable'> A tutaj text artykułu.</div>\
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

<div id="main" class="container">
    <div class="row hidden-xs">
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
            %for set in menu_left:
                <h4>${set['name']}</h4>
                <ul class="nav nav-stacked">
                %for item in set['items']:
                    <li><a href="${item['link']}">${item['name']}</a></li>
                %endfor
                </ul>
            %endfor
        </div>

        <div id="article_main" class="col-sm-6">
            <div class="row hidden-xs">
                <div class="col-sm-6">
                    <a href="http://www.120.ab.staszic.edu.pl"> <img src="http://staszic.edu.pl//pliki/banners/baner.jpg" alt="120 lecie"/> </a>
                </div>
                <div class="col-sm-6">
                    Podstrona 120.ab.staszic.edu.pl zawierajaca informacje o organizacji 120 - lecia naszego liceum.
                </div>
            </div>
            <div class="row hidden-xs">
                <div class="col-sm-12">
                    <button id="button_add_article" type="button" class="btn btn-default btn-lg btn-block">Zaproponuj artykuł</button>
                </div>
            </div>
            <br/>

            <div class="articles">
                % for x in articles:
                    <div class="article panel panel-default">
                        <div class="panel-heading" style="padding: 4px 4px 10px 4px;">
                            <h4 class="title">${x['title']}</h4>

                            <div class='author'>${x['author']}</div>
                            <time class="timeago" datetime="${x['time']}">${x['created']}</time>
                            <!--
                            <div class="reading_time">${x['reading_time']}</div>
                            -->

                            <div class="dropdown" style="font-size: 13px !important;color: #888;position: absolute; top: 5px; right: 10px;">
                              <a id="drop1" href="#" role="button" class="dropdown-toggle" data-toggle="dropdown"><b class="caret"></b></a>
                              <ul class="dropdown-menu" role="menu" aria-labelledby="drop1">
                                <li role="presentation" class="disabled"><a role="menuitem" tabindex="-1">Action</a></li>
                                <li role="presentation" class="disabled"><a role="menuitem" tabindex="-1">Zaproponuj poprawkę</a></li>
                                <li role="presentation"><a role="menuitem" tabindex="-1" href="http://twitter.com/fat">Link bezpośredni</a></li>
                              </ul>
                            </div>
                        </div>
                        <div class='panel-body video ${['', 'read_more'][int(x['read_more'])]}'>
                            ${x['text'] |n}
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
            % if last_gallery:
            <div class="panel panel-default">
                <div class="panel-heading">Ostatnio w galerii (<a href="/gallery">więcej</a>)</div>
                <ul id="Grid" style="margin-bottom: 0;">
                    <li style="width: 100%; margin-bottom: 0;">
                        <a href="${last_gallery[1]}" class="athumbnail">
                            <img src="${last_gallery[2]}" alt="">
                            <div class="caption">
                            <p>${last_gallery[0]}</p>
                            </div>
                        </a>
                    </li>
                </ul>
            </div>
            % endif
            <style>
                .panel-default > .panel-heading {position: relative;}
                .panel-heading > .add{position: absolute; top: -2px;right: -1px;color: #DDD;}
                .panel-heading > .add:hover{color: #AAA; cursor: pointer;}
            </style>
            <div class="panel panel-default">
                <div class="panel-heading">
                    Nasze sukcesy (<a href="/nasze-sukcesy">więcej</a>)
                    <i class="fa fa-plus-square fa-2x add"></i>
                </div>
                <table class="table">
                    <tr>
                        <td class="editable">
                            Na podstawie komunikatu przesłanego przez Wydział Edukacji, informujemy że wśród 39 laureatów
                            wojewódzkich konkursów przedmiotowych dla uczniów gimnazjów z ternu miasta Sosnowca,
                            aż 20 to nasi uczniowie.<br/>
                            Wśród szkół licealnych w Sosnowcu tytuł laureata i finalisty Ogólnopolskiej Olimpiady
                            przedmiotowe uzyskało 5 uczniów, z tego aż 4 stanowią nasi uczniowie.
                        </td>
                    </tr>
                </table>
            </div>
            <style>.panel-body > a{text-decoration: underline;
            font-family: 'Helvetica Neue', Helvetica, Arial, 'lucida grande',tahoma,verdana,arial,sans-serif;

            }</style>
            <div class="panel panel-default">
                <div class="panel-heading">Facebook</div>
                <div class="panel-body" style="padding: 6px;">
                    <a href="https://www.facebook.com/sustaszic" style="color: #3b5998;cursor: pointer;text-decoration: none;font-weight: bold;font-size: 13px;">Samorząd Uczniowski IV LO im. Stanisława Staszica w Sosnowcu</a>
                    <%include file="snippets/fb-root.mak"/>
                    <div class="fb-like" data-href="https://www.facebook.com/sustaszic" data-width="200" data-layout="button_count" data-action="like" data-show-faces="false" data-share="false"></div>
                </div>
            </div>

            <div class="panel panel-default">
                <div class="panel-heading">Szczęśliwy numerek (<a href="/lucky">więcej</a>)</div>
                <div class="lucky_number">${lucky_number}</div>
                <div class="lucky_number_date">${lucky_number_date}&nbsp;</div>
            </div>
	        <img src="/static/uploads/zebra.png" alt="Zebra - maskotka Staszica." style="margin-bottom: 20px;">
            <!--
            <a href="/syllabus"><img src="/static/uploads/syllabus.png" alt="Syllabus"></a>
            -->
            <div class="panel panel-default">
                <div class="panel-heading">Changelog (<a href="https://github.com/kamilx3/lerni/commits/master">więcej</a>)</div>
                ---14.06.2014---<br />
                Dodano cache galerii i szkic <a href="/syllabus">syllabusa.</a><br />
                ---13.06.2014---<br />
                Nowa <a href="/gallery"> galeria </a> (fotorama + flickr).<br />
                ---13.06.2014---<br />
                Dodano bbcode dla youtube.<br />
            </div>
        </div>
    </div>
</div>
<%include file="bottom_new.mak"/>
