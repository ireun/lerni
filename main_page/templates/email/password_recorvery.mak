<%include file='email_top.mak'/>
<table border="0" cellpadding="0" cellspacing="0" width="100%">
    <tr>
        <td style="color: #153643; font-family: Arial, sans-serif; font-size: 24px;">
            <b>Witaj, ${email_name}!</b>
        </td>
    </tr>
    <tr>
        <td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;">
            Otrzymujesz tę wiadomość, ponieważ otrzymaliśmy prośbę o ustanowienie nowego hasła do Twojego konta Lerni.<br/>
            Jeśli prośba ta nie wyszła od Ciebie, możesz zignorować tę wiadomość (Twoje hasło pozostanie wtedy niezmienione).<br/>
            <br/>
            Aby ustanowić nowe hasło, kliknij poniższy odsyłacz:<br/>
            <br/>
            <a href="${recorvery_link}">${recorvery_link}</a><br/>
            <br/>
            Możesz w każdej chwili zmienić swoje hasło.<br/>
            W tym celu otwórz panel administracyjny Lerni, z listy „Moje Konto” wybierz opcję „Bezpieczeństwo”, po czym kliknij przycisk „Zmień hasło”.<br/>
            <br/>
            ${signature| n}
        </td>
    </tr>
</table>
<%include file='email_bottom.mak'/>
