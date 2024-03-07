// number
var x = "This result"
console.log(x+45+50)
console.log("25"/"5") // This will perform the mathmatical function
// but + sign wont do that . it will concat the string
console.log("25"+"5")
x = 100
console.log(x)
console.log(x.toString())
console.log(1000/0)  // Infinity

var x = 1234567
console.log(x.toString(2)) //binary
console.log(x.toString(8)) // octal
console.log(x.toString(16)) // hexa decimal
var x = 3.456777
console.log(x.toPrecision(3))
console.log(parseInt(x))
console.log(parseFloat(x))

console.log(isNaN("a")) // true
console.log(isNaN("1")) // false
console.log(isNaN(1))   //false
console.log(isNaN(2))   // false




// string
mystring = "Tanvir Rahman"
var ln = mystring.length 
console.log(ln)
mystring2 = "Tanvir \nRahman"
var ln = mystring2.length
console.log(ln)
console.log(mystring[0])
console.log(mystring[100])
console.log(mystring.toUpperCase())
console.log(mystring.toLowerCase())
var x = "     Tanvir Rahman    "
console.log(x.trim())
var x = "Bangladesh"

start_index = 0
end_index = 5
console.log(x.slice(start_index,end_index))
z = "Bangladesh"


// index to length
index = 0
length = 5
console.log(z.substr(index,5))

z = "Bangladesh"
x = z.replace("Ba","Br")
console.log(x)


x = "My "
z = x.concat("name ","is ","Tanvir ","Rahman ")
console.log(z)


// boolean

var y;
console.log(Boolean(x))   // false
var y = null
console.log(Boolean(y))   // false
console.log(Boolean(NaN)) // false



// array

countries = ["Bangladesh","india","denmak","US","canada"]
console.log(countries)
console.log(countries[0])
console.log(countries[1])
console.log(countries[2])
console.log(countries[3])
// find the length of the array
console.log(countries.length)
// mutable
countries[0] = "France"
console.log(countries)


// adding something to the array


countries.push("Italy")
countries.push("brazil")
countries.push("Spain")
countries.push("China","Japan","America")
console.log(countries)
// manually adding new element
countries[countries.length] = "Arzentina"
console.log(countries)

countries[countries.length] = "italy"
console.log(countries)

// pop method
x = countries.pop()
console.log(x)
console.log(countries)


// shift and unshft

countries.shift() // first item removed
console.log(countries)
countries.unshift("Bangladesh") // first item added 
console.log(countries)
numbers = []
numbers.push(0)
numbers.push(1)
numbers.push(2)
console.log(numbers)
x = "Bangladesh"
var y = x.split("")
console.log(y)
var z = "Tanvir Rahman"
var y = z.split(" ")
console.log(y)


ct = "Bangladesh,china,Denmark"
console.log(ct.split(","))

ct = ["Bangladesh","China","Denmark"]
console.log(ct.toString())

z = ct.join(" ")
console.log(z)
// concat two array
z = countries.concat(ct)
console.log(z)


// ascending
countries.sort()
console.log(countries)
// descending
countries.reverse()
console.log(countries)


// in order to do a descending order 
// you need to first sort it the you reverse it


// make a number array in descending order


numbers = [1,5,100,3,4,5,6,7,8,9,10]
numbers.sort(function(a,b){
	return a-b
})
numbers.reverse()
console.log(numbers)



// objects

var student = {
	name : "Tanvir",
	age : 29,
	hometown: "Chitagong"

}

console.log(student.name)
console.log(student.age)
console.log(student.hometown)



// adding

student["accupation"] = "Student"
student.village = "Kurigram"
console.log(student)


// delete

delete student.village
console.log(student)
// undefinaed . empty, NaN
var x ;
console.log(x)  // undefined
// remember if you use === then type soho check home
// if you use == only value check hobe
console.log(null == undefined) // null
// setting en empty value
var b = ""  // empty value
var a = null  // it is null not empty vale
console.log(b===a) // false 




// remember array is reference type
// this is not a value type\
numbers = [1,2,3]
tmp = numbers
numbers[0] = 100
console.log(tmp)  // it will show  [100,2,3]
// same goes to object

age = 29
console.log(`My name is tanvir rahman.
I am a EEE Graduate
and my age is ${age}`)
