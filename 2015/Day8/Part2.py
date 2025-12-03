import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
hexDigits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
origCharacters = 0
total = 0
for i in range(len(Input)):
    workingArray = [*Input[i]]
    actualCharacters = origCharacters + len([*Input[i]]) 
    add = 0
    for j in range(len(workingArray)):
        if workingArray[j] == '\"':
            add = add + 1
        elif  workingArray[j] == '\\':
            add = add + 1
        add = add
    total = total + add + 2
print(total)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[15] = '2015|Day 8|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()