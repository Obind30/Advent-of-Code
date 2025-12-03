import time
start = time.process_time()

Input = open('Input.txt', 'r')
Data = Input.read()
Data = Data.splitlines()
for i in range(len(Data)):
    Data[i] = Data[i].split('x')
for i in range(len(Data)):
    bowLength = 1
    for j in range(3):
        Data[i][j] = int(Data[i][j])
        bowLength = bowLength*Data[i][j]
    Data[i].remove(max(Data[i]))
    Data[i] = sum(Data[i]*2)+bowLength
print(sum(Data))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[3] = '2015|Day 2|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()