import time
start = time.process_time()

row,collumn = 2978,3083
def pyramid(N):
    return int((N/2)*(N+1))
number = pyramid(collumn)+(pyramid(collumn+(row-2)))-(pyramid(collumn-1))
def deCoder(N):
    prev = 20151125
    result = (prev*252533)%33554393
    for i in range(N-2):
        prev = result
        result = (prev*252533)%33554393
    return result
print(deCoder(number))

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[48] = '2015|Day 25|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()