<%include file="top.mak"/>

<div id="main_page">
    <div id="left"> 
        <div id="nav">
            <ul>
            % for row in menu_left_list:
                <li><a href="${row[0]}" class="indent${row[2]}, current" id="homenav">${row[1]}</a></li>
            % endfor
            </ul>
        </div>
    </div>
    <div id="center">        
        <div id="browser-warning">
            Wygląda na to, że twoja przeglądarka nie spełnia minimalnych wymagań sprzętowych, lub masz wyłączoną obsługę javascriptu.
            <br>Jeśli możesz uaktualnij przeglądarkę. Polecam <a href="http://www.google.com/intl/en/chrome/">Chrome</a> lub <a href="http://www.mozilla.org/en-US/firefox/new/">Firefox</a> :)
        </div>
        
        <input type="file" id="filepicker-input" multiple="true"/>  	
        <span id="direct-upload-text">Dodaj pliki do wysłania.</span>   
        <div id="preview">
            <ul id="dropped-files">			
            </ul>
            <!--see button.css-->
            <center><a id="uploadbutton" class="large button green">Start Upload</a><center>
            <img id="ajax-loader" src="/static/ajax-loader.gif" alt=""/>
        
        </div>
        
        <script src="/static/jsUpload.js"></script>
        <script src="/static/main.js"></script>
        <link rel="stylesheet" href="/static/jquery-ui-1.8.19.custom.css" type="text/css" />
        <link rel="stylesheet" href="/static/main.css" type="text/css" />
        <script src="/static/jquery-ui-1.8.19.custom.min.js"></script>
        
        
        
        <div id="drop-box-overlay">
        <h1>Drop files anywhere to upload...</h1>
        </div>
     </div>
</div>	

<%include file="bottom.mak"/>
