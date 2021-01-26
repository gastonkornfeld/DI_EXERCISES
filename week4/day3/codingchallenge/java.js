

var calculation = [];

function my_f (value) {
    if (value != "=" && value != "AC" && value != "DEL" ) {
    calculation.push(value);
    var calculation2 = calculation.join(" "); // put the array in to a string
    var noSpaces = calculation2.replace(/\s+/g, ''); // take out the spaces
    console.log(value);
    console.log(calculation);
    document.getElementById("press").innerHTML = noSpaces;
    }
    else if (value == "=") {
        var calculation2 = calculation.join(" "); // put the array in to a string
        var noSpaces = calculation2.replace(/\s+/g, ''); // take out the spaces
        console.log(noSpaces);
        console.log(calculation2);
        document.getElementById("result").innerHTML = eval(noSpaces);
        // if i want a calculator that makes only one calculation i nedd this lines.
        // alert("the result is " + eval(noSpaces));
        // calculation.splice(0,500, "");
        // calculation2 = "";
        // calculation.splice(0,500, "");

    }
    else if (value == "AC"){
        calculation.splice(0,500, "");
        document.getElementById("press").innerHTML = 0;
    }

    else if (value == "DEL"){
        calculation.splice(0,500, "");
        document.getElementById("result").innerHTML = 0;
    }
}

