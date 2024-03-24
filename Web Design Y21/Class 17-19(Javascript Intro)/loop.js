
for(var i=1; i<=10; i++){
	document.write(i," ");
}

document.write("<br><br>");

for(var i=1; i<=20; i++){
	if(i%2==0){
		document.write(i," ");
	}
}

document.write("<br><br>");


function add(n1,n2){
	return n1+n2;
}

function greetings(){
	document.write("Welcome to JS Function");
}

greetings();

document.write("<br><br>");

var a = 12;
var b = 5;

document.write(a,"+",b,"=",add(a,b));

document.write("<br><br>");
document.write("<br><br>");



var a = [3,4,5,6,7]

document.write(a);
document.write("<br><br>");
document.write(a[1]);

document.write("<br><br>");

var s = 0;

for(var i=0; i<a.length; i++){
	s+=a[i];
}

document.write(s);