# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html lang="${lang}" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>${title} - ${subtitle}</title>
        <meta name="description" content="">
		<meta name="keywords" content="${keywords}" />
		<meta name="author" content="${author}" />
        <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css"  rel="stylesheet">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/assets/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/assets/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/assets/ico/apple-touch-icon-72-precomposed.png">
                      <link rel="apple-touch-icon-precomposed" href="/assets/ico/apple-touch-icon-57-precomposed.png">
                                     <link rel="shortcut icon" href="/assets/ico/favicon.png">
        <link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/normalize/2.1.0/normalize.css" />
        <link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">
        <script src="//cdnjs.cloudflare.com/ajax/libs/headjs/0.99/head.min.js"></script>
        <script src="/static/js/libs.min.js"></script>
        <script src="/static/js/content.min.js"></script>
        <link href="/static/css/content.min.css" rel="stylesheet">
        <link href="/static/css/entries.min.css" rel="stylesheet">

        <link href="/static/libs/socialcount/socialcount.min.css" rel="stylesheet">
        <link href="/static/libs/socialcount/socialcount-icons.min.css" rel="stylesheet">
        <link href="/static/css/social.min.css" rel="stylesheet">

      %if not editor:
		<%include file="snippets/mathjax.mak"/>
		%endif
		<style type="text/css">${css_data | n}</style>
	</head>
	<body>
		<div class="container">
			<div class="codrops-top clearfix">
				<a class="codrops-icon codrops-icon-prev" href="${back}"><span>Wstecz</span></a>
				<a class="pull-right" href="?edit"><span>Edytuj</span></a>
			</div>
			<header>
				<h1 id="title">${title}<span>${subtitle}</span></h1>
				<h2><span>
				%if date:
				Dodano: <abbr class="timeago" title="${date}">${date}</abbr>
				%endif
				%if author:
				Autor: ${author}
				%endif			
				</span></h2>
				<%include file="snippets/social.mak"/>
			</header>
			<section id="text">
				${content | n}
			</section>
			<div class="component">
				<button class="cn-button" id="cn-button">+</button>
				<div class="cn-wrapper" id="cn-wrapper">
				    <ul>				      
				      <li><a href="?download" id="link-download"><span class="icon-download-alt"></span></a></li>
				      <li><a href="#" id="link-edit"><span class="icon-comments"></span></a></li>
				      <li><a href="#" id="link-list"><span class="icon-list"></span></a></li>
				      <li><a href="#" id="link-love"><span class="icon-heart-empty"></span></a></li>
				      <li><a href="#" id="link-flag"><span class="icon-flag"></span></a></li>
				     </ul>
				</div>
				<div id="cn-overlay" class="cn-overlay"></div>
			</div>
		</div>
	</body>
</html>