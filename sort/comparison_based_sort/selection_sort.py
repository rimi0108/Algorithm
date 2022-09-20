# selection sort 선택 정렬
from typing import List

class Solution:
    def selection_sort(self, lst: List[int]) -> None:
        """
        Mutates lst so that is it sorted via selection the
        minimum element and 
        swapping it with the corresponding index
        """
        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                if lst[j] < lst[min_index]:
                    min_index = j
            
            # Swap current index with minimum element in rest of list
            lst[min_index], lst[i] = lst[i], lst[min_index]

lst: List[int] = [4, 3, 5, 1, 8, 2, 9]

solution1 = Solution()

solution1.selection_sort(lst)

print(lst)