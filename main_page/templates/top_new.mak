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
    <link href="//netdna.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <link type='text/css' rel='stylesheet' href='/static/libs/raptor/raptor.min.css'/>
    <link type='text/css' rel='stylesheet' href='/static/libs/raptor/raptor-front-end.min.css'/>

    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.1.1/js/bootstrap.min.js"></script>
    <script>
    var bootstrapButton = $.fn.button.noConflict()
    $.fn.bootstrapBtn = bootstrapButton;
    </script>
    <!-- Load Jquery first to allow raptor-editor to work -->
    <script src="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
    <script src="/static/libs/raptor/raptor.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/headjs/0.99/head.min.js"></script>
    <script src="/static/js/libs.min.js"></script>
    <script src="/static/js/main.min.js"></script>
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
    <link href="/static/css/base.min.css" rel="stylesheet">
</head>
<body ng-controller="LerniCtrl">
<div id="wrapper">
    <section id="chat" class="panel panel-primary" style="width: 400px;background: #FFF; position: fixed; bottom: -23px; right: 20px; overflow: hidden;">
        <header class="panel-heading top-bar">
            <i class="fa fa-comment"></i>
            Live Chat
            <i class="fa fa-minus pull-right"></i>
        </header>
        <div class="panel-body" style="padding: 6px;" ng-show="username == ''">
            <h3 style="text-align: center;">
            Wybierz swój pseudonim i kliknij<br>"Dołącz do chatu".<br>
            <br>
            <input type="text" ng-model="chat_choose_nick" placeholder="Twój pseudonim"></input>
            </h3>
            <button class="btn btn-default" ng-click="setUsername()">Dołącz do chatu</button>
            <button class="btn btn-default disabled">Skontaktuj się z pomocą techniczną</button>
        </div>
        <div ng-show="username != ''">
            <ul class="nav nav-tabs" role="tablist">
                <li class="active"><a href="#chatroom" role="tab" data-toggle="tab">Chat</a></li>
                <li><a href="#users" role="tab" data-toggle="tab">Użytkownicy</a></li>
                <li><a href="#messages" role="tab" data-toggle="tab">PM</a></li>
                <li><a href="#settings" role="tab" data-toggle="tab">Ustawienia</a></li>
            </ul>
            <div class="tab-content">
                <div class="tab-pane active" id="chatroom">
                    <ol class="conversation" style="height: 320px; overflow-y: scroll;">
                        <li ng-repeat="message in messages">
                            <div class="user">
                                <p>{{message.user}}</p>
                            </div>
                            <div class="message" >
                            <p>{{message.text}}</p>
                            </div>
                        <li>
                    </ol>
                    <input type="text" ui-keypress="{13:'keypressCallback($event)'}" ng-model="chat_message"></input>
                </div>
                <div class="tab-pane" id="users">
                    <ol class="user_list" style="height: 320px; overflow-y: scroll;">
                        <li class="{{member.type}}" ng-repeat="member in members">
                            {{member.nick}}
                        </li>
                    </ol>
                </div>
                <div class="tab-pane" id="messages">Work in progress ;)</div>
                <div class="tab-pane" id="settings">...</div>
            </div>
        </div>
    </section>
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
                            <li style="font-size: 22px;"><a href="/admin" class="fa fa-cog"></a></li>
                        </ul>
                    </div>
                %endif
            </div>
            <!--/.nav-collapse -->
        </div>
    </div>