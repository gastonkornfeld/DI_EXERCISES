
// exercise 1




// // Given the birthday year of two people, find the date 
// // when the younger one is exactly half the age of the other.
// // Notes: The dates are given in the format YYYY




// // solution

// let birthx = 1900;
// let birthy = 1000;

// // so when the first one will have the age of the difference the second one will have the double age

// // wich year 
// var agex = 2021 - birthx; //difAge es la diferencia de edad
// var agey = 2021 - birthy;//necesito saber en que ano el menor va a tener la diferencia de edad.
// if (agex > agey) {
//     var difAge = agex - agey;
//     var agey = difAge;
//     var agex = difAge * 2;
//     var YearofDouble = birthy + difAge ;
//     console.log(" in " + YearofDouble + " the person that born in " + birthx + " will have " + (agex) 
//     + " years old, the double of the person that born in " + birthy + " that will have " + (agey) + " years old")

// }
// else {
//     var difAge = agey - agex;
//     var agex = difAge;
//     var agey = difAge * 2;
//     var YearofDouble = birthx + difAge ;
//     console.log(" in " + YearofDouble + " the person that born in " + birthy + " will have " + (agey) 
//     + " years old, the double of the person that born in " + birthx + " that will have " + (agex) + " years old")
// }


















// exercise 2

// Harder exercise
// Hint : This exercise has 2 part. First, do this exercise without Regular Expression, then do it using Regular Expression

// You are working in a PostOffice and you need the zip code of the clients in order to send them letters.
// Ask your client for his zip code and console.log “good” or “error” based on the following rules.
// A valid zip code is as follows:
// Zip codes consist of 5 consecutive digits
// Must only contain numbers (no non-digits allowed).
// Must not contain any spaces.
// Must not be greater than 5 digits in length.

// I ask the user for the post code
// let zipCode = prompt("please input your zip code (no more than 5 numbers whitout spaces or other signs");

// // here I dont know how to take all symbols yes so i put them in to a long and if. there is more to add.
// // probably whit regular expressions will be easier.
// if (zipCode.indexOf(" ") == -1 && zipCode.indexOf("+") == -1 && zipCode.indexOf("=") == -1 && zipCode.indexOf("*") == -1
// && zipCode.indexOf("/") == -1 && zipCode.indexOf("-") == -1 && zipCode.indexOf(")") == -1 && zipCode.indexOf("(") == -1 
// && zipCode.indexOf("$") == -1 && zipCode.indexOf("%") == -1 && zipCode.indexOf("^") == -1 && zipCode.indexOf("&") == -1
//  && zipCode.indexOf("#") == -1 && zipCode.indexOf("@") == -1 && zipCode.indexOf("_") == -1 && zipCode.length <= 5) {
//     console.log("Good");
// }
// else {
//     console.log("wrong");

// }

// let zipCode2 = prompt("please input your zip code (no more than 5 numbers whitout spaces or other signs");
// var regex = zipCode2.search(/^[0-9]*$/);

// if (regex == 0 && zipCode2.length <= 5) {
//     console.log("good");
// }
// else {
//     console.log("bad");
// }




// exercise 3







// //Harder exercise
// //Hint : Use Regular Expression

// //Ask the user for a word and save it in a variable.
// //Delete all the vowels of the string and console.log the result







// var userWord = prompt("Please give me a word");
// var wordWithoutVowels = userWord.replace(/a/ig, "");
// wordWithoutVowels = wordWithoutVowels.replace(/e/ig, "");
// wordWithoutVowels = wordWithoutVowels.replace(/i/ig, "");
// wordWithoutVowels = wordWithoutVowels.replace(/o/ig, "");
// wordWithoutVowels = wordWithoutVowels.replace(/u/ig, "");
// console.log("the secret word is " + wordWithoutVowels);







// Bonus: Replace the vowels with another character and console.log the result
// a = 1
// e = 2
// i = 3
// o = 4
// u = 5




// // bonus


// var userWord2 = prompt("Please give me a  second word");
// var wordWithoutVowels2 = userWord.replace(/a/ig, "1");
// wordWithoutVowels2 = wordWithoutVowels2.replace(/e/ig, "2");
// wordWithoutVowels2 = wordWithoutVowels2.replace(/i/ig, "3");
// wordWithoutVowels2 = wordWithoutVowels2.replace(/o/ig, "4");
// wordWithoutVowels2 = wordWithoutVowels2.replace(/u/ig, "5");
// console.log("The secret word is " + wordWithoutVowels2);