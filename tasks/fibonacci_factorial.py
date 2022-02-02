"""Hamidreza Lolaei"""


def factR(n):                                           
    if n == 1: 
        return n
    if n == 0 : 
        return 1
    else : 
       return n*factR(n - 1)

# calculatin fibonacci numbers using iteration 
def fibonacci_factorial(n): 
    ost = ''
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b += 1
        ost += ' ' + str(factR(c))
    return str(factR(0)) + ' ' + str(factR(1)) + ' ' + ost
print(fibonacci_factorial(100))

    
  