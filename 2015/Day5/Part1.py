import time
start = time.process_time()

RawInput = open('Input.txt','r')
Input = RawInput.read().split()
niceCount = 0
vowels = ['a','e','i','o','u']
naughtyStrings = ['ab', 'cd', 'pq', 'xy']
for p in range(len(Input)):
    numOfVowels = 0
    duped = False
    constainsNaughtyString = False
    for i in Input[p]:
        if i in vowels:
            numOfVowels = numOfVowels+1
    for i in range(len(Input[p])-1):
        if Input[p][i] == Input[p][i+1]:
            duped = True
    for i in naughtyStrings:
        if i in Input[p]:
            constainsNaughtyString = True
    if numOfVowels >= 3 and duped and not(constainsNaughtyString):
        niceCount = niceCount+1
print(niceCount)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[8] = '2015|Day 5|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()