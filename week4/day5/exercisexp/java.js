// // exercise 1


// // In the div above, change the value of the identity attribute (id)
// //  from navBar to socialNetworkNavigation, using the setAttribute method.
// // We are going to add a new li to the ul.
// // First, create a new li tag (use the createElement method)
// // Then create a new text node with “Logout” as its specified text.
// // Append the text node to the newly created list node (li).
// // Finally, append this updated list node to the unordered list above, using the appendChild method.
// // Bonus
// // Use the firstElementChild and the lastElementChild properties
// //  to retrieve the first and last li elements under the parent ul node. Display the text of each link.(Hint: textContent property).


// // change the navbar id
// let navbar = document.getElementsByTagName("div")[0];
// navbar.setAttribute("id" , "socialNetworkNavigation");


// // add a new li to the ul and appendx a the node

// let newLi = document.createElement("li");
// let liNode = document.createTextNode("Logout");
// newLi.appendChild(liNode);


// // append the new li to the ul

// let theUl = document.getElementsByTagName("ul")[0];
// theUl.appendChild(newLi);


// // bonus

// console.log(theUl.firstElementChild.textContent);
// console.log(theUl.lastElementChild.textContent);




// // exercise 2

// // 1 part - Change the name “Pete” to “Richard”
// // i take the li pete in a variable and then change the content inside
// let byPete = document.getElementsByTagName("li")[1];
// byPete.innerHTML = "Richard";



// // 2 part -  Change each first name of the <ul> by your name


// // will create two different variables for each name
// let gaston1 = document.getElementsByTagName("li")[0];
// let gaston2 = document.getElementsByTagName("li")[2];
// // and then add my name to them
// gaston1.innerHTML = "Gaston1";
// gaston2.innerHTML = "Gaston2";

// //3 part -  Add at the end of each <ul>, a <li> that says “Hey students”

// // I need two new li
// let newLi1 = document.createElement("li");
// let newLi2 = document.createElement("li");
// // here I add the text to the two li
// newLi1.innerHTML = "hey students";
// newLi2.innerHTML = "hey students";

// // now i will need the two ul in a variable too

// let ul1 = document.getElementsByTagName("ul")[0];
// let ul2 = document.getElementsByTagName("ul")[1];

// ul1.appendChild(newLi1);
// ul2.appendChild(newLi2);




// // 4 Delete the <li> Sarah


// // I get the li and then i remove it
// let bySara = document.getElementsByTagName("li")[3];
// bySara.remove();

// // Bonus
// // Add a class “student_list” to both of the <ul>
// // Add the class “university” and “attendance” to the first <ul>
// ul1.setAttribute("class", "student_list university attendance" );
// ul2.setAttribute("class", "student_list");




// ecercise 3


// Exercise 3 : Change The Logo
// Open up Github in Chrome or Firefox, and open up the console.
// Find the Github navbar and store it in a variable. Use the DOM properties and methods to retrieve the element node. Don’t add an id or a class the the element.
// Change the color of the navbar.
// Find your Github name and store it in a variable.
// Change your name by “The Boss”

// was cool to play around with that.





// exercise 4




// For the following exercise use this website for assistance:
// 1. Add a “light blue” background color and some padding to the div above.
// 2. Do not display the first name (John) in the list and add a border to the second name (Pete).
// 3. Change the font size of the whole body.
// 4. Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div)

// // 1
// let divBig = document.getElementsByTagName("div")[0];
// divBig.style.background = "lightBlue";
// divBig.style.padding = "30px 20px 25px 10px";


// // 2
// let ul1 = document.getElementsByTagName("ul")[0];
// ul1.firstElementChild.remove();
// ul1.lastElementChild.style.border = "1px solid black";

// // 3
// let bodyes = document.getElementsByTagName("body")[0];
// bodyes.style.fontSize = "3em";



// // bonus, need to comment 2 and 3 to work
// let x = document.getElementsByTagName("li")[0];
// let y = document.getElementsByTagName("li")[1];



// if (divBig.style.background == "lightblue") {
//     alert("Hello " + x.innerText + " and " + y.innerText);
}
