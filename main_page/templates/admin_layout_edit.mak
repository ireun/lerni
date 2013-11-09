<%include file="top_admin.mak"/>
<section id="main">
    <div class="navbar navbar-static-top">
        <div class="navbar-inner">
            <ul class="breadcrumb">
                <li><a href="#">Kokpit</a> <span class="divider"></span></li>
                <li class="active">Indeks</li>
            </ul>
            <div id="reportrange" class="pull-right hidden-phone">
                <span class="icon icon-calendar"></span>
                <span id="rangedate">June 7, 2013 - June 13, 2013</span><span class="caret"></span>
            </div>
        </div>
    </div>
    <div class="layouts_grid" id="layouts_grid">
        <ul>
            <li class="layout_block" data-col="1" data-id="7" data-row="1" data-sizex="1" data-sizey="1" style="background-color: #D24726; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">Logo</span>
                </div>
            </li>

            <li class="layout_block" data-col="2" data-id="2" data-row="1" data-sizex="5" data-sizey="1" style="background-color: #15992A; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">Ads top</span>
                </div>
            </li>

            <li class="layout_block" data-col="1" data-id="13" data-row="2" data-sizex="4" data-sizey="1" style="background-color: #B60000; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">Ads small</span>
                </div>
            </li>

            <li class="layout_block" data-col="5" data-id="5" data-row="2" data-sizex="2" data-sizey="3" style="background-color: #666666; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">Ads right</span>
                </div>
            </li>

            <li class="layout_block" data-col="1" data-id="1" data-row="3" data-sizex="4" data-sizey="2" style="background-color: #333333; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">Main</span>
                </div>
            </li>

            <li class="layout_block" data-col="1" data-id="6" data-row="5" data-sizex="4" data-sizey="3" style="background-color: #008299; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">User photos</span>
                </div>
            </li>

            <li class="layout_block" data-col="5" data-id="3" data-row="5" data-sizex="2" data-sizey="3" style="background-color: #008A00; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">Feed</span>
                </div>
            </li>

            <li class="layout_block" data-col="1" data-id="8" data-row="8" data-sizex="6" data-sizey="1" style="background-color: #FE7C22; position: absolute;">
                <div class="remove_element">
                    X
                </div>

                <div class="info">
                    <span class="block_name">Ads middle</span>
                </div>
            </li>
        </ul>
    </div>
    <style>
        .additional_element {
    margin: 5px;
    padding: 5px;
    color: white;
    cursor: pointer;
}

.grid_elements {
    width: 300px;
    float: left;
}
.grid_elements table {
    border-collapse: separate;
    width: 200px;
    height: 200px;
}
.actions_block {
    padding: 9px;
    float: right
}

.grid_elements table td {
    background-color: #CFCFCF;
    border-radius: 1px;
    -webkit-border-radius: 1px;
    -moz-border-radius: 1px;
}

.grid_elements table td.hover {
    background-color: #999;
}

.grid_elements table td:hover {
    cursor: pointer;
}

.layout_block .block_name {
    cursor: pointer;
}

.ui-resizable-resizing {
    z-index: 9999999 !important;
}

.layout_name_edit {
    background-color: inherit;
    background: url( '../media/images/icons/edit_input.gif' );
    background-repeat: no-repeat;
    background-position: 0 center;
    padding: 0px;
    margin: 0px;
    padding-left: 14px;
    border: none;
    font-size: 16px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: white;
    outline: none;
    width: 90%;
    font-style: italic;
    cursor: text !important;
}
.layouts_grid .remove_element {
    float: right;
    color: black;
    font-size: 12px;
    font-weight: bold;
    padding: 2px 5px;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    cursor: pointer;
    margin: 3px 0px 4px 4px;
}
.layouts_grid .layout_block .info {
    color: white;
    font-size: 16px;
    font-family: Helvetica;
    padding: 10px;
}
/*! gridster.js - v0.1.0 - 2012-10-07
* http://gridster.net/
* Copyright (c) 2012 ducksboard; Licensed MIT */

.layouts_grid {
    position:relative !important;
    width: 700px;
    min-height: 300px;
    float: left;
}

.layouts_grid > * {
    margin: 0 auto;
    -webkit-transition: height .4s;
    -moz-transition: height .4s;
    -o-transition: height .4s;
    -ms-transition: height .4s;
    transition: height .4s;
}

.layouts_grid ul {
    list-style-type: none;
    min-height: 660px;
}
.layouts_grid .gs_w{
    z-index: 2;
    position: absolute;
}

.ready .gs_w:not(.preview-holder) {
    -webkit-transition: opacity .3s, left .3s, top .3s;
    -moz-transition: opacity .3s, left .3s, top .3s;
    -o-transition: opacity .3s, left .3s, top .3s;
    transition: opacity .3s, left .3s, top .3s;
}

.ready .gs_w:not(.preview-holder) {
    -webkit-transition: opacity .3s, left .3s, top .3s, width .3s, height .3s;
    -moz-transition: opacity .3s, left .3s, top .3s, width .3s, height .3s;
    -o-transition: opacity .3s, left .3s, top .3s, width .3s, height .3s;
    transition: opacity .3s, left .3s, top .3s, width .3s, height .3s;
}

.layouts_grid .preview-holder {
    z-index: 1;
    position: absolute;
    background-color: inherit;
    border: none;
    opacity: 0.3;
}

.layouts_grid .player-revert {
    z-index: 10!important;
    -webkit-transition: left .3s, top .3s!important;
    -moz-transition: left .3s, top .3s!important;
    -o-transition: left .3s, top .3s!important;
    transition:  left .3s, top .3s!important;
}

.layouts_grid .dragging {
    z-index: 10!important;
    -webkit-transition: all 0s !important;
    -moz-transition: all 0s !important;
    -o-transition: all 0s !important;
    transition: all 0s !important;
}

/* Uncomment this if you set helper : "clone" in draggable options */
/*.layouts_grid .player {
  opacity:0;
}*/
</style>


<script>
head.js(gridster, function(){
    var layout;
var grid_size = 100;
var grid_margin = 5;
var block_params = {
    max_width: 12,
    max_height: 6
};
$(function() {

    layout = $('.layouts_grid ul').gridster({
        widget_margins: [grid_margin, grid_margin],
        widget_base_dimensions: [grid_size, grid_size],
        serialize_params: function($w, wgd) {
            return {
                x: wgd.col,
                y: wgd.row,
                width: wgd.size_x,
                height: wgd.size_y,
                id: $($w).attr('data-id'),
                name: $($w).find('.block_name').html(),
            };
        },
        min_rows: block_params.max_height
    }).data('gridster');

    $('.layout_block').resizable({
        grid: [grid_size + (grid_margin * 2), grid_size + (grid_margin * 2)],
        animate: false,
        minWidth: grid_size,
        minHeight: grid_size,
        containment: '#layouts_grid ul',
        autoHide: true,
        stop: function(event, ui) {
            var resized = $(this);
            setTimeout(function() {
                resizeBlock(resized);
            }, 300);
        }
    });

    $('.ui-resizable-handle').hover(function() {
        layout.disable();
    }, function() {

        layout.enable();
    });

    function resizeBlock(elmObj) {

        var elmObj = $(elmObj);
        var w = elmObj.width() - grid_size;
        var h = elmObj.height() - grid_size;

        for (var grid_w = 1; w > 0; w -= (grid_size + (grid_margin * 2))) {

            grid_w++;
        }

        for (var grid_h = 1; h > 0; h -= (grid_size + (grid_margin * 2))) {

            grid_h++;
        }

        layout.resize_widget(elmObj, grid_w, grid_h);
    }
});});
    </script>
<%include file="bottom_admin.mak"/>