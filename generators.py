# 1
def squares(n):
    return [i ** 2 for i in range(n)]


# 2
def even(n):
    return ', '.join([str(i) for i in range(n) if not i % 2])


# 3
def three_four(n):
    return [i for i in range(n) if not i % 3 or not i % 4]


# 4
def squares_yield(a, b):
    for i in range(a, b + 1):
        yield i ** 2


# 5
def rever(n):
    return [i ** 2 for i in range(n, -1, -1)]
