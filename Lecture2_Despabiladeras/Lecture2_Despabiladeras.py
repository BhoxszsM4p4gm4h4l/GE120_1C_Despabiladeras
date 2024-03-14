"""listahan = ["mafe","justin","mika","uste"]
print(listahan[2])

print(listahan[0:2])
#print sa simula
print(listahan[:3])

print(listahan[2:])

#if from negative number, sa kabilang dulo yung start!
print(listahan[-1])

print(listahan[-3:3])

print(listahan[0:2]+listahan[2:4])
print(listahan[0:4])

#mutable - pweden palitan yung vaues ng elements sa loob
listahan[0]="chelsy"
print(listahan)

#tuple - sa paretheses and cannot be updated
tuple_1 = ("maja","gianna","jewel")
print(tuple_1)
print(tuple_1[0])

tuple_1[0]="quinmar"

grade = 59; paborite = True
if grade >= 92:
            print("YAHOO")
elif grade >= 60:
            print("nice")
elif grade< 60 and paborite:
            print("pasang awa")
else:
            print("sad") 

for letter in 'python':
    if letter == 'h':
        continue
    print('current letter: ', letter)

for letter in 'python':
    if letter == 'h':
        pass
        print('ulol')
    print('current letter: ', letter)

numbers = range (50,100)
print(numbers)
for number in range(10):
    if number == 5:
        pass #filler ang pass ulol
    print(number)
"""

rec = 0
while rec < 5000:
    rec = int(input("enter rec: "))
    kulang = 5000 - rec

    if rec == 4500:
        continue
        print("unti nalang pwede na")
    print("kulang ka ng rec na", kulang)

print("pasok na rec")
print("-----END-----")