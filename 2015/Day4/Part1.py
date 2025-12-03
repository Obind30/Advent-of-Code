import time
start = time.process_time()

import hashlib
BaseString = 'yzbqklnj'
i = 1
Hex = '111111'
while Hex[:5] != '00000':
    string = BaseString+str(i)
    Hex = (hashlib.md5(string.encode())).hexdigest()
    i+=1
print(i-1)

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[6] = '2015|Day 4|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()