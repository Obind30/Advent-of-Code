input = open("Input.txt", 'r').read().split("\n")
depth = 0
why = 0
aim = 0
for i in input:
    y = i.split()
    if y[0] == "forward":
        why += int(y[1])
        depth += aim * int(y[1])
    if y[0] == "down":
        aim += int(y[1])
    if y[0] == "up":
        aim -= int(y[1])
print(depth*why)