// Create A Hanging Game:
// Create the “Hangman” game. Your game will run in the console only.
// You need to guess a hidden word. Each letter you guess will appear, and you have 10 wrong guesses before you lose the game.
// Check it out here

// Player 1 enters a word. The secret word has to have at least 8 letters. It must be displayed as stars in the console.
// Eg. Player 1 chooses the word “javascript”.

let player1Word = "a"
while (player1Word.length < 8){
    player1Word = prompt("choose a word of 8 letter")
}

let WordinAsterisc = "*".repeat(player1Word.length);
console.log(WordinAsterisc);


// The word is displayed in the console as “**********“
// i will nedd another variable for this to be able to be changed on the game and to show on the platform




// Player 2 guesses a letter.
// create a variable to put the guess.






// Eg. “s”. The console must now display “****s*****“
// search for the position of the guess in the player1word and then change the 


// If the player guesses “a”, BOTH corresponding letters must be displayed, like this: “*a*as*****".
// Some Extra Rules:
// -The user will have 10 “lives” with which to guess the word. If they guess an incorrect letter, they lose a life.
// -You should also display a list of the incorrect letters chosen.
// -You should prevent a user from rechoosing an already chosen letter (correct or incorrect).
// -A message should inform the user when they win or lose.



