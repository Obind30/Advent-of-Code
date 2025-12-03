import time
start = time.process_time()

Input = open('Input.txt', 'r')
Data = Input.read()
Data = Data.splitlines()
for i in range(len(Data)):
    Data[i] = Data[i].split('x')
for i in range(len(Data)):
    areas = []
    for j in range(3):
        areas.append(2*int(Data[i][j])*int(Data[i][j-1]))
    Data[i] = sum(areas)+(min(areas)/2)
print(sum(Data))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[2] = '2015|Day 2|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()