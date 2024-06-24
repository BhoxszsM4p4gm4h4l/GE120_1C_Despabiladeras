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

# Initialize variables
linecount = 1
Lines = []
sumLat = 0
sumDep = 0
sumDist = 0

def getLatitude(distance, azimuth):
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

def azimuthToBearing(azimuth):
    azimuth = float(azimuth) % 360
    if azimuth > 0 and azimuth < 90:
        bearing = "S {:^5.2f} W".format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = "N {:^5.2f} W".format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = "S {:^5.2f} E".format(azimuth - 180)
    elif azimuth > 270 and azimuth < 360:
        bearing = "N {:^5.2f} E".format(360 - azimuth)
    elif azimuth == 0:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "UNKNOWN"
    
    return bearing

while True:
    print("\nLINE NO: ", linecount)

    # Input distance
    distance = input("Distance: ")
    try:
        distance = float(distance)
    except ValueError:
        print("Please enter a valid number for distance.")
        continue

    # Input azimuth
    azimuth = input("Azimuth from the South: ")
    try:
        azimuth = float(azimuth)
    except ValueError:
        print("Please enter a valid number for azimuth.")
        continue

    bearing = azimuthToBearing(azimuth)
    lat = getLatitude(distance, azimuth)
    dep = getDeparture(distance, azimuth) 

    sumLat += lat
    sumDep += dep
    sumDist += distance

    line = [linecount, distance, bearing, lat, dep]
    Lines.append(line)

    yn = input("Do you want to continue? (yes/y to continue): ").strip().lower()
    if yn in ("yes", "y"):
        linecount += 1
        continue
    else:
        break

print("{:^20}".format("\n\nLINES SIGHTED"))
print()
print("{:^10}{:^15}{:^20}{:^15}{:^15}".format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in Lines:
    print("{:^10}{:^15.2f}{:^20}{:^15.2f}{:^15.2f}".format(line[0], line[1], line[2], line[3], line[4]))


print("SUMMATION OF LAT:", sumLat)
print("SUMMATION OF DEP:", sumDep)
print("SUMMATION OF DISTANCE:", sumDist)

lec = sqrt(sumLat**2 + sumDep**2)

print("LEC: ", lec)
rec = sumDist/lec
print("1: ", round(rec,3))

print("{:^40}".format("\n----END----"))