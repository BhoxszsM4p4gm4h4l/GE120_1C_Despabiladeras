
linecount = 1
Lines = []

function getLatitude(distance, azimuth) {
    // Convert degrees to radians
function radians(degrees) {
    return degrees * (Math.PI / 180);
    }
if (azimuth % 180 == 90) (return 0) else {

}
    // Calculate departure
let departure = -distance * Math.cos(radians(azimuth));
    return departure;
}
function getDeparture(distance, azimuth) {
        // Convert degrees to radians
    function radians(degrees) {
        return degrees * (Math.PI / 180);
        }
    
        // Calculate departure
    let departure = -distance * Math.sin(radians(azimuth));
        return departure;
    }

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

linecount = 1
lines = []

sumLat = 0
sumDep = 0
sumDist = 0

while True:
    print()
    print("LINE NO: ", linecount)

    bobstyping = False
    while not(bobstyping):
        distance = input("Distance: ")
        if bobstyping:
            print("bobo")
            continue
        if not(bobstyping):
            break
    azimuth = input("Azimuth from the South: ")

    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(azimuth=float(azimuth),distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth),distance=float(distance)) 

    sumLat = sumLat+lat
    sumDep = sumDep+dep
    sumDist = float(distance)


    line = [linecount, distance, bearing, latitude(), departure()]
    Lines.append(line)

    if yn.lower == "yes" or yn == "Yes" or yn == "y" or yn.upper == "y":
        linecount = linecount + 1
        continue
    else:
        break


print("{: ^20}".format("\n\nLINES SIGHTED"))
print()
print("{: ^20}{: ^20}{: ^20}{: ^20}{: ^20}".format("LINE NO.","DISTANCE","BEARING","LATITUDE","DEPARTURE"))

for line in Lines:
    print("{: ^20}{: ^20}{: ^20}".format(line[0],line[1],line[2],line[3],[4]))
print("{:^40}".format("\n----END----"))

