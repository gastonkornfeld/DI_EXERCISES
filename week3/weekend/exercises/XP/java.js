
// // exercise 1



// // Create an array to hold your top colors.

// let topColors = ["blue", "yellow" , "red" , "lightblue", "pink"];
// let number = 1;
// // For each choice, console.log a string like: “My #1 choice is blue”, “My #2 choice is red” ect…
// for (color of topColors) {

//     console.log("my #" + number + " choise is " + color);
//     number = number + 1;
// }


// // Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the right suffix for the number.

// // first i need a function to create this suffix properly adn a new number for this function
// let number2 = 1
// function ordinal_suffix_of(i) {
//     var j = i % 10,
//         k = i % 100;
//     if (j == 1 && k != 11) {
//         return i + "st";
//     }
//     if (j == 2 && k != 12) {
//         return i + "nd";
//     }
//     if (j == 3 && k != 13) {
//         return i + "rd";
//     }
//     return i + "th";
// }

// // runing again the for but with the function
// for (color of topColors) {

//     console.log("my " + ordinal_suffix_of(number2) + " choise is " + color);
//     number2 = number2 + 1;
// }
// // Hint : create an array of suffix to do the Bonus












// // exercise 2


// let people = ["Greg", "Mary", "Devon", "James"];

// // Write the command to remove “Greg” from the array.
// people.shift();

// // Write the command to replace “James” by “Jason” in the array.
// people.splice(2, 1, "Jason");

// // Write the command to add your name to the end of the array.
// people.push("Gaston");
// console.log(people);
// // Using a loop, iterate through this array and console.log all of the people.
// for (x of people) {
//     console.log(x);
// }
// // Using a loop, iterate through this array and after console.log-ing “Jason”, exit from the loop.
// for (x of people) {
//     console.log(x);
//     if (x == "Jason") {
//         break;
//     }

// }
// // Write the command to make a copy of the array using slice. The copy should NOT include “Mary” or your name.
// let people2 = people.slice(1)
// console.log(people2);
// // Write the command that gives the indexOf where “Mary” is located. Look on google what indexOf is
// console.log(people.indexOf("Mary"));
// // Write the command that gives the indexOf where “Foo” is located (this should return -1). Why does it return -1
// console.log(people.indexOf("Foo"));
// // returns -1 because this is the value that says there is no Foo in the array.
// // Write a variable called last which value is the last element of the array.
// let last = people[(people.length) - 1];
// console.log(last);
// // Hint: What is the relationship between the index of the last element in the array and the length of the array?












// exercise 3

// Ask a number to the user, while the number is smaller than 10, ask him for a new number.
// Tip : Which while loop is more relevant for this situation?


// let userNumber = prompt("please give me a number higher than 10");


// while (userNumber < 10) {
//     userNumber = prompt("please give me a number higher than 10");
// }

// use the regular while loop because i want to control the condition before executing the code

// Suppose you have a guest list of students and the country they are from, stored as key-value pairs in an object. 
// You have to make the attendance.












// exercise 4
// having this list of guests

// let guestList = {
//     randy: "Germany",
//     karla: "France",
//     wendy: "Japan",
//     norman: "England",
//     sam: "Argentina"
// }


// Ask the student for his name :
// If the name is in the object, console.log the name of the student and the country he comes from.
// "Hi! I'm [name], and I'm from [country]."
// Hint: Look up the statement if in
// If the name is not in the object, console.log :"Hi! I'm a guest."

// let studentName = prompt(" Whats your name");
// let sayhi = ""
// for (let student in guestList) {
//     if (studentName == student) {
//         sayhi = ("hi I am " + student + ", and i am from " + guestList[student]);
        
//         break;
//     }
//     else {

//         sayhi = ("hi i am a guest");
        
//     }
// }

// console.log(sayhi);













// // exercise 5

// // Create an object called family with a few properties.

// let family = {
//     size : 25,
//     howManyVegans : 3,
//     mans : 12,
//     womans : 13,
//     frase : "Togheter we will succeed"
// } 


// // Display only the properties. (using a for loop)
// for (prop in family) {
//     console.log(prop);
// }


// // Display only the values. (using a for loop)
// for (prop in family) {
//     console.log(family[prop]);
// }










// // exercise 6


// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// // define a variable to put the name of the society
// let nameSoc = [];
// let x;
// // A group of friends have decided to start a secret society.
// //  The society’s name will be the first letter of each of their firstnames,
// for (let i = 0;  i < names.length ; i++) {
//     x = names[i][0];
//     nameSoc.push(x);
   
    
// }
// console.log(nameSoc);

// //  sorted in alphabetical order.
// nameSoc.sort();
// nameSoc = nameSoc.join("");

// console.log("the name of the secret society is " + nameSoc);

// // Hint: a string is an array of letters
// // Console.log the name of their secret society.



