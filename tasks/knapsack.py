"""Hamidreza Lolaei"""

# to solve using recursion: having two overlaying condition: 
#   1. item is bigger than the knapsack capacity and thus is excluded from the 
#      subset of all possibilities
#   2. the item is smaller than than knapsack capacity and resides in the subset of possibilities

# using recursion 

def knapsack(n, value, Wv, W):
    if n == 0 or W == 0:
        return 0 
    if (Wv[n-1] > W):
        return knapsack(n - 1, value, Wv, W)
    else:
        return max(value[n-1] + knapsack(n-1, value, Wv, W - Wv[n-1]), knapsack(n - 1, value, Wv, W)) 

Wv = [1, 4, 6, 7, 8]
values = [3, 5, 6, 7, 2]
n = len(values)
W = 7

print('Knapsack capacity :' , str(W)+'\n')
for i in range(len(values)):
    print(str(i+1) + ' :  val = ' + str(values[i]) + ' , weight = ' + str(Wv[i]))
print("Maximum value in knapsack : " ,knapsack(n, values, Wv,W))