<%include file="top_new.mak"/>
<link href="/static/css/entries.min.css" rel="stylesheet">
<header id="header" class="container">
    <div class="container">
        <h1 id="title">Syllabus</h1><h2><small>Program zajęć dydaktycznych<br/>IV LO im. Stanisława Staszica</small></h2>

        <a class="pull-left header-nav" href="${back}">Wstecz</a>
        %if logged_in:
            <a class="pull-right header-nav" href="?edit">Edytuj</a>
        %endif
    </div>
</header>
<div id="main" class="container">
	<div id="inner-wrapper" class="container" style="padding-top: 20px;">
        <div class="row">
            <!--
            <div class="col-sm-4">
                <label for="school_year">Pierwszy rok szkolny nauki</label>
                <select class="form-control" id="school_year">
                <option>2014/2015</option>
                </select>
            </div>
            <div class="col-sm-8">

                </ul>
            </div>
            -->
            %for x in range(1,6):
            Semsetr ${x}
            <div class="table-responsive">
                <table class="table table-striped table-bordered table-condensed">
                  <thead>
                    <tr>
                      <th>Przemiot</th>
                      <th colspan="6">Godziny</th>
                    </tr>
                    <tr>
                        <th></th>
                        <th>Wykład</th>
                        <th>Projekt*</th>
                        <th>Przygotowanie do egzaminu</th>
                        <th>Inne</th>
                        <th>E-learning*</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>Matematyka</td>
                      <td>Mark</td>
                      <td>Otto</td>
                      <td>Otto</td>
                      <td>Mark</td>
                      <td>Otto</td>
                    </tr>
                    <tr>
                      <td>Fizyka</td>
                      <td>Jacob</td>
                      <td>Thornton</td>
                      <td>Thornton</td>
                      <td>Jacob</td>
                      <td>Thornton</td>
                    </tr>
                    <tr>
                      <td>Informatyka</td>
                      <td>Larry</td>
                      <td>the Bird</td>
                      <td>the Bird</td>
                      <td>Larry</td>
                      <td>the Bird</td>
                    </tr>
                  </tbody>
                </table>
            </div>
            %endfor
            *Projekt oraz moduły e-lerningowe uczeń samodzielnie przygotowuje w domu.
        </div>
	</div>
</div>
<%include file="bottom_new.mak"/>