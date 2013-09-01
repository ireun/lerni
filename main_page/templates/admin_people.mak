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
                    %for row in tables:
                    <div class="accordion-group">
                        <div class="accordion-heading">
                            <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion1" href="#collapse${row[0]}">${row[1]}</a>
                        </div>
                        <div id="collapse${row[0]}" class="accordion-body collapse
                        %if row[0]=="1":
                        in
                        %endif
                        ">
                        <div class="accordion-inner" style="padding: 9px 10px;">
                            <table class="table table-striped">
                            <thead>
                                <tr>
                                %for r in row[2]:
                                <th class="${r[0]}">${r[1]}</th>
                                %endfor
                                </tr>
                            </thead>
                            <tbody>
                                % for r in row[3]:
                                <tr>
                                %for z in r:
                                <td class="${z[0]}">${z[1]}</td>
                                % endfor
                                </tr>
                                % endfor
                            </tbody>
                            </table>
                        </div>
                        </div>
                    </div>
                    %endfor
                    <!--- Opcja dodania nauczyciela -->
                    <div class="accordion-group">
                        <div class="accordion-heading">
                            <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion1" href="#collapseAdd">Dodaj</a>
                        </div>
                        <div id="collapseAdd" class="accordion-body collapse">
                        <div class="accordion-inner">
                            Dodaj 
                        </div>
                        </div>
                    </div>
                    <!--- Wyszukiwanie dostępnych nauczycieli -->
                    <div class="accordion-group">
                        <div class="accordion-heading">
                            <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion1" href="#collapseSearch">
                            Wyszukaj
                            </a>
                        </div>
                        <div id="collapseSearch" class="accordion-body collapse">
                        <div class="accordion-inner" style="padding: 9px 10px;">
                            Szukaj
                        </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
<!--/ END Template Main Content -->
<%include file="bottom_admin.mak"/>