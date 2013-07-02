<%include file="top.mak"/>
    <div id="main_page">
        <div id="left"> 
            <div id="nav">
                <ul>
                    % for row in menu_left_list:
                    <li><a href="${row[0]}" id="homenav">${row[1]}</a></li>
				    % endfor
                </ul>
            </div>
        </div>
        <div id="center" style="width:820px;">
            <div class='picasagallery'></div>
        </div>
    </div>
    <script>
    $(document).ready( function() {
    $('.picasagallery').picasagallery( {username:'117504295881600872844'} );
    } );
    </script>
<%include file="bottom.mak"/>