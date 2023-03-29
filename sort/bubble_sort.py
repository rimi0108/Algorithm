from typing import List

class Solution:
    def bubble_sort(self, lst: List[int]) -> None:
        """
        Mutates lst so that it is sorted via swapping adjacent elemets until
        the entire lst is sorted
        """
        has_swapped = True
        # if no swap occurred, lst is sorted
        while has_swapped:
            has_swapped = False
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + 1]:
                    # Swap adjacent elements
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]

                    has_swapped = True

        return lst

solution = Solution()

print(solution.bubble_sort([6, 4, 2, 3, 9, 7, 1]))
