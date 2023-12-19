'''
    Daily Coding Problem #481

    Good morning! Here's your coding interview problem for today.

    This problem was asked by Jane Street.

    Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
    Source: https://en.wikipedia.org/wiki/Reverse_Polish_notation

    The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

    For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] 
    should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

    You can assume the given expression is always valid.
'''

ops = {
    "+" : (lambda a, b: a + b),
    "-" : (lambda a, b: a - b),
    "*" : (lambda a, b: a * b),
    "/" : (lambda a, b: a / b),
    "**" : (lambda a, b: a ** b)
}

def eval(expression):
    tokens = expression.split()
    stack = []

    for token in tokens:
        if token in ops:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = ops[token](arg1, arg2)
            stack.append(result)
        
        else:
            stack.append(int(token))
    
    return stack.pop()


print(eval("1 2 +"))
print(eval("990 1 2 + *"))
print(eval("1000 990 1 2 + * +"))