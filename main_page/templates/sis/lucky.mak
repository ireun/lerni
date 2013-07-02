<html xmlns="http://www.w3.org/1999/xhtml">
    
        <head>
            <title>
                SIS | Szczęśliwy numerek
            </title>
            <link rel="stylesheet" type="text/css" href="/base.css" />
            <link rel="stylesheet" type="text/css" href="/beta.css" />
        </head>
        <body>
            <div id="header">
                <h1>
                    <a href="/">System Informacyjny Staszica</a> <span class="beta">beta</span>
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
                    <li><a href="/">Home</a></li>
                    <li><a href="/now">Now!</a></li>
                    <li><a href="/schedule">Plan</a></li>
                    <li><a href="/lucky">Szczęśliwy numerek</a></li>
                    <li><a href="http://www.staszic.edu.pl/zastepstwa/">Zastępstwa</a></li>
                    <li><a href="/about">About</a></li>
                </ul>
            </div>
            <div id="content">
        <h2>Szczęśliwy numerek</h2>
        <h3><a href="/lucky/current">
            Aktualny szczęśliwy numerek
        </a></h3>
    <div class="lucky_number">
        <div class="lucky_number_number">33</div>
        <div class="lucky_number_date">2013-06-06</div>
    </div>
        <h3><a href="/lucky/week">
            Szczęśliwe numerki na ten tydzień
        </a></h3>
                <ul>
                    <li>
                        2013-06-03 - <strong>36</strong>
                    </li><li>
                        2013-06-04 - <strong>30</strong>
                    </li><li>
                        2013-06-05 - <strong>34</strong>
                    </li><li>
                        2013-06-06 - <strong>33</strong>
                    </li><li>
                        2013-06-07 - <strong>16</strong>
                    </li>
                </ul>
        <h3><a href="/lucky/left">
            Pozostały do wylosowania
        </a></h3>
        <p>
            Poniżej znajduje się pełna lista wszystkich szcześliwych numerków,
            które pozostały jeszcze do wylosowania, tj. nie były one jeszcze
            użyte w obecnej turze.
        </p>
        <ul>
            <li>11</li><li>13</li><li>29</li><li>31</li>
        </ul>
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
            </div>
        </body>
</html>