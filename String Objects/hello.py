#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class MyString(str):
    def __str__(self):
        return self[::-1]


s = MyString('Hello, World.')
print(s)
