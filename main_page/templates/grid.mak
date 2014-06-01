<%include file="top_new.mak"/>
<%include file="snippets/header.mak"/>
<div id="main" class="container">
	<div id="inner-wrapper" class="container">
        <ul id="Grid">

		%for box in boxes:
		<li style="background: 'holder.js/275x275/text:${box[0]}'">
			<a href="${box[1]}" class="athumbnail">
			    %if box[2]:
			    <img src="${box[2]}" alt="">
			    %else:
				<img data-src="holder.js/410x305/text:Placeholder" alt="">
				%endif
                <div class="caption">
                <p>${box[0]}</p>
                </div>
			</a>
		</li>
		%endfor
		</ul>
	</div>		
</div>


<style type="text/css">
.container-wrapper {text-align: center;}
/*
.athumbnail {display: block;padding: 20px;line-height: 20px;}
*/
.owl-pagination {top: -40px;}
</style>
<%include file="bottom_new.mak"/>