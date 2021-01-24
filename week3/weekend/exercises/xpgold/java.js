// // exercise 1


// // giving this information

// let building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 990],
//         "Dan":  [4, 1000],
//         "David": [1, 500],
//     },
// }


// // Display the number of levels in the building.
// console.log(building.number_levels);
// // Display how many apartments are on level 1 and 3.
// console.log(building.number_of_apt_by_level["1"]);
// console.log(building.number_of_apt_by_level["3"]);

// // Display the name of the second tenant and the number of rooms he has in his apartment.

// console.log(building.name_of_tenants[1]);

// console.log(building.number_of_rooms_and_rent[building.name_of_tenants[1]][0]);

// // Check if the rent of Sarah plus the rent David is bigger than the rent of Dan.
// let rentSarah = building.number_of_rooms_and_rent["Sarah"][1];
// let rentDavid = building.number_of_rooms_and_rent["David"][1];
// let rentDan = building.number_of_rooms_and_rent["Dan"][1];
// let isBigger = (parseInt(rentSarah) + parseInt(rentDavid)) > parseInt(rentDan) ;
// console.log("The rent of Sarah and david togheter are bigger than the Dan rent is " + isBigger);


// // If it is than ask the owner to increase Dan’s rent (ask him for a new amount).
// rentDan = prompt("we need to set a new rent for Dan bigger than 1000");
// // Change the rent of Dan accordingly inside the object.
// building.number_of_rooms_and_rent["David"][1] = parseInt(rentDan);


















// // exercise 2


// // An elementary school’s trick to determine whether or not a number was divisible 
// // by three is to add all of the integers in the number together and to divide the resulting sum by three.
// // If there is no remainder from dividing the sum by three, then the original number is divisible by three as well.

// // Given a series of numbers as a string, determine if the number represented by the string is divisible by three.
// // You can expect all test case arguments to be strings representing values greater than 0.

// let numberToGuess = "100853";
// let sumNum = 0;
// for (digit of numberToGuess) {
//     sumNum = sumNum + parseInt(digit);
    
    
    

// }

// console.log("The number is divisible for 3:" + (sumNum % 3 == 0))














// // exercise 3

// let age = [20,5,12,43,98,55];
// let sumElements = 0;
// let moment = 0;

// // You have to create the logic by yourself, with simple for and while loops.

// // 1. Console.log the sum of all the elements of the array.

// for (let i = 0; i < age.length; i++) {
//     sumElements = sumElements + age[i];
// }

// console.log(sumElements);

// // 2. Console.log the largest number of the array.

// for (let j = 0; j < (age.length) -1 ; j++) {
//     for (let i = 0; i < (age.length) -1 ; i++) {
//         if (age[i] < age[i+1]) {
//             moment = age [i];
//             age[i] = age[i+1];
//             age[i+1] = moment;

//         }
//     }


// }
// console.log(age);
// console.log("the largest number of the array is " + age[0]);