input = open("Input.txt", 'r').read().split("\n")
gamma = 0
episolon = 0
for i in range(12):
    Count = 0
    for j in input:
        if j[i] == '1':
            Count += 1
    if Count > len(input)-Count:
        gamma += 2**(12-i-1)
    else:
        episolon += 2**(12-i-1)
print(gamma*episolon)