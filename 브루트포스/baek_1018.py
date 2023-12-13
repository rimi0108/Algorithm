# 0. input 받기
row, col = map(int, input().split())
board = [input() for _ in range(row)]
# 3. 전체 최적의 값과 비교하여 갱신하기
def solution(start_row, start_col, board):
    org_board = ["WBWBWBWB", "BWBWBWBW"]
    white_sol = 0

    for i in range(8):
        row = start_row + i
        for j in range(8):
            col = start_col + j
            if board[row][col] != org_board[row % 2][j]:
                white_sol += 1

    result = min(white_sol, 64 - white_sol)

    return result

# 1. 체스판 자르기

sol = float('inf')

for i in range(row - 7):
    for j in range(col - 7):
        # 2. 현 체스판의 최소 비용 구하기
        cur_sol = solution(i, j, board)
        if sol > cur_sol:
            sol = cur_sol

print(sol)