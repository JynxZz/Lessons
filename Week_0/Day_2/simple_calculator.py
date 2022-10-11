def simple_calculator(calcul):
    valid_operator = "+-*/%"
    operator = calcul[1]
    
    if operator in valid_operator and len(calcul)==3:
        n1 = float(calcul[0])
        n2 = float(calcul[2])
        if operator == "+":
            return n1+n2
        if operator == "-":
            return n1-n2
        if operator == "*":
            return n1*n2
        if operator == "/":
            return n1/n2
        if operator == "%":
            return n1%n2
    elif operator not in valid_operator and len(calcul) != 3:
        return 'Please enter valid format: [Operand, Operator, Operand]'
    else:
        return 'Please enter a valid operator [ +, -, /, *, % ]'