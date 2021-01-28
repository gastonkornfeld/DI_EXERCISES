// You know the infamous song “99 Bottles of Beer?”

// You need to generate in JavaScript the lyrics to the song 99 Bottles of Beer as an output.

// Ask the user to input a starting number of bottles of beer, and start the bottles falling.
// But instead of 1 falling each time, the number falling goes up by one each time.

// ==============================

// 99 bottles of beer on the wall  "this two lines when is 0"
// 99 bottles of beer
// Take 1 down, pass it around          "here the rest of the son in 4 lines"
// 98 bottles of beer on the wall
// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall
// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ==============================

// How will you choose to make the song end?
// Make sure you get the grammer right…
// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around.


// variables for the strings
let first = " bottles of beer on the wall";
let second = " bottles of beer";
let ta = "take ";
let down = " down, pass them around";
let finish = "I think I should put more bottles on the wall, if I want to continue the song";


// variable for the count down of the bottles
let bottles = 96;
console.log("99 bottles of beer on the wall");  
console.log("99 bottles of beer");
console.log("Take 1 down, pass it around");
console.log("98 bottles of beer on the wall");
console.log("98 bottles of beer on the wall");
console.log("98 bottles of beer");

for (var i = 2; i < 15; i = i+1) {
        
    var prueba = i;
    console.log(ta + prueba + down);
    console.log(bottles + first);
    console.log(bottles + first);
    console.log(bottles + second);
    bottles = bottles - prueba;
   
    
   

}
console.log(finish);