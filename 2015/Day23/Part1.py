import time
start = time.process_time()

Input = [i.split() for i in open('Input.txt', 'r').read().splitlines()]
registers = {'a':0, 'b':0}
i = 0
while not(i >= len(Input) or i<0):
    if Input[i][0] == 'jmp':
        i += int(Input[i][1])
    elif Input[i][0] == 'jio':
        if registers[Input[i][1][0]] == 1:
            i += int(Input[i][2])
        else:
            i += 1
    elif Input[i][0] == 'jie': 
        if registers[Input[i][1][0]]%2 == 0:
            i += int(Input[i][2])
        else:
            i += 1
    elif Input[i][0] == 'hlf':
        registers[Input[i][1]] //= 2
        i += 1
    elif Input[i][0] == 'tpl':
        registers[Input[i][1]] *= 3
        i += 1
    elif Input[i][0] == 'inc':
        registers[Input[i][1]] += 1
        i += 1
print(registers['b'])

elap = str((time.process_time()-start)*1000)
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'r')
lines = Runtimes.readlines()
lines[44] = '2015|Day 23|Part 1|'+elap+'ms \n'
Runtimes = open('/Users/2024oliverbindewald/Documents/Code/AOC/2015/runtimes.txt', 'w')
Runtimes.writelines(lines)
Runtimes.close()