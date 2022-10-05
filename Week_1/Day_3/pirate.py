def grabscrab(word, possible_words):
    wordsList = []
    letterDict = {l:word.count(l) for l in word}
    
    for word in possible_words:
        tester = {l:word.count(l) for l in word}
        if letterDict == tester:
            wordsList.append(word)

    return wordsList