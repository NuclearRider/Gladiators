import csv
import random

print("Tonight's Fighters")
f = open('namesyllables.csv')
csv_f = csv.reader(f)

names = []

for row in csv_f:
    names.append(row[0])

g = open('adjectives.csv')
csv_g = csv.reader(g)

descript = []

for row in csv_g:
    descript.append(row[0])

t = open('Weapons.csv')
csv_t = csv.reader(t)

weapons = []

for row in csv_t:
    weapons.append(row[0])

b = open('Body.csv')
csv_b = csv.reader(b)

body = []

for row in csv_b:
    body.append(row[0])

ftr1first = names[random.randrange(1, 125)] + names[random.randrange(1, 125)]
ftr2first = names[random.randrange(1, 125)] + names[random.randrange(1, 125)]
ftr1 = ftr1first + " the " + descript[random.randrange(1, 1300)] + "ly " +descript[random.randrange(1, 1300)]
ftr2 = ftr2first  + " the " + descript[random.randrange(1, 1300)] + "ly " +descript[random.randrange(1, 1300)]

print(ftr1)
print("Versus")
print(ftr2)

bothalive = True

while bothalive == True:
    print(ftr1first + " hits " + ftr2first + " with a " + weapons[random.randrange(1, 96)] + " in the " + body[random.randrange(1, 163)])
    attk = random.randrange(1, 100)
    if attk > 89:
        print(ftr2 + " is killed!")
        bothalive = False
    if bothalive == False:
        break
     
    print(ftr2first + " hits " + ftr1first + " with a " + weapons[random.randrange(1, 96)] + " in the " + body[random.randrange(1, 163)])
    attk = random.randrange(1, 100)
    if attk > 89:
        print(ftr2 + " is killed!")
        bothalive = False     
     