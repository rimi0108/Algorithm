# n번째 피보나치 수열 찾기
# 입력: n 값(0부터 시작)
# 출력: n번째 피보나치 수열 값


def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 2) + fibo(n - 1)


print(fibo(4))
