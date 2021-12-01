def find_max(a, n):  # 리스트의 a의 앞부분 n개 중 최댓값을 구하는 재귀 함수
    if n == 1:
        return a[0]
    max_n_1 = find_max(a, n - 1)  # n-1개 중 최댓값을 구함
    if max_n_1 > a[n - 1]:  # n-1개 중 최댓값과 n-1번 위치 값을 비교
        return max_n_1
    else:
        return a[n - 1]


v = [10, 20, 45, 37, 47, 56, 45, 85]

print(find_max(v, len(v)))
