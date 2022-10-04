import random
def manual_shuffle(shuffleList):
    
    for i in range(0, len(shuffleList)):
        j = random.randint(0, len(shuffleList)-1)
        temp = shuffleList.pop(j)
        shuffleList.append(temp)
    return shuffleList