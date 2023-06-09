#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    lista = [False if my_list[i] % 2 != 0 else True for i in range(len(my_list)-1)]
    return (lista)
