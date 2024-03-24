var uname = document.querySelector("#uname");
var email = document.querySelector("#email");
var pass1 = document.querySelector("#pass1");
var pass2 = document.querySelector("#pass2");
var mobile = document.querySelector("#mobile");
var error = document.querySelector("#error");


function validate(){
	if(uname.value === ""){
		error.innerText = "Username is Required!";
		return false;
	}

	else if(email.value === ""){
		error.innerText = "Email is Required!";
		return false;
	}

	else if(pass1.value === ""){
		error.innerText = "Password must have 8 characters!";
		return false;
	}

	else if(pass1.value != pass2.value){
		error.innerText = "Confirmed Password didn't match!";
		return false;
	}

	else if(mobile.value.length != 11){
		error.innerText = "Mobile Number must have 11 characters."
		return false;
	}

	else{
		error.innerText = "";
	}

}