<%include file="top.mak"/>
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
   </div>
   
   <div id="center">
      <div id="substitutions_list_wrapper">
         <table id="substitutions_list">
            <thead>
               <tr>
                  <th width="60px;">ID</th>
                  <th width="450px;">Zastępstwa na dzień</th>
                  <th></th>
                  <th></th>
                  <th></th>
               </tr>
            </thead>
            <tbody>
               % for row in substitutions:
                  <tr>
                     <th>${row[0]}</th>
                     <th>${row[1]}</th>
                     <th><a href="${row[2]}">Podgląd</a></th>
                     <th><a href="${row[3]}">Edytuj</a></th>
                     <th><a href="${row[4]}">Usuń</a></th>
                  </tr>
               % endfor
            </tbody>
         </table>
      </div>
   </div>
</div>	
<%include file="bottom.mak"/>
