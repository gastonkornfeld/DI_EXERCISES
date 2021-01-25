

// // Exercise 1 : Keyless Car
// // Ask the user for his age, and save the value into a variable


// // Create a function called checkDriverAge() that will alert the user if he can drive depending on his age.

// function chekDriverAge (age) {
//     if (age < 18) {
//         alert("Sorry, you are too young to drive this car. Powering off");
//     }
//     else if (age == 18) {
//         alert("Congratulations on your first year of driving. Enjoy the ride!");
//     }
//     else {
//         alert("You are old enough to drive, Powering On. Enjoy the ride!");
//     }

// }
// chekDriverAge(18);
// chekDriverAge(28);
// chekDriverAge(8);

// // if he is too young, alert “Sorry, you are too young to drive this car. Powering off”
// // if he is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// // if he just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// // Instead of using prompt to ask the user for his age, make the checkDriverAge() function 
// // accept an argument age, so that if you enter: checkDriverAge(92); it alerts “You are old enough to drive, Powering On. Enjoy the ride!”
















// // Exercise 2 : What’s In My Wallet ?
// // Given a total due and an array representing the amount of change in your pocket, 
// // determine whether or not you are able to pay for the item.
// // Change will always be represented in the following order: quarters, dimes, nickels, pennies.

// // Quarters  = 0.25
// // Dimes = 0.10
// // Nickels = 0.05
// // Pennies = 0.01
// // To illustrate:
// // changeEnough([25, 20, 5, 0], 4.25) should return true
// // , since having 25 quarters, 20 dimes, 5 nickels and 0 pennies
// //  gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)


// function changeEnough ([q, d, n, p] , due ) {
//     let total = (q*0.25) + (d*0.1) + (n*0.05) + (p*0.01);
//     return (total > due);
// }


// console.log(changeEnough([2, 100, 0, 0], 14.11));
// console.log(changeEnough([0, 0, 20, 5], 0.75));












// // Exercise 3: Find The Multiples Of 23
// // Write a js function that console.log the multiples of 23 less than 500 and at the end return the sum of all of them

// let sum = 0;
// let elements = [];
// function multipliers (x) {
//     for (let i = 0; (i * x) < 500 ; i++) {
//         elements.push(i * x);
        
        
//         sum = sum + (i * x);
//     }
//     console.log("Elements:" + elements);
//     console.log("SUM");
//     return sum ;
// }

// console.log(multipliers (23));

















// // Exercise 4 : Amazon Shopping

// // 
// // Create a function called checkBasket().
// // It should:
// // ask the user for the item he wants
// // and let him know if it’s in the basket or not
// // Hint: Use the in keyword inside the conditional


// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// function checkBasket() {
//     let item = prompt("wich item you want?");
//     for (x in amazonBasket) {
//         if (x == item) {
//             alert("you already have " + x + " in your basket");
//             break;
//         }
//     }
//     alert("you dont have " + item + " in you Basket");
// }

// checkBasket();

















// // Exercise 5 : Shopping List
// // Create an array called shoppingList with the values “banana”, “orange”, and “apple”.
// // Copy these two above objects into your js file
// // Create a function called myBill() that takes no argument.
// // Depending on the list of items that you have in your array shoppingList and the prices listed in the prices object,
// // return the price spent on shopping.
// // Call the function myBill()
// // Bonus: In the function above, only add the price if the item is in stock (use the stock object).
// // If the item is in stock, decrease the item’s stock by 1

// let shoppingList = ["banana", "orange", "apple"];

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  
// let stock1 = Object.values(stock);
// let fruit = Object.keys(stock);

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let prices1 = Object.values(prices);
// let fruitOnPrice = Object.keys(prices);

// let myCount = 0;

// function myBill () {
//     for (let i = 0 ; i < shoppingList.length; i++){
//         for (let j = 0; j < prices1.length; j++) {
//             if (shoppingList[i] == fruit[j] && stock1[j] > 0) {
//                 myCount = myCount + prices1[j];
//                 stock1[j] = stock1[j] - 1;

//             }
//         }
//     }
//     return "the bill is " + myCount;
// }

// console.log(myBill());

















// // Exercise 6 : Tips
// // John and his family went on a holiday and went to 3 different restaurants.
// // To tip the waiter a fair amount, John created a simple tip calculator (as a function).

// // He likes to tip:
// // 20% of the bill when the bill is less than $50,
// // 15% when the bill is between $50 and $200,
// // and 10% if the bill is more than $200.

// // Ask John for the amount of the 3 bills. He has to enter a list of bills, each one separated by a comma.
// // Create the program explained above.
// // In the end, John would like to have 2 arrays:
// // Containing all three tips (one for each bill).
// // Containing all three final paid amounts (bill + tip).
// // (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)



// let listOfBills = prompt("bills separate by a ,");
// // put the info of the user in an array
// let arrayOfBills = listOfBills.split(",");
// // empty arrays to push the data in to it

// let finalTips = [];
// let finalBills = [];



// function myTips () {
//     for (let i = 0; i< arrayOfBills.length; i++) { //this way i can put any amount of bills.
//         if (arrayOfBills[i] < 50) { //case that the bill is less than 50
//             var tip = parseInt(arrayOfBills[i])*0.2;
//             var totalbill = parseInt(arrayOfBills[i]) + tip;
//             finalBills.push(totalbill);
//             finalTips.push(tip);

//         }
//         else if (arrayOfBills[i] < 200) { // case in between of 50 and 200
//             var tip = parseInt(arrayOfBills[i])*0.15;
//             var totalbill = parseInt(arrayOfBills[i]) + tip;
//             finalBills.push(totalbill);
//             finalTips.push(tip);
//         }
//         else { // up to 200
//             var tip = parseInt(arrayOfBills[i])*0.1;
//             var totalbill = parseInt(arrayOfBills[i]) + tip;
//             finalBills.push(totalbill);
//             finalTips.push(tip);
//         }
//     }
//     return "the tips are: " + finalTips + " and the bills are: " + finalBills;
// }


// console.log(myTips());









// // Exercise 7 : Vacations Costs
// // Let’s create functions that calculate your vacation’s costs:

// // Define a function called hotel_cost().
// // It should ask the user for the number of nights he wants to stay in the hotel.
// // If the user’s answer isn’t relevant to the question (ie: if he doesn’t answer, or if the answer is a string), ask him again.
// // The hotel costs $140 per night. The function should return the total price of the hotel.







// let question = "";
// function hotel_cost() {
//     while (isNaN(question) || question == "" ) {
//         question = (prompt("How many hotel nights are you planning?"));
//         console.log(typeof(question));
//     }
//     let value = question * 140;
//     return value;

// }
// // hotel_cost();





// // Define a function called plane_ride_cost().
// // It should ask the user for his destination.
// // The function should return a different price depending on the location.
// // “London”: 183$
// // “Paris” : 220$
// // All other destination : 300$
// // If the user’s answer isn’t relevant to the question (ie: if he doesn’t answer, or if the answer is a number), ask him again.








// let plane = 2;

// function plane_ride_cost () {
//     while (!(isNaN(plane))) {
//         plane = prompt("what is the destination?");
//     }
//     if (plane == "london") {
//         var price1 = 183;
//         return price1;
//     }
//     else if (plane == "paris") {
//         var price1 = 220;
//         return price1;

//     }
//     else {
//         var price1 = 300;
//         return price1;
//     }


// }

// // plane_ride_cost();





// // Define a function called rental_car_cost().
// // It should ask the user for the number of days he wants to rent the car.
// // If the user’s answer isn’t relevant to the question (ie: if he doesn’t answer, or if the answer is a string), ask him again.
// // Calculate the cost of renting the car: the car costs $40 everyday.
// // If the user rents a car for more than 10 days, he gets 5% discount.
// // The function should return the total price of the car.








// let car = "";
// function rental_car_cost (){

//     while (isNaN(car) || car == "") {
//         car = (prompt("How many Days you need to rent a car?"));
        
//     }
//     if (car <= 10) {
//         var price = car * 40 ;
//         return price;
//     }
//     else {
//         var price = car *  40 * 0.95;
//         return price;
//     }


// }

// // rental_car_cost();








// // Define a function called total_vacation_cost() that returns the total cost of the user’s vacation depending on the 3 functions that you created above.
// // Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// // Hint: You have to call the functions hotel_cost(), plane_ride_cost() and rental_car_cost() inside the function total_vacation_cost.
// // Call the function total_vacation_cost()
// // Bonus: Instead of using a prompt inside the 3 first functions, use a prompt only inside the total_vacation_cost() function. What should you implement for it to work?

// function total_vacation_cost () {
//     console.log("your hotel cost is: " + hotel_cost());
//     console.log ("your plane cost is:  " + plane_ride_cost());
//     console.log("your car cost is: " + rental_car_cost());  
//     console.log("and the total cost is: " + ((hotel_cost() + plane_ride_cost() + rental_car_cost())));
// }

// console.log(total_vacation_cost());