a = int(input())
b = list(map(int, input().split()))

for i in range(1, 24):
    if i in b:
        c = b.count(i)
        print(c)
    else:
        print(0)
