# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수


def gcd_1(a, b):
    i = min(a, b)  # 두 수 중에서 최솟값을 구하는 파이썬 함수
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


print(gcd_1(2, 34))

# 유클리드 알고리즘
# 재귀호출 적용
# a와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'의 최대공약수와 같다. 즉, gcd(a, b) = gcd(b, a % b)
# 어떤 수와 0의 최대공약수는 자기 자신이다. 즉, gcd(n, 0) = n

# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수


def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a % b)


print(gcd_2(2, 34))
