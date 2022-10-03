def is_colorful(number):
    
        
    numList = []
    for c in str(number):
        R = (numList.append(int(c)))
        

    n = len(numList) 
    _produit = 1
    for i in numList:
        _produit = _produit * i
    
    i =0
    if n >2 :  
        while i < (n-1) :
            numList.append(numList[i]*numList[i+1])
            i = i+1
 
    
    numList.append(_produit)
    print (numList)
    if n > 2 : 
        if len(set(numList)) == (n+3):
            return True
        else : 
            return False
    else : 
        if len(set(numList)) == (n+1): 
            return True 
        else : 
            return False