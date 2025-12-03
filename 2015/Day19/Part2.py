import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
medicine = []
toAdd = ''
for i in range(len(Input[-1])): 
    if Input[-1][i].isupper():
        medicine.append(toAdd)
        toAdd = Input[-1][i]
    else:
        toAdd = toAdd + Input[-1][i]
medicine.append(toAdd)
medicine.pop(0)
sum = 0
for i in medicine:
    if i == 'Y':
        sum += -2
    elif i == 'Rn' or i == 'Ar':
        sum += -1
    sum += 1
sum += -1
print(sum)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[37] = '2015|Day 19|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()