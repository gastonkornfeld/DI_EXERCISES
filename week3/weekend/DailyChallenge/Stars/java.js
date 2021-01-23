// Write a JavaScript program to recreate the pattern below
// Hint: use nested for loop.
// Do this Daily Challenge by youself, without looking at the answers on the internet



// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *
// let array = 


for (let i = 1; i < 7; i++) {
    if (i == 1) {
        console.log('%c *', 'color: green;',)

    }
    else if (i % 2 == 0) {
        console.log('%c *', 'color: green;', '* '.repeat(i-1));

    }
    else {
        console.log( ' *'.repeat(i));
    }
}

