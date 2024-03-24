
var display = document.querySelector("#display");


function showIt(m){
	var n = display.value+m;
	display.value = n;
}


function cleanIt() {
	display.value = "";
}

function result() {
	var b = eval(display.value);
	display.value=b;
}
