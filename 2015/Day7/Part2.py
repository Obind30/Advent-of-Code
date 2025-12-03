import time
start = time.process_time()

Input = open('Input.txt','r').read().splitlines()
for i in range(len(Input)):
    Input[i] = Input[i].split()
valuesList = []
for i in range(len(Input)):
    valuesList.append('z')
def findValue(directory):
    if directory.isnumeric():
        return int(directory)
    dirIndex = -1
    for i in range(len(Input)):
        if Input[i][len(Input[i])-1] == directory:
            dirIndex = i
    if not(valuesList[dirIndex] == 'z'):
        return valuesList[dirIndex]
    if Input[dirIndex][0] == 'NOT':
        x = ~findValue(Input[dirIndex][1])
        valuesList[dirIndex] = x
        return x
    elif Input[dirIndex][1] == 'AND':
        x = findValue(Input[dirIndex][0])&findValue(Input[dirIndex][2])
        valuesList[dirIndex] = x
        return x
    elif Input[dirIndex][1] == 'OR':
        x = findValue(Input[dirIndex][0])|findValue(Input[dirIndex][2])
        valuesList[dirIndex] = x
        return x
    elif Input[dirIndex][1] == 'RSHIFT':
        x = findValue(Input[dirIndex][0])>>int(Input[dirIndex][2])
        valuesList[dirIndex] = x
        return x
    elif Input[dirIndex][1] == 'LSHIFT':
        x = findValue(Input[dirIndex][0])<<int(Input[dirIndex][2])
        valuesList[dirIndex] = x
        return x
    else:
        x = findValue(Input[dirIndex][0])
        valuesList[dirIndex] = x
        return x
oldA = findValue('a')
valuesList = []
for i in range(len(Input)):
    valuesList.append('z')
for i in range(len(Input)):
    if Input[i][len(Input[i])-1] == 'b':
        valuesList[i] = oldA
print(findValue('a'))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[13] = '2015|Day 7|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()