// // exercise 1 














// // Give to all paragraphs inside the <article> tag the class of para_article.

// var allp = document.querySelectorAll("p");
// for (p of allp) {
//     p.classList.add("para_article");
// }
// // Remove the last paragraph in the article.

// allp[3].remove();

// // Add an event listener so that when you click on the h2, it is removed from the DOM.

// var h2 = document.querySelector("h2");
// h2.addEventListener('click',  () => {
//     h2.remove();
// } )

// // Set the font size of the h1 to be a random pixel size from 0 to 100.

// var h1 = document.querySelector("h1");
// h1.style.fontSize = Math.random() * 100 + "px";

// // Hide the 1st paragraph, when it’s clicked. (use the display property )

// allp[0].addEventListener('click', () => {
//     allp[0].style.display = "none";
// })



// // Get the values from the inputs and append them to the end of the html, inside a table.
// let doItButton = document.getElementsByTagName("button")[0];
// let username = document.getElementsByTagName("input")[0];
// let question = document.getElementsByTagName("input")[1];


// let doIt = function() {
//     let tr1 = document.createElement("tr");
//     tr1.innerHTML = username.value;
//     let tr2 = document.createElement("tr");
//     tr2.innerHTML = question.value;
//     let body1 = document.getElementsByTagName("body")[0];
//     body1.appendChild(tr1);
//     body1.appendChild(tr2);
//     username.value = "";
//     question.value = "";
//     };


// doItButton.addEventListener('click', doIt);



// // Bonus: Fade out the 2nd paragraph over 2000 milliseconds, when it’s clicked.

// allp[1].addEventListener('click', () => {
//     allp[1].style.opacity = 0.4;
//     allp[1].style.transition = "opacity 2s ease-in";
// })




// exercise 2



// Exercise 2 : Transform The Sentence
// Add this sentence to your html then follow the steps :

/* <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
<strong>end</strong> you <strong>will</strong> be great Developers!
<strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>

Create a function called : getBold_items() that takes no parameter. This function has to collect all the bold items inside the paragraph.
Create a function called : highlight() that changes the color of each bold item to blue.
Create a function called : return_normal() that changes the color of each bold item to black.
Call the function highlight() onMouseOver and the function return_normal() onMouseOut */


// exercise 2 resolution

// let allBoldParagraph = document.getElementsByTagName("strong");
// function getBold_items() {
//     for (paragraph of allBoldParagraph) {
//         console.log(paragraph);
//     }
// }


// function highlight() {
//     for (let i = 0; i < allBoldParagraph.length; i++) {
//         allBoldParagraph[i].style.color = "blue";
//     }
// }

// function return_normal() {
//     for (let i = 0; i < allBoldParagraph.length; i++) {
//         allBoldParagraph[i].style.color = "black";
//     }
// }

// // making the mouse in and mouse out events.

// // first i need the div in a variable

// let divexercise2 = document.getElementById("exercise2");

// divexercise2.addEventListener('mouseover', highlight);
// divexercise2.addEventListener('mouseout', return_normal);



// // exercise 3

// // Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:

// // (4*πrcubo) /3


// // first i get the radius input to take the value, and the volume input to display the result
// let Myform = document.forms.MyForm;
// let radiusImput = document.getElementsByTagName("input")[0];
// let volumeInput = document.getElementsByTagName("input")[1];
// let volumeValue = volumeInput.value

// function test (e) {
//     e.preventDefault()
//     if (radiusImput.value != "") {
//         volumeValue = ((Math.pow(radiusImput.value, 3) * 4 * 3.14) / 3);
//         volumeInput.setAttribute("value", volumeValue);
//     }
    
    
// }

// Myform.addEventListener ('submit', test);
    
    



// exercise 4 
// i will put a div to work in the html


// let lotOffEvents = document.getElementById("exercise4");


// lotOffEvents.addEventListener('click', () => {
//     lotOffEvents.style.color = "red";
//     lotOffEvents.style.fontSize = "30px";
// })


// lotOffEvents.addEventListener('dblclick', () => {
//     lotOffEvents.style.color = "blue";
//     lotOffEvents.style.fontSize = "70px";
// })


// lotOffEvents.addEventListener('mouseover', () => {
//     lotOffEvents.style.fontFamily = "monospace";
//     lotOffEvents.style.fontSize = "50px";
// })


// lotOffEvents.addEventListener('mouseleave', () => {
//     lotOffEvents.style.fontFamily = "verdana";
//     lotOffEvents.style.fontSize = "20px";
//     lotOffEvents.style.border = "5px solid red";

// })







