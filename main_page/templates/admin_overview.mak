<%include file="top_admin.mak"/>
<section id="main">
    <div class="navbar navbar-static-top">
        <div class="navbar-inner">
            <ul class="breadcrumb">
                <li><a href="#">Kokpit</a> <span class="divider"></span></li>
                <li class="active">Indeks</li>
            </ul>
        </div>
    </div>
    <div class="container">
        %for row in rows:
            %if row != []:
            <div class="row">
                %for widget in row:
                <div id="${widget[0]}" class="col-md-${widget[1]} ${widget[2]}" >
                    ${widget[3] | n}
                </div>
                %endfor
            </div>
            %endif
        %endfor
    </div></section></div>
<%include file="bottom_admin.mak"/>
