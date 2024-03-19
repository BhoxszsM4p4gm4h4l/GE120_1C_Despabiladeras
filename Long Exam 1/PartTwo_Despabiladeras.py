"""
Direct Levelling Computations

GE120 - DESPABILADERAS, MARIOLE B.
CLosed loop traverse for dorect levelling

"""
#we need to lagay yung mga initial things muna in order to add add stuff nalang later
counter = 1
level=[]
sumDist=0
Elev1 = 0
total_distance = float(sumDist)

def floatInput(prompt):
    bm0 = input("What is the initial Benchmark?")
    bs = float(input("What is the backsight (in meters): "))
    fs = float(input("What is the foresight (in meters): "))
    sumElev = 0
    hi = sumElev +  bs
    elev = hi - fs
    
    return
while True:
    print()
    print("MEASUREMENT NO: ", counter)

    woop = False
    while not(woop):
        distance = input("Distance: ")
        if woop:
            print("incorrect type of variable")
            continue
        if not(woop):
            break
     = input("Azimuth from the South: ")

    yn = input("add new line? ")
    if yn.lower == "yes" or yn == "Yes" or yn.upper == "yes" or yn == "y":
        counter = counter +1
        continue
    else:    
        break


"""
print("\n\nLINES SIGHTED")
print("{: ^20}{: ^20}{: ^20}".format("Sta.","B.S.","H.I.","F.S.","Elev"))
for levelling_table in level:
    print("{: ^20}{: ^20}{: ^20}".format(line[0],line[2],line[1],line[3]))
print("{:^40}".format("\n----END----"))
"""