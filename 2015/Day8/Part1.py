import time
start = time.process_time()

Input = open('Input.txt', 'r').read().splitlines()
hexDigits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
charactersInMemory = 0
actualCharacters = 0
for i in range(len(Input)):
    workingString = [*Input[i]]
    subtract = 0
    actualCharacters = actualCharacters + len([*Input[i]]) 
    for j in range(1,len(workingString)):
        if (workingString[j] == '\\' or workingString[j] == '\"') and workingString[j-1] == '\\' :
            workingString[j] = '@'
            workingString[j-1] = '$'
    for j in range(3, len(workingString)):
        if hexDigits.count(workingString[j]) >= 1 and hexDigits.count(workingString[j-1]) >= 1 and workingString[j-2] == 'x' and workingString[j-3] == '\\':
            workingString[j] = '@'
            workingString[j-1] = '$'
            workingString[j-2] = '$'
            workingString[j-3] = '$'
    for j in reversed(range(len(workingString))):
        if workingString[j] == '$':
            workingString.pop(j)
    charactersInMemory = charactersInMemory + (len(workingString)-2)
print(actualCharacters - charactersInMemory)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[14] = '2015|Day 8|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()