import time
start = time.process_time()

import json
Input = json.load(open('Input.json'))
def evaluate(item):
    if type(item) == type(1):
        return item
    elif type(item) == type('ashfdjk'):
        return 0 
    elif type(item) == type([]):
        sum = 0
        for i in range(len(item)):
            sum += evaluate(item[i])
        return sum
    elif type(item) == type({}):
        vals = list(item.values())
        if vals.count("red")>0:
            return 0
        else:
            sum = 0
            for i in range(len(vals)):
                sum += evaluate(vals[i])
            return sum      
print(evaluate(Input))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[23] = '2015|Day 12|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()