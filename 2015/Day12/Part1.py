import time
start = time.process_time()

Input = list(open('Input.txt', 'r').read())
numbers = []
toAdd = []
for i in range(len(Input)):
    if Input[i].isnumeric() or Input[i] == '-':
        toAdd.append(Input[i])
    elif len(toAdd) > 0:
        numbers.append(int(''.join(toAdd)))
        toAdd = []
print(sum(numbers))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[22] = '2015|Day 12|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()