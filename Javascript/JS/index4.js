var mystring = "Hello world";
console.log(mystring);
var mystring = 'Hello world';
console.log(mystring);

var mystring = 'my name is "Tanvir" ';
console.log(mystring);

var mystring = "my name is \n Tanvir";
console.log(mystring);

// find the length of a string

var mystring = "Tanvir Rahman"

lenofstring = mystring.length;
console.log(lenofstring)

// indexing

x = "Tanvir Rahman"

console.log(x[0])
console.log(x[1])

// convert to  upper case
y = x.toUpperCase()
console.log(y)

y = x.toLowerCase()
console.log(y)


x = "     Tanvir Rahman      "
y = x.trim()
console.log(y)

// substring
x = "Tanvir Rahman"
whichindextostart = 7
howmanychar = 6
z = x.substr(whichindextostart,howmanychar)
console.log(z)

x = "Tanvir Rahman"
z = x.replace("Rahman","Ahmed")
console.log(z)

// concat
x = "Tanvir"
y = x.concat(" ","Rahman"," ","Ornob")
console.log(y)