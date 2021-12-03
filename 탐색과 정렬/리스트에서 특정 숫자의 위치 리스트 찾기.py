# 순차 탐색
# 계산 복잡도 : O(n)
def search_list(a, x):
    result = []
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            result.append(i)
    return result


v = [17, 90, 18, 33, 90, 7, 33, 42]
print(search_list(v, 900))
