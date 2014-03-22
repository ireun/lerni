<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>ZSO nr 15 w Sosnowcu</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="Kamil Danak">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/assets/ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/assets/ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/assets/ico/apple-touch-icon-57-precomposed.png">
    <link rel="shortcut icon" href="/assets/ico/favicon.png">
    <link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/normalize/2.1.0/normalize.css"/>
    <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
    <script src="//cdnjs.cloudflare.com/ajax/libs/headjs/0.99/head.min.js"></script>
    <script src="/static/js/libs.min.js"></script>
    <script src="/static/js/main.min.js"></script>
    <link href="/static/css/base.min.css" rel="stylesheet">
    <link href="/static/libs/bootstrap/bootstrap.min.css" rel="stylesheet">
    <link href="/static/libs/typeahead/typeahead.js-bootstrap.min.css" rel="stylesheet">
    <link href="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/css/base/jquery.ui.all.min.css" rel="stylesheet">
    <link href="/static/libs/jtable/themes/staszic/jtable_staszic_base.min.css" rel="stylesheet">
    <link href="/static/libs/jtable/themes/staszic/lightgray/jtable.min.css" rel="stylesheet">
    <link href="/static/libs/owl-carousel/owl.carousel.min.css" rel="stylesheet">
    <link href="/static/libs/owl-carousel/owl.theme.min.css" rel="stylesheet">
    <link href="/static/libs/progression/progression.min.css" rel="stylesheet">
    <link href="/static/libs/gridforms/gridforms.min.css" rel="stylesheet">
    <link href="/static/libs/footable/footable.core.min.css" rel="stylesheet">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/leaflet/0.6.4/leaflet.css" type="text/css"/>
</head>
<body>
<div id="wrapper">
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/">${page_title}</a>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/about">Szkoła</a></li>
                    <li><a href="/education">Edukacja</a></li>
                    <li><a href="/competitions">Konkursy</a></li>
                    <li><a href="/student_zone">Strefa ucznia</a></li>
                    <li><a href="/support">Support</a></li>
                    %if not logged_in:
                        <li><a href="/login">Login</a></li>
                    %endif
                </ul>
                %if logged_in:
                    <div class="pull-right">
                        <ul class="nav navbar-nav">
                            <li><a href="/logout">Wyloguj</a></li>
                            <li style="font-size: 22px;"><a href="/admin" class="icon-cog"></a></li>
                        </ul>
                    </div>
                %endif
            </div>
            <!--/.nav-collapse -->
        </div>
    </div>