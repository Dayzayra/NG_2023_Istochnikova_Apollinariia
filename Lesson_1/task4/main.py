def plus ( a, b):
    c=a+b
    return c

def min (a, b):
    c=a-b
    return c

def mult(a,b):
    c=a/b
    return c

def div(a,b):
    c=a/b
    return c

def pow(a,b):
    c=a**b
    return c

def root (a,b):
    c=a**(1/b)
    return c
  
math_operation = (input("Choose math operation +,-,/,*,pow,root: "))
a=(float(input("Enter first number: ")))
b=(float(input("Enter second number: ")))

match math_operation:
    case '+': 
        result=plus(a,b)
    case '-':
        result=min(a,b)  
    case '*':
        result=mult(a,b)   
    case '/':
        result=div(a,b)
    case 'pow':
        result=pow(a,b)    
    case 'root':
        result=root(a,b)  
    case _:
        print('You made an input error, reload program and try again.'),
        exit()
        
print ('Result of math operation is number: ', result)
