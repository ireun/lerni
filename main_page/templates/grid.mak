<%include file="top_new.mak"/>
<%include file="snippets/header.mak"/>
<div >
	<div id="main" class="container-wrapper">
		%for box in boxes:
		<div>
			<a href="${box[1]}" class="athumbnail">
				<img data-src="holder.js/300x200/text:${box[0]}" alt="">
			</a>
		</div>
		%endfor
	</div>		
</div>


<style type="text/css">
.container-wrapper {text-align: center;}
#main div {margin: 0 auto;display: inline-block;}
.athumbnail {display: block;padding: 20px;line-height: 20px;}
.owl-pagination {top: -40px;}
</style>
<%include file="bottom_new.mak"/>