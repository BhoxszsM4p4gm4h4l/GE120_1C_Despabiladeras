"""

hello am yole!
GE120: Intro To Geomatic Application
Mariole B. Despabiladeras
2023-11218

Exercise 2

"""

from math import cos, sin, radians, sqrt 

def getLatitude(distance,azimuth):
    '''
    input:
    distance
    azimuth

    output:
    lat
    dep

    '''
    lat = -distance * cos(radians(azimuth))

    return lat

def getDeparture(distance, azimuth):
    dep = -distance * sin(radians(azimuth))

    return dep

def azimuthtobearing (azimuth):
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

counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

while True:
    print()
    print("LINE NO: ", counter)

    bobstyping = False
    while not(bobstyping):
        distance = input("Distance: ")
        if bobstyping:
            print("bobo")
            continue
        if not(bobstyping):
            break
    azimuth = input("Azimuth from the South: ")

    bearing = azimuthtobearing(azimuth)
    lat = getLatitude(azimuth=float(azimuth),distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth),distance=float(distance)) 

    sumLat = sumLat+lat
    sumDep = sumDep+dep
    sumDist = float(distance)

    yn = input("add new line? ")
    if yn.lower == "yes" or yn == "Yes" or yn.upper == "yes" or yn == "y":
        counter = counter +1
        continue
    else:    
        break
