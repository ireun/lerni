<%include file="../top_new.mak"/>
<%include file="../snippets/header.mak"/>
<link rel="stylesheet" type="text/css" href="/static/libs/html5uploader/main.min.css" media="screen"/>

<div id="main" class="container">
	<div id="inner-wrapper" class="container">
        <div class="row">
            <div class="col-md-8">
                <h2>Upload dodatkowych plików.</h2>
                <h4>Podczas instalacji możesz chcieć wykorzystać poprzednią bazę danych.</br>
                Możesz ją przesłać <span id="direct-upload-text">tutaj.</span></h4>

                <div id="browser-warning">
                    Twoja przegladarka nie spełnia minimalnych wymagań.
                    <br>Spróbuj pobrać nową wersję
                    <a href="http://www.google.com/intl/en/chrome/">Chrome</a> lub
                    <a href="http://www.mozilla.org/en-US/firefox/new/">Firefox</a> :)
		        </div>
                <!--dierct upload input ("fakeinput")-->
                <input type="file" id="filepicker-input" multiple="true"/>
                <div id="preview">
                    <ul id="dropped-files">
                    </ul>

                    <!--see button.css-->
                    <center><a id="uploadbutton" class="large button green">Start Upload</a><center>
                    <img id="ajax-loader" src="/static/ajax-loader.gif" alt=""/>

                </div>
            <script src="//cdnjs.cloudflare.com/ajax/libs/jqueryui/1.10.3/jquery-ui.min.js"></script>
            <script src="/static/libs/html5uploader/jsUpload.min.js"></script>
            <script src="/static/libs/html5uploader/main.min.js"></script>
            </div>
            <div class="col-md-4">
                <h3>Postęp instalacji</h3>
                <ul class="list-group no-padding">
                    <a href="/install" class="list-group-item">Wymagania systemowe</a>
                    <a href="/install?s=1" class="list-group-item active">Upload dodatkowych plików</a>
                    <a class="list-group-item">Ustawienia bazy danych</a>
                    <a class="list-group-item">Porta ac consectetur ac</a>
                    <a class="list-group-item">Vestibulum at eros</a>
                </ul>

            </div>
        </div>

    </div>
</div>
<%include file="../bottom_new.mak"/>