

var score = document.getElementById("score");

s = 0;

function barao(){
	s++;
	score.innerText = s;
}


function reset(){
	s = 0;
	score.innerText = s;
}


function komao(){
	s--;
	score.innerText = s;
}