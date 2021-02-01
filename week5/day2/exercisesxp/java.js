// exercise 1 














// Give to all paragraphs inside the <article> tag the class of para_article.

var allp = document.querySelectorAll("p");
for (p of allp) {
    p.classList.add("para_article");
}
// Remove the last paragraph in the article.

allp[3].remove();

// Add an event listener so that when you click on the h2, it is removed from the DOM.

var h2 = document.querySelector("h2");
h2.addEventListener('click',  () => {
    h2.remove();
} )

// Set the font size of the h1 to be a random pixel size from 0 to 100.

var h1 = document.querySelector("h1");
h1.style.fontSize = Math.random() * 100 + "px";

// Hide the 1st paragraph, when it’s clicked. (use the display property )

allp[0].addEventListener('click', () => {
    allp[0].style.display = "none";
})



// Get the values from the inputs and append them to the end of the html, inside a table.
let doItButton = document.getElementsByTagName("button")[0];
let username = document.getElementsByTagName("input")[0];
let question = document.getElementsByTagName("input")[1];


let doIt = function() {
    let tr1 = document.createElement("tr");
    tr1.innerHTML = username.value;
    let tr2 = document.createElement("tr");
    tr2.innerHTML = question.value;
    let body1 = document.getElementsByTagName("body")[0];
    body1.appendChild(tr1);
    body1.appendChild(tr2);
    username.value = "";
    question.value = "";
    };


doItButton.addEventListener('click', doIt);



// Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.

allp[1].addEventListener('click', () => {
    allp[1].style.opacity = 0.4;
    allp[1].style.transition = "opacity 2s ease-in";
})




// exercise 2