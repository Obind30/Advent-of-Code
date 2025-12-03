import time
start = time.process_time()

Data = open('Input.txt', 'r')
Input = Data.read()
currentPos = [0,0]
visited = [[0,0]]
for i in Input:
    if i == '^':
        currentPos = [currentPos[0], currentPos[1]+1]
    elif i == '>':
        currentPos = [currentPos[0]+1, currentPos[1]]
    elif i == 'v':
        currentPos = [currentPos[0], currentPos[1]-1]
    elif i == '<':
        currentPos = [currentPos[0]-1, currentPos[1]]
    print(currentPos)
    if visited.count(currentPos) == 0:
        visited.append(currentPos)
print(len(visited))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[4] = '2015|Day 3|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()