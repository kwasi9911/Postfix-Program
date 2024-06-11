# Name: Nana Kwasi Owusu
# Partner name: Daniel Amayaenvbo
# Partner id: doa29
# Program Description: This is a program that evaluates mathematical expressions in postfix notation. It uses the stack data structure to compute the results

import sys
from stackclass import Stack

def postfix(expression):
    '''
    This function evaluates a postfix expression.
    The parameter of the function is the expression that the user enters and it returns a float value of the expression calculated
    '''
    stack = Stack()
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit() or (token[0]=='-' and token[1:].isdigit()):
            stack.push(float(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '-':
                result = left - right
            elif token == '+':
                result = left + right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right
            stack.push(result)
    return stack.pop()
            
    

if __name__ =="__main__":
    '''
    Testing for all the methods in stackclass.py and the postfix function
    
    creating stack object
    stack = Stack()
    
    populating the stack with a few values
    stack.push(20)
    stack.push(55)
    stack.push(90)
    stack.push(100)
    
    printing the stack
    print(stack)
    
    removing a few values from the stack
    stack.pop()
    stack.pop()
    
    printing the stack after removing a couple of values
    print(stack)
    
    checking which element is at the top of the stack
    print(f'The element at the top of the stack is {stack.top()}')
    
    checking if the stack is empty
    print(stack.isEmpty())
    
    testing postfix() function for subtraction
    print(postfix("4 5 -"))
    print(postfix("4 9 7 - -"))
    print(postfix("1 2 3 4 - - -"))
    print(postfix("1 2 - 3 - 4 -"))
    
    testing postfix() function for addition, multiplication, division
    print(postfix("15 20 12 + +"))
    print(postfix("11 2 3 * *"))
    print(postfix("100 4 2 4 / / /"))
    print(postfix("4 -1 9 5 2 3 + * - * /"))
    print(postfix("2 5 + 7 *")) 
    print(postfix("1 2 * 7 + 9 * 11 +"))
    print(postfix("-1 2 * 7 + -9 * 11 +"))
    '''
    
    print('Welcome to Postfix Calculator')
    print('Enter exit to quit')
    
    while True:
        userInput = input('Enter Expression: ')
        if userInput.lower() == 'exit':
            sys.exit(0)
            
        answer = postfix(userInput)
        print(f'Result: {answer}')
        
