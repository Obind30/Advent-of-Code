import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
BaseChemical = Input[len(Input)-1]
Input.pop()
Input.pop()
for i in range(len(Input)):
    Input[i] = Input[i].split()
variations = []
for i in range(len(Input)):
    for j in range(len(BaseChemical)-len(Input[i][0])+1):
        checkingStr = BaseChemical[j:j+len(Input[i][0])]
        if checkingStr == Input[i][0]:
            add = BaseChemical[0:j]+Input[i][2]+BaseChemical[j+len(Input[i][0]):]
            if variations.count(add) == 0:
                variations.append(add)
print(len(variations))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[36] = '2015|Day 19|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()