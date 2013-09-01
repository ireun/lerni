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
	      <div class="span4 widget dark">
	          <header><h4 class="title">Wybierz rok szkolny</h4></header>
	          <section class="body">
	            <div class="body-inner">
	            <div class="yearpicker">
	                <div class="bar">
	                    <div class="row-fluid">
	                        <div class="span3 icon-long-arrow-left"></div>
	                        <div class="title span6">2001-2010</div>
	                        <div class="span3 icon-long-arrow-right"></div>
	                    </div>
	                </div>
	                <div class="years">
	                    <table>
	                    <tr><td class="prev">2000</td><td>2001</td><td>2002</td><td>2003</td></tr>
	                    <tr><td>2004</td><td>2005</td><td>2006</td><td>2007</td></tr>
	                    <tr><td>2008</td><td>2009</td><td>2010</td><td class="next">2011</td></tr>
	                    </table>
	                </div>
	            </div>
	            </div>
	          </section>      
	      </div>
	      <div class="span8 widget dark" id="basic_year_info">
	            <header><h4 class="title">Podstawowe informacje</h4></header>
	            <section class="body">
	                <div class="body-inner">
	                Wybierz rok rozpoczęcia roku szkolnego z listy po lewej.
	                </div>
	            </section>
	      </div>
	    </div>
	 </div>
</section>
<%include file="bottom_admin.mak"/>