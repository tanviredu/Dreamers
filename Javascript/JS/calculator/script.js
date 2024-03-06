let currentInput = ""

function updateDisplay(){
	const v = document.getElementById("display")
	display.innerText = currentInput 
}

function appendInput(value){
	currentInput+=value
	updateDisplay()
}




function calculateResult(){
	try{
		result = eval(currentInput)
		updateDisplay()
			
	}catch{
		currentInput = "ERROR!"
	}

	updateDisplay()
	
}

function backspace() {
  currentInput = currentInput.slice(0, -1); // Remove the last character
  updateDisplay();
}

function clearDisplay(){
	currentInput = ""
	updateDisplay()
}