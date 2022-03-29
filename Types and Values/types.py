#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
"""When will you want to use a decimal.Decimal type?
when numbers need to be treated as accurate decimals
The Decimal type is useful for accurate arithmetic calculation (e.g., when money is involved)"""
x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x[1]))
if isinstance(x, tuple):
    print('Tuple')
elif isinstance(x, list):
    print('List')
else:
    print('nope')

print(id(x))
print(id(y))
print(type(x))
print(type(y))