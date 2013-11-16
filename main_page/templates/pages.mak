<%include file="top_new.mak"/>
<%include file="snippets/header.mak"/>
<div id="main" class="container">
	<div id="inner-wrapper" class="container">
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
  </div>
</div>
<%include file="bottom_new.mak"/>