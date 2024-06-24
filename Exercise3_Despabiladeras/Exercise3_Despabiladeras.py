"""

hello am yole!
GE120: Intro To Geomatic Application
Mariole B. Despabiladeras
2023-11218

Exercise 2

Computes the latitude of a given line based on its distance and azimuth from the South. o Function Name: getLatitude 
o Parameters: distance, azimuth from the south 
o Return: latitude 
• Computes the departure of a given line based on its distance and azimuth from the South. o Function Name: getDeparture 
o Parameters: distance, azimuth from the south 
o Return: departure 
• Converts an azimuth (decimal degrees) to bearing (string) with signs (N,S,E,W) o Function Name: azimuthToBearing 
o Parameters: azimuth from the south 
o Return: bearing 
"""

from math import cos, sin, radians, sqrt 

linecount = 1
Lines = []

def getLatitude(distance,azimuth):
    '''
    input:
    distance
    azimuth

    output:
    lat
    dep

    '''
    latitude = -distance * cos(radians(azimuth))

    return latitude

def getDeparture(distance, azimuth):
    departure = -distance * sin(radians(azimuth))

    return departure

def azimuthToBearing (azimuth):
    if "-" in str(azimuth):
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees))+(int(minutes/60))+(float(seconds/3600))%3600
    else:
        azimuth = float(azimuth)%360
    
    if azimuth > 0 and azimuth < 90:
        bearing = "s {:^5}  W".format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = "N {:^5} W".format(180-azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = "S {:^5} E".format(azimuth-180)
    elif azimuth > 270 and azimuth < 360:
        bearing = "N {:^5} E".format(360-azimuth)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "alaws" 
    
    return bearing

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

