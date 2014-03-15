head.js(jquery, autosize, function (){
   $(document).ready(function(){ $('textarea').autosize(); });
});


head.js(jquery, jflickrfeed, owl, function (){
    $(document).ready(function() {
      $("#owlCarousel").owlCarousel({
          navigation : false,
          slideSpeed : 300,
          paginationSpeed : 400,
          items : 1,
          itemsDesktop : false,
          itemsDesktopSmall : false,
          itemsTablet: false,
          itemsMobile : false
      });
    });

    var show_allert = function(message, type, allert_location){
    var noty2 = $('.custom_container').noty({text: message, type: type, layout: allert_location})
    };
    $(document).ready(function() {
        $('iframe[src*="about:blank"]').hide();
        $('.thumbs').jflickrfeed({
        limit: 4,
        qstrings: {
        id: '98176379@N02'
    },
    itemTemplate:
    '<div class="thumb" style="background-image: url({{image_b}});"></div>'
    });
    updateContainer();
    $(window).resize(function() {
        updateContainer();
    });
    });
    function updateContainer() {
        $('.thumbs').css('height', $('.thumbs').width());
        $('#events').css('height', $('#last-photos').height());
        $('#competitions').css('height', $('#last-photos').height());
    };
});
head.js(time_ago, function () {
  function numpf(n, s, t) {
    // s - 2-4, 22-24, 32-34 ...
    // t - 5-21, 25-31, ...
    var n10 = n % 10;
    if ( (n10 > 1) && (n10 < 5) && ( (n > 20) || (n < 10) ) ) {
      return s;
    } else {
      return t;
    }
  }
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
  };
  $(".timeago").timeago();
});
head.js(jquery, fit_vids, function() { $(".video").fitVids() });
head.js(holder);
/*
function flickr() {
http://api.flickr.com/services/rest/?method=flickr.collections.getTree&api_key=0b66eb5d7aff00167bcca14019c61c2c&user_id=98176379%40N02&format=json&auth_token=72157634444201156-090ad63f20af64af&api_sig=feb4198a3e78d4c513a01e5f5fec6c75
}
*/




