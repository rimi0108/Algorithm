# 대표값2

n_list = [int(input()) for _ in range(5)]

average = sum(n_list) // 5

for index in range(1, len(n_list)):
    position = index
    temp_value = n_list[index]

    while position > 0 and n_list[position - 1] > temp_value:
        n_list[position] = n_list[position - 1]
        position -= 1

    n_list[position] = temp_value


center = n_list[2]

print(average)
print(center)
