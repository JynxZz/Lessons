def is_colorful(num):
    numList = []
    result = []
    
    #List de tous les occurences possibles
    for i in range(len(str(num))):
        for j in range(i, len(str(num))):
            numList.append(str(num)[i:j + 1])
            
    #List avec les produits     
    for i in range(len(numList)):
        n = 1
        p = numList[i]
        for j in range(len(p)):
            n = int(p[j]) * n
            if n not in result:
                result.append(n)
            
    #On donne la réponse 
    return True if len(numList) == len(result) else False