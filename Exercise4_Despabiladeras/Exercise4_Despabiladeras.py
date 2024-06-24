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


class Line:

    def __init__(self, distance, azimuth):
        self.distance = float(distance)
        self.azimuth = float(azimuth) % 360

    def latitude(self):
        '''
        input:
        distance
        azimuth

        output:
        lat
        dep

        '''
        latitude = -self.distance* cos(radians(self.azimuth))

        return latitude

    def departure(self):
        departure = -self.distance* sin(radians(self.azimuth))

        return departure

    def bearing (self):

        '''
        if "-" in str(azimuth):
            degrees, minutes, seconds = azimuth.split("-")
            azimuth = (int(degrees))+(int(minutes/60))+(float(seconds/3600))%3600
        else:
            azimuth = float(azimuth)%360
        '''
        if azimuth > 0 and azimuth < 90:
            bearing = "s {:^5}  W".format(azimuth)
        elif azimuth > 90 and azimuth < 180:
            bearing = "N {:^5} W".format(180-azimuth)
        elif azimuth > 180 and azimuth < 270:
            bearing = "S {:^5} E".format(azimuth-180)
        elif azimuth > 270 and azimuth < 360:
            bearing = "N {:^5} E".format(360-azimuth)
        else:
            bearing = 'lol'

        return bearing
    
class Cardinal(Line):
        def __init__(self,distance,azimuth):
            super().__init__(distance,azimuth)

        def bearing(self):
            if azimuth == 0:
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
Lines = []

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

    if "-" in str(azimuth):
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%3600
    else:
        azimuth = float(azimuth)%360

    if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    else: 
        line = Line(distance, azimuth)

    sumLat += line.latitude()
    sumDep += line.departure()
    sumDist += float(azimuth)%360

    Lines.append((linecount, line.distance, line.bearing(),line.latitude(),line.departure())) 

    yn =  input("Add new linw? (Y/N)")
    if yn.lower == "yes" or yn == "Yes" or yn == "y" or yn.upper == "y":
        linecount = linecount + 1
        continue
    else:
        break


print("{: ^20}".format("\n\nLINES SIGHTED"))
print()
print("{: ^20}{: ^20}{: ^20}{: ^20}{: ^20}".format("LINE NO.","DISTANCE","BEARING","LATITUDE","DEPARTURE"))

for line in Lines:
    print("{: ^20}{: ^20}{: ^20}".format(line[0],line[1],line[2],line[3],line[4]))

print('SUMMATION OF LAT: {}'.format(sumLat))
print('SUMMATION OF DEP: {}'.format(sumDep))
print('SUMMATION OF DIST: {}'.format(sumDist))

lec = sqrt(sumLat**2 +sumDep**2)
print('LEC: {}'.format(lec))
rec = sumDist/lec
print('REC: {}'.format(round(rec,5)))
print("{:^40}".format("\n----END----"))

