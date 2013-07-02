//////////////////////////////////////////
// Kreator zastepstw online		//
// Autor: Kamil Danak				//
// Email: kamilx3@gmail.com		//
// Ostatnia modyfikacja: 11.02.2012	//
//////////////////////////////////////////
var table_absent_teacher_rows=[]
var table_replace_teacher_rows=[]
var table_duty_rows=[]
var table_exemption_rows=[]
var table_ltc_rows=[]
var table_ltc2_rows=[]

Array.prototype.remove = function(from, to) {
  var rest = this.slice((to || from) + 1 || this.length);
  this.length = from < 0 ? this.length + from : from;
  return this.push.apply(this, rest);
};
function AddItemsTM(DropDownList,Array) // To Many
{
	var dropdown;
	for (dropdown=0;dropdown<DropDownList.length;dropdown++)
	{
		AddItems(document.getElementById(DropDownList[dropdown]),Array);
	}
}
function AddItems(DropDownList,Array)
{
	for (itemid=0;itemid<=Array.length-1;itemid++)
	{
		AddItem(DropDownList,Array[itemid])
	}
}
function AddItem(DropDownList,Text)
{
	var opt = document.createElement("option");
	DropDownList.options.add(opt);
	opt.text = Text;
}
//////////////////////////////////
// Dodawanie danych do tabeli	//
//////////////////////////////////
function addToTable1(table,table2){
	var row = table.insertRow(table.rows.length);
	var x=0
	while (table_absent_teacher_rows.indexOf(x)!=-1) {
		x++;
	}	
	table_absent_teacher_rows.push(x);	
	addCell3(row,'delete',i2,"0",'1',x,table,1);
	i=10
	for (var i2=9; i2>=2; i2--) {
		//addCell2(row,"button",i2,"0",'1','82px');
		addCell3(row,"button",i2,"0",'1',x,table,1,'82px');
	}
	i=1
	addCell2(row,'input',i2,"0",'1','130px');
	i=0
	addCell2(row,'select','',teacher_array,'1','109px');
	refresh();
}
function addToTable4(table,table2){
	var row = table.insertRow(table.rows.length);
	var x=0
	while (table_replace_teacher_rows.indexOf(x)!=-1) {
		x++;
	}
	table_replace_teacher_rows.push(x);	
	addCell3(row,'delete',i2,"0",'1',x,table,4);
	i=10
	for (var i2=9; i2>=2; i2--) {
		addCell2(row,'select','',class_array,'1','82px');
	}
	i=1
	addCell2(row,'input',i2,"0",'1','130px');
	i=0
	addCell2(row,'select','',teacher_array,'1','109px');
	refresh();
}

function addToTable2(table) {
	var row = table.insertRow(table.rows.length);
	var x=0
	while (table_duty_rows.indexOf(x)!=-1) {
		x++;
	}
	table_duty_rows.push(x);	
	addCell3(row,'delete',"","0",'1',x,table,2);
	addCell2(row,'select','',teacher_array,'1','109px');
	addCell2(row,'input',"","0",'1','130px');
	addCell2(row,'select','',teacher_array,'1','109px');
	refresh();
}
function addToTable5(table) {
	var row = table.insertRow(table.rows.length);
	var x=0
	while (table_exemption_rows.indexOf(x)!=-1) {
		x++;
	}
	table_exemption_rows.push(x);
	addCell3(row,'delete',"","0",'1',x,table,5);
	addCell2(row,'select','',["1","2","3","4","5","6","7","8"],'1','50px');
	addCell2(row,'select','',class_array,'1','82px');
	refresh();
}
function addToTable6(table) {
	var row = table.insertRow(table.rows.length);
	var x=0
	while (table_ltc_rows.indexOf(x)!=-1) {
		x++;
	}
	table_ltc_rows.push(x);	
	addCell3(row,'delete',"","0",'1',x,table,6);
	addCell2(row,'select','',["1","2","3","4","5","6","7","8"],'1','50px');
	addCell2(row,'select','',class_array,'1','82px');
	refresh();
}
function addToTable7(table) {
	var row = table.insertRow(table.rows.length);
	var x=0
	while (table_ltc2_rows.indexOf(x)!=-1) {
		x++;
	}
	table_ltc2_rows.push(x);	
	addCell3(row,'delete',"","0",'1',x,table,7);
	addCell2(row,'select','',["1","2","3","4","5","6","7","8"],'1','50px');
	addCell2(row,'select','',class_array,'1','82px');
	refresh();
}
function addCell2(row,type,value,array,span,width){
	addCell3(row,type,value,array,span,0,0,0,width);
}
function addCell3(row,type,value,array,span,num,table,table2,width){
	var cell0 = row.insertCell(0);
	span = typeof(span) != 'undefined' ? span : "";
	width = typeof(span) != 'undefined' ? width : "";
	if(span!="") {
		cell0.colSpan=span;
	}
	if(width!="") {
		cell0.style.width = width;
	}
	if (type=="delete"){
		var element0 = document.createElement("button");
	}
	else{
		var element0 = document.createElement(type);
	}
	if (type == 'select') {
		AddItems(element0,array);	
		element0.value=value;
		element0.onchange=function(){refresh();};
		element0.style.width = "100%";
	}
	else if (type == "text"){
		element0 = document.createTextNode(value);
		cell0.style.backgroundColor = "#3333cc";
	}
	else if (type == "delete"){
		element0.value="";
		element0.style.height = "20px";
		element0.onclick=function(){removeRow(table,num,table2);};
	}
	else if (type == "button"){
		element0.style.width = "90%";
		element0.style.height = "20px";
		element0.style.marginLeft = "10%";
		element0.style.marginRight = "10%";
		element0.value="";
		element0.onclick=function(){change(table,num,table2,value);};
	}
	else{
		element0.style.width = "100%";
		element0.value=value;
		element0.oninput=function(){refresh();};
	}
	cell0.appendChild(element0);
}

function addCell(row,type,value,array,span){
	var cell0 = row.insertCell(0);
	span = typeof(span) != 'undefined' ? span : "";
	if(span!="") {
		cell0.colSpan=span;
	}
	if (type=="delete"){
		var element0 = document.createElement("button");
	}
	else{
		var element0 = document.createElement(type);
	}
	if (type == 'select') {
		AddItems(element0,array);	
		element0.value=value;
		element0.onchange=function(){refresh();};
	}
	else if (type == "text"){
		element0 = document.createTextNode(value);
	}
	else if (type == "delete"){
		element0.value="";
		element0.onclick=function(){removeRow(table,row);};
	}
	else{
		element0.value=value;
		element0.oninput=function(){refresh();};
	}
	cell0.appendChild(element0);
}
function removeRow(table, rowID, table2){
	try {
		if (table2==1){
			var x=-1;
			while (table_absent_teacher_rows[x]!=rowID){
				x++;
			}
			//alert(rowID+"    "+x);
			table.deleteRow(x);
			table_absent_teacher_rows.remove(x);
		}
		else if (table2==2){
			var x=-1;
			while (table_duty_rows[x]!=rowID && x<20){
				x++;
			}
			table.deleteRow(x);
			table_duty_rows.remove(x);			
		}
		else if (table2==4){
			var x=-1;
			while (table_replace_teacher_rows[x]!=rowID){
				x++;
			}
			table.deleteRow(x);
			table_replace_teacher_rows.remove(x);			
		}	
		else if (table2==5){
			var x=-1;
			while (table_exemption_rows[x]!=rowID){
				x++;
			}
			table.deleteRow(x);
			table_exemption_rows.remove(x);			
		}	
		else if (table2==6){
			var x=-1;
			while (table_ltc_rows[x]!=rowID){
				x++;
			}
			table.deleteRow(x);
			table_ltc_rows.remove(x);			
		}
		else if (table2==7){
			var x=-1;
			while (table_ltc2_rows[x]!=rowID){
				x++;
			}
			table.deleteRow(x);
			table_ltc2_rows.remove(x);			
		}			

		refresh();
	}catch(e) {
		alert(e);
	}
}
function change(table, rowID, table2, value2){
	try {
			var x=-1;
			while (table_absent_teacher_rows[x]!=rowID){
				x++;
			}
			//alert(x+"   "+value2);		
		var row = table.rows[x];
		if (row.cells[value2].childNodes[0].style.backgroundColor==''){
			row.cells[value2].childNodes[0].style.backgroundColor='rgb(224, 27, 106)';
		}
		else{
			row.cells[value2].childNodes[0].style.backgroundColor='';
			row.cells[value2].childNodes[0].value=	"";
		}
		refresh();
			
	}catch(e) {
		//alert(e);
	}
}
//////////////////////////////////////////
//	Usuwanie danych z tabeli	//
//////////////////////////////////////////
function deleteRow(tableID, cell2check) {
	try {
		var table = document.getElementById(tableID);
		var rowCount = table.rows.length;

		for(var i=0; i<rowCount; i++) {
		var row = table.rows[i];
		var chkbox = row.cells[cell2check].childNodes[0];
		if(null != chkbox && true == chkbox.checked) {
			table.deleteRow(i);
			rowCount--;
			i--;
			}
		}
	}catch(e) {
		alert(e);
	}
}
function deleteAll(tableID) {
	try {
		var table = document.getElementById(tableID);
		var rowCount = table.rows.length;

		for(var i=0; i<rowCount; i++) {
			table.deleteRow(i);
			rowCount--;
			i--;
		}
	}catch(e) {
		alert(e);
	}	
}
function getValues(Array2) {
var result=new Array();
for(var i=0;i<Array2.length;i++) {
	result.push(document.getElementById(Array2[i]).value);
}
return result
}

function getdata(tableid, columns, number) {
	try{
		var table = document.getElementById(tableid);
		var array_column=new Array();

		for(var i=0; i<table.rows.length; i++) {
			var row = table.rows[i];
			var array_row=new Array();
			if (row.cells[0].childNodes[0].value != undefined){
				if(typeof(number) != 'undefined'){
					array_row.push(i+1);
				}
				for (x=0;x<columns;x++){
					array_row.push(row.cells[x].childNodes[0].value);
				}
			array_column.push(array_row);
			}
		}
	}catch(e) {
		alert(e);
	}
	return array_column
}

//function antyzaz(evt){
//        if(evt.which==1) return false
//}
//document.onmousedown=antyzaz;<20