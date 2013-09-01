# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html lang="${lang}" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>${title} - ${subtitle}</title>
		<meta name="keywords" content="${keywords}" />
		<meta name="author" content="${author}" />
		<link rel="stylesheet" type="text/css" href="//cdnjs.cloudflare.com/ajax/libs/normalize/2.1.0/normalize.css" />
		<script src="//cdnjs.cloudflare.com/ajax/libs/modernizr/2.6.2/modernizr.min.js"></script>
		<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
		<script src="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
		<script type='text/javascript' src='/assets/raptor/default.js'></script>
      <script type='text/javascript' src='/assets/raptor/tags.js'></script>
		<link rel="stylesheet" type="text/css" href="/assets/raptor/raptor-front-end.min.css" />
		<link rel="stylesheet" type="text/css" href="/assets/raptor/theme.css" />
		<link rel="stylesheet" type="text/css" href="/assets/raptor/theme-icons.css" />
		<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">
		<style type="text/css">
		${css_data | n}
		</style>
	</head>
	<body>
		<div class="container">
		<!--
			<div class="codrops-top clearfix">
				<a class="codrops-icon codrops-icon-prev" href=""><span>Wstecz</span></a>
			</div>
		-->
			<header>
				<h1 id="title">${title}<span>${subtitle}</span></h1>
				<h2><span>Dodano: <abbr class="timeago" title="${date}">${date}</abbr> Autor: ${author}</span></h1>
			</header>
			<section id="text">
				${content | n}
			</section>
			<!--
			<div class="component">
				<button class="cn-button" id="cn-button">+</button>
				<div class="cn-wrapper" id="cn-wrapper">
				    <ul>
				      <li><a href="#" id="link-home"><span class="icon-home"></span></a></li>
				      <li><a href="#" id="link-download"><span class="icon-download-alt"></span></a></li>
				      <li><a href="#" id="link-list"><span class="icon-list"></span></a></li>
				      <li><a href="#" id="link-love"><span class="icon-heart-empty"></span></a></li>
				      <li><a href="#" id="link-flag"><span class="icon-flag"></span></a></li>
				     </ul>
				</div>
				<div id="cn-overlay" class="cn-overlay"></div>
			</div>
			-->
		</div>
		<script type="text/javascript">
		$(document).ready(function(){
			$.scrollUp({scrollText: 'Przewiń do góry'});
		  	jQuery("abbr.timeago").timeago();
			$(".diagram").sequenceDiagram({theme: 'hand'});
		});
		</script>
		<script src="/static/js/content.js"></script>
		<script src="/assets/raphael/raphael-min.js"></script>
		<script src="/assets/jquery.browser/jquery.browser.js"></script>
		<script src="//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.1/underscore-min.js"></script>
		<script src="//cdnjs.cloudflare.com/ajax/libs/js-sequence-diagrams/1.0.4/sequence-diagram-min.js"></script>
		<script src="//cdnjs.cloudflare.com/ajax/libs/fitvids/1.0.1/jquery.fitvids.min.js"></script>
		<script src="//cdnjs.cloudflare.com/ajax/libs/noisy/1.1.1/jquery.noisy.min.js"></script>
	</body>
</html>