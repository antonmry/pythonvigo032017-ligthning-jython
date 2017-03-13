#!/usr/bin/env python


def fib(n):
    return fib(n-2) + fib(n-1) if 2 <= n else 1

for n in range(1, 40):
    print("fib(%d) = %d" % (n, fib(n)))
