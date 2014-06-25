<script>
    var NWave = function () {
        this.css = function (p) {
            var path_len = $(document).width() - 300;
            var s = Math.abs(Math.sin(p * 60));
            var x = path_len - p * path_len;
            var y = s * 50 - 50;
            var o = 0;
            /*((s+2)/4+0.1)*/
            return {bottom: y + "px", left: x + "px", opacity: 1}
        }
    };
    var NWave2 = function () {
        this.css = function (p) {
            var path_len = $(document).width() - 300;
            var s = Math.abs(Math.sin(p * 60));
            var x = path_len - p * path_len;
            var y = s * 50 - 10;
            var o = 0;
            /*((s+2)/4+0.1)*/
            return {top: y + "px", right: x + "px", opacity: 1}
        }
    };

    head.js(jquery, ion_sound, jwerty, function () {
        $().ready(function () {
            (function ($) {
                $.path = {};
                $.fx.step.path = function (fx) {
                    var css = fx.end.css(1 - fx.pos);
                    if (css.bottom) {
                        fx.elem.style.bottom = css.bottom;
                    }
                    if (css.top) {
                        fx.elem.style.top = css.top;
                    }
                    if (css.right) {
                        fx.elem.style.right = css.right;
                    }
                    if (css.left) {
                        fx.elem.style.left = css.left;
                    }
                };
            })(jQuery);
            $.ionSound({sounds: ["rasputin"]});
            jwerty.key('↑,↑,↓,↓,←,→,←,→,B,A', function () {
                var natalia = $("#natalia");
                var natalia2 = $("#natalia2");
                natalia.width($(document).width() / 6);
                natalia2.width($(document).width() / 6);
                natalia.delay(200).show();
                natalia.delay(200).animate({path: new NWave}, 7800, "linear", function () {
                    natalia.hide();
                    natalia2.show();
                    natalia2.animate({path: new NWave2}, 8300, "linear", function () {
                        natalia2.hide()
                    });

                });
                $.ionSound.play("rasputin");
            });
        });
    });
</script>
<style>.natalia{z-index: 1020;}</style>
<img class="natalia" id="natalia" src="/static/images/natalia_poklonskaya.png" alt=""/>
<img class="natalia" id="natalia2" src="/static/images/natalia_poklonskaya2.png" alt=""/>