#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
   if idx > len(my_list)-1:
       return (my_list)
   else:
       lista = [my_list[i] for i in range(len(my_list)) if i != idx]
       return (lista)