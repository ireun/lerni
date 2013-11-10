<%include file="top_new.mak"/>
<%include file="snippets/header.mak"/>
<div id="main" class="container">
	<div id="inner-wrapper" class="container">
        <div class="settings_header">Temat rozmowy: ${ticket_id}</div>
        <table width="100%" cellspacing="0" cellpadding="4" border="0">
            <tbody>
                % for x in messages:
                <tr>
                    <td width="25%">${x[0]}</td>
                    <td width="75%">
                        <div class="timeago" title="${x[1]}"></div>
                        ${x[2]}
                    </td>
                </tr>
                % endfor
            </tbody>
        </table><br></br>
        <form class="grid-form" action="" method="post">
            <fieldset>
                <div data-row-span="1">
                    <div data-field-span="1">
                        <label>Odpowiedz</label>
                        <textarea style="resize: vertical;" name="answer"></textarea>
                    </div>
                </div>
            </fieldset>
            <input type="submit" value="Wyślij" name="action">
        </form>
    </div>
</div>
<%include file="bottom_new.mak"/>