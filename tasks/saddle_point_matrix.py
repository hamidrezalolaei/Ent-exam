"""Hamidreza Lolaei"""
# any intersection between the minimum item in each set and the maximum item in the column is considered to be the saddle point
import numpy as np

def saddle_point(mat):
    rows_mins = set(mat.min(axis=1))
    print("rows : " , rows_mins)
    columns_maxes = set(mat.max(axis=0))
    print("columns :" ,columns_maxes)
    if rows_mins.intersection(columns_maxes):
        print("saddle point : " + str(rows_mins.intersection(columns_maxes)))
    else : 
        print("no saddle point")

rg = np.random.default_rng(1)

test1 = rg.random(9).reshape((3,3))   
test2 = rg.random(9).reshape((3,3))   
test3 = rg.random(9).reshape((3,3))   
test4 = rg.random(9).reshape((3,3))   
test5 = rg.random(9).reshape((3,3))   
test6 = rg.random(9).reshape((3,3))   
test7 = rg.random(9).reshape((3,3))   
test8 = rg.random(9).reshape((3,3))   
test9 = rg.random(9).reshape((3,3))   
test10 = rg.random(9).reshape((3,3))   

print("test1 : ", test1)
saddle_point(test1)
print("test2 : ", test2)
saddle_point(test2)
print("test3 : ", test3)
saddle_point(test3)
print("test4 : ", test4) # saddle point = 0.6130033010530405
saddle_point(test4)
print("test5 : ", test5)
saddle_point(test5)
print("test6 : ", test6)
saddle_point(test6)
print("test7 : ", test7)
saddle_point(test7)
print("test8 : ", test8)
saddle_point(test8)
print("test9 : ", test9)
saddle_point(test9)
print("test10 : ", test10)
saddle_point(test10)

