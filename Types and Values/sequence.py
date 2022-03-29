#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))

a = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
a['three']=42
for k,v in a.items():
    print('k: {}, v: {}'.format(k,v))

for i in a:
    print('i is {}'.format(i))