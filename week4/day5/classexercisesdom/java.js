


// // For each of the questions, find 2 WAYS of accessing :

// // 1. The div DOM node?
// let divdom = document.querySelector("div");
// console.log(divdom);
// console.log(document.getElementsByTagName ("div")[0]);
// // 2. The ul DOM node?
// let uldom = document.querySelector("ul");
// console.log(uldom);
// console.log(document.getElementsByTagName ("ul")[0]);
// // 3. The second li (with Pete)?
// let allli = document.querySelectorAll("li");
// console.log(allli[1]);
// console.log(document.querySelector("li:nth-child(2)"));
// console.log(document.getElementsByTagName ("li"));






// // exercise 2
// // For each of the questions, find 2 PROPERTIES to access :

// // 1. The div node
// console.log(document.getElementById("container"));
// console.log(document.getElementsByTagName("div")[1]);


// // 2. The ul nodes, and render all of it's children one by one

// let allul = document.getElementsByTagName("ul");
// for (elem of allul) {
//     console.log(elem);   
//     console.log(elem.firstElementChild); 
//     console.log(elem.lastElementChild);   
// }
// console.log(document.getElementsByTagName("ul")[0]);
// console.log(document.getElementsByTagName("li")[0]);
// console.log(document.getElementsByTagName("li")[1]);
// console.log(document.getElementsByTagName("ul")[1]);
// console.log(document.getElementsByTagName("li")[0]);
// console.log(document.getElementsByTagName("li")[1]);


// // 3. The first li of each 

// for (elem of allul) {
      
//     console.log(elem.firstElementChild); 
       
// }


// let ululul = document.querySelectorAll("li");
// console.log(ululul[0]);
// console.log(ululul[2]);





// // exercise 3

// // Write variables to get the value of the attributes of the specified link :
// let theId = document.getElementById("dI");
// // href
// console.log(theId.href);
// // hreflang
// console.log(theId.hreflang);
// // rel
// console.log(theId.rel);
// // target
// console.log(theId.target);
// // type
// console.log(theId.type);



// exercise 4


// Modify the style of the paragraph text (such as fontSize, fontFamily, color, etc. )through javascript code.

let paragraph = document.getElementById("text");
paragraph.style.fontSize = "35px";
paragraph.style.fontFamily = "arial";
paragraph.style.color = "salmon";
paragraph.style.textAlign = "center";
paragraph.style.textTransform = "lowercase";
