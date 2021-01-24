

// const numbers = [5,0,9,1,7,4,2,6,3,8];
// let moment = 0;

// Using the .toString() method, convert the array to a string.

// let numbersString = numbers.toString();
// console.log(numbersString);
// let numbersString2 = numbers.join("");
// console.log(numbersString2);
// numbersString2 = numbers.join("**");
// console.log(numbersString2);
// numbersString2 = numbers.join(":) ");
// console.log(numbersString2);

// Using the .join(), convert the array to a string. Try passing different values into the join.

// Eg .join(“+”), .join(” “), .join(“”)
// Bonus : To do the Bonus, look up how to work with nested for loops
// Sort the array numbers in descending order using for loops (Not using built-in sort methods).
// The output should be: [9,8,7,6,5,4,3,2,1,0]


//  The algorithm compare two by two numbers starting from the very first two of the array
// if the nleft number is smaller have to be switched. 
// we need to repeat the process the lenght of the array minus 1 time to assurre if the las number is the bigger in 
// the array i will be dragged to the beggining.





// for (let j = 0; j < (numbers.length) -1 ; j++) {
//     for (let i = 0; i < (numbers.length) -1 ; i++) {
//         if (numbers[i] < numbers[i+1]) {
//             moment = numbers [i];
//             numbers[i] = numbers[i+1];
//             numbers[i+1] = moment;
//             console.log(numbers);

//         }
//     }
// }




// Hint: The algorithm is called “Bubble Sort”

// Use a temporary variable to swap values in the array.
// Use 2 “nested” for loops (Nested means one inside the other).
// Add comments and console.log the result for each step, it will help you understand.
// Requirement: Don’t copy paste solutions from Google


