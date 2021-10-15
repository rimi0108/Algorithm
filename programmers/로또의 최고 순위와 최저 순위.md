```
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    match = []
    c = lottos.count(0)
    
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                match.append(lotto)
    
    max = len(match) + c
    min = len(match)
            
    answer = [rank[max], rank[min]]
    return answer
```