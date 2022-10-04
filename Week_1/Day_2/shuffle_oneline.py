import random

def manual_shuffle(original_list):
	shuffle_list = []
	tmp_list = original_list.copy()

	while len(tmp_list) > 0:
		shuffle_list.append(tmp_list.pop(random.randint(0, len(tmp_list)-1)))
	return shuffle_list