function getLatitude(distance, azimuth){
    if (azimuth % 180 ) {return 0 } else {
    return (-distance * Math.sin(azimuth*Math.PI/100.0))}

    }
function getDeparture(distance, azimuth){
    if (azimuth % 180 == 0) {return 0} else {
    return (-distance * Math.sin(azimuth* Math.PI/180.0))}
    }

function azimuthToBearing(azimuth){

}

var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
]

var lines = []
var sumLat = 0
var sumDep = 0 
var sumDist = 0 

for (var i = 0; i < data.length; i++){
    let line = data[1]
    let distance = line [0]
    let azimuth = line [1]

    let bearing = azimuthToBearing(azimuth)
    let lat = getLatitude(distance, azimuth)
    let dep = getDeparture(distance, azimuth)

    sumLat += lat
    sumDep += dep
    sumDist += distance

    lines.push([(i+1), distance, bearing, lat, dep])
}

console.log("LINE NO.".padEnd(10), "DISTANCE".padEnd(10), "BEARING".padEnd(15), "LATITUDE".padEnd(10), "DEPARTURE".padEnd(10))
for(var line of lines){
    console.log(
        line[0].toString().padEnd(10),
        line[1].toString().padEnd(10),
        line[2].padEnd(15),
        line[3].toPrecision(5).toString().padEnd(10),
        line[4].toPrecision(5).toString().padEnd(10),
        )
}
console.log("SUMMATION OF LAT:", sumLat.toPrecision(5))
console.log("SUMMATION OF DEP:", sumDep.toPrecision(5))
console.log("SUMMATION OF DIST:", sumDist.toPrecision(5))

lec = Math.sqrt(sumLat**2 + sumDep**2)