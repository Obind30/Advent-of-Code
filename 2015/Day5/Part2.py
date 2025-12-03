import time
start = time.process_time()

RawInput = open('Input.txt','r')
Input = RawInput.read().split()
#Input = ['qjhvhtzxzqqjkmpb']
niceCount = 0
for p in range(len(Input)):
    repetedString = False
    for i in range(len(Input[p])-1):
        if Input[p].count(Input[p][i]+Input[p][i+1])>1:
            repetedString = True
    oneLetterBetween = False
    for i in range(len(Input[p])-2):
        if Input[p][i] == Input[p][i+2]:
            oneLetterBetween = True
    if repetedString == True and oneLetterBetween == True:
        niceCount += 1
print(niceCount)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[9] = '2015|Day 5|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()