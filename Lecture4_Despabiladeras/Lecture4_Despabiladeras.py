print("hello")
a=1

str(a)
b=str(a)
print(type(b))
"""
#walang nanyare bc walang call func pa!!!
def shout(word1,word2):
    '''
    Given a word, kunin yung last letter ulitin ng ilang beses taos kapag prinint print the word plus inulit a last letter + exclamation point

    Parameters:
    word1 (string) - word to be printed
    '''
    print (word1.upper()+ word1[-1].upper()*(word2)"!")
    print ("i created this function")

print(len.__doc__)
help(shout)

"""

def convertdmstodeg(dms="118-25-14.48",name="jannah"):
    '''
    converts dms to deg
    
    arguments: 
    dms - string
    '''

    degrees, minutes, seconds = dms.split("-")
    dd = int(degrees) + (int(minutes)/60)+float(seconds/3600)
    print(name + "eto olol:", round(dd,6))

convertdmstodeg("maja","123-13-14")  