<html xmlns="http://www.w3.org/1999/xhtml">
    
        <head>
            <title>
                SIS | Szczęśliwy numerek
            </title>
            <link rel="stylesheet" type="text/css" href="/static/sis/base.min.css" />
            <link rel="stylesheet" type="text/css" href="/static/sis/beta.min.css" />
        </head>
        <body>
            <div id="header">
                <h1>
                    <a href="/sis">System Informacyjny Staszica</a> <span class="beta">beta</span>
                </h1>
                <div id="user-tools">
                    Ostatnia aktualizacja planu: 2013-05-26 |
                        <span>
                            <a href="/login">Zaloguj</a>
                        </span>
                </div>
            </div>
            <div id="menu">
                Menu:
                <ul>
                    <li><a href="/sis">Home</a></li>
                    <!--
                    <li><a href="/now">Now!</a></li>
                    -->
                    <li><a href="/sis/schedule">Plan</a></li>
                    <li><a href="/sis/lucky">Szczęśliwy numerek</a></li>
                    <li><a href="http://www.staszic.edu.pl/zastepstwa/">Zastępstwa</a></li>
                    <li><a href="/sis/about">About</a></li>
                </ul>
            </div>
            <div id="content">
        <h2>Szczęśliwy numerek</h2>
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
        <!--
        <h3><a href="/lucky/search">
            Szukaj szczęśliwego numerka
        </a></h3>
        <p>
            Wpisz tutaj numerek, by zobaczyć jego historię.
        </p>
        <form action="/lucky/search" method="POST">
            <input type="text" id="number" name="number" maxlength="2" size="2" value="0" />
            <input type="submit" value="Szukaj" />
        </form>
        <h3>
            <a href="/lucky/all">Archwium szczęśliwych numerków</a>
        </h3>
        -->
            </div>
        </body>
</html>
