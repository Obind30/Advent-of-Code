import time
import math
start = time.process_time()

Input = int(open('Input.txt','r').read())
def factorsOf(n):
    factors = []
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if n%i == 0 and i == n//i:
            factors.append(i)
        elif n%i == 0: 
            factors.append(i)
            factors.append(n//i)
    return factors
currentHouseScore = 0    
house = 9
while currentHouseScore < Input:
    currentHouseScore = sum(factorsOf(house))*10
    house = house+1
print(house-1)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[38] = '2015|Day 20|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()