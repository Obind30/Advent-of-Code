input = open("Input.txt", 'r').read().split()
callOrder = [int(i) for i in input[0].split(',')]
print(callOrder)