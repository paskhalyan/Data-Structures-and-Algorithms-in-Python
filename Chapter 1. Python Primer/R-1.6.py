def ssum(n):
    s = 0
    for i in range(n):
        if i % 2 != 0:
            s += i * i
    return s


print(ssum(6))
