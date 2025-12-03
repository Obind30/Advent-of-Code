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
    Sue = 0
    for j in range(len(Input[i])):
        if 'cats' in Input[i][j] and int(Input[i][j][len(Input[i][j])-1]) > int(TrueAuntie[1][len(TrueAuntie[1])-1]):
            Sue = Sue+1
        elif 'trees' in Input[i][j] and int(Input[i][j][len(Input[i][j])-1]) > int(TrueAuntie[7][len(TrueAuntie[7])-1]):
            Sue = Sue+1
        elif 'pomeranians' in Input[i][j] and int(Input[i][j][len(Input[i][j])-1]) < int(TrueAuntie[3][len(TrueAuntie[3])-1]):
            Sue = Sue+1
        elif 'goldfish' in Input[i][j] and int(Input[i][j][len(Input[i][j])-1]) < int(TrueAuntie[6][len(TrueAuntie[6])-1]):
            Sue = Sue+1
        elif TrueAuntie.count(Input[i][j]) > 0 and not('cats' in Input[i][j]) and not('trees' in Input[i][j]) and not('pomeranians' in Input[i][j]) and not('goldfish' in Input[i][j]):
            #Sue = False
            Sue = Sue + 1
        else:
            Sue = 0
    if Sue == 3:
        theOneTrueAuntie = i+1
        print(i+1)
#print(theOneTrueAuntie)
#Should be 405

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[31] = '2015|Day 16|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()