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
        <div id="center" style="width:820px;" data-mercury="full">
            ${str(context.write(data))[0:0]}
        </div>
    </div>
<%include file="bottom.mak"/>