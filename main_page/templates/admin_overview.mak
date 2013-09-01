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
    <div class="container-fluid">
        <div class="row-fluid">
            <div class="span12">
                <div class="page-header line1">
                    <h4>Kokpit <small>Tutaj znajdują się wszystkie podstawowe informacje zgromadzone w jednym miejscu.</small></h4>
                </div>
            </div>
        </div>
        <div class="row-fluid">
            <div class="span4 widget dark">
            <header><h4 class="title">Szczęśliwy numerek (data)</h4></header>
            <section class="body">
                <div class="body-inner">
                <div id="lucky_number">
                 32
                </div>
                </div>
            </section>
            </div>
            <div class="span4 widget dark">
            <header><h4 class="title">Jutrzejszy dzień</h4></header>
            <section class="body">
                <div class="body-inner">
                <div id="lucky_number">
                 32
                </div>
                </div>
            </section>
            </div>
            <div class="span4 widget dark">
            <header><h4 class="title">Notyfikacje</h4></header>
            <section class="body">
                <div class="body-inner">
                <div id="lucky_nukmber">
                 Kamil Danak wysłał plik
                 AAA wrzucił artykuł
                </div>
                </div>
            </section>
            </div>
        </div>
        <!--
        <div class="row-fluid">
            <div class="span12 widget borderless">
                <section class="body">
                    <div class="body-inner no-padding" style="text-align:center;">
                        <figure class="stats sparkline stacked">
                            <span class="chart sparkline-line">5,6,7,9,9,5,3,2,2,4,6,7</span>
                            <figcaption>
                                <h3><small>Daily Visits</small>+230</h3>
                            </figcaption>
                        </figure>
                        <figure class="stats sparkline stacked">
                            <span class="chart sparkline-bar">5,6,7,2,9,2,1,4,8</span>
                            <figcaption>
                                <h3><small>My Balance</small>$16,763</h3>
                            </figcaption>
                        </figure>
                        <figure class="stats summary stacked">
                            <div class="icon circle teal"><span class="icon-ticket"></span></div>
                            <figcaption>
                                <h3>+230<small>Open tickets</small></h3>
                            </figcaption>
                        </figure>
                        <figure class="stats sparkline stacked">
                            <span class="chart sparkline-2line">8,4,0,0,0,0,1,4,4,10,10,10</span>
                            <figcaption>
                                <h3><small>Visitors</small>-6,763</h3>
                            </figcaption>
                        </figure>
                    </div>
                </section>
            </div>
        </div>
        <div class="row-fluid">
            <div class="span12 widget stacked">
                <header>
                    <h4 class="title">Rich Chart</h4>
                    <ul class="toolbar pull-right">
                        <li><a href="#" class="link" data-widget="refresh"><span class="icon icon-refresh"></span></a></li>
                        <li>
                            <a href="#" class="link" data-toggle="dropdown"><span class="icon icon-ellipsis-vertical"></span></a>
                            <ul class="dropdown-menu pull-right">
                                <li><a href="#"><span class="icon icon-pencil"></span> Edit</a></li>
                                <li><a href="#"><span class="icon icon-trash"></span> Delete</a></li>
                                <li><a href="#"><span class="icon icon-cog"></span> Setting</a></li>
                            </ul>
                        </li>
                    </ul>
                </header>
                <section class="body">
                    <div class="body-inner">
                        <div class="row-fluid">
                            <div class="span8">
                                <div class="flot" id="chart2" style="height:220px;"></div>
                            </div>
                            <div class="span4 widget">
                                <section class="body">
                                    <div class="body-inner">
                                        <div class="flot" id="chart4"></div>
                                    </div>
                                </section>
                            </div>
                        </div>
                    </div>
                    <div class="footer" align="center">
                        <figure class="stats borderless circular">
                            <div class="gauge gauge-teal" data-percent="20">
                                <span class="icon icon-lightbulb"></span>
                            </div>
                            <figcaption>
                                <h4>Server Load<small>20% CPU Usage</small></h4>
                            </figcaption>
                        </figure>
                        <figure class="stats borderless circular">
                            <div class="gauge gauge-red" data-percent="70">
                                <span class="icon icon-exchange"></span>
                            </div>
                            <figcaption>
                                <h4>Bandwidth<small>70% Used</small></h4>
                            </figcaption>
                        </figure>
                        <figure class="stats prog borderless">
                            <figcaption>
                                <span class="text pull-left"><span class="icon-cloud-upload"></span> Upload Progress</span>
                                <span class="text pull-right">10%/100%</span>
                            </figcaption>
                            <div class="progress progress-striped active">
                                <div class="bar bar-danger" style="width: 20%;"></div>
                            </div>
                        </figure>
                        <figure class="stats prog borderless">
                            <figcaption>
                                <span class="text pull-left"><span class="icon-cloud-download"></span> Download Progress</span>
                                <span class="text pull-right">99MB</span>
                            </figcaption>
                            <div class="progress progress-striped active">
                                <div class="bar bar-success" style="width: 99%;"></div>
                            </div>
                        </figure>
                    </div>
                </section>
            </div>
        </div>
            -->
        <div class="row-fluid">
            <div class="span6 widget dark">
                <header>
                    <h4 class="title">Zadania</h4>
                    <span class="label label-important pull-right">2 Oczekujące</span>
                </header>
                <section class="body">
                    <div class="body-inner no-padding">
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th><input type="checkbox" class="checkall"></th>
                                    <th>Lista zadań</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Lorem ipsum dolor sit amet</td>
                                    <td><span class="label label-important">Pending</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Eos ei tamquam ornatus deleniti</td>
                                    <td><span class="label label-success">Success</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Mei minim saepe sententiae no</td>
                                    <td><span class="label">Draf</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Ius commune elaboraret scripserit te</td>
                                    <td><span class="label label-success">Success</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>In ipsum delicata duo, quaeque corpora</td>
                                    <td><span class="label label-success">Success</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Dissentias deterruisset ne ius</td>
                                    <td><span class="label label-important">Pending</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
            </div>
            <div class="span6 widget dark">
                <header>
                    <h4 class="title"><span class="icon icon-envelope-alt"></span> Ostatnie emaile.</h4>
                    <ul class="toolbar pull-right">
                        <li><a href="#" class="link"><span class="icon icon-cog"></span></a></li>
                        <li>
                            <a href="#" class="link" data-toggle="dropdown"><span class="icon icon-ellipsis-vertical"></span></a>
                            <ul class="dropdown-menu pull-right">
                                <li><a href="#"><span class="icon icon-pencil"></span> Edit</a></li>
                                <li><a href="#"><span class="icon icon-trash"></span> Delete</a></li>
                                <li><a href="#"><span class="icon icon-cog"></span> Setting</a></li>
                            </ul>
                        </li>
                    </ul>
                </header>
                <section class="body">
                    <div class="body-inner no-padding">
                        <table class="table table-striped">
                            <thead>
                                <tr>
                                    <th><input type="checkbox" class="checkall"></th>
                                    <th>Lista zadań</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Lorem ipsum dolor sit amet</td>
                                    <td><span class="label label-important">Pending</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Eos ei tamquam ornatus deleniti</td>
                                    <td><span class="label label-success">Success</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Mei minim saepe sententiae no</td>
                                    <td><span class="label">Draf</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Ius commune elaboraret scripserit te</td>
                                    <td><span class="label label-success">Success</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>In ipsum delicata duo, quaeque corpora</td>
                                    <td><span class="label label-success">Success</span></td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"></td>
                                    <td>Dissentias deterruisset ne ius</td>
                                    <td><span class="label label-important">Pending</span></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>
            </div>
        </div>
    </div>
</section>
<%include file="bottom_admin.mak"/>
