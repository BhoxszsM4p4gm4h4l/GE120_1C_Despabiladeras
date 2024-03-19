"""

hello am yole!
GE120: Intro To Geomatic Application
Mariole B. Despabiladeras
2023-11218

Exercise 2

"""
counter=1

Lines = []

while True:
    print()
    print("Line #", counter)
    
    distance = input("Distance: ")
    azi = (input("Azimuth from the South: "))

    if "-" in str(azi):
        degrees,minutes, seconds = azi.split("-")
        azi = (int(degrees)+(int(minutes)/60)+(float(seconds)/3600))
        dms = 118.42069
        deg = int(dms)
        print("Degrees to be converted to DMS: ", dms)


        #for minutes we need to...
        mins=(dms - deg)*60
        mins_frac = int(mins)

        #for seconds we get...
        sec = (mins - mins_frac)*60
        rsec = round(sec,2)
        dems = [deg,mins_frac,rsec]
        print("The resulting DMS is " + str(deg) + "-" + str(mins_frac)+"-"+ str(rsec))
        #were now done for deg to dms!
    else: 
        azi = float(azi%360)
    if azi > 0 and azi <90:
        bearing = 'S {: ^10} W'.format(azi)
    elif azi > 90 and azi < 180:
        bearing = 'N {: ^10} W'.format(180 - azi)
    elif azi > 180 and azi < 270:
        bearing = 'N {: ^10} E'.format(azi - 180)
    elif azi > 270 and azi < 360:
        bearing = 'N {: ^10} E'.format(360 - azi)
    elif azi == 0:
        bearing = "DUE SOUTH"
    elif azi == 90:
        bearing = "DUE WEST"
    elif azi == 180:
        bearing = "DUE NORTH"
    elif azi == 270:
        bearing = "DUE EAST"
    else:
        bearing = "alaws"      

    line = (counter, distance, bearing)
    Lines.append(line)

    yn = input("add new line? ")
    if yn.lower == "yes" or yn == "Yes" or yn.upper == "yes" or yn == "y":
        counter = counter +1
        continue
    else:    
        break


print("\n\nLINES SIGHTED")
print("{: ^20}{: ^20}{: ^20}".format("LINE NO.","DISTANCE","BEARING"))
for line in Lines:
    print("{: ^20}{: ^20}{: ^20}".format(line[0],line[1],line[2]))
print("{:^40}".format("\n----END----"))
