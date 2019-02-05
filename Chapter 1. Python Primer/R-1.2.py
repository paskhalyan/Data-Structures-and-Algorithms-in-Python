def is_even(k):
    if k & 1 == 0:
        return True
    return False


k = int(input('Input an integer: '))
print(is_even(k))
