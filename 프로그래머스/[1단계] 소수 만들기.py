# 2023.09.07

from itertools import *


def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0: return False
    return True


def solution(nums):
    com_list = list(combinations(nums, 3))

    sum_nums = [sum(i) for i in com_list]

    result = 0

    for sum_num in sum_nums:
        if is_prime_number(sum_num):
            result += 1

    return result

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))