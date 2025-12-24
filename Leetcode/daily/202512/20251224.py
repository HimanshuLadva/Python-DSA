from typing import List
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity.sort()

        count = 0
        for c in capacity[::-1]:
            if total_apple > 0:
                total_apple -= c
                count += 1
            else:
                break
        return count
    
    def minimumBoxesV1(self, apple: List[int], capacity: List[int]) -> int:
        total_apple = sum(apple)
        capacity.sort(reverse=True)

        cap_sum = 0
        for i,c in enumerate(capacity):
            cap_sum += c
            if cap_sum >= total_apple:
                return i+1
        return 0
    
sol = Solution()
apple = [1,3,2]
capacity = [4,3,1,5,2]
sol.minimumBoxes(apple, capacity)