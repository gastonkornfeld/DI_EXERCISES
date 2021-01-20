
// create the sring and search for the words on it

let sentence = "My Program was not working, so bad";
let wordnot = sentence.indexOf("not");
let wordbad = sentence.indexOf("bad");

// with an if we compare if not is before bad
if (wordnot < wordbad && wordnot != -1) {
    // with this reggex we sustitute "not"..."bad" for good

    sentence2 = sentence.replace(/(not)(.+?)(?= bad)/, "$1 good");

    // then i will take the word bad and not from the sentence
    sentence2 = sentence2.replace("bad", "");
    sentence2 = sentence2.replace("not", "");
    sentence2 = sentence2.replace("  ", " ");
    console.log(sentence2);
}
else {
    console.log(sentence);
}








// If the word “bad” follows the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
// For example, the result here should be : “The movie is good really, I like it”
// If the words “not” and “bad” are not in the right sequence (or are not in the sentence), just console.log the original sentence.