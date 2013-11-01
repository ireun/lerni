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
head.ready("jquery", function () {
    head.js(sparkline, function () {

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
var make_table = function(x){
        $('#table'+x).jtable({
        messages: polishMessages,
        title: ["Poniedziałek","Wtorek","Środa","Czwartek","Piątek","Sobota","Niedziela"][x.substr(0,1)-1]+' - Lekcja'+x.substr(1),
        paging: true, //Enable paging
        pageSize: 7, //Set page size (default: 10)
        sorting: true, //Enable sorting
        defaultSorting: 'Teacher ASC', //Set default sorting
        actions: {
            listAction: '/api/jsonp/lesson-list/?timetableID=1&day='+x.substr(0,1)+'&hour='+x.substr(1),
            deleteAction: '/api/jsonp/delete-lesson?timetableID=1&day='+x.substr(0,1)+'&hour='+x.substr(1),
            updateAction: '/api/jsonp/update-lesson?timetableID=1&day='+x.substr(0,1)+'&hour='+x.substr(1),
            createAction: '/api/jsonp/create-lesson?timetableID=1&day='+x.substr(0,1)+'&hour='+x.substr(1)
        },
        fields: {
            LessonID: {
                key: true,
                create: false,
                edit: false,
                list: false
            },
            Teacher: {
                title: 'Nauczyciel',
                options: "/api/jsonp/options-teacher-list"
            },
            Subject: {
                title: 'Przedmiot',
                options: "/api/jsonp/options-subjects-list"
            },
            Group: {
                title: 'Grupy',
                /*options: "/api/jsonp/options-groups-list/"+"1"*/
                input: function (data) {
                        if (data.record) {
                            /*return '<input type="text" name="Name" style="width:200px" value="' + data.record.Name + '" />';*/
                            return '<input type="hidden" id="e6" style="width: 500px;" value="34:Donnie Darko,54:Heat,27:No Country for Old Men"  />'
                        } else {
                            return '<input type="hidden" id="e6" style="width: 500px;" value="34:Donnie Darko,54:Heat,27:No Country for Old Men"  />' +
                                '<script>' +
                                'head.js(select2, function(){ \
                                MultiAjaxAutoComplete("#e6", "http://api.rottentomatoes.com/api/public/v1.0/movies.json");\
                                console.log("Q!#!#!#!");\
                                })' +
                                '</script>'
                        }

                }
            },
            Room: {
                title: 'Sala'
            },
            ModificationDate: {
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
            ajax: {
                url: url,
                dataType: 'jsonp',
                data: function(term, page) {

                    return {
                        q: term,
                        page_limit: 10,
                        apikey: "z4vbb4bjmgsb7dy33kvux3ea" //my own apikey
                    };
                },
                results: function(data, page) {
                    return {
                        results: data.movies
                    };
                }
            },
            formatResult: formatResult,
            formatSelection: formatSelection,
            initSelection: function(element, callback) {
                var data = [];
                $(element.val().split(",")).each(function(i) {
                    var item = this.split(':');
                    data.push({
                        id: item[0],
                        title: item[1]
                    });
                });
                //$(element).val('');
                callback(data);
            }
        });
    };

    function formatResult(movie) {
        return '<div>' + movie.title + '</div>';
    };

    function formatSelection(data) {
        return data.title;
    };








var done=new Array()
head.ready("jtable", function() {
    $('a[data-toggle="tab"]').on('show', function (e) {
        var id=$(e.target).attr('href').substring(4);
        console.log($.inArray(id, done)==-1);
        console.log(done);
        if($.inArray(id, done)==-1){
            done.push(id);
            make_table(id);
        }
    })
    $('#table_timetables').jtable({
        messages: polishMessages,
        title: 'Plany lekcji',
        paging: true, //Enable paging
        pageSize: 7, //Set page size (default: 10)
        sorting: true, //Enable sorting
        selecting: true,
        defaultSorting: 'Start DESC', //Set default sorting
        actions: {
            listAction: '/api/jsonp/timetable-list',
            deleteAction: '/api/jsonp/delete-timetable',
            updateAction: '/api/jsonp/update-timetable',
            createAction: '/api/jsonp/create-timetable'
        },
        fields: {
            TimetableId: {
                key: true,
                create: false,
                edit: false,
                list: false
            },
            Start: {
                title: 'Początek planu lekcji',
                type: 'date',
                displayFormat: 'dd.mm.yy'
            },
            End: {
                title: 'Koniec planu lekcji',
                type: 'date',
                displayFormat: 'dd.mm.yy'
            },
            ModificationDate: {
                title: 'Data Modyfikacji',
                type: 'date',
                displayFormat: 'dd.mm.yy',
                create: false,
                edit: false,
                sorting: false //This column is not sortable!
            }
        }
    });
    $('#table_timetables').jtable('load');

    weee='\
        <span id="add-lessons" class="jtable-toolbar-item jtable-toolbar-item-add-record" style="">\
        <span class="jtable-toolbar-item-icon"></span>\
        <span class="jtable-toolbar-item-text"> Dodaj lekcje</span></span>'
    $('.jtable-toolbar').append(weee)
    $('#add-lessons').hover(function() {
    $(this).addClass("jtable-toolbar-item-hover");
        }, function() {
    $(this).removeClass("jtable-toolbar-item-hover");
    });
    $('#add-lessons').click(function(){ if ($('#table_timetables').jtable('selectedRows').first().data('record')){
    window.location = '/admin/log/timetables/edit?id='+$('#table_timetables').jtable('selectedRows').first().data('record').TimetableId }else{
        alert("Wybierz plan do którego chcesz dodać lekcje.") } });

/*first_name,second_name,last_name,pesel,birthdate,phonenumber,email,password,key_data,fingerprint,wallet_id,email_confirmed,gpg_confirmed,phone_confirmed,group_id):*/
    $('#table_users').jtable({
        messages: polishMessages,
        title: 'Użytkownicy',
        paging: true, //Enable paging
        pageSize: 10, //Set page size (default: 10)
        sorting: true, //Enable sorting
        selecting: true,
        defaultSorting: 'UserID DESC', //Set default sorting
        actions: {
            listAction: '/api/jsonp/user-list',
            deleteAction: '/api/jsonp/delete-user',
            updateAction: '/api/jsonp/update-user',
            createAction: '/api/jsonp/create-user'
        },
        fields: {
            UserID: {
                key: true,
                create: false,
                edit: false,
                list: false
            },
            FirstName: {title: 'Imię'},
            SecondName: {title: 'Drugie Imię'},
            LastName: {title: 'Nazwisko'},
            Pesel: {title: 'Pesel'},
            PhoneNumber: {title: 'Numer telefonu'},
            BirthDate: {
                title: 'Data urodzenia',
                type: 'date',
                displayFormat: 'dd.mm.yy'
            },
            Email: {title: 'Email'},
            Password: {title: 'Hasło'},
            Group: {title: 'Grupa'}
        }
    });
    $('#table_users').jtable('load');

    send_welcome_button='\
        <span id="send-welcome-button" class="jtable-toolbar-item jtable-toolbar-item-add-record" style="">\
        <span class="jtable-toolbar-item-icon"></span>\
        <span class="jtable-toolbar-item-text"> Wyślij wiadomość powitalną </span></span>'
    $('#table_users .jtable-toolbar').append(send_welcome_button)
    $('#send-welcome-button').hover(function() {
    $(this).addClass("jtable-toolbar-item-hover");
        }, function() {
    $(this).removeClass("jtable-toolbar-item-hover");
    });
    $('#send-welcome-button').click(function(){ if ($('#table_users').jtable('selectedRows').first().data('record')){
    window.location = '/admin/log/timetables/edit?id='+$('#table_timetables').jtable('selectedRows').first().data('record').TimetableId }else{
        alert("Wybierz użytkownika.") } });



/* Foldery  */
    $('#table_folders').jtable({
        messages: polishMessages,
        title: 'Moje foldery',
        paging: true, pageSize: 10, //Enable pagin
        sorting: true, selecting: true, //
        defaultSorting: 'FolderID DESC', //Set default sorting
        actions: {
            listAction: '/api/jsonp/folder-list', deleteAction: '/api/jsonp/delete-folder',
            updateAction: '/api/jsonp/update-folder', createAction: '/api/jsonp/create-folder'
        },
        fields: {
            FolderID: {key: true,create: false,edit: false,list: false},
            Title: {title: 'Tytuł'},
            Tags: {title: 'Tagi'},
            CSS: {title: 'Własny CSS'},
            GPG: {title: 'Podpis GPG (to do)'},
            Published: {title: 'Opublikowany', options: {'False':'Nie', 'True':'Tak'}}
        }
    });
    $('#table_folders').jtable('load');
/* Wpisy  */
    $('#table_entries').jtable({
        messages: polishMessages,
        title: 'Moje Wpisy',
        paging: true, pageSize: 10, //Enable pagin
        sorting: true, selecting: true, //
        defaultSorting: 'EntryID DESC', //Set default sorting
        actions: {
            listAction: '/api/jsonp/entry-list', deleteAction: '/api/jsonp/delete-entry',
            updateAction: '/api/jsonp/update-entry', createAction: '/api/jsonp/create-entry'
        },
        fields: {
            EntryID: {key: true,create: false,edit: false,list: false},
            FolderID: {title: 'Folder', options: "/api/jsonp/options-folders-list"},
            Title: {title: 'Tytuł'},
            Tags: {title: 'Tagi'},
            CSS: {title: 'Własny CSS'},
            Published: {title: 'Opublikowany', options: {'False':'Nie', 'True':'Tak'}}
        }
    });
    $('#table_entries').jtable('load');
    edit_entry_button='\
        <span id="edit-entry-button" class="jtable-toolbar-item jtable-toolbar-item-add-record" style="">\
        <span class="jtable-toolbar-item-icon"></span>\
        <span class="jtable-toolbar-item-text"> Edytuj treść wpisu. </span></span>'
    $('#table_entries .jtable-toolbar').append(send_welcome_button)
    $('edit-entry-button').hover(function() {
    $(this).addClass("jtable-toolbar-item-hover");
        }, function() {
    $(this).removeClass("jtable-toolbar-item-hover");
    });
    $('#edit-entry-button').click(function(){ if ($('#table_entires').jtable('selectedRows').first().data('record')){
    window.location = '/admin/log/timetables/edit?id='+$('#table_entries').jtable('selectedRows').first().data('record').TimetableId }else{
        alert("Wybierz wpis.") } });



});

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