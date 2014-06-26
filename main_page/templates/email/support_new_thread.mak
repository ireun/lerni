<%include file='email_top.mak'/>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
    <tr>
        <td style="color: #153643; font-family: Arial, sans-serif; font-size: 24px;">
            <b>Witaj, ${email_name}!</b>
        </td>
    </tr>
    <tr>
        <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;">
            Dziękujemy za zgłoszenie problemu do naszego działu supportu.<br/>
            Aby potwierdzić swoją tożsamość kliknij poniższy odsyłacz:<br/>
            <a href="${confirmation_link}">${confirmation_link}</a><br/>
            <br/>
            Treść pytania:
            <div style="padding: 10px; background: #DDD;">${question}</div>
            <br/>
            Jeśli nie ty jesteś autorem tego pytania prosimy zignorować tę wiadomość.<br/>
            <br/>
            ${signature| n}
        </td>
    </tr>
</table>
<%include file='email_bottom.mak'/>
