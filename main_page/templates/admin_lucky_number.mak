<%include file="top.mak"/>

<div id="main_page">
    <div id="left"> 
        <div id="nav">
            <ul>
            % for row in menu_left_list:
                <li><a href="${row[0]}" class="indent${row[2]}, current" id="homenav">${row[1]}</a></li>
            % endfor
            </ul>
        </div>
    </div>
    <div id="center">
        Tutaj bd jakieś informacje ogólne (ilość odwiedziń, statystyki jakieś)</br>
        Narazie wybierz co chcesz zrobić z menu po lewej.
    </div>
</div>	

<%include file="bottom.mak"/>
