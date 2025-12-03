import time
start = time.process_time()

Input = open("Input.txt",'r')
Data = Input.read()
floor = 0
for i in Data:
    if i == '(':
        floor = floor+1
    else:
        floor = floor-1
print(floor)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[0] = '2015|Day 1|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()