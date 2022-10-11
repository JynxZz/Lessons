import random

def manual_shuffle(original_list):
	shuffle_list = []
	tmp_list = original_list.copy()

	for n in range(0, len(tmp_list)):
		number = random.choice(tmp_list)
		shuffle_list.append(number)
		tmp_list.remove(number)

	return shuffle_list
