





// You’re given a string of words. You need to find the word “Nemo”, 
// and return a string like this: “I found Nemo at [the order of the word you find nemo]!”.
// Bonus : If you can’t find Nemo, console.log “I can’t find Nemo”.
// Hint : use an if/else statement




let stringnemo = "lets try to find nemo in this string very long";

// variable that store the index of nemo if its exist.

var nemoindex = stringnemo.indexOf("nemo");
console.log(nemoindex);
// if nemo is not in the string we return the console log if not the number of the word

if (nemoindex == -1) {
    console.log("“I can’t find Nemo”");
}
else {
    var arrayofwords = stringnemo.split(" "); //array of the words.
    var position = arrayofwords.indexOf("nemo");
    console.log("i found nemo at position " + position);
}


