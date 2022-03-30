#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = 5
    kitten(x)
    print(f'in main: x is {x}')
    kitten()


def kitten(a):
    a[0] = 3  # call by reference
    print(a)
    print('Meow.')


if __name__ == '__main__': main()
