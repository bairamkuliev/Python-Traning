#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
'''
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')

    return f2


@f1
def f3():
    print('this is f3')


f3()'''


def Sort_Tuple(tuples):
    # getting length of list of tuples
    list = len(tuples)
    for i in range(0, list):
        for j in range(0, list - i - 1):
            if (tup[j][1] > tuples[j + 1][1]):
                temp = tuples[j]
                tup[j] = tuples[j + 1]
                tuples[j + 1] = temp
    return tuples


# Driver Code
tup = [('for', 24), ('is', 10), ('Geeks', 28),('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]

print(Sort_Tuple(tup))
import numpy as np
t = np.array([1,1,1,2,2,3,8,3,8,8])
np.nonzero(t==8)[0][0]
def eval(var1,var2)