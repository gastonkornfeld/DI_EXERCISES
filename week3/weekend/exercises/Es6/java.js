
// Analyse the code below without running it, what will be the output ?

// var num = 8;
// var num = 10;
// console.log(num);

// an error is gonna ocure because the variable num was create two times.
// was wrong. the num var was overrigthed.





// let i = 0;


// //   Change the code so the var i will be undefined outside of the for loop
// function numbers() {
//     for (var i = 0; i < 5; i += 1) {
//       console.log(i);
//     }
//     i = undefined;
//       console.log(i);
//   }
//   numbers();



// yo have to decide wich tipe of variable you have to use
// Create a global variable that save the amount of money you have in your account
let moneyOnAccount = 0;

// Create a variable that saves the amount of VAT
// with a bat of %17 percent i will do like this
let vat = 17/100;

// Create a variable that saves the amout of all the expenses and revenu you did /received for the past last month
let expensesRevenue = [3000, 5000];

// Create a JS code that multiplies of the expenses by the VAT
let expsAddVat = (expensesRevenue[0]*vat) + expensesRevenue[0];
console.log(expsAddVat);

// Create a JS code that changes the amount of the money you have in your account depending on your expenses/revenu.

moneyOnAccount = moneyOnAccount + (expensesRevenue[1] - expsAddVat);
// Display it
console.log("i have " + moneyOnAccount + " Dollars in my account");





