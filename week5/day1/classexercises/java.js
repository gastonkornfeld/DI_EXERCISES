// Write a JavaScript function to add rows to a table. Use the code below as a base



let table = document.getElementById("sampleTable");
function insert_Row() {


    var newRow = document.createElement("tr");
    
    table.appendChild(newRow);

    var td1 = document.createElement("td");
    var td2 = document.createElement("td");
    td1.innerHTML = "new 1";
    td2.innerHTML = "new 2";
    newRow.appendChild(td1);
    newRow.appendChild(td2);
}
