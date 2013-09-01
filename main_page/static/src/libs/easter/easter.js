$(document).ready( function () {
     
    /**
    *   cul_easteregg 
    *   2012.04.05 markus gottschau www.crossundlecker.de
    *   update to jQuery 1.91 2013.03.18
    *
    *   feel free to filch the code, customize and publish it. 
    *   what the hell?! even the eggs (images) are totally free stuff! 
    *   THANK TO ARTILL for the great eggs: www.artill.de
    *
    **/
    console.log("INIT");
    cul_easteregg = {
            init:function(){
                // where can i hide the eggs and do they need to have background-color? 
                // ups, bgcolor-check not implemented yet... feel free to do it! 
                this.hideouttags = {
                        '.article': true,
                        '.thumb': true,
                        '#inner-wrapper': true,
                        '.row-fluid [class*="span"]': true
						
                };
                // skip some elems?
                this.skipids = ['wrapper, main, header, site-logo-shizzle'];
                this.skipclasses = '.line, .navbar';
                 
                 
                // pre-init hideouts;
                this.hideouts = new Array();                        
                // where do i have to go, when all eggs are found?
                this.yeah = 'yeah.html';
                // give me some eggs!
                this.pathtoeggs = '/static/libs/easter/img';
                this.eggs = ['egg_1.png','egg_2.png','egg_3.png','egg_4.png','egg_5.png','egg_6.png','egg_7.png','egg_8.png','egg_9.png','egg_10.png','egg_11.png','egg_12.png'];
                // how many eggs please?
                this.eggnum = 10; // 0 = hide everywhere! WOW!
                this.elementcount = 0;
                 
                // let the eggs look some px above the hiding-place oO 
                this.peepthroughleft = 30;
                this.peepthroughtop = 30;
                 
                this.found = 0;
                this.zindex = 0;
                this.maxrotate = 90;
                 
                 
                // the old this and that lovestory!
                that = this;
                 
                // lets go!
                this.parsedom();
                 
            },
            parsedom: function() {
                $.each(this.hideouttags, function (i,v) {
                 
                    $(i).each( function () {
                        if($.inArray($(this).attr('id'),that.skipids) != -1 || $(this).is(''+that.skipclasses+'')) {
                            //console.log('skip id:'+$(this).attr('id')+' | class:'+$(this).attr('class'));
                        } else {
                            that.hideouts.push($(this));
                            that.elementcount++;
                        }
                    });
                     
                });
                // turn around please, i will hide the eggs now.
                this.hidetheeggs();
            },
            hidetheeggs: function () {
                // shuffle and shake and shuffle the dom
                this.shuffle(this.hideouts);
                this.eggnum == 0 ? this.eggnum = this.elementcount : this.eggnum;
                this.eggnum > this.hideouts.length ? this.eggnum = this.hideouts.length : this.eggnum;
                 
                for (i = 0; i < this.eggnum; i++) {
                    o = this.hideouts[i];
                     
                    // hope, this is not radical? beware of offsets in your css!
                    if (o.css('position')=='static') {
                        o.css('position','relative');
                    }
                     
                    $('body').append('<div class="cul-easteregg" data-test="'+o.attr('id')+'" id="cul-easteregg-'+i+'"><img src="'+that.pathtoeggs+'/'+that.randomegg()+'" /></div>');
                     
                    if (o.css('z-index')=='auto') {
                        o.css('z-index',this.zindex +1);
                         
                    } else {
                        var zindex = o.css('z-index')-1;
                    }
                     
                    var offset = o.offset();
                    $('#cul-easteregg-'+i).css({
                            position: 'absolute',
                            top: (offset.top-this.peepthroughtop)+'px',
                            left: (offset.left-this.peepthroughleft)+'px',
                            zIndex: this.zindex
                        });
                    this.rotate($('#cul-easteregg-'+i), -(Math.floor(Math.random() * (this.maxrotate + 1))));
                     
                    this.zindex++;
                }
                 
                // add som eggtions :D brüller!
                this.addeggtions();
                 
            },
            addeggtions: function() {
                $('.cul-easteregg').on('mouseenter', function () {
                    $(this).css('zIndex',that.zindex+100);
                    $(this).removeClass('cul-easteregg').off();
                    $(this).fadeOut(200,function () {
                        that.found++;
                        $(this).html('<span class="yeah">Yeah '+that.found+' / '+that.eggnum+'</span>');
                        $(this).fadeIn(1, function () {
                            if (that.found == that.eggnum) {
                            alert('DAMN, you found all my eggs, killa! Redirecting you to: '+that.yeah);
                            window.location.href = that.yeah;
                            }
                        });
                    });
                });
                 
            },
            randomegg: function() {
                return this.eggs[Math.floor(Math.random() * this.eggs.length)];
            },
            rotate: function(e,degree) {
                //console.log(e.attr('id'));
                e.css({
                            '-webkit-transform': 'rotate(' + degree + 'deg)',
                            '-moz-transform': 'rotate(' + degree + 'deg)',
                            '-ms-transform': 'rotate(' + degree + 'deg)',
                            '-o-transform': 'rotate(' + degree + 'deg)',
                            'transform': 'rotate(' + degree + 'deg)',
                            'zoom': 1
                });
            },
            // thanks to css-tricks ( http://css-tricks.com/snippets/javascript/shuffle-array/ ) for shuffle and vardump. nice job!
            vardump: function(o) {
                for (var i=0;i<o.length;i++) {
                    console.log(o[i]);
                   }
            },
            shuffle: function(o) {
                for(var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
                return o;
            }
    }
    $(window).load(function(){  
        //initialize after placehold-images are loaded  
        cul_easteregg.init();
    });  
     
});