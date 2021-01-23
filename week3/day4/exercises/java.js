



// Create 2 variables, x and y. Each of them has a different numeric value.
// Write an if/else statement that checks the biggest number.


// let x = 8;
// let y= 5;

// if (x > y) {
//     console.log(x + " is the biggest number");
// }
// else {
//     console.log(y + " is the biggest number");
// }


// Create a variable newDog that is equal to the string “Chihuahua”.

// let newDog = "Chihuahua";

// Check and display how many letters are in newDog.

// console.log(newDog.length);

// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just use 2 console.log).

// console.log(newDog.toLowerCase());
// console.log(newDog.toUpperCase());

// Check if the variable newDog equals to “Chihuahua”
// if it does, display ‘I love Chihuahua, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’

// if (newDog == "Chihuahua") {
//     console.log("‘I love Chihuahua, it’s my favorite dog breed’");
// }
// else {
//     console.log("‘I dont care, I prefer cats’");
// }







// Ask a number to the user, and save it to a variable.
// let numberUser = prompt("Please Choose a number");


// Check if the variable is an even number
// If it is, display: “x is an even number’. Where x is the actual number of the user.
// If it isn’t, display “x is not an even number’. Where x is the actual number of the user


// if ((numberUser % 2) == 0) {
//     console.log(numberUser + " is an even number");
// }
// else {
//     console.log(numberUser + " is not an even number");
// }



// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

// Using the array above, console.log the number of users in a group conversation based on the following rules:
// If there is no one, display “no one is online”.

// if (users.length == 0) {
//     console.log("“no one is online”");
// }

// If there is 1 person, display “<name_user> is online”.

// else if (users.length == 1) {
//     console.log(users[0] + " is online");
// }

// If there are 2 people, display “<name_user1> and <name_user2> are online”.

// else if (users.length == 2) {
//     console.log(users[0] + " and" + users[1] + " are online");
// }

// If there are n>2 people, display the first two names and add “and n-2 more are online”.

// else {
//     onlinePerson = users.length - 2;
//     console.log(users[0] + ", " + users[1] + " and " + onlinePerson + " more are online");
// }



// Hint: Use Switch Case

// Ask the user which language he speaks.
// Create a few conditions :
// If he speaks French : display “Bonjour”
// If he speaks English : display “Hello”
// If he speaks Hebrew : display “Shalom”
// If he doesn’t speak none of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’


// let lng = prompt("wich language did you speak").toLowerCase();


// switch(lng) {
//     case "french" :
//         console.log("bonjour")
//         break;
//     case "english" :
//         console.log("Hello")
//         break;
//     case "hebrew" :
//         console.log("Shalom")
//         break;
//     default : console.log("‘01110011 01101111 01110010 01110010 01111001’")
// }



// Ask the user for his grade

//  let grade = prompt("How much did you got in the exam?");

// If the score is bigger than 90, console.log “A”

// if (grade > 90 && grade<= 100) {
//     console.log("A");
// }

// // If the score is between 80 and 90 (included), console.log “B”
//  else if (grade > 80 && grade<= 90) {
//     console.log("B");
// }

// If the score is between 70(included) and 80 (included), console.log “C”

//  else if (grade >= 70 && grade<= 80) {
//     console.log("C");
// }


// If the score is lower than 70, console.log “D”

// else if (grade >= 0 && grade<= 70) {
//     console.log("D");
// }
// else {
//     console.log("Your score should be between 0 and 100");
// }



// Create a variable, it must be a verb.
// If the length of this string is at least 3, it should add ‘ing’ to its 
// end, unless it already ends in ‘ing’, in which case it should add ‘ly’ instead.
// If the string length is less than 3, it should leave it unchanged.

let verb = "create";

let verbaArray = verb.split("");
let lenghtverb = verbaArray.length;
console.log(lenghtverb);

if (lenghtverb > 2 ) {
    if ((verbaArray[lenghtverb - 3]) == "i" && (verbaArray[lenghtverb - 2]) == "n" && (verbaArray[lenghtverb - 1]) == "g" ) 
}
