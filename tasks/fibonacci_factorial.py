"""Hamidreza Lolaei"""


def factR(n):                                           
    if n == 1 and n == 0 : 
        return 0
    else : 
       return n*factR(n - 1)

# calculatin fibonacci numbers using iteration 
def fibonacci_factorial(n): 
    ost = ''
    a = 0
    b = 1
    for i in range(n-1):
        c = a + b
        a = b
        b += 1
        ost += ' ' + str(factR(c))
    return ost
print(fibonacci_factorial(20))


    
  