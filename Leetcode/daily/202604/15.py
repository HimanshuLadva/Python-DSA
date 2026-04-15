# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/?envType=daily-question&envId=2026-04-15
from typing import List
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex] == target:
            return 0
        
        n = len(words)

        left = (startIndex - 1 + n) % n
        end = (startIndex + n) % n
        right = (startIndex + 1) % n

        # for left
        left_count = 0
        is_found = False
        while left != end:
            left_count += 1
            if words[left] == target:
                is_found = True
                break
            left = (left - 1 + n) % n
        
        if not is_found:
            left_count = 0
        
        # for right
        right_count = 0
        is_found = False
        while right != end:
            right_count += 1
            if words[right] == target:
                is_found = True
                break
            right = (right + 1) % n
        
        if not is_found:
            right_count = 0
            
        return -1 if left_count == 0 and right_count == 0 else min(right_count, left_count)
    
sol = Solution()
print(sol.closestTarget(words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1))
print(sol.closestTarget(words = ["a","b","leetcode"], target = "leetcode", startIndex = 0))
print(sol.closestTarget(words = ["i","eat","leetcode"], target = "ate", startIndex = 0))