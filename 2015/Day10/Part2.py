import time
start = time.process_time()

Input = open('Input.txt', 'r').read()
def lookAndSay(y,repetitions):
    x = y
    for k in range(repetitions):
        print(k)
        strOut = ''
        prevCharacter = x[0]
        tally = 0
        for i in range(len(x)):
            if i>0:
                prevCharacter = x[i-1]
            if prevCharacter == x[i]:
                tally = tally+1
            else:
                strOut = strOut + str(tally) + prevCharacter
                tally = 1
        strOut = strOut = strOut + str(tally) + x[len(x)-1]
        x = strOut
    return strOut
print(len(lookAndSay(Input, 50)))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[19] = '2015|Day 10|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()