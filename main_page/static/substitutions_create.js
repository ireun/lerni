var lessons=[["T. Szyjkowski",
["", "", "2bch", "2bch", "", "", "", ""],
["", "", "2bch", "", "", "", "", ""],
["2bch", "", "", "", "", "", "", ""],
["", "", "", "", "", "", "", ""],
["", "", "2bch", "", "", "", "", ""]],
["B. Strączek",
["2gm", "1bch", "2gm", "2mat2", "2mat1", "", "", ""],
["2mat1", "1bch", "1bch", "2mat2", "2gm", "3pol", "3pol", ""],
["", "3pol", "3pol", "", "1bch", "2gm", "2gm", ""],
["2mat2", "2mat2", "2gm", "3pol", "3pol", "", "2mat1", ""],
["2mat1", "2mat1", "2mat2", "", "", "", "", ""]],
["J. Wolszczak",
["3gm", "3gm", "", "2ls", "2pol", "1mat2", "2pol", ""],
["2rpol", "2rpol", "", "2ls", "", "", "", ""],
["2pol", "2pol", "3gm", "3gm", "", "", "", ""],
["1mat2", "2pol ", "2pol", "3gm", "2ls", "2ls", "", ""],
["", "", "2ls", "1mat2", "1mat2", "", "", ""]],
["A. Siechowska",
["1mat1", "3ls", "", "1mat2", "3ls", "1gm", "1gm", ""],
["3ls", "1gm", "", "", "", "", "", ""],
["1gm", "3ls", "3ls", "1mat1", "1mat1", "1bch", "", ""],
["1mat1", "1mat1", "3ls", "3ls", "", "", "", ""],
["", "", "", "", "3ls", "1gm", "", ""]],
["B. Mozgawa",
["3inf", "3inf", "1ls", "3bch", "3bch", "1pol", "", ""],
["1ls", "3inf", "1pol", "3bch", "", "", "", ""],
["1rpol", "3inf", "", "1pol", "3bch", "", "1ls", ""],
["1pol", "", "3bch", "3inf", "1ls", "1ls", "", ""],
["1rpol", "", "", "", "", "", "", ""]]]

var class_basic_array=["1b","1bch","1c","1d","1e1","1e2","1gm","1ls",
              "1mat1","1mat2","1pol","1rchem1","1rchem2","1rfiz1",
              "1rfiz2","1rgeo","1rinf","1rpol","1rwos","2b","2bch",
              "2c","2d","2e","2gm","2ls","2mat1","2mat2","2pol","2rchem1",
              "2rchem2","2rgeo","2rinf","2rpol","2rwos","3b","3bch","3c",
              "3d","3gm","3inf","3ls","3pol"]
var class_array=[""]
for (var ff=0; ff<class_basic_array.length; ff++) {
	class_array.push(class_basic_array[ff]);
	class_array.push(class_basic_array[ff]+"1");
	class_array.push(class_basic_array[ff]+"2");
}


function group_check(text) {
	for (var ff=0; ff<class_basic_array.length; ff++) {
		text=text.replace(class_basic_array.sort().reverse()[ff],"");
	}
	return text;
}

function get_lessons(teacher) {
	for (var uu=0; uu<lessons.length; uu++) {
		if (lessons[uu][0] == teacher){
			return lessons[uu];
		}
	}
}
var teacher_array=[]
function getTeacherArray(){		// ZROBIC NORMALNIE
	teacher_array=[""]
	for (x=0;x<lessons.length;x++){
		teacher_array.push(lessons[x][0])
	}	
}

getTeacherArray()



function show()
{
$('#datepicker').datepicker({
	dateFormat: 'd MM yy r (DD)',
	dayNames: ['niedziela', 'poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota'],
	monthNames: ['stycznia','lutego','marca','kwietnia','maja','czerwca','lipca','sierpnia','września','października','listopada','grudnia'],
});
$('#datepicker').datepicker( "setDate" ,+1);
var zdate = $('#datepicker').datepicker('getDate');
if (zdate.getUTCDay()==5){
	$('#datepicker').datepicker( "setDate" ,+3);
}
if (zdate.getUTCDay()==6){
	$('#datepicker').datepicker( "setDate" ,+2);
}

$("#dialog").dialog({
	autoOpen: false,
	width: 257,
	height: 120,
	modal: true,
	buttons: {
		"Ok": function() {			
			var table=$(this).data('table')
			var rowid=$(this).data('rowid')
			var cellid=$(this).data('cellid')
			moreAction(table,rowid,cellid,lesson1.value,lesson2.value,true);
			$(this).dialog("close");
		}, 
		"Cancel": function() {
			var table=$(this).data('table')
			var rowid=$(this).data('rowid')
			var cellid=$(this).data('cellid')
			moreAction(table,rowid,cellid,lesson2.value,lesson2.value,false);			
			$(this).dialog("close");
		} 
	}  

});
/*
AddItemsTM(["lesson1","lesson2"],class_array);
class_array.push("więcej");
refresh();*/
}