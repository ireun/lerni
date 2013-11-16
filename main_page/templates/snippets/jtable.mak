<div id="jtable"></div>
<script>
var add_jtable_button = function(table, button_id, button_text, func){
    weee='\
        <span id="'+button_id+'" class="jtable-toolbar-item jtable-toolbar-item-add-record" style="">\
        <span class="jtable-toolbar-item-icon"></span>\
        <span class="jtable-toolbar-item-text">'+button_text+'</span></span>';
    $('.jtable-toolbar').append(weee)
    button=$("#"+button_id)
    button.hover(function() {
    $(this).addClass("jtable-toolbar-item-hover");
        }, function() {
    $(this).removeClass("jtable-toolbar-item-hover");
    });
    $(button).click(func);
};
var polishMessages = {"serverCommunicationError": "Próba połączenia z serwerem zakończona niepowodzeniem.",
"loadingMessage": "Ładowanie...",
"noDataAvailable": "Brak danych do wyświetlenia",
"addNewRecord": "Dodaj nowy rekord",
"editRecord": "Edytuj",
"areYouSure": "Czy jesteś pewien?",
"deleteConfirmation": "Czy jesteś pewien, że chcesz usunąć wybrany rekord?",
"save": "Zapisz",
"saving": "Zapisywanie",
"cancel": "Anuluj",
"deleteText": "Usuń",
"deleting": "Usuwanie",
"error": "Błąd",
"close": "Zamknij",
"cannotLoadOptionsFor": "{0} cannotLoadOptionsFor!",
"pagingInfo": "Rekordy od {0} do {1} / {2}",
"canNotDeletedRecords": "Nie można usunąć {1} kayıttan {0}",
"deleteProggress": "{1} usuwanie {0} adedi silindi, devam ediliyor..."}

head.js(jquery, jtable, function(){
        $('#jtable').jtable({
        messages: polishMessages,
        % if title:
            title: "${title}",
        % else:
            title: "Title not set",
        % endif
        % if paging:
            paging: ${paging | n},
        % else:
            paging: true,
        % endif
        % if page_size:
            pageSize: ${page_size},
        % else:
            pageSize: 10,
        % endif
        % if selecting and selecting == True:
            selecting: true,
        % else:
            selecting: false,
        % endif
        % if sorting and sorting == True:
            sorting: true,
        % else:
            sorting: false,
        % endif
        % if defaultSorting:
            defaultSorting: '${defaultSorting | n}',
        % else:
            defaultSorting: 'teacher ASC',
        % endif
        actions: {
            listAction: '${list | n}',
            deleteAction: '${delete | n}',
            updateAction: '${update | n}',
            createAction: '${create | n}'
        },
        fields: {
        % for x in fields:
            ${x['name'] |n}: {
                % if 'key' in x and x['key'] == True:
                    key: true,
                % endif
                % if 'create' in x and x['create'] == True:
                    create: true,
                % endif
                % if 'edit' in x and x['edit'] == True:
                    edit: true,
                % endif
                % if 'list' in x and x['list'] == False:
                    list: false,
                % endif
                % if 'title' in x:
                    title: '${x['title'] | n}'
                % endif
                % if 'options' in x:
                    options: '${x['options'] | n}'
                % endif
            },
        % endfor
        }
        /*
            lesson_id: {
                key: true,
                create: false,
                edit: false,
                list: false
            },
            teacher: {
                title: 'Nauczyciel',
                options: "/api?format=jsonp&method=lerni.teachers.getList"
            },
            subject: {
                title: 'Przedmiot',
                options: "/api/jsonp/options-subjects-list"
            },
            group: {
                title: 'Grupy',
                /*options: "/api/jsonp/options-groups-list/"+"1"
                input: function (data) {
                        if (data.record) {
                            /*return '<input type="text" name="Name" style="width:200px" value="' + data.record.Name + '" />';
                            return '<input type="hidden" id="e6" style="width: 500px;" value="34:Donnie Darko,54:Heat,27:No Country for Old Men"  />'
                        } else {
                            return '<input type="hidden" id="e6" style="width: 500px;" value="34:Donnie Darko,54:Heat,27:No Country for Old Men"  />' +
                                '<script>' +
                                'head.js(select2, function(){ \
                                MultiAjaxAutoComplete("#e6", "http://api.rottentomatoes.com/api/public/v1.0/movies.json");\
                                console.log("Q!#!#!#!");\
                                })'
                        }

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
        */
    });
    $('#jtable').jtable('load');
    % if buttons:
        %for x in buttons:
            add_jtable_button("jtable", "add_lol", "LOL" , function(){
                function(){
                    if ((table).jtable('selectedRows').first().data('record')){
                        window.location = '/admin/log/timetables/edit?id='+
                            $(table).jtable('selectedRows').first().data('record').timetable_id;
                    }else{
                        alert("Wybierz plan do którego chcesz dodać lekcje.");
                    }
                }
            });
        %endfor
    % endif
});
</script>