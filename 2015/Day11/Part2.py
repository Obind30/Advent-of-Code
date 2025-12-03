import time
start = time.process_time()

Input = open('Input.txt', 'r').read()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','~']
def incrementstr(x):
    x[len(x)-1] = alphabet[alphabet.index(x[len(x)-1])+1]
    for i in reversed(range(len(x))):
        if x[i] == '~':
            x[i] = 'a'
            if i-1 == -1:
                x.insert(0,'b')
            x[i-1] =  alphabet[alphabet.index(x[i-1])+1]
    return x
def checkPaswordValidity(x):
    oneCheck = False
    twoCheck = True
    threeCheck = False
    twoInaRowCount = []
    for i in range(len(x)-2):
        if alphabet.index(x[i]) == alphabet.index(x[i+1])-1 and alphabet.index(x[i]) == alphabet.index(x[i+2])-2:
            oneCheck = True
    for i in x:
        if i == 'i' or i == 'o' or i == 'l':
            twoCheck = False
    for i in range(len(x)-1):
        if x[i] == x[i+1] and twoInaRowCount.count(x[i]) == 0:
            twoInaRowCount.append(x[i])
    if len(twoInaRowCount) >= 2:
        threeCheck = True
    if oneCheck and twoCheck and threeCheck:
        return True
    else:
        return False
string = list(Input)
while not(checkPaswordValidity(string)):
    string = incrementstr(string)
lastOne = incrementstr(string)
string = list(lastOne)
while not(checkPaswordValidity(string)):
    string = incrementstr(string)
print(string)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[21] = '2015|Day 11|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()