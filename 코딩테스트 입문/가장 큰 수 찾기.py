def solution(array):
    # answer = [원소, 인덱스]
    answer = [0, 0]
    i = 0
    for i in range(len(array)):
        if answer[0] <= array[i]:
            answer = [array[i], i]
    return answer


print(solution([9, 10, 11, 8]))
