
<html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <title>
                SIS | Plan lekcji
            </title>
            <link rel="stylesheet" type="text/css" href="//sis.staszic.edu.pl/base.css" />
            <link rel="stylesheet" type="text/css" href="//sis.staszic.edu.pl/beta.css" />
        </head>
        <body>
            <div id="header">
                <h1>
                    <a href="/">System Informacyjny Staszica</a> <span class="beta">beta</span>
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
                    <li><a href="/">Home</a></li>
                    <li><a href="/now">Now!</a></li>
                    <li><a href="/schedule">Plan</a></li>
                    <li><a href="/lucky">Szczęśliwy numerek</a></li>
                    <li><a href="http://www.staszic.edu.pl/zastepstwa/">Zastępstwa</a></li>
                    <li><a href="/about">About</a></li>
                </ul>
            </div>
            <div id="content">
        <h2>Plan lekcji</h2>
                <!--
        <h3>
            <a href="/schedule/teachers">
                Pełny plan lekcji dla nauczycieli
            </a>
        </h3>
        <h3>
            <a href="/schedule/groups">
                Pełny plan lekcji dla klas
            </a>
        </h3>
        -->
        <h3>Plan lekcji dla klasy</h3>
        <form method="post">
            <select name="group_name">
                % for x in groups:
                    <option value="${x}">${x}</option>
                % endfor
            </select>
            <input type="submit" value="Pokaż" />
        </form>
        <!--
        <h3>Plan lekcji dla ucznia</h3>
        <form>
            <ol>
                <li>
                    <label for="group_name">Wybierz klasę</label>
                    <select id="group_name" name="group_name">
                        % for x in groups:
                            <option value="${x}">${x}</option>
                        % endfor
                    </select>
                </li>
                <li>
                    <label for="course_name">Wybierz lektorat</label>
                    <select id="course_name" name="course_name">
                        % for x in groups:
                            <option value="${x}">${x}</option>
                        % endfor
                    </select>
                </li>
                <li>
                    <input type="submit" value="Pokaż plan!" />
                </li>
            </ol>
        </form>
        -->
        <h3>Plan lekcji dla nauczyciela</h3>
        <form method="post">
            <select name="teacher_last_name">
                % for x in teachers:
                    <option value="${x}">${x}</option>
                % endfor
            </select>
            <input type="submit" value="Pokaż" />
        </form>
            </div>
        </body>
</html>