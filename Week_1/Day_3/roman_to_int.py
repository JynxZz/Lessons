roman = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
    'IV':4,
    'IX':9,
    'XL':40,
    'XC':90,
    'CD':400,
    'CM':900
}
 
def roman_to_int(num_roman):
    result = 0
    i = 0
    
    while i < len(num_roman):
        if i+1 < len(num_roman) and num_roman[i:i+2] in roman:
            result += roman[num_roman[i:i+2]]
            i += 2
        elif num_roman[i] in roman:
            result += roman[num_roman[i]]
            i += 1
        else:
            return "Not a Roman Number"
        
    return result