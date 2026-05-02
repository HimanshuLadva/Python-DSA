# https://leetcode.com/problems/rotated-digits/?envType=daily-question&envId=2026-05-02.

class Solution:
    def rotatedDigits(self, n: int) -> int:
        master = [2,5,6,9]
        not_allow = [3,4,7]
        count = 0

        for i in range(1, n+1   ):
            j = i
            is_valid = True
            has_changed = False

            while j > 0:
                temp = (j % 10)

                if temp in not_allow:
                    is_valid = False
                    break

                if temp in master:
                    has_changed = True

                j //= 10

            if is_valid and has_changed:
                count += 1

        return count

sol = Solution()
print(sol.rotatedDigits(10))