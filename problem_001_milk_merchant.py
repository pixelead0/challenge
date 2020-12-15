#!/bin/python3


def milk_merchant(n: int, ar: list):
    """
    n: the number of milk box in the pile
    ar: the colors of each milk box
    """
    stack: dict = {}
    pairs: int = 0
    ar.sort()

    for i in range(n):
        if stack.get(ar[i], None):
            stack.pop(ar[i])
            pairs += 1
        else:
            stack[ar[i]] = 1
    return pairs
