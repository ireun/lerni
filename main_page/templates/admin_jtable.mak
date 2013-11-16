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
    <div class="container">
	    <div class="row-fluid">
            <div class="span12">
	            <div class="page-header line1">
	                <h4>${title}<small>${title_desc}</small></h4>
	            </div>
	        </div>
	    </div>
        <div class="row-fluid">
            <div class="span12">
                <%include file="snippets/jtable.mak"/>
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