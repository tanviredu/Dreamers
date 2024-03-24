
var a = document.getElementById("head1");

a.innerText = "Welcome to Document Object Model";
a.style.color = "darkred";
a.style.fontFamily = "Calibri";
a.style.fontSize = "50px";
a.style.background = "cyan";


var b = document.querySelector("#head2");

b.innerText = "Document Object Model is powerfull!";

function fun1(){
	b.style.background = "black";
	b.style.color = "white";
	b.style.padding = "20px";
}

var im1 = document.getElementById("im1");

im1.src = "LK7.jpg";


var im2 = document.getElementById("im2");
var btn2 = document.getElementById("btn2");
var btn1 = document.getElementById("btn1");
btn2.style.display = "none";

function showIt() {	
	im2.src = "jaflong.jpg";
	btn1.style.display = "none";
	btn2.style.display = "";
}

function hideIt() {	
	im2.src = "";
	btn1.style.display = "";
	btn2.style.display = "none";
}
