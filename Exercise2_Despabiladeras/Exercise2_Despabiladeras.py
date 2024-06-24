linecount = 1
Lines = []

while True:
    
    print()
    print("Line #", linecount)

    distance = input("Distance:")
    azimuth = float(input("Azimuth from South:"))
    yn = input("Add a new line (Y/N)? ")

    if "-" in str(azimuth):
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees))+(int(minutes/60))+(float(seconds/3600))%3600
    else:
        azimuth = float(azimuth)%360
 
    deg=int(azimuth)
    min=(azimuth-deg)*60
    sec=(min-int(min))*60
    degminsec = [deg,int(min),round(sec,2)]
    dms = '-'.join(map(str, degminsec))

    if deg > 0 and deg < 90 and int(min)>=0 and sec>0:
        bearing ="N {} E".format(dms)
    elif deg > 90 and deg < 180 and int(min)>=0 and sec>=0:
        bearing = "N {} W".format(dms)
    elif deg > 180 and deg < 270 and int(min)>=0 and sec>=0:
        bearing = "S {} W".format(dms)
    elif deg > 270 and deg < 360 and int(min)>=0 and sec>=0:
        bearing = "S {} E".format(dms)
    elif deg == 90 and int(min) == 0 and sec == 0:
        bearing = "DUE NORTH"
    elif deg == 180 and int(min) == 0 and sec == 0:
        bearing = "DUE WEST"
    elif deg == 270 and int(min) == 0 and sec == 0:
        bearing = "DUE SOUTH"
    elif deg == 0 and int(min) == 0 and sec == 0:
        bearing = "DUE EAST"
    else:
        print('error')

    if azimuth > 0 and azimuth < 90:
        bearing = "S {:^5}  W".format(azimuth)
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
        bearing = "error"


    line = [linecount, distance, dms]
    Lines.append(line)

    if yn.lower == "yes" or yn == "Yes" or yn == "y" or yn.upper == "y":
        linecount = linecount + 1
        continue
    else:
        break


print("{:^20}".format("\n\nLINES SIGHTED"))
print()  
print("{:^20}{:^20}{:^20}".format("LINE NO.", "DISTANCE", "BEARING"))
for line in Lines:
    print('{: ^20} {: ^20} {: ^20}'.format(line[0], line[1], line[2]))
print("{:^40}".format("\n----END----"))

    
