


let allH2 = document.getElementsByTagName("h2")
for (let i = 0; i < allH2.length; i++) {
    allH2[i].addEventListener('mouseover', () => {
        allH2[i].style.color= "black"
        allH2[i].style.backgroundColor = "aliceblue"
        allH2[i].style.fontFamily = "garamond"
    })
}
for (let i = 0; i < allH2.length; i++) {
    allH2[i].addEventListener('mouseleave', () => {
        allH2[i].style.color= "orange"
        allH2[i].style.backgroundColor = "black"
        allH2[i].style.fontFamily = "garamond"
    })
}

let allImages = document.getElementsByTagName("img")

for (let i = 0; i < allImages.length; i++) {
    allImages[i].addEventListener('mouseover', () => {
        allImages[i].style.border= "2px solid black"
    })    
}

for (let i = 0; i < allImages.length; i++) {
    allImages[i].addEventListener('mouseleave', () => {
        allImages[i].style.border= ""
    })    
}



let allIcons = document.getElementsByTagName("i")


for (let i = 0; i < allIcons.length; i++) {
    allIcons[i].addEventListener('mouseover', () => {
        allIcons[i].style.transform= "scale(2)"
        allIcons[i].style.border= "2px solid black"
    })    
}

for (let i = 0; i < allIcons.length; i++) {
    allIcons[i].addEventListener('mouseleave', () => {
        allIcons[i].style.transform= "scale(1)"
        allIcons[i].style.border= ""
    })    
}


