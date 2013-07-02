<%include file="top.mak"/>
			<div id="main_page">
			<div id="left"> 
				<div id="nav">
					<ul>
						% for row in menu_left_list:
							<li><a href="${row[0]}" id="homenav">${row[1]}</a></li>
						% endfor
	    			</ul>
			 </div>
			</div>
				<div id="center" style="width:820px;">
					<div class="settings_container" style="width:800px;">
						<div class="settings_header">Absolwenci</div>



                <div id="contacts">
                                <th colspan="2">
                                    <input type="text" class="search" placeholder="Search contact">
                                </th>
                    <table>
                        <thead>
                            <tr>
                                <th class="sort  " data-sort="name">Imię i Nazwisko</th>
                                <th class="sort  " data-sort="category">Rodzaj konkursu</th>
                                <th class="sort  " data-sort="type">Typ osiągnięcia</th>
                                <th class="sort desc " data-sort="year">Rok szkolny</th>
                            </tr>
                        </thead>
                        <tbody class="list">
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Czyrnek Maciej</td>
                                <td class="category">Olimpiada Filozoficzna</td>
                                <td class="type">Laureat</td>
                                <td class="year">2012/2013</td>
                            </tr>
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Kalska Anna</td>
                                <td class="category">Olimpiada Języka Angielskiego</td>
                                <td class="type">Laureatka</td>
                                <td class="year">2012/2013</td>
                            </tr>
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Dziewit Michał</td>
                                <td class="category">Olimpiada Historyczna</td>
                                <td class="type">Laureat</td>
                                <td class="year">2012/2013</td>
                            </tr>
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Barwiński Kacper</td>
                                <td class="category">Olimpiada Historyczna</td>
                                <td class="type">Finalista</td>
                                <td class="year">2012/2013</td>
                            </tr>
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Zbiegień Sławomir</td>
                                <td class="category">Olimpiada Chemiczna</td>
                                <td class="type">Finalista</td>
                                <td class="year">2012/2013</td>
                            </tr>
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Motyka Justyna</td>
                                <td class="category">Olimpiada Artystyczna</td>
                                <td class="type">Finalistka</td>
                                <td class="year">2012/2013</td>
                            </tr>
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Barwiński Kacper</td>
                                <td class="category">Olimpiada Wiedzy o Polsce i Świecie Współczesnym</td>
                                <td class="type">Finalista</td>
                                <td class="year">2012/2013</td>
                            </tr>
                            <tr>
                                <td class="id" style="display:none;">3</td>
                                <td class="name">Porębska Izabela</td>
                                <td class="category">Olimpiada Lingwistyki Matematycznej</td>
                                <td class="type">Finalistka</td>
                                <td class="year">2012/2013</td>
                            </tr>
                        </tbody>
                    </table>
                </div>     
					</div>
				</div>
			</div>

<script type="text/javascript">

    /*
    * CONTACT LIST
    */

    // Define value names
    var options = {
	    valueNames: [ 'id', 'name', 'category', 'type', 'year' ]
    };

    // Init list
    var contactList = new List('contacts', options);

    var idField = $('#id-field'),
        nameField = $('#name-field'),
        ageField = $('#age-field'),
        cityField = $('#city-field'),
        addBtn = $('#add-btn'),
        editBtn = $('#edit-btn').hide(),
        removeBtns = $('.remove-item-btn'),
        editBtns = $('.edit-item-btn');

    // Sets callbacks to the buttons in the list
    refreshCallbacks();

    addBtn.click(function() {
       contactList.add({
           id: Math.floor(Math.random()*110000),
           name: nameField.val(),
           age: ageField.val(),
           city: cityField.val()
       });
       clearFields();
       refreshCallbacks();
    });

    editBtn.click(function() {
       var item = contactList.get('id', idField.val());
       item.values({
           id:idField.val(),
           name: nameField.val(),
           age: ageField.val(),
           city: cityField.val()
       });
       clearFields();
       editBtn.hide();
       addBtn.show();
    });

    function refreshCallbacks() {
        // Needed to add new buttons to jQuery-extended object
        removeBtns = $(removeBtns.selector);
        editBtns = $(editBtns.selector);

        removeBtns.click(function() {
           var itemId = $(this).closest('tr').find('.id').text();
           contactList.remove('id', itemId);
        });

        editBtns.click(function() {
           var itemId = $(this).closest('tr').find('.id').text();
           var itemValues = contactList.get('id', itemId).values();
           idField.val(itemValues.id);
           nameField.val(itemValues.name);
           ageField.val(itemValues.age);
           cityField.val(itemValues.city);

           editBtn.show();
           addBtn.hide();
        });
    }
</script>

<%include file="bottom.mak"/>