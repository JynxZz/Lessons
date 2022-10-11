import random

def manual_shuffle(original_list):
	shuffle_list = []
	tmp_list = original_list.copy()

	while len(tmp_list) > 0:
		index = random.randint(0, len(tmp_list)-1)
		shuffle_list.append(tmp_list[index])
		del tmp_list[index]

	return shuffle_list