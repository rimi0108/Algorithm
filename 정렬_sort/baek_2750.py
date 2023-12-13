# 수 정렬하기

# 1 ≤ N ≤ 1,000
N = int(input())

n_list = [int(input()) for _ in range(N)]

arr = list(set(n_list))

for i in range(N - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for i in arr:
    print(i)



