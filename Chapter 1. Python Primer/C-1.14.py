def odd_product(data):
	odd_sum = 0
	for number in data:
		if number % 2 != 0:
			odd_sum += 1
		if odd_sum > 1:
			return True
	return False


def one_line_odd_product(data):
	return len([i for i in data if i % 2 != 0]) > 1


data = [1, 3, 2, 4]
print(one_line_odd_product(data))
