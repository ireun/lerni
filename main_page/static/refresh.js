function refresh()
{
   var date = $('#datepicker').datepicker('getDate');
   var dayOfWeek = date.getUTCDay();
   var absent=[[],[],[],[],[],[],[],[]];
	var replace=[[],[],[],[],[],[],[],[]];
	var errors="";
	checkForDuplicateTeacher("absent_table_edit2")
	checkForDuplicateTeacher("replace_table_edit2")
	//checkForMore()   // returns error have to be uncommented
	///////////////////////////////////
	// CHECK ABSENT TEACHERS LESSONS	//
	///////////////////////////////////
	//try {
		var table = document.getElementById("absent_table_edit2");
		for(var rowid=0; rowid<table.rows.length; rowid++) {
			var row = table.rows[rowid];
			if (row.cells[0].childNodes[0].value!=""){
				for (cellid=2;cellid<10;cellid++){
					var lesson=get_lessons(row.cells[0].childNodes[0].value)[dayOfWeek+1][cellid-2];
					if (row.cells[cellid].childNodes[0].style.backgroundColor==''){
						row.cells[cellid].childNodes[0].value="";
					}else{
						row.cells[cellid].childNodes[0].value=lesson;
						if (lesson.indexOf("/")!=-1){
							absent[cellid-2].push(lesson.split("/")[0])
							absent[cellid-2].push(lesson.split("/")[1])
						}
						else{
							absent[cellid-2].push(lesson)
						}
					}
				}
			}else{
				for (cellid=1;cellid<10;cellid++){
					row.cells[cellid].childNodes[0].value="";
					row.cells[cellid].childNodes[0].style.backgroundColor='';
				}
			}
		}
	//}catch(e) {
	//	alert(e);
	//}
	//////////////////////////////////////
	// CHECK REPLACE TEACHERS LESSONS	//
	//////////////////////////////////////
	try {
		var table = document.getElementById("replace_table_edit2");
		for(var rowid=0; rowid<table.rows.length; rowid++) {
			var row = table.rows[rowid];
			za_klase_array=[]
			if (row.cells[0].childNodes[0].value!=""){
				for (cellid=2;cellid<10;cellid++){
					var lesson=get_lessons(row.cells[0].childNodes[0].value)[dayOfWeek+1][cellid-2];
					if (lesson!="" && row.cells[cellid].childNodes[0].value!="" && za_klase_array.indexOf(lesson)==-1){
						if (lesson.indexOf("/")!=-1){
							za_klase_array.push(lesson.split("/")[0])
							absent[cellid-2].push(lesson.split("/")[0])
							za_klase_array.push(lesson.split("/")[1])
							absent[cellid-2].push(lesson.split("/")[1])
						}
						else{
							za_klase_array.push(lesson);
							absent[cellid-2].push(lesson);	
						}								
					}
					var red=false
					if(row.cells[cellid].childNodes[0].value!=""){
						if (replace[cellid-2].indexOf(row.cells[cellid].childNodes[0].value)==-1){
							for (x=0;x<replace[cellid-2].length;x++){
								if (getClass(replace[cellid-2][x],row.cells[cellid].childNodes[0].value).length!=2){
									if(replace[cellid-2][x].substr(0,replace[cellid-2][x].length-1)==row.cells[cellid].childNodes[0].value.substr(0,row.cells[cellid].childNodes[0].value.length-1)){
										red=red;
									}else{
										red=true;
									}								
								}
							}						
						}else{
							red=true;
						}
						if (red){
							row.cells[cellid].style.backgroundColor='rgb(224, 27, 106)';
						}else{
							if (row.cells[cellid].childNodes[0].value.indexOf("/")!=-1){
								replace[cellid-2].push(row.cells[cellid].childNodes[0].value.split("/")[0])
								replace[cellid-2].push(row.cells[cellid].childNodes[0].value.split("/")[1])
							}
							else{
								replace[cellid-2].push(row.cells[cellid].childNodes[0].value);
							}
						}
					}
				}
			}else{
				for (cellid=1;cellid<10;cellid++){
					row.cells[cellid].childNodes[0].value="";
					row.cells[cellid].childNodes[0].style.backgroundColor='';
				}
			}
			var za_klase = za_klase_array.join(",");
			row.cells[1].childNodes[0].value=za_klase;
		}
	}catch(e) {
		alert(e);
	}
	///////////////////////////
	// Additional exemptions //
	///////////////////////////
	/*
	
	var table = document.getElementById("table_ltc");
	for(var rowid=0; rowid<table.rows.length; rowid++) {
		var row = table.rows[rowid];
		if (row.cells[0].childNodes[0].value!=""){
			//alert(absent[row.cells[1].childNodes[0].value-1]);
			alert(include(absent[row.cells[1].childNodes[0].value-1], row.cells[0].childNodes[0].value));
			if (include(absent[row.cells[1].childNodes[0].value-1], row.cells[0].childNodes[0].value)!=-1) {
				absent[row.cells[1].childNodes[0].value-1].remove(include(absent[row.cells[1].childNodes[0].value-1], row.cells[0].childNodes[0].value));
			}			
			//absent[row.cells[1].childNodes[0].value-1].push(row.cells[0].childNodes[0].value);
		}
	}	

	var table = document.getElementById("table_ltc2");
	for(var rowid=0; rowid<table.rows.length; rowid++) {
		var row = table.rows[rowid];
		if (row.cells[0].childNodes[0].value!=""){
			absent[row.cells[1].childNodes[0].value-1].push(row.cells[0].childNodes[0].value);
		}
	}	
	*/
function include(arr, obj) {
	for(var i=0; i<arr.length; i++) {
		if (arr[i] == obj){
			return i;
		}
	}
	return -1;
}
	
	/////////////////////////////
	// JOIN ABSENT & REPLACING //
	/////////////////////////////
	var absent_full=[[],[],[],[],[],[],[],[]];
	var replace_full=[[],[],[],[],[],[],[],[]];
	for (y=0;y<7;y++){
		for (x=0;x<absent[y].length;x++){
			if (absent[y][x]!=""){
				if (group_check(absent[y][x])==""){
					absent_full[y].push(absent[y][x]+"1");
					absent_full[y].push(absent[y][x]+"2");
				}else{
					absent_full[y].push(absent[y][x])
				}
			}
		}
		for (x=0;x<replace[y].length;x++){
			if (replace[y][x]!=""){
				if (group_check(replace[y][x])==""){
					replace_full[y].push(replace[y][x]+"1");
					replace_full[y].push(replace[y][x]+"2");
				}else{
					replace_full[y].push(replace[y][x])
				}
			}
		}
	}
	
	for (y=0;y<7;y++){
		for (x=replace_full[y].length-1;x>-1;x--){
			if (absent_full[y].indexOf(replace_full[y][x])!=-1){
				absent_full[y].remove(absent_full[y].indexOf(replace_full[y][x]));
				replace_full[y].remove(replace_full[y].indexOf(replace_full[y][x]));
			}
		}	
	}
	for (y=0;y<7;y++){
		var absent_full=order(absent_full)
		var replace_full=order(replace_full)
		var x=0;
		while (x<absent_full[y].length-1){
			if (getClass(absent_full[y][x],absent_full[y][x+1]).length!=2){
				absent_full[y].push(absent_full[y][x].substr(0,absent_full[y][x].length-1));
				absent_full[y].remove(x+1)
				absent_full[y].remove(x)
				var absent_full=order(absent_full)
				var replace_full=order(replace_full)
				var x=-1
			}
		x++
		}
		var x=0;
		while (x<replace_full[y].length-1){
			if (getClass(replace_full[y][x],replace_full[y][x+1]).length!=2){
				replace_full[y].push(replace_full[y][x].substr(0,replace_full[y][x].length-1));
				replace_full[y].remove(x+1)
				replace_full[y].remove(x)
				var replace_full=order(replace_full)
				var replace_full=order(replace_full)
				var x=-1
			}
		x++
		}
	}	
	
	for (y=0;y<7;y++){
		for (x=0;x<replace_full[y].length;x++){
			errors=errors+"Zastępstwo dla klasy "+replace_full[y][x]+" na lekcji "+(y+1)+" mimo braku nieobecności nauczyciela.</br>";
		}
	}
	absent=absent_full;
	replace=absent_full;

	///////////////////////////
	// Additional exemptions //
	///////////////////////////
	
	//var table = document.getElementById("table_exemption");
	//for(var rowid=0; rowid<table.rows.length; rowid++) {
	//	var row = table.rows[rowid];
	//	if (row.cells[0].childNodes[0].value!=""){
	//		absent[row.cells[1].childNodes[0].value-1].push(row.cells[0].childNodes[0].value);
			//@!!!
			//alert(include(absent, "2rpol"));
		//if (row.cells[0].childNodes[0].value!=""){
		//	if (row.cells[cellid].childNodes[0].style.backgroundColor=='rgb(224, 27, 106)'){  /// nie dziala pod opera
		//		row.cells[cellid].childNodes[0].value=lesson;
		//		if (lesson.indexOf("/")!=-1){
		//			absent[cellid-2].push(lesson.split("/")[0])
		//			absent[cellid-2].push(lesson.split("/")[1])
		//		}
		//		else{
		//			absent[cellid-2].push(lesson)
		//		}
		//	}else{
		//		row.cells[cellid].childNodes[0].value="";
		//	}
		//}else{
		//	for (cellid=1;cellid<10;cellid++){
		//		row.cells[cellid].childNodes[0].value="";
		//		row.cells[cellid].childNodes[0].style.backgroundColor='';
		//	}
		//}	
		///@!!!
	//	}
	//}
	
	absent_teacher_array = getdata("absent_table_edit2", 10, 1);
	rep_teacher_array = getdata("replace_table_edit2", 10, 1);
	duty_teacher_array = getdata("duty_table_edit2", 3, 1);
	document.getElementById("errors").innerHTML=errors;
	//alert(absent)
	document.getElementById("released").innerHTML="L1: "+absent[0].join(", ")+"<br />L2: "+absent[1].join(", ")+"<br />L3: "+absent[2].join(", ")+"<br />L4: "+absent[3].join(", ")+"<br />L5: "+absent[4].join(", ")+"<br />L6: "+absent[5].join(", ")+"<br />L7: "+absent[6].join(", ")+"<br />L8: "+absent[7].join(", ");
   //makeTablePreview(absent);
	//makeUploadButton(absent);
}
function order(array){
	array2=[];
	for (var x=0;x<array.length;x++){
		array3=[];
		for (var y=0;y<array[x].sort().length;y++){
			array3.push(array[x].sort()[y]);
		}
		array2.push(array3);
	}
	return array2
}
function changeToList(table,rowid,cellid){
	var row = table.rows[rowid];
	var element0 = document.createElement("select");
	AddItems(element0,class_array);	
	element0.value="";
	element0.style.width = "100%";
	element0.onchange=function(){refresh();};
	
	row.cells[cellid].removeChild(row.cells[cellid].childNodes[0]);
	row.cells[cellid].appendChild(element0);
}
function moreAlert(table,rowid,cellid){
	$('#dialog')
		.data('table', table)
		.data('rowid', rowid)
		.data('cellid', cellid)
		.dialog('open');
}
function moreAction(table,rowid,cellid,lesson1,lesson2,okClicked){
	document.getElementById("lesson1").value="";
	document.getElementById("lesson2").value="";
	var row = table.rows[rowid];
	if (okClicked && lesson1!="" && lesson2!=""){
		if(lesson1!=lesson2){
			if (getClass(lesson1,lesson2).length==2){
				var element0 = document.createElement("button");
				element0.style.width = "100%";
				element0.innerHTML=lesson1+"/"+lesson2;
				element0.value=lesson1+"/"+lesson2;
				element0.onclick=function(){changeToList(table,rowid,cellid);};
				row.cells[cellid].removeChild(row.cells[cellid].childNodes[0]);
				row.cells[cellid].appendChild(element0);
			}else{
				row.cells[cellid].childNodes[0].value=getClass(lesson1,lesson2);
			}
		}else{
			row.cells[cellid].childNodes[0].value=lesson1;
		}
	}else{
		row.cells[cellid].childNodes[0].value="";
	}
	refresh()
}
function checkForMore(){
	try {
 		var date = $('#datepicker').datepicker('getDate');
   	var dayOfWeek = date.getUTCDay();
		var table = document.getElementById("table_replace_teachers");
		for(var rowid=0; rowid<table.rows.length; rowid++) {
			var row = table.rows[rowid];
			if (row.cells[0].childNodes[0].value!=""){
				for (cellid=2;cellid<10;cellid++){
					if (row.cells[cellid].childNodes[0].value=="więcej"){
						moreAlert(table,rowid,cellid)
					}
				}
			}
		}
	}catch(e) {
		alert(e);
	}	
}
function checkForDuplicateTeacher(tableID){
	var absent_teachers=[];
	try {
		var table = document.getElementById(tableID);
		for(var rowid=0; rowid<table.rows.length; rowid++) {
			var row = table.rows[rowid];
			if (row.cells[0].childNodes[0].value!=""){
				if (absent_teachers.indexOf(row.cells[0].childNodes[0].value)!=-1){
					for (cellid=0;cellid<10;cellid++){
						row.cells[cellid].style.backgroundColor='rgb(255, 0, 0)';
					}
				}else{
					absent_teachers.push(row.cells[0].childNodes[0].value);
					for (cellid=0;cellid<10;cellid++){
						row.cells[cellid].style.backgroundColor='';
					}
				}
			}else{
				absent_teachers.push(row.cells[0].childNodes[0].value);
				for (cellid=0;cellid<10;cellid++){
					row.cells[cellid].style.backgroundColor='';
				}
			}
		}
	}catch(e) {
		alert(e);
	}
}

function makeTablePreview(absent) {
	deleteAll("table_preview");
	addRow("table_preview",['LP','Nauczyciel','Przyczyna','Lekcja 1','Lekcja 2','Lekcja 3','Lekcja 4','Lekcja 5','Lekcja 6','Lekcja 7','Lekcja 8']);
	for(var i=0; i<absent_teacher_array.length; i++){
		addRow("table_preview",absent_teacher_array[i]);
	}
	while(i<row_min.value) {
		i++;
		addRow("table_preview",[i,"","","","","","","","","",""]);
	}
	rep_teacher=new Array('LP','Nauczyciel','Za klasę','Lekcja 1','Lekcja 2','Lekcja 3','Lekcja 4','Lekcja 5','Lekcja 6','Lekcja 7','Lekcja 8');
	addRow("table_preview",rep_teacher);
	for(var i=0; i<rep_teacher_array.length; i++){
		addRow("table_preview",rep_teacher_array[i]);
	}
	while(i<row_min.value) {
		i++;
		addRow("table_preview",[i,"","","","","","","","","",""]);
	}
	var galowy="";
	if (document.getElementById("dzien_galowy").checked){
	galowy="Dzień galowy! "
	}
	addRow("table_preview",[" Zwolnione klasy: "+
		"L1: "+absent[0].join(", ")+
		" L2: "+absent[1].join(", ")+
		" L3: "+absent[2].join(", ")+
		" L4: "+absent[3].join(", ")+
		" L5: "+absent[4].join(", ")+
		" L6: "+absent[5].join(", ")+
		" L7: "+absent[6].join(", ")+
		" L8: "+absent[7].join(", ")],["11"]);
		addRow("table_preview",["Uwagi: "+galowy+document.getElementById("comments").value],["11"])
	addRow("table_preview",["DYŻURY"],["11"])
	addRow("table_preview",["LP","Nauczyciel zastępujący","Zmiana - miejsce","Nauczyciel nieobecny"],["1","3","4","3"])
	for(var i=0; i<duty_teacher_array.length; i++){
		addRow("table_preview",duty_teacher_array[i],["1","3","4","3"]);
	}
	while(i<row2_min.value) {
		i++;
		addRow("table_preview",[i,"","",""],["1","3","4","3"])
	}
	document.getElementById("preview_day").innerHTML="na dzień: "+document.getElementById("datepicker").value;
}
function makeUploadButton(absent) {
	
	document.getElementById("lista_absent_teacher").value=absent_teacher_array;
	//document.getElementById("lista_rep_teacher").value=rep_teacher_array;
	//document.getElementById("lista_duty_teacher").value=duty_teacher_array;
	//document.getElementById("lista_row_min").value=row_min.value;
	//document.getElementById("lista_row2_min").value=row2_min.value;
	//document.getElementById("lista_comments").value=document.getElementById("comments");
	//document.getElementById("lista_dzien_galowy").value=document.getElementById("dzien_galowy").checked;
	//document.getElementById("lista_zwolnione").value=" Zwolnione klasy: "+"L1: "+absent[0].join(", ")+" L2: "+absent[1].join(", ")+" L3: "+absent[2].join(", ")+" L4: "+absent[3].join(", ")+" L5: "+absent[4].join(", ")+" L6: "+absent[5].join(", ")+" L7: "+absent[6].join(", ")+" L8: "+absent[7].join(", ");
	//document.getElementById("lista_data").value=document.getElementById("datepicker").value;
}
function getGroups(lesson, absent) {
	if (group_check(lesson)==""){
		if ((absent[x-2].indexOf(lesson+"1")==-1) && (absent[x-2].indexOf(lesson+"2")==-1)){
			return [lesson+"1",lesson+"2"];
		}
		if (absent[x-2].indexOf(lesson+"1")==-1){
			return [lesson+"1"];
		}
		if (absent[x-2].indexOf(lesson+"2")==-1){
			return [lesson+"2"];
		}
		return 0;
	}
	else{
		return [lesson];
	}
}
function getClass(lesson1, lesson2) {
	if (lesson1==lesson2){
		alert("DUPLICATED LESSON");
		return [];
	}
	else if (group_check(lesson1)=="" && group_check(lesson2)!="" && lesson1==lesson2.substr(0,lesson2.length-1)){
		return [lesson1];
	}
	else if (group_check(lesson2)=="" && group_check(lesson1)!="" && lesson1.substr(0,lesson1.length-1)==lesson2){
		return [lesson2];
	}
	else if (group_check(lesson1)=="1" && group_check(lesson2)=="2" && lesson1.substr(0,lesson1.length-1)==lesson2.substr(0,lesson2.length-1)){
		return [lesson1.substr(0,lesson1.length-1)];
	}
	else{
		return [lesson1,lesson2]
	}
}