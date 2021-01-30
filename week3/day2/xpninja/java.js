
// exercise 1
// // evaluate this comparisions
// 5 >= 1 //true
// 0 === 1 //false
// 4 <= 1 //false
// 1 != 1 //false
// "A" > "B" //no idea checked is false
// "B" < "C" // //true
// "a" > "A" //checked is true
// "b" < "A" //false
// true === false //false
// true != true // false



// // exercise 2

// // run this code
// let c; 
// let a = 34;
// let b = 21;
// a = 2;
// a + b;

// What will return a + b?
// 23

// What is the variable c equal to?
// undefined


// Analyse the code below without running it, what will be the output ?
// console.log(3 + 4 + '5');
// 3 plus 4 will be trat as two number so 7 and then plus a sting will return 75 (concat).






// // exercise 3

// // Ask the user for a string of numbers separated by a comma and space, return the product of the numbers.
// // Hint: use some string methods




// let stringNum = prompt("Please put numbers separated by a coma and space, to be multiplicated");




// // now i need to make this string be an array of the numbers. I use the (",") as the divider in the split method
// // then stored in to another variable




// let anotherstring = stringNum.split(",");





// // now whit an for loop i will put the multiplication in to a variable. and it will start on 1



// let multiplication = 1;



// // the last is to loop and alert the result




// for (let i = 0 ; i < anotherstring.length; i++) {
//     multiplication = multiplication * (parseInt(anotherstring[i])); //multiplicate one by one all the elements of the array 
// }
// alert("the result of your multiplication is " + multiplication);




// // exercise 4


// // Hint: if statement (tomorrow’s lesson)
// // Ask the user for a number, return a string of the word “Boom”, which varies in the following ways:

// // The string should include n number of “o”s, unless n is below 2 (in that case, return “boom”).
// // If n is evenly divisible by 2, add an exclamation mark to the end.
// // If n is evenly divisible by 5, return the string in ALL CAPS.
// // If n is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
// // The example below should help clarify these instructions.



// // first ask the user for the number 

// let boomNumber = prompt("Please give me an explosive number");

// // I will want to work with a string so i think the best way to start this problem i with this one

// let boomString = "B";
// let letO= "o";

// // the first condition i will check is if it is less than 2
// //  In this case i need to add just the letters o, o , m to the array and display it as required.

// if (boomNumber < 2) {
//     alert(boomString +"o" + "o" +"m");
// }
// // then i will put as conditions the ones evenly divisible by two and the ones that are also evenly divisible by 5.
// // bit before we need to set the ampunt of o that are gonna be concat to the string
// else if (boomNumber >= 2) {

//     if (boomNumber % 2 == 0 && boomNumber % 5 == 0) {
        
//         alert(boomString + (letO.repeat(boomNumber)).toUpperCase() + "M" + "!");
        
//     }

//     else if (boomNumber % 2 == 0) {
//         alert(boomString + (letO.repeat(boomNumber)) + "m" + "!");
        
//     }

//     else if (boomNumber % 5 == 0) {
//         alert(boomString + (letO.repeat(boomNumber)).toUpperCase() + "M");
        
//     }



//     else {
//        alert(boomString + (letO.repeat(boomNumber)) + "m");

//     }
// }







