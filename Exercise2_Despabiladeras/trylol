# FUNCTIONS: because the uphold the DRY principle (Don't repeat Yourself)

# print("Hello World")

# Convert a number into a string
# a=1
# b=str(a)
# print(type(b))

# Define our own functions
# def shout(word):
#     # number = 2
#     print(number)
#     print(word + "!")

# number = 1

# Calling a fxn
# shout("YOLE")
# shout("AJ")
# shout("MIKA")
# shout("PETER")

# number = 3

# shout("JUSTIN")


# variables inside fxns are not available globally
# print(word)
# print(number)

# Use global variable if not in local
def shout(word1, num_ulit_last_letter):
    '''
    Given a word, kunin yung last letter, ulitin ng ilang beses
    tapos kapag prinint, print the word, plus inulit na last
    letter + exclamation point.

    Parameters:
    word1 (string) - word to be printed
    '''
    print(word1.upper()+word1[-1].upper()*(num_ulit_last_letter-1)+"!!!!!")
    # print(list_of_names)

# shout("Mafe", 5)

# print(len.__doc__)
# help(len)
# help(shout)

# TYPES OF ARGUMENTS

def convertDMStoDEG(dms="118-25-14.48", name="JANNUH"):
    '''
    Convert DMS to degrees

    Arguments:
        dms - string
    '''

    degrees, minutes, seconds = dms.split("-")
    dd = int(degrees) + (int(minutes)/60) + (float(seconds)/3600)
    return round(dd,6)

# convertDMStoDEG(name="MAJA", dms="123-13-14")

# VARIABLE LENGTH ARGUMENTS
def print_as_table(*lines):
    print('{: ^10} {: ^10} {: ^10}'.format("LINE NO.", "DISTANCE", "BEARING"))
    for line in lines:
        print('{: ^10} {: ^10} {: ^10}'.format(line[0], line[1], line[2]))

line1 = (1, '112.13', 'N    30.0    E')
line2 = (2, '123.124', 'S   12.124   W')
line3 = (3, '4357.11', 'DUE SOUTH')

# print_as_table(line1, line2, line3)

# RETURNING FROM A FUNCTION
result = convertDMStoDEG("12-12-12")
result += 10
print(result)


# printing after returning smth
def getDirection(degrees):
    '''
    Gives the direction of an angle

    Input:
    degrees - float

    Output
    quadrant - string
    '''

    print("HELLO DOM")
    if degrees > 0 and degrees < 90:
        return "S-W"
    elif degrees > 90 and degrees < 180:
        return "N-W"
    elif degrees > 180 and degrees < 270:
        return "N-E"
    elif degrees > 270 and degrees < 360:
        return "S-E"
    else:
        return "IDK"

dms = "100-12-14"
dd = convertDMStoDEG(dms)
direction = getDirection(dd)
print(direction)