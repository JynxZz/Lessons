def is_colorful(num):
	n_str = str(num)

	if len(n_str) == 1:
		return True

	if len(n_str) == 2:
		n1=int(n_str[0])
		n2=int(n_str[1])
		num_list = [n1, n2, n1*n2]
		return len(set(num_list)) == 3

	if len(n_str) == 3:
		n1=int(n_str[0])
		n2=int(n_str[1])
		n3=int(n_str[2])
		num_list = [n1, n2, n3, n1*n2, n2*n3, n1*n2*n3]
		return len(set(num_list)) == 6

from math import prod

def is_colorful_evolve(num):

	n=list(map(int, str(num)))
	# ==> n=[int(i) for i in str(num)]
	table = []

	for i in range(0, len(n)):
		for j in range(i + 1, len(n)+1):
			table.append(prod(n[i:j]))

	return len(set(table)) == len(table)