// Instructions
// This webpage is just a blank universe, and you’ll fill it with planets and moons in this challenge.
// You only have to work with a JS file

// Create an array of planets of the solar system
// For each planet, in the array, create a div using createElement. This div should have a class named ‘planet’.
// Each planet should have a different background color. (Hint: add a new class to each planet)
// Finally append each div to the body.
// Bonus Do the same process for moons. Be careful, each planet has a certain amount of moons; How should you display them ?


let planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"];

// here i use a for to create the divs with the planets, only the text inside the div was created separate

for (elem of planets) {
    var elem = document.createElement("div");
    
    elem.style.color = "white";
    var body = document.querySelector("body");
    body.appendChild(elem);
    
}
// here i put the names of the planets inside the divs



let namesPlanets = document.querySelectorAll("div");
namesPlanets[0].innerHTML = "mercury";
namesPlanets[1].innerHTML = "venus";
namesPlanets[2].innerHTML = "earth";
namesPlanets[3].innerHTML = "mars";
namesPlanets[4].innerHTML = "jupiter";
namesPlanets[5].innerHTML = "saturn";
namesPlanets[6].innerHTML = "uranus";
namesPlanets[7].innerHTML = "neptune";
// add the clases planet and the different backgrounds colors



namesPlanets[0].setAttribute("class", "orange planet")
namesPlanets[1].setAttribute("class", "red planet")
namesPlanets[2].setAttribute("class", "blue planet")
namesPlanets[3].setAttribute("class", "green planet")
namesPlanets[4].setAttribute("class", "salmon planet")
namesPlanets[5].setAttribute("class", "yellow planet")
namesPlanets[6].setAttribute("class", "purple planet")
namesPlanets[7].setAttribute("class", "brown planet")


namesPlanets[5].style.color = "black";


// adding the earth moon

let earth = namesPlanets[2];

let earthMoon = document.createElement("div");
earth.appendChild(earthMoon);
earthMoon.innerHTML = "Earth Moon";
earthMoon.setAttribute("class", "moon");


// adding the mars moons

let mars = namesPlanets[3];

let marsMoon1 = document.createElement("div");
mars.appendChild(marsMoon1);
marsMoon1.innerHTML = "mars Moon1";
marsMoon1.setAttribute("class", "moon");



let marsMoon2 = document.createElement("div");
mars.appendChild(marsMoon2);
marsMoon2.innerHTML = "mars Moon2";
marsMoon2.setAttribute("class", "moon right");
