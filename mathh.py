import math


# 1
def rad(n):
    return math.pi * n / 180


# 2
def trap(h, a, b):
    return (a + b) / 2 * h


# 3
def polygon(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))


# 4
def parallelogram(h, a):
    return float(a * h)