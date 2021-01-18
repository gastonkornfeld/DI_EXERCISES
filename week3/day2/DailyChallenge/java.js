
let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruitsFirst = fruits.shift();
fruits = fruits.sort();
fruits.push("kiwi");
fruits.splice(0, 1);
let posA = fruits[0];
fruits[0] = fruits[2];
fruits[2] = posA;



console.log(fruits);



let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(moreFruits[1][1][0]);














