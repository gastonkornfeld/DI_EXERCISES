// first exercise

let adressNumber = 5;
let adressStret = "Hertzel";
let country = "Israel";
let global_adress = "I live in " + adressStret + " " + adressNumber + ", in " + country;

console.log(global_adress)
document.getElementById("demo1").innerHTML = global_adress

// second exercise


let birth = 1988;
let futureYear = 2053;
let iWillHave = futureYear - birth;
let sentence = "I will be " + iWillHave + " in " + futureYear;
console.log(sentence)

document.getElementById("demo2").innerHTML = sentence



// exercise 3


let pets = ["cat", "dog", "fish", "rabbit", "cow"];


pets.push("horse");

pets.splice(3, 1);
console.log(pets);

let lenghtArray = pets.length;
document.getElementById("demo3").innerHTML =  pets[1] + " and the array lenght is " + lenghtArray;





