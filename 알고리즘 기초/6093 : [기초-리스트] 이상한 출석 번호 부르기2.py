a = int(input())
n = list(map(int, input().split()))

for i in range(a-1, -1, -1):
    print(n[i], end=' ')