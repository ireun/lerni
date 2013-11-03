<html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>
                SIS | System Informacyjny Staszica
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
                    Ostatnia aktualizacja planu: ${last_update} |
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
        <h2>System Informacyjny Staszica <span class="beta">beta</span></h2>
        <!--
        <h3><a href="/now">Now! <span class="beta">beta</span></a></h3>
        <p>
            System do wyszukiwania uczniów oraz nauczycieli w czasie
            rzeczywistym.
        </p>
        -->
        <h3><a href="/schedule">Plan</a></h3>
        <p>
            Czyli wszystko co związane z planem zajęć lekcyjnych -
            dla ucznia i dla nauczyciela!
        </p>
        <h3><a href="/lucky">Szczęśliwy numerek</a></h3>
        <p>
            Sprawdź aktualny szczęśliwy numerek, a także numerki na ten,
            czy na przyszły tydzień. W razie wątpliwości co do częstości
            występowania danego numerka zawsze możesz sprawdzić nasze
            <a href="/lucky/all">archiwum</a>.
        </p>
        <h3><a href="/about">About</a></h3>
        <p>Jeśli chcesz wiedzieć więcej...</p>
            </div>
        </body>
</html>