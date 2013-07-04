$(window).scroll(function()
{
    if($(window).scrollTop() == $(document).height() - $(window).height())
    {
        $('div#loadmoreajaxloader').show();
        $.ajax({
        url: "loadmore.php",
        success: function(html)
        {
            if(html)
            {
                $("#postswrapper").append(html);
                $('div#loadmoreajaxloader').hide();
            }else
            {
                $('div#loadmoreajaxloader').html('<center>No more posts to show.</center>');
            }
        }
        });
    }
});
$(document).ready(function() {
    jQuery("#logo #name").squishy({minSize: 6});
    jQuery("#logo #additional").squishy({minSize: 6});
    jQuery("#main .title").squishy({minSize: 6, maxSize: 20});
    $('.slider').unslider({speed: 500, delay: 3000, complete: function() {}, dots: true});      
    $("#example2").nested({minWidth: 100, gutter: 10});
    updateContainer();
    $(window).resize(function() {
	   updateContainer();
    });
    $('.thumbs').jflickrfeed({
    	limit: 4,
    	qstrings: {
    		id: '98176379@N02'
    	},
    	itemTemplate: 
    	'<div class="thumb" style="background-image: url({{image_b}});"></div>'
    });
    /*
                 <li class="span4">
                <a href="#" class="thumbnail">
                <img data-src="holder.js/300x200" alt="">
                </a>
                </li>
*/
          jQuery(".timeago").timeago();
		  jQuery.timeago.settings.strings = {
		    prefixAgo: null,
		    prefixFromNow: "za",
		    suffixAgo: "temu",
		    suffixFromNow: null,
		    seconds: "mniej niż minutę",
		    minute: "minutę",
		    minutes: function(value) { return numpf(value, "%d minuty", "%d minut"); },
		    hour: "godzinę",
		    hours: function(value) { return numpf(value, "%d godziny", "%d godzin"); },
		    day: "dzień",
		    days: "%d dni",
		    month: "miesiąc",
		    months: function(value) { return numpf(value, "%d miesiące", "%d miesięcy"); },
		    year: "rok",
		    years: function(value) { return numpf(value, "%d lata", "%d lat"); }
		  }
});
function updateContainer() {
     $('#slider').css('max-height', $('#logo').height());
     $('#slider').css('min-height', $('#logo').height());
     $('.thumbs').css('height', $('.thumbs').width());
     $('#events').css('height', $('#last-photos').height());
     $('#competitions').css('height', $('#last-photos').height());
};

/*
function flickr() {
http://api.flickr.com/services/rest/?method=flickr.collections.getTree&api_key=0b66eb5d7aff00167bcca14019c61c2c&user_id=98176379%40N02&format=json&auth_token=72157634444201156-090ad63f20af64af&api_sig=feb4198a3e78d4c513a01e5f5fec6c75
}
*/


// By Chris Coyier & tweaked by Mathias Bynens
$(function() {

	// Find all YouTube videos
	var $allVideos = $("iframe[src^='http://www.youtube.com']"),

	    // The element that is fluid width
	    $fluidEl = $("#video");

	// Figure out and save aspect ratio for each video
	$allVideos.each(function() {

		$(this)
			.data('aspectRatio', this.height / this.width)
			
			// and remove the hard coded width/height
			.removeAttr('height')
			.removeAttr('width');

	});

	// When the window is resized
	// (You'll probably want to debounce this)
	$(window).resize(function() {

		var newWidth = $fluidEl.width();
		
		// Resize all videos according to their own aspect ratio
		$allVideos.each(function() {

			var $el = $(this);
			$el
				.width(newWidth)
				.height(newWidth * $el.data('aspectRatio'));

		});

	// Kick off one resize to fix all videos on page load
	}).resize();

});