def is_multiple(n, m):
    if n % m == 0:
        return True
    return False


n = int(input('Input integer: '))
m = int(input('Input integer: '))
print(is_multiple(n, m))
