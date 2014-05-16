/*head.js(twitter_bootstrap);*/
head.js(jquery, jquery_ui, function () {head.js(bootstrap, hogan, typeahead).js(mixitup).js(filtertable).js(jtable)});
head.ready("mixitup",function () { $('#Grid').mixitup();});
/*head.js(tagsinput, function () { });*/
head.ready("filtertable",function () {$('table').filterTable({bindExistingInput: $(".typeahead")});})

head.ready("typeahead", function () {
    console.log("Startin");
    $('.typeahead').typeahead({
        name: 'repos'
        , prefetch: '/api/jsonp/people'
        , template: [
            '<p class="user-email">{{email}}</p>'
            , '<p class="repo-name">{{name}}</p>'
            , '<div class="row-fluid"><div class="span4"><p class="user-pesel">{{pesel}}</p></div>'
            , '<div class="span4"><p class="user-pesel">{{pesel}}</p></div>'
            , '<div class="span4"><p class="-pesel">{{pesel}}</p></div></div>'
        ].join('')
        , engine: Hogan
    });
/*remote: '../data/films/queries/%QUERY.json',*/
});
head.js(jquery, sparkline, function () {
    $(function () {

            // Sparkline 1
            $(".sparkline-line").sparkline('html', {
                disableHiddenCheck: true,
                enableTagOptions: true,
                type: 'line',
                width: '60',
                height: '35',
                lineColor: 'red',
                fillColor: 'pink',
                lineWidth: 1.5,
                spotColor: '#972525',
                minSpotColor: '#972525',
                maxSpotColor: '#972525',
                spotRadius: 2
            });

            // Sparkline 2
            $(".sparkline-bar").sparkline('html', {
                disableHiddenCheck: true,
                enableTagOptions: true,
                type: 'bar',
                height: '35',
                barWidth: 6,
                barColor: 'teal'
            });

            // Sparkline 3
            $(".sparkline-tristate").sparkline('html', {
                disableHiddenCheck: true,
                enableTagOptions: true,
                type: 'tristate',
                height: '35',
                posBarColor: 'green',
                negBarColor: 'red',
                barWidth: 6,
                zeroAxis: true
            });
            $('.sparkline-2line').sparkline('html', {
                disableHiddenCheck: true,
                enableTagOptions: true,
                fillColor: false,
                changeRangeMin: 0,
                chartRangeMax: 10,
                lineColor: 'yellow',
                width: '60',
                height: '35',
                lineWidth: 1.5,
                spotRadius: 2
            });
            $('.sparkline-2line').sparkline([4,1,5,7,9,9,8,7,6,6,4,7], {
                disableHiddenCheck: true,
                enableTagOptions: true,
                composite: true,
                fillColor: false,
                lineColor: 'red',
                changeRangeMin: 0,
                chartRangeMax: 10,
                lineColor: 'green',
                width: '60',
                height: '35',
                lineWidth: 1.5,
                spotRadius: 2
            });
    });
});
var next_decade = function () {
	$( ".years td" ).each(function( index ) {
	$(this).html( parseInt($(".next").html()) + index -1);
	$(".yearpicker .bar .title").html( (parseInt($(".next").html())-10)+"-"+(parseInt($(".next").html())-1));
	});
}
var prev_decade = function () {
	$( ".years td" ).each(function( index ) {
	$(this).html( parseInt( $(".next").html() ) + index -21);
  	$(".yearpicker .bar .title").html( (parseInt($(".next").html())-10)+"-"+(parseInt($(".next").html())-1));
	});	
}
head.js(jquery,masked_input, function () {
$(".years td:not(.next, .prev)").click(function () {
	console.log( $(this).html() );
	$("#basic_year_info .title").html("Podstawowe informacje ("+$(this).html()+")")
	$("#basic_year_info .body-inner").html("Ładowanie...");
	$.getJSON('/api/jsonp/year/'+$(this).html(), function(data) {
		var items = [];
		$.each(data, function(key, val) {
		items.push('<li id="' + key + '">' + val + '</li>');
	}); 
  $("#basic_year_info .body-inner").html('\
	                Ilość uczniów:<br>\
	                Ilość otwartych klas:<br>\
	                Ilość pracujących nauczycieli:<br>\
	                Sukcesy w konkursach:<br>\
	                Średnia ocen w placówce:<br>\
	                Średnia ocen w klasach maturalnych:<br>\
	                Średni procent punktów z matury:<br>\
                	<table style="width:100%; text-align: left;">\
                		<thead>\
                			<tr>\
                				<th scope="col" title="President Number">ID</th>\
                				<th scope="col">Początek semestru</th>\
                				<th scope="col">Koniec semestru</th>\
                				<th scope="col">Ilość planów lekcji</th>\
                			</tr>\
                		</thead>\
                		<tbody>\
                			<tr><td>1</td><td>12.07.1995</td><td>two</td><td>1789-1797</td></tr>\
                			<tr><td>2</td><td>John Adams</td><td>one</td><td>1797-1801</td></tr>\
                			<tr><td>3</td><td>Thomas Jefferson</td><td>two</td><td>1801-1809</td></tr>\
    	                </tbody>\
	                </table>');
  $("#basic_year_info .body-inner").html('Wybrany rok nie istnieje w bazie danych.<br>Wypełnij poniższy formularz aby go utworzyć.\
   <input id="startdate" type="text" class="input-block-level" placeholder="Data rozpoczęcia roku szkolnego">\
	<input id="enddate" type="text" class="input-block-level" placeholder="Data rozpoczęcia roku szkolnego">\
	<button class="btn large primary">Utwórz rok szkolny</button>');
	
	$('#startdate').mask("99/99/9999",{placeholder:"_"});
	$('#enddate').mask("99/99/9999",{placeholder:"_"});
});

});
$(".yearpicker .next").click(next_decade);
$(".icon-long-arrow-right").click(next_decade);
$(".yearpicker .prev").click(prev_decade);
$(".icon-long-arrow-left").click(prev_decade);
});
var polishMessages = {
    serverCommunicationError: 'Próba połączenia z serwerem zakończona niepowodzeniem.',
    loadingMessage: 'Ładowanie...',
    noDataAvailable: 'Brak danych do wyświetlenia',
    addNewRecord: ' Dodaj nowy rekord',
    editRecord: 'Edytuj',
    areYouSure: 'Czy jesteś pewien?',
    deleteConfirmation: 'Czy jesteś pewien, że chcesz usunąć wybrany rekord?',
    save: 'Zapisz',
    saving: 'Zapisywanie',
    cancel: 'Anuluj',
    deleteText: 'Usuń',
    deleting: 'Usuwanie',
    error: 'Błąd',
    close: 'Zamknij',
    cannotLoadOptionsFor: '{0} cannotLoadOptionsFor!',
    pagingInfo: 'Strona {2}, {0} z {1}',
    canNotDeletedRecords: 'Nie można usunąć {1} kayıttan {0}',
    deleteProggress: '{1} usuwanie {0} adedi silindi, devam ediliyor...'
};
function getVars(url)
{
    var formData = new FormData();
    var split;
    $.each(url.split("&"), function(key, value) {
        split = value.split("=");
        formData.append(split[0], decodeURIComponent(split[1].replace(/\+/g, " ")));
    });

    return formData;
}


var make_table = function(x){
        $('#table'+x).jtable({
        messages: polishMessages,
        title: ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"][x.substr(0,1)-1]+' - Lekcja'+x.substr(1),
        paging: true, //Enable paging
        pageSize: 7, //Set page size (default: 10)
        sorting: true, //Enable sorting
        defaultSorting: 'teacher ASC', //Set default sorting
        actions: {
            listAction: '/api?format=jsonp&method=lerni.timetables.lessons.getList&timetable_id=1&day='+x.substr(0,1)+'&hour='+x.substr(1),
            deleteAction: '/api?format=jsonp&method=lerni.timetables.lessons.delete&timetable_id=1&day='+x.substr(0,1)+'&hour='+x.substr(1),
            updateAction: function (postData) {
                    var formData = getVars(postData);
                    var groups = JSON.stringify( $("#e6").select2('data') );
                    formData.append("groups", groups);

                    return $.Deferred(function ($dfd) {
                        $.ajax({
                            url: '/api?format=jsonp&method=lerni.timetables.lessons.edit&timetable_id=1&day='+x.substr(0,1)+'&hour='+x.substr(1),
                            type: 'POST',
                            dataType: 'json',
                            data: formData,
                            processData: false, // Don't process the files
                            contentType: false, // Set content type to false as jQuery will tell the server its a query string request
                            success: function (data) {
                                $dfd.resolve(data);
                                $('#table'+x).jtable('reload');
                            },
                            error: function () {
                                $dfd.reject();
                            }
                        });
                    });
                },
            createAction: function (postData) {
                    var formData = getVars(postData);
                    var groups = JSON.stringify( $("#e6").select2('data') );
                    formData.append("groups", groups);

                    return $.Deferred(function ($dfd) {
                        $.ajax({
                            url: '/api?format=jsonp&method=lerni.timetables.lessons.add&timetable_id=1&day='+x.substr(0,1)+'&hour='+x.substr(1),
                            type: 'POST',
                            dataType: 'json',
                            data: formData,
                            processData: false, // Don't process the files
                            contentType: false, // Set content type to false as jQuery will tell the server its a query string request
                            success: function (data) {
                                $dfd.resolve(data);
                            },
                            error: function () {
                                $dfd.reject();
                            }
                        });
                    });
                }
        },
        fields: {
            lesson_id: {
                key: true,
                create: false,
                edit: false,
                list: false
            },
            teacher: {
                title: 'Nauczyciel',
                options: "/api?format=jsonp&method=lerni.teachers.nameList"
            },
            subject: {
                title: 'Przedmiot',
                options: "/api?format=jsonp&method=lerni.subjects.nameList"
            },
            group: {
                title: 'Grupy',
                input: function (data) {
                        if (data.record) {
                            return '<div id="Edit-groups"><input type="hidden" id="e6" style="width: 500px;" value="'+
                            data.value + '"  /></div>' +
                                '<script>' +
                                'head.js(select2, function(){ \
                                MultiAjaxAutoComplete("#e6", "/api?format=jsonp&method=lerni.groups.nameList");\
                                })' +
                                '</script>'
                        } else {
                            return '<div id="Edit-groups"><input type="hidden" id="e6" style="width: 500px;" value=""  /></div>' +
                                '<script>' +
                                'head.js(select2, function(){ \
                                MultiAjaxAutoComplete("#e6", "/api?format=jsonp&method=lerni.groups.nameList");\
                                })' +
                                '</script>'
                        }

                },
                options: function (data) {
                    var rdata = [];
                    var display = "";
                    $(data.value.split(',')).each(function(i) {
                        var item = this.split(':');
                        display = display + item[1] + ", "
                    });
                    rdata.push({
                        Value: data.value,
                        DisplayText: display
                    });
                    return rdata;
                }
            },
            room: {
                title: 'Sala'
            },
            modification_date: {
                title: 'Data Modyfikacji',
                type: 'date',
                displayFormat: 'dd.mm.yy',
                create: false,
                edit: false,
                sorting: false //This column is not sortable!
            }
        }
    });
    $('#table'+x).jtable('load');
}





    function MultiAjaxAutoComplete(element, url) {
        $(element).select2({
            placeholder: "Search for a movie",
            minimumInputLength: 1,
            multiple: true,
            id: function(element){
                return element.Value},
            ajax: {
                url: url,
                dataType: 'jsonp',
                data: function(term, page) {

                    return {
                        q: term,
                        page_limit: 10
                    };
                },
                results: function(data, page) {
                    return { results: data.Options };
                }
            },
            formatResult: formatResult,
            formatSelection: formatSelection,
            initSelection: function(element, callback) {
                var data = [];
                $(element.val().split(",")).each(function(i) {
                    var item = this.split(':');
                    data.push({
                        Value: item[0],
                        DisplayText: item[1]
                    });
                });
                //$(element).val('');
                callback(data);
            }
        });
    };

    function formatResult(movie) { return '<div>' + movie.DisplayText + '</div>'; };

    function formatSelection(data) { return data.DisplayText; };








var done = new Array()
head.ready("jtable", function() {
    $('a[data-toggle="tab"]').on('show.bs.tab', function (e) {
        var id=$(e.target).attr('href').substring(4);
        console.log($.inArray(id, done)==-1);
        console.log(done);
        if($.inArray(id, done)==-1){
            done.push(id);
            make_table(id);
        }
    }) });

/*first_name,second_name,last_name,pesel,birthdate,phonenumber,email,password,key_data,fingerprint,wallet_id,email_confirmed,gpg_confirmed,phone_confirmed,group_id):*/

/*
head.js(fit_vids, function () {
	$(".video").fitVids();
});
head.js(underscore, sequence_diagram, function () {
	$(".diagram").sequenceDiagram({theme: 'hand'});
}); 
head.js(noisy, function () { 
	$('body').noisy({'intensity' : 1,'size' : 200,'opacity' : 0.08,'fallback' : '','monochrome' : false})
});
$.scrollUp({scrollText: 'Przewiń do góry'});

*/