# -*- coding: utf-8 -*-
<%include file="top_admin.mak"/>
<section id="main">
    <div class="navbar navbar-static-top">
        <div class="navbar-inner">
            <ul class="breadcrumb">
                %for row in breadcrumbs[:-1]:
                <li><a href="${row[0]}">${row[1]}</a> <span class="divider"></span></li>
                %endfor
                <li class="active">${breadcrumbs[-1][1]}</li>
            </ul>
        </div>
    </div>
    <div class="container-fluid">
	    <div class="row-fluid">
            <div class="span12">
	            <div class="page-header line1">
	                <h4>${title}<small>${title_desc}</small></h4>
	            </div>
	        </div>
	    </div>
        <div class="row-fluid">
            <div class="span12">
                <div class="accordion" id="accordion1">
                    %for x in lessons:
                    <div class="accordion-group">
                        <div class="accordion-heading">
                            <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion1" href="#collapse${x[0]}">${x[1]}</a>
                        </div>
                        <div id="collapse${x[0]}" class="accordion-body collapse">
                        <div class="accordion-inner" style="padding: 0;">
                            <div class="row-fluid">
                                <div class="span12">
                                    <section class="body">
                                        <div class="body-inner no-padding">
                                            <div class="tabbable tabs-left">
                                                <ul class="nav nav-tabs">
                                                    %for y in x[2]:
                                                    <li class=""><a href="#tab${x[0]}${y[0]}" data-toggle="tab">${y[1]}</a></li>
                                                    %endfor
                                                </ul>
                                                <div class="tab-content">
                                                    %for y in x[2]:
                                                    <div class="tab-pane" id="tab${x[0]}${y[0]}">
                                                        <div class="content">
                                                            <div id="table${x[0]}${y[0]}">

                                                            </div>
                                                        </div>
                                                    </div>
                                                    %endfor
                                                </div>
                                            </div>
                                        </div>
                                    </section>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    %endfor
                </div>
            </div>
        </div>
	    <!--
        <div class="row-fluid">
            <div class="span12 widget dark">
            <header><h4 class="title">Plany lekcji</h4>

            </header>
            <section class="body">
                <div class="body-inner">
                	<table style="width:100%; text-align: left;">\
                		<thead>\
                			<tr>\
                				<th scope="col" title="President Number">ID</th>\
                				<th scope="col">Początek planu lekcji</th>\
                				<th scope="col">Koniec planu lekcji</th>\
                				<th scope="col">Akcje</th>\
                			</tr>\
                		</thead>\
                		<tbody>\
                			<tr><td>1</td><td>12.07.1995</td><td>two</td><td>1789-1797</td></tr>\
                			<tr><td>2</td><td>John Adams</td><td>one</td><td>1797-1801</td></tr>\
                			<tr><td>3</td><td>Thomas Jefferson</td><td>two</td><td>1801-1809</td></tr>\
    	                </tbody>\
	                </table>
                </div>
            </section>
            </div>
        </div>
        -->
    </div>
</section>

<%include file="bottom_admin.mak"/>