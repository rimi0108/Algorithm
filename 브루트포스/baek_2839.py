# 설탕 배달

# 3 ≤ N ≤ 5000
N = int(input())

sugar_box = 0
result = []

max_5kg_bags = N // 5
max_3kg_bags = N // 3

for i in range(max_5kg_bags + 1):
    for j in range(max_3kg_bags + 1):
        sugar_box = (5 * i) + (3 * j)
        # print(f"(5 * {i}) + (3 * {j})")
        # print(sugar_box)
        if sugar_box == N:
            result.append(i + j)

if len(result) == 0:
    print(-1)
else:
    print(min(result))

