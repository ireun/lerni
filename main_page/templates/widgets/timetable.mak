<table border="1" style="width: 100%;">
<tr>
    <th>lp.</th>
    <th>poniedziałek</th>
    <th>wtorek</th>
    <th>środa</th>
    <th>czwartek</th>
    <th>piątek</th>
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