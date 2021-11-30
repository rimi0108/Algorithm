# 1
def add(n):
    s = 0
    for i in range(n + 1):
        s = s + (i * i)
    return s


# 2
def add_n(n):
    return n * (n + 1) * (2 * n + 1) // 6
