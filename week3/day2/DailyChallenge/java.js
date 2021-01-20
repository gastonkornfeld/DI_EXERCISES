// array
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(fruits);
// taking out one
fruitsFirst = fruits.shift();
console.log(fruits);

fruits = fruits.sort();
console.log(fruits);

fruits.push("kiwi");
console.log(fruits);

fruits.splice(0, 1);
console.log(fruits);

let posA = fruits[0];
fruits[0] = fruits[2];
fruits[2] = posA;



console.log(fruits);



let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(moreFruits[1][1][0]);














