"""

hi its me yole

"""

from math import cos, sin, radians 

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
latitude = getLatitude(12,45)
print(latitude)
departure = getDeparture(12,135)
print(departure)

#now for azimuth to bearing

def azimuthToBearing (azimuth):
    '''
    int
    azimuth - float

    out 
    bearing - string
    '''
    if  
    
    if azimuth > 0 and azimuth <90:
        bearing = 'S {: ^10} W'.format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'S {: ^10} W'.format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'S {: ^10} W'.format(azimuth - 180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^10} W'.format(360 - azimuth)
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
    line = (counter, distance, azimuth)
    Lines.append(line)

"""
how to get summation of lat and dep 
make a variable na 
sumLat  =+  lat ng line 
sumdep = sumdep + dep 

to geth teh running total of all the thinsg

gawa din ng summation ni distance


"""