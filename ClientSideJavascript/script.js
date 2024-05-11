document.getElementById("test2").innerHTML = new Date().getFullYear();
var data = document.getElementsByClassName("tagtest")[0].getElementsByTagName("p")
//data[0].textContent = "HelloFirst";
//data[1].textContent = "HelloSecond";
//data[2].textContent = "HelloThird";
//data[3].textContent = "Hellofourth";

var data2 = document.querySelector("div.tagtest");

// Get all the <p> elements inside the second <div>
var ptags = data2.querySelectorAll("p");

ptags[0].textContent = "First";
ptags[1].textContent = "Second";
ptags[2].textContent = "Third";
ptags[3].textContent = "Fourth";

//console.log(document.querySelector("footer div").childNodes[0].innertext)
//console.log(document.querySelector("footer div").childNodes[1])
document.querySelector("footer div").childNodes[1].textContent = "Hi I am inside span"

//var footerSpan = document.querySelector("footer div span");
//footerSpan.textContent = "Hi";

console.log(document.querySelector("footer div").childNodes[1].classList)
document.querySelector("footer div").childNodes[1].classList.remove("hello");
console.log(document.querySelector("footer div").childNodes[1].classList)
document.querySelector("footer div").childNodes[1].classList.add("myfont");

var items = document.querySelectorAll("#mytable tbody tr");
items[1].remove()