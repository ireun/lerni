<p>
Search: <input id="filter" type="text">
<select id="competition_group_select">
  <option value="all">Wszyscy</option>
  <option value="prof">Naukowcy i Profesorowie</option>
  <option value="mini">Ministrowie i urzędnicy ministerstw</option>
  <option value="duch">Duchowni</option>
</select>
</p>
<div id="jtable"></div>
<script>
head.js(jquery, jquery_ui, jtable, jtable_pl, function(){
        $('#jtable').jtable({
            title: "Absolwenci",
            paging: true,
            pageSize: 10,
            selecting: true,
            sorting: true,
            defaultSorting: 'id DESC',
        actions: {
            listAction: '/api?format=jsonp&method=lerni.graduates.getList'
        },
        fields: {
            id: {
                    key: true,
                    list: false,
            },
            name: {
                    title: 'Imię i nazwisko',
                    width: '20%'
            },
            graduation: {
                    title: 'Matura',
                    width: '20%'
            },
            about: {
                    title: 'O absolwenice',
                    width: '60%'
            }
        }
    });
    var search_competitors = function(){
            $('#jtable').jtable('load', {
                name: $("#filter").val(),
                competitionGroupId: $("#competition_group_select option:selected").val()
            });
            var a = {"all":"Absolwenci", "prof": "Absolwenci - Naukowcy i Profesorowie",
                "mini":"Absolwenci - Ministrowie i urzędnicy ministerstw", "duch":"Absolwenci - Duchowni",};
            $('#jtable .jtable-title-text').html(a[$("#competition_group_select option:selected").val()])
    }
    $("#competition_group_select").change(search_competitors);
    $("#filter").on('input', search_competitors);
    search_competitors();
});
</script>
Powyższe zestawienie powstało na podstawie akt i materiałów posiadanych przez Stowarzyszenie Wychowanków i Sympatyków Liceum oraz archiwum historii szkoły.<br/>
Zestawienia dokonali:<br/>
Jan Strzelecki<br/>
Anna Żelechowska<br/>
aktualizacja 007, wersja poprawiona i rozszerzona<br/><br/>
Od Redakcji<br/>
IV Liceum Ogólnokształcące w Sosnowcu wykształciło w ciągu stu czternastu lat swojego istnienia ponad 7 tysięcy absolwentów .<br/>
Tę ogromną rzeszę “Staszicaków” tworzą ludzie , którzy dotarli do wielu odległych zakątków świata i ci, którzy w kraju zaakcentowali swoją obecność we wszystkich bez mała dziedzinach życia. W gronie absolwentów znaleźli się naukowcy, artyści, duchowni, lekarze, prawnicy, literaci oraz specjaliści wielu innych profesji.<br/>
Niniejsze zestawienie składa się z trzech części.<br/>
Część I to spis nazwisk ludzi nauki- absolwentów i wychowanków z tytułem profesorskim i innymi tytułami naukowymi.<br/>
Część II zawiera nazwiska ministrów i pracowników ministerstw.<br/>
Część III gromadzi specjalistów różnych profesji i obejmuje nazwiska absolwentów i wychowanków.<br/>
Ostatnia część IV składa się z nazwisk i obejmuje wykaz absolwentów, których udziałem stała się służba duchowna.<br/>
Ogółem zestawienie obejmuje nazwiska najwybitniejszych absolwentów Gimnazjum i Liceum<br/>
im. Stanisława Staszica w Sosnowcu.<br/>
Redakcja działu "Wybitni Absolwenci" prosi wszystkich zainteresowanych wychowanków i absolwentów IV LO im. St.Staszica w Sosnowcu o informację. Dziękujemy.<br/>