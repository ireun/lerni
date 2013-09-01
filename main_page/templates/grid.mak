<%include file="top_new.mak"/>
<header id="header" class="container-wrapper">
	<div id="owlCarousel" class="owl-carousel owl-theme hidden-phone">
        %for x in banners:
        <div class="item"><img src="${x[0]}" alt="${x[1]}"></div>
        %endfor
	</div>
</header>
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