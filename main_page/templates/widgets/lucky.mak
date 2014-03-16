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