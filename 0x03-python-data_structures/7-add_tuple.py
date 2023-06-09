#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        newtuple = (0, 0) if len(tuple_a) == 0 else tuple_a + (0, )
    elif len(tuple_a) >= 2:
        newtuple = tuple_a
    if len(tuple_b) < 2:
        new1 = (0, 0) if len(tuple_b) == 0 else tuple_b + (0, )
    elif len(tuple_b) >= 2:
        new1 = tuple_b
    tuple_somme = tuple(x + y for x, y in zip(newtuple, new1))
    return tuple_somme
