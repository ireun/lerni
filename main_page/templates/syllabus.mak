<%include file="top_new.mak"/>
<link href="/static/css/entries.min.css" rel="stylesheet">
<header id="header" class="container">
    <div class="container">
        <h1 id="title">Syllabus</h1><h2><small>Program zajęć dydaktycznych<br/>IV LO im. Stanisława Staszica</small></h2>

        <a class="pull-left header-nav" href="${back}">Wstecz</a>
        %if logged_in:
            <a class="pull-right header-nav" href="?edit">Edytuj</a>
        %endif
    </div>
</header>
<div id="main" class="container">
	<div id="inner-wrapper" class="container" style="padding-top: 20px;">
        <div class="row">
            <div class="col-sm-4">
                <label for="school_year">Pierwszy rok szkolny nauki</label>
                <select class="form-control" id="school_year">
                <option>2014/2015</option>
                </select>
            </div>
            <div class="col-sm-8">
                <ul class="list-group">
                    %for profile in profiles:
                        <a href="${profile['path']}" class="list-group-item">
                        <h4 class="list-group-item-heading">${profile['name']}</h4>
                        %if profile['description']:
                            <p class="list-group-item-text">${profile['description']}</p>
                        %endif
                        </a>
                    %endfor
                </ul>
            </div>
        </div>
	</div>
</div>
<%include file="bottom_new.mak"/>