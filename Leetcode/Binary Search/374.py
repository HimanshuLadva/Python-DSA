# https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=problem-list-v2&envId=binary-search

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 if num is equal to the picked number
# def guess(num: int) -> int:

#implogic
#howtowork
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            # result = guess(mid)
            result = 0

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1

sol = Solution()
print(sol.guessNumber(10))