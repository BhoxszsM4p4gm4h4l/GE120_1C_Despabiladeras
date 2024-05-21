//Title of the App: Azimuth to bearing Converter. This would be modeled simply with 2 box for the input and output as well as a big button that says convert in the middle of the boxes. The display of the solution is optional. For this to work, javascript as well as python is needed.
//For this, a button is one of the major elements in this project so that it can activate the said program. 

function convertToBearing(azimuth) {
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

while (true) {
    console.log();
// this will get the azimuth for our program
    let azimuth = readlineSync.question("Azimuth from the South: ");

    // make an array for the final output
    let line = [azimuth, bearing];
    lines.push(line);
//let us add a counter to take note of our lists
    let yn = readlineSync.question("Add another line (yes/no)? ");
    if (yn.toLowerCase() === "yes" || yn.toLowerCase() === "y") {
        linecount++;
        continue;
    } else {
        break;
    }
}

console.log("\n\nCONVERTED AZIMUTH TO BEARINGS");
console.log();
console.log("INPUT        OUTPUT");

lines.forEach(line => {
    console.log(`${line[0]}            ${line[1]}            `);
});

console.log("\n----END----")
