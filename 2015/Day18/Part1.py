import time
start = time.process_time()

Input = open('Input.txt','r').read().splitlines()
for i in range(len(Input)):
    Input[i] = list(Input[i])
def countNeighbors(point, matrix):
    checks = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
    adjacent = 0
    for i in checks:
        if [point[0]+i[0],point[1]+i[1]].count(-1) == 0 and [point[0]+i[0],point[1]+i[1]].count(len(matrix)) == 0:
            if matrix[point[0]+i[0]][point[1]+i[1]] == '#':
                adjacent = adjacent + 1
    return adjacent
for k in range(100):
    tempInput = []
    for i in range(len(Input)):
        tempInput.append(['.']*len(Input[0]))
    for i in range(len(Input)):
        for j in range(len(Input[i])):
            neighbors = countNeighbors([i,j], Input)
            if Input[i][j] == '#' and (neighbors == 3 or neighbors == 2):
                tempInput[i][j] = '#'                
            if Input[i][j] == '.' and neighbors == 3:
                tempInput[i][j] = '#'
    Input = tempInput.copy()
sum = 0
for i in Input:
    sum = sum + i.count('#')
print(sum)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[34] = '2015|Day 18|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()