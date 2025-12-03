import time
start = time.process_time()

import re
Input = open('Input.txt', 'r').read().splitlines()
TrueAuntie = open('AuntSue.txt', 'r').read().splitlines()
for i in range(len(Input)):
    Input[i] = re.split(',',Input[i])
    Input[i][0] = Input[i][0][Input[i][0].index(':')+1:len(Input[i][0])]
    for j in range(len(Input[i])):
        Input[i][j] = Input[i][j][1:len(Input[i][j])]
theOneTrueAuntie = 0
for i in range(len(Input)):
    Sue = True
    for j in range(len(Input[i])):
        if TrueAuntie.count(Input[i][j]) == 0:
            Sue = False
    if Sue:
        theOneTrueAuntie = i+1
print(theOneTrueAuntie)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[30] = '2015|Day 16|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()