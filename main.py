#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "???"


def add(x, y):
    """Add two integers."""
    # your code here
    return x + y


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    # your code here
    res = 0
    for i in range(abs(y)):
        res = add(res, abs(x))
    if x < 0 < y or y < 0 < x:
        return -res
    return res


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    # your code here
    res = 1
    for i in range(n):
        res = multiply(res, x)
    return res


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    # your code here
    res = 1
    for i in range(x, 0, -1):
        res = multiply(res, i)
    return res


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    # your code here
    res = []
    for i in range(n + 1):
        if i < 2:
            res.append(i)
        else:
            res.append(add(res[-2], res[-1]))
    print(res)
    return res[-1]


if __name__ == '__main__':
    # your code to call functions above
    pass
