<p>
Search: <input id="filter" type="text">
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
<table class="footable table" data-filter="#filter" data-filter-text-only="true" data-sort="true">
<thead>
<tr>
  <th data-ignore="true" data-hide="all">>
    ID
  </th>
  <th>
    Imię i Nazwisko
  </th>
  <th>
    Rodzaj konkursu
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
            <td>${row[4]}</td>
            <td>${row[5]}</td>
            <td>${row[6]}</td>
        </tr>
    % endfor
</tbody>
</table>