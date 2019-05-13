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
fighters_short = []
i = 1
while i < 9:
    
    fighters_short.append(names[random.randrange(1, len(names))] + names[random.randrange(1, len(names))])
    
    fighters_name.append(fighters_short[i-1] + " the " + descript[random.randrange(1, len(descript))] + "ly " +descript[random.randrange(1, len(descript))])
    i += 1

#ftr1first = names[random.randrange(1, len(names))] + names[random.randrange(1, len(names))]
#ftr2first = names[random.randrange(1, len(names))] + names[random.randrange(1, len(names))]
#ftr1 = ftr1first + " the " + descript[random.randrange(1, len(descript))] + "ly " +descript[random.randrange(1, len(descript))]
#ftr2 = ftr2first  + " the " + descript[random.randrange(1, len(descript))] + "ly " +descript[random.randrange(1, len(descript))]

print("Tonight's Fighters")
print(" ")
print("\n".join(fighters_name))
#print(fighters_name)

p = 0
while p < 8:
    print(" ")
    print("Match "+ str(p/2+1) )
    print(fighters_name[p])
    print("Versus")
    print(fighters_name[p+1])
    print(" ")
    p += 2

bothalive = True

while bothalive == True:
    print(fighters_short[0] + " hits " + fighters_short[1] + " with their " + weapons[random.randrange(1, len(weapons))] + " in the " + body[random.randrange(1, len(body))])
    attk = random.randrange(1, 1000)
    if attk > 900:
        print(fighters_name[1] + " is killed!")
        bothalive = False
    if bothalive == False:
        break
    
    print(fighters_short[1] + " hits " + fighters_short[0] + " with their " + weapons[random.randrange(1, len(weapons))] + " in the " + body[random.randrange(1, len(body))])
    attk = random.randrange(1, 1000)
    if attk > 900:
        print(fighters_name[0] + " is killed!")
        bothalive = False
