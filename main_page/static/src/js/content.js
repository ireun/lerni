/*scroll_up_js, owl_js, social_js, diagrams,*/
head.js(jquery, jquery_browser, noisy, function () {
	$('body').noisy({'intensity' : 1,'size' : 200,'opacity' : 0.08,'fallback' : '','monochrome' : false})
});
head.js(jquery, fit_vids, function() { $(".video").fitVids() });
head.js(social_count);
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
head.js(holder);

head.js(jquery, jquery_ui, raptor, function(){
    if ($('.reveal').raptor) {
    $('.reveal').raptor({
        autoEnable: true,
        partialEdit: $('.slides section'),
        layouts: {
           toolbar: {
              uiOrder: [
                    ['historyUndo', 'historyRedo','cancel','save'],
                    ['tagMenu','classMenu','alignLeft', 'alignCenter', 'alignJustify', 'alignRight','textBold', 'textItalic', 'textUnderline', 'textStrike'],
                    ['textSuper', 'textSub'],
                    ['colorMenuBasic'],
                    ['snippetMenu', 'specialCharacters'],
                    ['listUnordered', 'listOrdered'],
                    ['hrCreate', 'textBlockQuote'],
                    ['textSizeDecrease', 'textSizeIncrease'],
                    ['clearFormatting'],
                    ['floatLeft', 'floatNone', 'floatRight'],
                    ['tableCreate', 'tableInsertRow', 'tableDeleteRow', 'tableInsertColumn', 'tableDeleteColumn'],
                    ['guides','viewSource']
              ]
           },
           hoverPanel: {
              uiOrder: [['clickButtonToEdit']]
           },
           messages: {}
        },
        enablePlugins: true,
        reloadOnDisable: true,
        plugins:{
            dock: { docked: true, dockToScreen: true,persist: false},
            save: { plugin: 'saveJson'},
            saveJson: {url: '/entry/save', postName: 'raptor-content', id: function() { return 1} },
            textBlockQuote: false,
            classMenu: { classes: {'Lol':'lol'} }
        }
    });
    };

    /*!
     * classie - class helper functions
     * from bonzo https://github.com/ded/bonzo
     *
     * classie.has( elem, 'my-class' ) -> true/false
     * classie.add( elem, 'my-new-class' )
     * classie.remove( elem, 'my-unwanted-class' )
     * classie.toggle( elem, 'my-class' )
     */

    /*jshint browser: true, strict: true, undef: true */
    /*global define: false */

    ( function( window ) {

    'use strict';

    // class helper functions from bonzo https://github.com/ded/bonzo

    function classReg( className ) {
      return new RegExp("(^|\\s+)" + className + "(\\s+|$)");
    }

    // classList support for class management
    // altho to be fair, the api sucks because it won't accept multiple classes at once
    var hasClass, addClass, removeClass;

    if ( 'classList' in document.documentElement ) {
      hasClass = function( elem, c ) {
        return elem.classList.contains( c );
      };
      addClass = function( elem, c ) {
        elem.classList.add( c );
      };
      removeClass = function( elem, c ) {
        elem.classList.remove( c );
      };
    }
    else {
      hasClass = function( elem, c ) {
        return classReg( c ).test( elem.className );
      };
      addClass = function( elem, c ) {
        if ( !hasClass( elem, c ) ) {
          elem.className = elem.className + ' ' + c;
        }
      };
      removeClass = function( elem, c ) {
        elem.className = elem.className.replace( classReg( c ), ' ' );
      };
    }

    function toggleClass( elem, c ) {
      var fn = hasClass( elem, c ) ? removeClass : addClass;
      fn( elem, c );
    }

    var classie = {
      // full names
      hasClass: hasClass,
      addClass: addClass,
      removeClass: removeClass,
      toggleClass: toggleClass,
      // short names
      has: hasClass,
      add: addClass,
      remove: removeClass,
      toggle: toggleClass
    };

    // transport
    if ( typeof define === 'function' && define.amd ) {
      // AMD
      define( classie );
    } else {
      // browser global
      window.classie = classie;
    }

    })( window );
    // EventListener | @jon_neal | //github.com/jonathantneal/EventListener
    !window.addEventListener && window.Element && (function () {
        function addToPrototype(name, method) {
            Window.prototype[name] = HTMLDocument.prototype[name] = Element.prototype[name] = method;
        }

        var registry = [];

        addToPrototype("addEventListener", function (type, listener) {
            var target = this;

            registry.unshift({
                __listener: function (event) {
                    event.currentTarget = target;
                    event.pageX = event.clientX + document.documentElement.scrollLeft;
                    event.pageY = event.clientY + document.documentElement.scrollTop;
                    event.preventDefault = function () { event.returnValue = false };
                    event.relatedTarget = event.fromElement || null;
                    event.stopPropagation = function () { event.cancelBubble = true };
                    event.relatedTarget = event.fromElement || null;
                    event.target = event.srcElement || target;
                    event.timeStamp = +new Date;

                    listener.call(target, event);
                },
                listener: listener,
                target: target,
                type: type
            });

            this.attachEvent("on" + type, registry[0].__listener);
        });

        addToPrototype("removeEventListener", function (type, listener) {
            for (var index = 0, length = registry.length; index < length; ++index) {
                if (registry[index].target == this && registry[index].type == type && registry[index].listener == listener) {
                    return this.detachEvent("on" + type, registry.splice(index, 1)[0].__listener);
                }
            }
        });

        addToPrototype("dispatchEvent", function (eventObject) {
            try {
                return this.fireEvent("on" + eventObject.type, eventObject);
            } catch (error) {
                for (var index = 0, length = registry.length; index < length; ++index) {
                    if (registry[index].target == this && registry[index].type == eventObject.type) {
                        registry[index].call(this, eventObject);
                    }
                }
            }
        });
    })();

    (function(){

        var button = document.getElementById('cn-button'),
        wrapper = document.getElementById('cn-wrapper'),
        overlay = document.getElementById('cn-overlay');

        //open and close menu when the button is clicked
        var open = false;
        button.addEventListener('click', handler, false);
        wrapper.addEventListener('click', cnhandle, false);

        function cnhandle(e){
            e.stopPropagation();
        }

        function handler(e){
            if (!e) var e = window.event;
            e.stopPropagation();//so that it doesn't trigger click event on document

            if(!open){
                openNav();
            }
            else{
                closeNav();
            }
        }
        function openNav(){
            open = true;
            button.innerHTML = "-";
            classie.add(overlay, 'on-overlay');
            classie.add(wrapper, 'opened-nav');
        }
        function closeNav(){
            open = false;
            button.innerHTML = "+";
            classie.remove(overlay, 'on-overlay');
            classie.remove(wrapper, 'opened-nav');
        }
        document.addEventListener('click', closeNav);

    })();




});