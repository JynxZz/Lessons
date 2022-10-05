ROMAN = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
}

# IV ==> -1 + 5
# XVI ==> 10 + 5 + 1
# MI ==> 1000 + 1

def roman_to_int(string):
    counter = 0 
    for i in range(0, len(string)-1):
        if ROMAN[string[i]] >= ROMAN[string[i+1]]:
            counter += ROMAN[string[i]]
        else:
            counter -= ROMAN[string[i]]

    return counter + ROMAN[string[-1]]