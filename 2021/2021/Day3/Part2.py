import copy
input = open("Input.txt", 'r').read().split("\n")
possibleO = copy.copy(input)
possibleC = copy.copy(input)
for i in range(12):
    ones = 0
    for j in range(len(possibleO)):
        if possibleO[j][i] == '1':
            ones += 1
    lookingFor = "0"
    if ones >= len(possibleO) - ones:
        lookingFor = "1"
    for j in range(len(possibleO)-1,-1,-1):
        if len(possibleO) == 1:
            break
        if possibleO[j][i] != lookingFor:
            possibleO.pop(j)
for i in range(12):
    ones = 0
    for j in range(len(possibleC)):
        if possibleC[j][i] == '1':
            ones += 1
    lookingFor = "0"
    if ones < len(possibleC) - ones:
        lookingFor = "1"
    for j in range(len(possibleC)-1,-1,-1):
        if len(possibleC) == 1:
            break
        if possibleC[j][i] != lookingFor:
            possibleC.pop(j)
print(possibleO)
print(possibleC)
print(int(possibleC[0], base = 2) * int(possibleO[0], base = 2))