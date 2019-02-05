n = int(input('Input a positive integer: '))
print(sum([i*i for i in range(n) if i % 2 != 0]))
