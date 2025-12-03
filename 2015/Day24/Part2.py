import time
start = time.process_time()

Input = [int(i) for i in open('Input.txt','r').read().splitlines()]
#Input.reverse()
containerweights = sum(Input)//4
ind = [i for i in range(len(Input))]
def combinationsThatAddTo(x,indicies, usedIndicies):
    if len(usedIndicies)>lowLength:
        return []
    if x == 0:
        return [usedIndicies]
    else:
        out = []
        toUse = indicies.copy()
        i = 0
        while len(toUse)>0:
            if x-Input[toUse[i]]>=0:
                nextIndicies = toUse.copy()
                nextIndicies.pop(0)
                recurs = combinationsThatAddTo(x-Input[toUse[i]],nextIndicies,usedIndicies+[toUse[i]])
            else:
                recurs = []
            toUse.pop(0)
            out = out + recurs 
        return out
lowLength = 1
combos = []
while len(combos) == 0:
    combos = combinationsThatAddTo(containerweights, ind, [])
    lowLength += 1
print(combos)
for i in range(len(combos)):
    product = 1
    for j in combos[i]:
        product *= Input[j]
    combos[i] = product
print(min(combos))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[47] = '2015|Day 24|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()