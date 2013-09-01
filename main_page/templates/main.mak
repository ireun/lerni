<%include file="top_new.mak"/>
<header id="header" class="container-wrapper">
	<div id="owlCarousel" class="owl-carousel owl-theme hidden-phone">
        %for x in banners:
        <div class="item"><img src="${x[0]}" alt="${x[1]}"></div>
        %endfor
	</div>
</header>
<div id="main" class="container-wrapper">
	<div id="inner-wrapper" class="container">
		<div class="row-fluid">
			<div class="span8" id="last_news">
				<div class="title" >Ostatnie newsy</div>
				%for x in news:
				<div class="article">
				    <div class="author">${x[0]}</div> <div class="timeago" title="${x[1]}"></div> <br>
				    <div class="content">${x[2]}
                    <a href="${x[3]}">${x[4]}</a>
                    </div>
				</div>
				%endfor
			</div>
			<div class="span4" id="best_content">
				<div class="title">Najlepsze treści</div>
			</div>
		</div>
		<div class="row-fluid">
			<div class="span4" id="upcoming_events">
		  		<div class="title">Nadchodzące wydarzenia</div>
			</div>
		  	<div class="span4" id="our_successes">
				<div class="title">Nasze sukcesy</div>
				%for x in successes:
				<div class="article">
				    <div class="author">${x[0]}</div> <div class="timeago" title="${x[1]}"></div> <br>
				    <div class="content">${x[2]}</div>
				</div>
				%endfor
		  	</div>
		  	<div class="span4" id="last_galleries">
				<div class="title">Ostatnio dodadne galerie</div>
				<div class="thumbs"> </div>
		  	</div>
		</div>
        %for row in rows:
		<div class="row-fluid">
            %for widget in row:
			<div class="${widget[4]}" id="${widget[1]}" class="${widget[2]}">
				<div class="title">${widget[0]}</div>
                ${widget[3] | n}
			</div>
            %endfor
    	</div>
        %endfor
  </div>
</div>
<%include file="bottom_new.mak"/>