
// Create a new HTML file

// Create a banner saying "The sales end in 10min ! " . Style the banner and make it visible to the user after 5 sec.
let content;
let banner = document.createElement("div");



function appearBanner () {
    document.body.appendChild(banner);
    banner.style.backgroundColor = "black"
    banner.style.color = "white";
    banner.style.fontSize = Math.random()*50 + "px";
}


// Use the same code as before but create a countdown in the banner.

// ... "The sales end in 10sec ! "

// ... "The sales end in 9sec ! "

// etc ... until 0

// If you need help for this exercise, look at the 1st video of this tutorial


let timeleft = 1000;
function countdown () {
    
    if (timeleft <= 0) {
        clearInterval(interval1);
        banner.innerHTML = "Time end";
        banner.style.backgroundColor = "red";
        banner.style.border = "10px solid black";
        banner.style.textAlign = "center";
        banner.style.padding = "25px";
    } else {
        banner.innerHTML = timeleft + " seconds remaining";
        banner.style.backgroundColor = "green";
        banner.style.border = "3px solid red";
        banner.style.textAlign = "center";
        banner.style.padding = "25px";
    }
    timeleft -= 1;

}

setTimeout(appearBanner, 1000);
var interval1 = setInterval(countdown, 10);


