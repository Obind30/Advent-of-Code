input = open("Input.txt", 'r').read().split()
count = 0
for i in range(len(input)-1):
    if int(input[i])<int(input[i+1]):
        count += 1;
print(count)