def factorial(n):
    prod = 1
    for i in range(1, n, -1):
        prod *= i
    return prod


def fibo(n):
    a, b = 0, 1
    c = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c
