def fibonacci(n):
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(2, n+1):
        temp = a + b
        a = b
        b = temp
    return b


def lucas(n):
    a = 2
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(2, n+1):
        temp = a + b
        a = b
        b = temp
    return b


def sum_series(n, a=0, b=1):
    if a == 0:
        for i in range(2,n+1):
            temp = a + b
            a = b
            b = temp

        return b
    if a == 2:
        for i in range(2,n+1):
            temp = a + b
            a = b
            b = temp

        return b
    if b == 1:
        return b
