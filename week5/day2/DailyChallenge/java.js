

let libButton = document.getElementById('lib-button');
var noun = document.getElementById('noun');
var adjective = document.getElementById('adjective');
var person = document.getElementById('person');


let libIt = function() {
let storyDiv = document.getElementById("story");
storyDiv.innerHTML = "Once upon a time in a far away land call it Developers intitute there was a big creature call it " 
+ person.value 
+ ". " + person.value + " was really " + adjective.value 
+ ". At lest that was what all of the neighbours of the place would say if you ask." 
+ " One day he was trying to create " + noun.value + " , and he was remember as the bigger "
+ noun.value + " creator, and the most " + adjective.value + " in the world" ;
};


libButton.addEventListener('click', libIt);