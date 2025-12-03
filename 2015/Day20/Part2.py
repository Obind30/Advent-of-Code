import time
import math
start = time.process_time()

Input = int(open('Input.txt','r').read())
tallies = [0]*Input
def factorsOf(n):
    factors = []
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if n%i == 0 and i == n//i and tallies[i]<50:
            factors.append(i)
            tallies[i] = tallies[i] + 1
        elif n%i == 0: 
            if tallies[i]<50:
                factors.append(i)
                tallies[i] = tallies[i] + 1
            tep = n//i
            if tallies[tep]<50:
                factors.append(n//i)
                tallies[tep] = tallies[tep] + 1
    return factors
currentHouseScore = 0    
house = 9
while currentHouseScore < Input:
    currentHouseScore = sum(factorsOf(house))*11
    house = house+1
print(house-1)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[39] = '2015|Day 20|Part 2|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()