const readlineSync = require('readline-sync');

let linecount = 1;
let lines = [];

let sumLat = 0;
let sumDep = 0;
let sumDist = 0;

function azimuthToBearing(azimuth) {
    if (typeof azimuth === 'string' && azimuth.includes('-')) {
        let [degrees, minutes, seconds] = azimuth.split('-').map(Number);
        azimuth = (parseInt(degrees)) + (parseInt(minutes) / 60) + (parseFloat(seconds) / 3600);
        azimuth %= 360;
    } else {
        azimuth = parseFloat(azimuth) % 360;
    }

    let bearing;

    if (azimuth > 0 && azimuth < 90) {
        bearing = `S ${azimuth.toFixed(2)} W`;
    } else if (azimuth > 90 && azimuth < 180) {
        bearing = `N ${(180 - azimuth).toFixed(2)} W`;
    } else if (azimuth > 180 && azimuth < 270) {
        bearing = `S ${(azimuth - 180).toFixed(2)} E`;
    } else if (azimuth > 270 && azimuth < 360) {
        bearing = `N ${(360 - azimuth).toFixed(2)} E`;
    } else if (azimuth === 0) {
        bearing = "DUE SOUTH";
    } else if (azimuth === 90) {
        bearing = "DUE WEST";
    } else if (azimuth === 180) {
        bearing = "DUE NORTH";
    } else if (azimuth === 270) {
        bearing = "DUE EAST";
    } else {
        bearing = "UNKNOWN";
    }

    return bearing;
}

function getDeparture(distance, azimuth) {
    function radians(degrees) {
        return degrees * (Math.PI / 180);
    }

    return -distance * Math.sin(radians(azimuth));
}

function getLatitude(distance, azimuth) {
    function radians(degrees) {
        return degrees * (Math.PI / 180);
    }

    return distance * Math.cos(radians(azimuth));
}

while (true) {
    console.log();
    console.log("LINE NO: ", linecount);

    let distance;
    while (true) {
        distance = readlineSync.question("Distance: ");
        if (!distance) {
            console.log("Invalid input, please enter a distance.");
        } else {
            break;
        }
    }

    let azimuth = readlineSync.question("Azimuth from the South: ");

    let bearing = azimuthToBearing(azimuth);
    let lat = getLatitude(parseFloat(distance), parseFloat(azimuth));
    let dep = getDeparture(parseFloat(distance), parseFloat(azimuth));

    sumLat += lat;
    sumDep += dep;
    sumDist += parseFloat(distance);

    let line = [linecount, distance, bearing, lat, dep];
    lines.push(line);

    let yn = readlineSync.question("Add another line (yes/no)? ");
    if (yn.toLowerCase() === "yes" || yn.toLowerCase() === "y") {
        linecount++;
        continue;
    } else {
        break;
    }
}

console.log("\n\nLINES SIGHTED");
console.log();
console.log("LINE NO.        DISTANCE       BEARING        LATITUDE       DEPARTURE");

lines.forEach(line => {
    console.log(`${line[0]}            ${line[1]}            ${line[2]}       ${line[3].toFixed(2)}       ${line[4].toFixed(2)}`);
});

console.log("\n----END----")

//to print
console.log("Hello, World!");

// Declaring variables
var name = "Alice";
let age = 25;
const city = "New York";

// Using variables
console.log(name);  // Outputs: Alice
console.log(age);   // Outputs: 25
console.log(city);  // Outputs: New York

// Function definition
function greet(name) {
    return "Hello, " + name + "!";
}

// Function call
console.log(greet("Bob"));  // Outputs: Hello, Bob!

let number = 10;

if (number > 0) {
    console.log("The number is positive.");
} else if (number < 0) {
    console.log("The number is negative.");
} else {
    console.log("The number is zero.");
}

let number = 10;

if (number > 0) {
    console.log("The number is positive.");
} else if (number < 0) {
    console.log("The number is negative.");
} else {
    console.log("The number is zero.");
}

// For loop
for (let i = 0; i < 5; i++) {
    console.log("For loop iteration: " + i);
}

// While loop
let j = 0;
while (j < 5) {
    console.log("While loop iteration: " + j);
    j++;
}

let fruits = ["Apple", "Banana", "Cherry"];

// Accessing elements
console.log(fruits[0]);  // Outputs: Apple

// Adding an element
fruits.push("Date");
console.log(fruits);  // Outputs: ["Apple", "Banana", "Cherry", "Date"]

// Removing an element
fruits.pop();
console.log(fruits);  // Outputs: ["Apple", "Banana", "Cherry"]

let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    fullName: function() {
        return this.firstName + " " + this.lastName;
    }
};

// Accessing object properties
console.log(person.firstName);  // Outputs: John
console.log(person["lastName"]);  // Outputs: Doe

// Calling object methods
console.log(person.fullName());  // Outputs: John Doe

<!DOCTYPE html>
<html>
<body>

<button id="myButton">Click me</button>

<script>
// Function to handle the click event
function handleClick() {
    alert("Button was clicked!");
}

// Adding event listener to the button
document.getElementById("myButton").addEventListener("click", handleClick);
</script>

</body>
</html>
 