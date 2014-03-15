<p>
Search: <input id="filter" type="text">
<select id="competition_group_select">
  <option value="gimnazjum_olimpiady">Gimnazjum Olimpiady</option>
  <option value="gimnazjum_konkursy">Gimnazjum Konkursy</option>
  <option value="liceum_olimpiady">Liceum Olimpiady</option>
  <option value="liceum_konkursy">Liceum Konkursy</option>
</select>
</p>
<div id="jtable"></div>
<script>

head.js(jquery, jquery_ui, jtable, jtable_pl, function(){
        $('#jtable').jtable({
            title: "Olimpijczycy - Gimnazjum",
            paging: true,
            pageSize: 10,
            selecting: true,
            sorting: true,
            defaultSorting: 'id DESC',
        actions: {
            listAction: '/api?format=jsonp&method=lerni.competitors.getList'
        },
        fields: {
            id: {
                    key: true,
                    list: false,
            },
            first_name: {
                    title: 'Imię',
                    width: '10%'
            },
            last_name: {
                    title: 'Nazwisko',
                    width: '10%'
            },
            competition_id: {
                    title: 'Nazwa konkursu/olimpiady',
                    options: '/api?format=jsonp&method=lerni.competitors.competitions.nameList',
                    width: '30%'
            },
            competitor_type_id: {
                    title: 'Stopień',
                    options: '/api?format=jsonp&method=lerni.competitors.types.nameList',
                    width: '10%'
            },
            subject_id: {
                    title: 'Przedmiot',
                    options: '/api?format=jsonp&method=lerni.subjects.nameList',
                    width: '10%'
            },
            competitor_tutor_id: {
                    title: 'Opiekun',
                    options: '/api?format=jsonp&method=lerni.competitors.tutors.nameList',
                    width: '20%'
            },
            year: {
                    title: 'Rok szkolny',
                    width: '10%'
            },
        }
    });
    var search_competitors = function(){
            $('#jtable').jtable('load', {
                name: $("#filter").val(),
                competitionGroupId: $("#competition_group_select option:selected").val()
            });
    }
    $("#competition_group_select").change(search_competitors);
    $("#filter").on('input', search_competitors);
    search_competitors();
});
</script>

<!--
<table class="footable table" data-filter-text-only="true" data-sort="true" data-page-size="20">
<thead>
<tr>
  <th data-ignore="true" data-hide="all">
    ID
  </th>
  <th>
    Imię i Nazwisko
  </th>
  <th>
    Nazwa konkursu/olimiady
  </th>
  <th data-ignore="true" data-hide="all">
    Typ konkursu
  </th>
  <th>
    Stopień
  </th>
  <th>
    Przedmiot
  </th>
  <th>
    Opiekun
  </th>
  <th>
    Rok szkolny
  </th>
</tr>
</thead>
<tbody>
    % for row in competitors:
        <tr>
            <td></span>${row[0]}</td>
            <td data-value="${row[1]}">${row[1]}</td>
            <td>${row[2]}</td>
            <td>${row[3]}</td>
            <td>${row[4]}</td>
            <td>${row[5]}</td>
            <td>${row[6]}</td>
            <td>${row[7]}</td>
        </tr>
    % endfor
</tbody>
<tfoot>
    <tr>
        <td colspan="5" style="text-align: center">
            <div class="paginate"></div>
        </td>
    </tr>
</tfoot>
</table>

-->