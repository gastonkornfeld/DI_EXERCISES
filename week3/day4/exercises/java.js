



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



let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]

// Using the array above, console.log the number of users in a group conversation based on the following rules:
// If there is no one, display “no one is online”.
if (users.length == 0) {
    console.log("“no one is online”");
}
// If there is 1 person, display “<name_user> is online”.
else if (users.length == 1) {
    console.log(users[0] + " is online");
}
// If there are 2 people, display “<name_user1> and <name_user2> are online”.
else if (users.length == 2) {
    console.log(users[0] + " and" + users[1] + " are online");
}
// If there are n>2 people, display the first two names and add “and n-2 more are online”.
else {
    onlinePerson = users.length - 2;
    console.log(users[0] + ", " + users[1] + " and " + onlinePerson + " more are online");
}



