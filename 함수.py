def hello(name):
    print("Hello!",name)


def square(x):
    a = x*x
    return a

def triangle(a,b):
    width = a*b/2
    return width

def summation(x):
    n=0
    for i in range(x+1):
        n+= i
    return n

def factorial(x):
    n=1
    for i in range(1,x+1):
        n= n*i
    return n
print(factorial(6))
        
