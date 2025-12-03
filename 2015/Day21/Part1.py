import time
start = time.process_time()

import math
ShopInput = open('Shop.txt','r').read().splitlines()
ShopInput = [x.split() for x in ShopInput]
def playerW():
    playerWins = False
    pDam, bDam = ((playerStats[1]-bossStats[2]),(bossStats[1]-playerStats[2]))
    if pDam <= 0:
        pDam = 1
    if bDam <= 0:
        bDam = 1
    if math.ceil(bossStats[0]/(pDam))<=math.ceil(playerStats[0]/(bDam)):
        playerWins = True
    return playerWins

Weapons = [[int(x) for x in i if x.isnumeric()] for i in ShopInput[1:6]]
Armour = [[0,0,0]]+[[int(x) for x in i if x.isnumeric()] for i in ShopInput[8:13]]
Rings = [[0,0,0],[0,0,0]]+[[int(x) for x in i if x.isnumeric()] for i in ShopInput[15:21]]
playerStats,bossStats = ([100,0,0],[103,9,2])#health,damage,armour

lowCost = float('inf')
for i in Weapons:
    for j in Armour:
        for k in Rings[:-1]:
            for l in Rings[Rings.index(k)+1:]:
                cost = i[0]+j[0]+k[0]+l[0]
                playerStats = [100, i[1]+k[1]+l[1], j[2]+k[2]+l[2]]
                if cost < lowCost and playerW():
                    lowCost = cost
                    loc = [i,j,k,l]
print(lowCost, loc)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[40] = '2015|Day 21|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()