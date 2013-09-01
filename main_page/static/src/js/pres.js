head.js(uiji,raptor,raptor2,raptor3,reveal,function(){
    enableRaptor=function () {
        raptor=$('.slides').raptor({
            autoEnable: true,
            unify: true,
            partialEdit: $('section').not(":has('section')"),
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
                        ['floatLeft', 'floatNone', 'floatRight'],
                        ['tableCreate', 'tableInsertRow', 'tableDeleteRow', 'tableInsertColumn', 'tableDeleteColumn'],
                        ['guides','viewSource'],
                        ['slideRemove','slideAdd']
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
        /*s=document.createElement('script');s.type='text/javascript';document.body.appendChild(s);s.src='//hi.kickassapp.com/kickass.js';*/
    };


    if ($('.slides').raptor) {
    Raptor.registerUi(new Raptor.Button({
        name: 'slideAdd',
        init: function() {
            var button = Raptor.Button.prototype.init.apply(this, arguments);
            button.find('.ui-button-icon-primary').css({'background':'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QgQEgIPvzaxAgAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAABeSURBVDjLY2DAAdjY2KTY2Nj+Q7EULnVMDLhBDA420QYQBYaBASzQEMYWSPbIbDY2Nmz6lzCysbH9H1gvMDAwSOPxgheUvY2BgeEgNi8w4EmJZUgpsWw0IZEBiM3OAAMmDuSrNmxAAAAAAElFTkSuQmCC)'});
            return button;
        },
        action: function() { $('.present').after( "<section contenteditable='true'>Nowy slajd</section>"); }
    }));
    Raptor.registerUi(new Raptor.Button({
        name: 'slideRemove',
        init: function() {
            var button = Raptor.Button.prototype.init.apply(this, arguments);
            button.find('.ui-button-icon-primary').css({'background':'url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3QgQEgkg9xNVkAAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAAAySURBVDjLY2AYBQMPGNnY2KQYGBhiyNS/hJGNje0/JS5gotQLLAwMDNKUeGE0FQwGAAAYLgNhYgXyRAAAAABJRU5ErkJggg==)'});
            return button;
        },
        action: function() { Reveal.prev(); Reveal.getPreviousSlide().remove(); }
    }));
    enableRaptor();
    setInterval(function() { Reveal.layout();}, 500);
    $('head').append('<style> .past{display: hidden; !important} .spacer {display: none !important;} .raptor-ui-tag-menu{width: 140px !important;}</style>');
    $('.navigate-right').click(function () {console.log("LOOOKL");});
    }

                Reveal.initialize({
                    center: true,
                    // rtl: true,
                    transition: 'linear'
                    // transitionSpeed: 'slow',
                    // backgroundTransition: 'linear'
                });



});