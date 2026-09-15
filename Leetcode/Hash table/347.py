# https://leetcode.com/problems/top-k-frequent-elements/
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # print(freq)
        temp = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        # print(temp)
        ans = []
        for f in temp:
            if k == 0:
                break
            ans.append(f)
            k -= 1

        return ans

sol = Solution()
print(sol.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))