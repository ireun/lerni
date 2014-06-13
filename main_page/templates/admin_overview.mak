<%include file="top_admin.mak"/>
<script>
head.js(jquery, jquery_flot, function(){
$(function () {
    // we use an inline data source in the example, usually data would
    // be fetched from a server
    var data = [], totalPoints = 300;
    function getRandomData() {
        if (data.length > 0)
            data = data.slice(1);

        // do a random walk
        while (data.length < totalPoints) {
            var prev = data.length > 0 ? data[data.length - 1] : 50;
            var y = prev + Math.random() * 10 - 5;
            if (y < 0)
                y = 0;
            if (y > 100)
                y = 100;
            data.push(y);
        }

        // zip the generated y values with the x values
        var res = [];
        for (var i = 0; i < data.length; ++i)
            res.push([i, data[i]])
        return res;
    }

    // setup control widget
    var updateInterval = 30;
    $("#updateInterval").val(updateInterval).change(function () {
        var v = $(this).val();
        if (v && !isNaN(+v)) {
            updateInterval = +v;
            if (updateInterval < 1)
                updateInterval = 1;
            if (updateInterval > 2000)
                updateInterval = 2000;
            $(this).val("" + updateInterval);
        }
    });

    // setup plot
    var options = {
        series: { shadowSize: 0 }, // drawing is faster without shadows
        yaxis: { min: 0, max: 100 },
        xaxis: { show: false }
    };
    var plot = $.plot($("#placeholder"), [ getRandomData() ], options);

    function update() {
        plot.setData([ getRandomData() ]);
        // since the axes don't change, we don't need to call plot.setupGrid()
        plot.draw();

        setTimeout(update, updateInterval);
    }

    update();
});
});
</script>
<section id="main">
    <div class="navbar navbar-static-top">
        <div class="navbar-inner">
            <ul class="breadcrumb">
                <li><a href="#">Kokpit</a> <span class="divider"></span></li>
                <li class="active">Indeks</li>
            </ul>
        </div>
    </div>
    <div class="container">
        <div id="canvas">
            <div class="row">
                <div class="col-md-12" >
                    <div class="page-header line1"> <h4>Kokpit <small>Tutaj znajdują się wszystkie podstawowe informacje zgromadzone w jednym miejscu.</small></h4> </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-8" >
                    <div class="panel panel-default">
                      <div class="panel-heading">
                        <h3 class="panel-title">Plan lekcji</h3>
                      </div>
                      ${timetable | n}
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">Lista TODO</h3>
                        </div>
                        <ul class="list-group" style="max-height: 279px; overflow-y: scroll;">
                            <li class="list-group-item">Cras justo odio</li>
                            <li class="list-group-item">Dapibus ac facilisis in</li>
                            <li class="list-group-item">Morbi leo risus</li>
                            <li class="list-group-item">Porta ac consectetur ac</li>
                            <li class="list-group-item">Vestibulum at eros</li>
                            <li class="list-group-item">Morbi leo risus</li>
                            <li class="list-group-item">Porta ac consectetur ac</li>
                            <li class="list-group-item">Vestibulum at eros</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-8" >
                    <div class="panel panel-default">
                        <div class="panel-heading" style="padding: 0;">
                            <ul class="nav nav-tabs border-none">
                              <li class="active"><a href="#home" data-toggle="tab">Home</a></li>
                              <li><a href="#profile" data-toggle="tab">Profile</a></li>
                              <li><a href="#messages" data-toggle="tab">Messages</a></li>
                              <li><a href="#settings" data-toggle="tab">Zużycie procesora</a></li>
                            </ul>
                        </div>
                        <style>.nav-tabs.border-none{border: none;} .nav-tabs.border-none > li.active > a{border: none; border-radius: 0;}</style>
                        <div class="panel-body" style="height: 330px;">
                            <div class="tab-content">
                                <div class="tab-pane active" id="home"></div>
                                <div class="tab-pane" id="profile">...2</div>
                                <div class="tab-pane" id="messages">...23</div>
                                <div class="tab-pane" id="settings"><div id="placeholder" style="width:600px;height:300px;"></div></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="panel panel-default">
                      <div class="panel-heading">
                        <h3 class="panel-title">Notyfikacje</h3>
                      </div>
                      <div class="panel-body">
                        Panel content
                      </div>
                    </div>
                </div>
            </div>
    </div>

<%include file="bottom_admin.mak"/>
