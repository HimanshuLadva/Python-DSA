# https://leetcode.com/problems/first-bad-version/?envType=problem-list-v2&envId=binary-search
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

sol = Solution()
sol.firstBadVersion(5)