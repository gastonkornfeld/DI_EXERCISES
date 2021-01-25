
// Ask a user for several words (separated by commas).
// Push the words into an array.
// Console.log them, one per line, in a rectangular frame.
// For example, if the user gives you:
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:

let userWord = "";
// array the user input
while ((userWord.indexOf(",")) == -1) {
    userWord = prompt("please write at least 5 words separate by a ,. i will display it as a message for you");
}


// I need the words in to an array
let arrayOfWords = userWord.split(",");
var arrayOfWords2 =userWord.split(",");

// first i need to get the longest word of the array.
var longest = arrayOfWords.sort(
    function (a, b) {
        return b.length - a.length;
    }
)[0];
console.log(arrayOfWords2);





// The square part STARTS HERE

// first line
console.log( '*'.repeat((longest.length) + 4));

// medium part
for (word of arrayOfWords2) {
    console.log("* " + word + " ".repeat((longest.length) - (word.length)) + " *");
}





// last line
console.log( '*'.repeat((longest.length) + 4));

// the square part ENDS HERE