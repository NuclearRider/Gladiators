import csv
import random


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

fighters_name = []
i = 1
while i < 9:
    fighters_name.append(names[random.randrange(1, len(names))] + names[random.randrange(1, len(names))]
                         + " the " + descript[random.randrange(1, len(descript))] + "ly " +descript[random.randrange(1, len(descript))])
    i += 1

#ftr1first = names[random.randrange(1, len(names))] + names[random.randrange(1, len(names))]
#ftr2first = names[random.randrange(1, len(names))] + names[random.randrange(1, len(names))]
#ftr1 = ftr1first + " the " + descript[random.randrange(1, len(descript))] + "ly " +descript[random.randrange(1, len(descript))]
#ftr2 = ftr2first  + " the " + descript[random.randrange(1, len(descript))] + "ly " +descript[random.randrange(1, len(descript))]
#Rider rules

print("Tonight's Fighters")
print(" ")
print(fighters_name)

print(" ")
print("First Match")

print(fighters_name[1])
print("Versus")
print(fighters_name[2])
print(" ")

bothalive = True

while bothalive == True:
    print(fighters_name[1] + " hits " + fighters_name[2] + " with his " + weapons[random.randrange(1, len(weapons))] + " in the " + body[random.randrange(1, len(body))])
    attk = random.randrange(1, 1000)
    if attk > 800:
        print(fighters_name[2] + " is killed!")
        bothalive = False
    if bothalive == False:
        break
    
    print(fighters_name[2] + " hits " + fighters_name[1] + " with his " + weapons[random.randrange(1, len(weapons))] + " in the " + body[random.randrange(1, len(body))])
    attk = random.randrange(1, 1000)
    if attk > 800:
        print(fighters_name[1] + " is killed!")
        bothalive = False     
     
