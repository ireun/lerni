<p>
Search: <input id="filter" type="text">
<select id="competition_group_select">
  <option value="gimnazjum_olimpiady">Gimnazjum Olimpiady</option>
  <option value="gimnazjum_konkursy">Gimnazjum Konkursy</option>
  <option value="liceum_olimpiady">Liceum Olimpiady</option>
  <option value="liceum_konkursy">Liceum Konkursy</option>
</select>
    <!--
Status: <select class="filter-status">
<option></option>
<option value="active">Active</option>
<option value="disabled">Disabled</option>
<option value="suspended">Suspended</option>
</select>
<a href="#clear" class="clear-filter" title="clear filter">[clear]</a>
<a href="#api" class="filter-api" title="Filter using the Filter API">[filter API]</a>
-->
</p>
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