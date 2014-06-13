<!DOCTYPE html>

<html lang="en">
<head>
    <title>ZSO nr 15 w Sosnowcu</title>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">
    <meta content="" name="description">
    <link href="/assets/ico/apple-touch-icon-144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144">
    <link href="/assets/ico/apple-touch-icon-114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114">
    <link href="/assets/ico/apple-touch-icon-72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72">
    <link href="/assets/ico/apple-touch-icon-57-precomposed.png" rel="apple-touch-icon-precomposed">
    <link href="/assets/ico/favicon.png" rel="shortcut icon">
    <link href="//cdnjs.cloudflare.com/ajax/libs/normalize/2.1.0/normalize.css" rel="stylesheet" type="text/css">
    <link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="/static/libs/fotorama/fotorama_style.min.css" rel="stylesheet">
    <link href="//cdnjs.cloudflare.com/ajax/libs/fotorama/4.5.1/fotorama.css" rel="stylesheet">
    <style>
    .body-wrap{padding: 0 16px 0 16px;}
    </style>
</head>

<body class="frontpage" id="root">
    <div class="header-wrap">
        <div class="header">
            <ul class="menu">
                <li class="li logo"><span><strong>${page_title}</strong></span></li>

                    <li class="li visited"><a class="no-u" href="/about">Szkoła</a></li>
                    <li class="li visited"><a class="no-u" href="/education">Edukacja</a></li>
                    <li class="li visited"><a class="no-u" href="/competitions">Konkursy</a></li>
                    <li class="li visited"><a class="no-u" href="/student_zone">Strefa ucznia</a></li>
                    <li class="li visited"><a class="no-u" href="/support">Support</a></li>
                    %if not logged_in:
                        <li class="li visited"><a href="/login">Login</a></li>
                    %endif
            </ul>

            <p class="lead">Witamy w galerii.</p>
        </div>
    </div>

    <div class="body-wrap">
        <div class="fotorama-wrap-frontpage noise">
            <div class="fotorama" data-height="100%" data-keyboard="true" data-nav="thumbs" data-width="100%">
                % for image in images:
                    <a href="${image['Original']}"><img src="${image['Square']}"></a>
                % endfor
            </div>
        </div>
        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/fotorama/4.5.1/fotorama.js"></script>
    </div>
</body>
</html>