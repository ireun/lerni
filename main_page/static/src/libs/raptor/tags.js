/**
 * Provides "All tags" hover behaviour & tag display
 */
$(function() {
    var supportsTouch = 'ontouchstart' in window || navigator.msMaxTouchPoints;
    // check if tags are longer than 1 line
    // constant of 38 could be replaced with the outerheight of .raptor-article-tags > div
    $('.raptor-tags-label-min').siblings('div').each(function() {
        if($(this).height() > 38) {
            // replace label with functional show/hide label
            $(this).siblings('.raptor-tags-label-min').replaceWith('<span class="raptor-tags-label">All Tags&hellip;</span>');
        }
        else {
            // offset padding for content:after (spaces label from tags)
            $(this).find('a:last-child').css('margin-right', '-82px');
        }
    });

    // show/hide hidden tags
    $('.raptor-tags-label').on('mouseenter touchstart', function() {

        // find container div
        var outerdiv = $(this).closest('.raptor-article-tags');

        // close function
        var closeTags = function() {
            // reset inline css, css transitions will run
            outerdiv.css('margin-top', '');
            outerdiv.css('height', '');

            // reset classes & events so 'show' functionality will run next time
            if (!supportsTouch) {
                outerdiv.removeClass('raptor-article-tags-open');
                outerdiv.unbind('mouseleave');
            }
        }

        // on touch, close the menu if it is currently open (dictated by is-touched class)
        if (supportsTouch && $(this).hasClass('is-touched')) {
            closeTags();
            $(this).toggleClass('is-touched');
            return;
        }

        //add close event if there is no touch support, signal css to hide label via classname
        if (!supportsTouch) {
            outerdiv.addClass('raptor-article-tags-open');
            outerdiv.mouseleave(closeTags);
        }

        // find div holding all tags
        var innerdiv = $(this).siblings('div');
        // find height of div holding all tags
        var innerheight = $(innerdiv).outerHeight() + parseInt($(innerdiv).css('margin-top'), 10) + parseInt($(innerdiv).css('margin-bottom'), 10);
        // find original height of tags when closed
        var originalheight = $(outerdiv).outerHeight();

        // Signal CSS transitions to fire by setting new values for margin & height
        outerdiv.css('margin-top', -1 * innerheight + originalheight + parseInt(outerdiv.css('margin-top'), 10) - 2);
        outerdiv.css('height', innerheight);

        // tell touch devices that the label has been touched or touched to open, or alternatively touched a second time to close it
        if (supportsTouch) {
            $(this).toggleClass('is-touched');
        }
    });

    // if touch is supported remove touch emulation of mouseenter event
    if (supportsTouch) {
        $('.raptor-tags-label').unbind('mouseenter');
    }

    // TO DO: jquery animations as fallbacks for css transitions in ie 8 & 9
});
