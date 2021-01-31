// // Exercise 1 : The World Translator
// // Hint: Use Switch Case

// // Ask the user which language he speaks.
// // Create a few conditions :
// // If he speaks French : display “Bonjour”
// // If he speaks English : display “Hello”
// // If he speaks Hebrew : display “Shalom”
// // If he doesn’t speak none of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’


// // ask the user 


// let language = prompt("wich language do you speak");


// // evaluate the case

// switch (language) {
//     case "french":
//         alert("Bonjour");
//         break;


//     case "english": 
//         alert("Hello");
//         break;

//     case "hebrew": 
//         alert("Shalom");
//         break;

//     default :
//         alert("‘01110011 01101111 01110010 01110010 01111001’");
        
    
// }



// exercise 2


// // Ask the user for his grade

// // If the score is bigger than 90, console.log “A”
// // If the score is between 80 and 90 (included), console.log “B”
// // If the score is between 70(included) and 80 (included), console.log “C”
// // If the score is lower than 70, console.log “D”



// let userGrade = prompt("grade??");

// if (userGrade > 90) {
//     console.log("Your score is A");

// }

// else if (userGrade > 80) {
//     console.log("Your score is B");
// }

// else if (userGrade >= 70) {
//     console.log("Your score is C");
// }

// else {
//     console.log("Your score is D");
// }




// // exercise 3


// // Create a variable, it must be a verb.
// // If the length of this string is at least 3, it should add ‘ing’ to its end, 
// // unless it already ends in ‘ing’, in which case it should add ‘ly’ instead.
// // If the string length is less than 3, it should leave it unchanged.


// let verb = "singing";

// if (verb.length > 2) {
//     if (verb.lastIndexOf("ing") == verb.length - 3) {
//         var newVerb = verb.concat("ly");
//         console.log(newVerb);
        
        
//     }
//     else if (verb.length > 2) {
//         var newVerb = verb.concat("ing");
//         console.log(newVerb);
//     }
// }
// else {
//     console.log(verb);   
// }



