def minmax(data):
    minimum = data[0]
    maximum = data[0]
    for i in data:
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
    return minimum, maximum


seq = [1, 6, 8, 9, 7, 4, 5, 6]
print(minmax(seq))
