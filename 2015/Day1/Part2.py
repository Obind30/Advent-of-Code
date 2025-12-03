import time
start = time.process_time()

Input = open("Input.txt",'r')
Data = Input.read()
floor = 0
position = 0
for i in range(len(Data)):
    if Data[i] == '(':
        floor = floor+1
    else:
        floor = floor-1
    if floor == -1 and position == 0:
        position = i+1
print(position)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[1] = '2015|Day 1|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()