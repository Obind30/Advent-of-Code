input = open("Input.txt", 'r').read().split()
count = 0
for i in range(len(input)-2):
    if (int(input[i-1])+int(input[i])+int(input[i+1])) < (int(input[i])+int(input[i+1])+int(input[i+2])):
        count += 1;
print(count)