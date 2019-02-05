from random import randrange


def choice(data):
    return data[randrange(len(data))]


data = [1, 3, 8, 4, 2, 6, 15, 645421, 9]
print(choice(data))
