

var mark = prompt("Enter Mark");

document.write("Entered Mark: ",mark);
document.write("<br><br>");

if(mark>=80 && mark<=100){
	document.write("Grade: A+<br>GPA: 5.00");
}
else if(mark>=70 && mark<80){
	document.write("Grade: A<br>GPA: 4.50");
}
else if(mark>=60 && mark<70){
	document.write("Grade: A-<br>GPA: 4.00");
}
else if(mark>=50 && mark<60){
	document.write("Grade: B<br>GPA: 3.50");
}
else if(mark>=40 && mark<50){
	document.write("Grade: C<br>GPA: 3.00");
}
else if(mark>=0 && mark<40){
	document.write("Grade: F<br>GPA: 0.00");
}
else{
	document.write("Invalid Mark! Please enter a mark between 0-100");
}

