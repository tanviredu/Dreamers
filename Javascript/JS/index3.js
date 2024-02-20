// data type
// number
// both data type are number
// javascript does not have separate data type
// for floating and interger value
var x = 10
var x = 10.2
var x = 25/0
console.log(x)
// output = infinity
var y = Infinity 
// infinity itself a number

var x = 100
// convert it to the string
// toString apply to number
// to convert it to the string
var y = x.toString()

var x = 10.2
var y = x.toString()
console.log(y)
// convert the number to binary
x = 10
var y = x.toString(2)
console.log(y)
// to precision
x = 3.11415134565
console.log(x)
y = x.toPrecision(3) // and it will convert to the string
console.log(y)
x = 3.1415
y = parseInt(x)
console.log(y)
console.log(parseFloat(x))  // this will convert the string
							// into numbers
x = "a"
console.log(isNaN(x)) // true
x = "1"
console.log(isNaN(x)) // false






