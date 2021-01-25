

// Exercise 1
// 1. Create a structured html file linked to a js file
// 2. Write a JS function that takes a parameter: myAge
// 3. Console.log the age of my mum and my dad (my mum is twice my age, and my dad is 1.2 the age of my mum)
// 4. Call the function


function myAge (myAge) {
    var mumAge = myAge *2;
    var dadAge = mumAge*1.2;
    console.log("my dad age is " + dadAge + " and my mum age is " + mumAge );
}

myAge(23);



// Exercise 2
// 1. Create a structured html file linked to a js file
// 2. Write a JS function that takes a parameter: myAge
// 3. Return the age of my mum (my mum is twice my age)
// 4. Call the function
// 5. Console.log the age of my mum

function myAge2 (myAge) {
    var mumAge = myAge *2;
    return mumAge;
}

console.log("my mum age is " + myAge2(32));