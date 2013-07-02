<%include file="top.mak"/>
 <script type='text/javascript'>
        $(document).ready(function() {
            //  Randomly Create Data Rows
            for (var i = 0; i < 50; i++) {
              var tr = $('<tr>' +
                '<td>Value' + Math.floor(Math.random() * 500) + '</td>' +
                '<td>' + Math.floor(Math.random() * 500) + ' </td>' +
                '<td>' + (Math.random() > 0.5 ? 'yes' : 'no') + '</td>' +
                '<td>' + (Math.random() <= 0.333 ? 'Item 1' : Math.random() > 0.5 ? 'Item 2' : 'Item 3') + '</td>' +
                '<td></td>' +
                '<td>' + parseInt(10 + Math.random() * 18) + '/' + parseInt(10 + Math.random() * 2) + '/2009</td>' +
                '<td></td>' +
                '</tr>');
              $('#demotable1 tbody').append(tr);
            }

          // Initialise Plugin
            var options1 = {
                additionalFilterTriggers: [$('#onlyyes'), $('#onlyno'), $('#quickfind')],
                clearFiltersControls: [$('#cleanfilters')],
                matchingRow: function(state, tr, textTokens) {
                  if (!state || !state.id) {
                    return true;
                  }
                  var child = tr.children('td:eq(2)');
                  if (!child) return true;
                  var val = child.text();
                  switch (state.id) {
                  case 'onlyyes':
                    return state.value !== true || val === 'yes';
                  case 'onlyno':
                    return state.value !== true || val === 'no';
                  default:
                    return true;
                  }
                }
            };

            $('#demotable1').tableFilter(options1);
        });
    </script>
<div id="main_page">
	<div id="left"> 
		<div id="nav">
			<ul>
				% for row in menu_left_list:
					<li><a href="${row[0]}" class="indent${row[2]}" id="homenav">${row[1]}</a></li>
				% endfor
			</ul>
		</div>
	</div>
	<div id="right">
		<h2>Filtry</h2>
		<label><span>Imię:</span><input type="text" name="price-min"></label>
		<label><span>Nazwisko:</span><input type="text" name="price-max"></label>
		<label><span>Stanowisko:</span><input type="text" name="price-max"></label>
		<label><span>Strona</span><input type="text" name="price-max"></label>
	</div>
	<div id="center">
      <div id="people_list_wrapper">
         <table id="people_list">
				<colgroup>
					<col width="60px;"/>
					<col width="140px;"/>
					<col width="180px;"/>
					<col width="70px;"/>
					<col width="63px;"/>
					<col width="52px;"/>
					<col width="43px;"/>
				</colgroup>
            <thead>
               <tr>
                  <th>ID</th>
                  <th>Imię</th>
                  <th>Nazwisko</th>
                  <th>Stanowisko</th>
                  <th></th>
                  <th></th>
                  <th></th>
               </tr>
            </thead>
            <tbody>
            </tbody>
         </table>
      </div>
    </div>
	</div>
</div>	
<%include file="bottom.mak"/>