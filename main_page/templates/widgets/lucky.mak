<h3>Aktualny szczęśliwy numerek</h3>
<div class="lucky_number">
<div class="lucky_number_number">${lucky_number}</div>
<div class="lucky_number_date">${lucky_number_date}</div>
</div>
<h3>Szczęśliwe numerki na ten tydzień</h3>
        <ul>
            %for x in numbers:
            <li>
                ${x[0]} - <strong>${x[1]}</strong>
            </li>
            %endfor
        </ul>
<h3>Pozostały do wylosowania</h3>
<p>
    Poniżej znajduje się pełna lista wszystkich szcześliwych numerków,
    które pozostały jeszcze do wylosowania, tj. nie były one jeszcze
    użyte w obecnej turze.
</p>
<ul>
    %for x in left:
        <li>${x}</li>
    %endfor
</ul>
<h3>Historia szczęśliwego numerka</h3>
<div id="jtable"></div>
<script>
head.js(jquery, jquery_ui, jtable, jtable_pl, function(){
        $('#jtable').jtable({
            title: "Szczęśliwe numerki",
            paging: true,
            pageSize: 10,
            selecting: false,
            sorting: false,
            defaultSorting: 'name ASC',
        actions: {
            listAction: '/api?format=jsonp&method=lerni.lucky.getList'
        },
        fields: {
            first_date: {
                    key: true,
                    list: false,
                    title: 'From',
            },
            0: {
                    title: 'Pon',
            },
            1: {
                    title: 'Wt',
            },
            2: {
                    title: 'Śr',
            },
            3: {
                    title: 'Czw',
            },
            4: {
                    title: 'Pt',
            },
            5: {
                    title: 'Sob',
            },
            6: {
                    title: 'Ndz',
            },
            start: {
                    title: 'start',
            },
            end: {
                    title: 'end',
            },
        }
    });
    $('#jtable').jtable('load');
});
</script>