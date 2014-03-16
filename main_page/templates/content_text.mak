<%include file="top_new.mak"/>
<link href="/static/libs/socialcount/socialcount.min.css" rel="stylesheet">
<link href="/static/libs/socialcount/socialcount-icons.min.css" rel="stylesheet">
<link href="/static/css/social.min.css" rel="stylesheet">
<link href="/static/css/entries.min.css" rel="stylesheet">
<!---
<script src="/static/js/content.min.js"></script>
<link href="/static/css/content.min.css" rel="stylesheet">
<link href="/static/css/entries.min.css" rel="stylesheet">

{title} - {subtitle}</title>
<meta name="description" content="">
<meta name="keywords" content="{keywords}" />
<meta name="author" content="{author}" />
-->
<header id="header" class="container">
    <div class="container">
        <h1 id="title">${title}<span>${subtitle}</span></h1>
        <h2><span>
            % if date:
                Dodano: <abbr class="timeago" title="${date}">${date}</abbr>
            % endif
            %if author:
                Autor: ${author}
            %endif
            %if time:
                <br /> Przewidywany czas czytania: ${time} min.
            %endif
        </span></h2>
        <a class="pull-left header-nav" href="${back}">Wstecz</a>
        <a class="pull-right header-nav" href="?edit">Edytuj</a>
    </div>
</header>
<div id="main" class="container">
    <div style="height: 30px;"></div>
	<div id="inner-wrapper" class="container">
        <div class="row">
<!--
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
-->
        <div class="row">
            <section id="text" class="col-md-12">
                ${content | n}
            </section>
        </div>
    </div></div>
</div>
<%include file="bottom_new.mak"/>