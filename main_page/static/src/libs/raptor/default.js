/**
 * Select anchors with URI's beginning with the current location.pathname and
 * call the highlighter function with these anchors as the argument.
 *
 * @param  {string} selector A selector for an element containing anchors.
 * @param  {Function} highlighter A function that is passed matches.
 */
var highlightCurrentItem = function(selector, highlighter, exactMatchesOnly) {
    if (location.pathname === '/') {
        return highlighter($(selector + ' > a[href="/"]'));
    }
    if (exactMatchesOnly) {
        return highlighter($(selector + ' > a[href="' + location.pathname + '"]'));
    }
    return highlighter($(selector + ' > a').filter(function() {
        if (this.getAttribute('href', 2) === '/') return false;
        return (new RegExp('^' + this.getAttribute('href', 2))).test(location.pathname);
    }));
};
