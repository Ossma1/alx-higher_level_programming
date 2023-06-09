#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    cp = [a for a in my_list]
    cp[idx] = element
    return (cp)
