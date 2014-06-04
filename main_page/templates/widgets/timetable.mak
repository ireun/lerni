<table class="table table-striped table-bordered table-condensed">
<tr>
    <th></th>
    <th>Poniedziałek</th>
    <th>Wtorek</th>
    <th>Środa</th>
    <th>Czwartek</th>
    <th>Piątek</th>
</tr>
%for x in lessons:
<tr>
    <td>${x[0]}.</td>
    <td>${"/".join(x[1])}</td>
    <td>${"/".join(x[2])}</td>
    <td>${"/".join(x[3])}</td>
    <td>${"/".join(x[4])}</td>
    <td>${"/".join(x[5])}</td>
</tr>
%endfor
</table>