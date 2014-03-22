<header id="header" class="container hidden-xs">
<div id="owlCarousel" class="owl-carousel owl-theme hidden-phone">
        %for x in banners:
        <div class="item"><img src="${x[0]}" alt="${x[1]}"></div>
        %endfor
	</div>
</header>