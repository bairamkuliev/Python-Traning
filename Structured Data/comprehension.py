#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
from math import pi


def main():
    seq = range(11)
    seq2 = [(x, x ** 2) for x in seq]
    seq3 = [round(pi, i) for i in seq]
    seq4 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq4)
    print_list(seq2)
    print_list(seq3)


def print_list(o):
    for x in o: print(x, end=' ')
    print()


if __name__ == '__main__': main()
