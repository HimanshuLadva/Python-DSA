# https://leetcode.com/problems/4sum-ii/description/

class Solution:
    #howtowork
    #revision
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        hasmap = {}

        for a in nums1:
            for b in nums2:
                total = a + b
                hasmap[total] = hasmap.get(total, 0) + 1

        count = 0
        for c in nums3:
            for d in nums4:
                total = 0-(c + d)
                if total in hasmap:
                    count += hasmap[total]

        return count
    
    # TLE
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count = 0
        for a in nums1:
            for b in nums2:
                for c in nums3:
                    for d in nums4:
                        if a + b + c + d == 0:
                            count += 1
        
        return count

sol = Solution()
print(sol.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))