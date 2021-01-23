


// Create a stuctured html file linked to a JS file

// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration,
//  it will check if the current number is odd or even, and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"


for (let i = 0; i < 16; i++) {
    if (i % 2 == 0) {
        console.log( i + " is an even number")
    }
    else {
        console.log(i + " is not an odd number")
    }
}

// exercise 2
let names= ["john", "sarah", 23, "Rudolf",34]
// Write a JavaScript for loop that will go through the variable names.
for (let x of names) {
        if (typeof(x) != 'string') {
            continue;
        }
        else if (typeof(x) == 'string') {

            if ((x[0]) == x[0].toUpperCase()) {
                console.log()
            }


        }
}
// if the item is not a string, pass.
// if the item is a string, check if it's first letter is in uppercase. If not, change it to uppercase and then display the name.
// 2. Write a JavaScript for loop that will go through the variable names

// if the item is not a string, go out of the loop.
// if the item is a string, display it.


( word[0] === word[0].toUpperCase() );