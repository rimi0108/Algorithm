# 최대 수익 문제를 푸는 두 알고리즘의 계산 속도 비교하기
# 최대 수익 문제를 O(n*n)과 O(n)으로 푸는 알고리즘을 각각 수행하여
# 걸린 시간을 출력/비교함

import time  # 시간 측정을 위한 time 모듈
import random  # 테스트 주가 생성을 위한 random 모듈

# 최대 수익: 느린 O(n*n) 알고리즘
def max_profit_slow(prices):
    n = len(prices)
    max_profit = 0  # 최대 수익은 항상 0 이상의 값
    min_price = prices[0]  # 첫째 날의 주가를 주가의 최솟값으로 기억
    for i in range(1, n):
        # 지금까지의 최솟값에 주식을 사서 i날에 팔 때의 수익
        profit = prices[i] - min_price
        if profit > max_profit:  # 이 수익이 지금까지 최대 수익보다 크면 값을 고침
            max_profit = profit
        if prices[i] < min_price:  # i날 주가가 최솟값보다 작으면 값을 고침
            min_price = prices[i]

    return max_profit


# 최대 수익: 빠른 O(n) 알고리즘
def max_profit_fast(prices):
    n = len(prices)
    max_profit = 0  # 최대 수익은 항상 0 이상의 값
    min_price = prices[0]  # 첫째 날의 주가를 주가의 최솟값으로 기억
    for i in range(1, n):
        # 지금까지의 최솟값에 주식을 사서 i날에 팔 때의 수익
        profit = prices[i] - min_price
        if profit > max_profit:  # 이 수익이 지금까지 최대 수익보다 크면 값을 고침
            max_profit = profit
        if prices[i] < min_price:  # i날 주가가 최솟값보다 작으면 값을 고침
            min_price = prices[i]

    return max_profit


def test(n):
    # 테스트 자료 만들기(5000부터 20000까지의 난수를 주가로 사용)
    a = []
    for i in range(0, n):
        a.append(random.randint(5000, 20000))
    # 느린 O(n*n) 알고리즘 테스트
    start = time.time()  # 계산 시작 직전 시각을 기억
    mps = max_profit_slow(a)  # 계산 수행
    end = time.time()  # 계산 시작 직후 시각을 기억
    time_slow = end - start  # 직후 시각에서 직전 시각을 뻬면 계산에 걸린 시간
    # 빠른 O(n) 알고리즘 테스트
    start = time.time()  # 계산 시작 직전 시각을 기억
    mpf = max_profit_fast(a)  # 계산 수행
    end = time.time()  # 계산 시작 직후 시각을 기억
    time_fast = end - start  # 직후 시각에서 직전 시각을 뻬면 계산에 걸린 시간
    # 결과 출력: 계산 결과
    print(n, mps, mpf)  # 입력 크기, 각각 알고리즘이 계산한 최대 수익 값(같아야 함)
    # 결과 출력: 계산 시간 비교
    m = 0  # 느린 알고리즘과 빠른 알고리즘의 수행 시간 비율을 저장할 변수
    if time_fast > 0:
        m = time_slow / time_fast
    print("%d %.5f %.5f %.2f" % (n, time_slow, time_fast, m))


test(100)
test(10000)
# test(100000)  # 수행 시간이 오래 걸리므로 일단 주석 처리
