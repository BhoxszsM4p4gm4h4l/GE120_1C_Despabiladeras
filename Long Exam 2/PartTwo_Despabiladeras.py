
class Parcel:
    def __init__(self,owner,area):
        self.owner = owner
        self.area = area
    def getClassification(self):
        
        if self.area < 1:
            print("Residential")
        elif self.area > 1 and self.area<12:
            print("Private Agricultural")
        elif self.area > 12:
            print("Public Agricultural")
        else:
            pass          
    
    def __str__(self.owner,areasqm):
        areasqm = self.area * 10000    
        print('A parcel of land owned by {} with an area of {} square meters'.format(self.owner,areasqm))


class Riparian(Parcel):
    def __init__(self, owner, area, type):
        self.owner = owner
        self.area = area
        self.type = type
    
    def getAdjoiningWaterbody(owner, type):
        if type == 1:
            print('Adjacent to River - can be subject to tilting')
        elif type == 2:
            print('Adjacent to Ocean (Littoral)')
        else:
            print('Invalid Riparian Parcel')
        pass
    

while True:
    print()
    print('PARCEL OF LAND DEFINITION')
#this is where we get our values to put onto the function (we can also check whether the variables are followed) 
    owner = input(str('Name of Owner'))
    area = input(int("Area (in sq. meters): "))

    if area < 1:
            print("Residential")
    elif area > 1 and area<12:
            print("Private Agricultural")
    elif area > 12:
            print("Public Agricultural")
    else:
            pass 

