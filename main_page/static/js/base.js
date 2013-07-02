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
    $('.slider').unslider({speed: 500, delay: 3000, complete: function() {}, dots: true});      
    $("#example2").nested({minWidth: 100, gutter: 10});
    updateContainer();
    $(window).resize(function() {
	   updateContainer();
    });    
});
function updateContainer() {
     $('#slider').css('max-height', $('#logo').height());
     $('#slider').css('min-height', $('#logo').height());
};