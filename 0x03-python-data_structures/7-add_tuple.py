#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
        c = tuple(x-y for x, y in zip(tuple_a, tuple_b))
