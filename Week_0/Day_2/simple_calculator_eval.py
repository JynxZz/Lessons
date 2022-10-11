def simple_calculator(operation):
    format_prompt = "Please enter valid format: [Operand, Operator, Operand]"
    operator_prompt = "Please enter a valid operator [ +, -, /, *, % ]"
    if not len(operation) == 3: 
        return format_prompt
    elif not operation[1] in['+','-','/','*','%']: 
        return operator_prompt
    else: 
        return eval(f'{operation[0]}{operation[1]}{operation[2]}')