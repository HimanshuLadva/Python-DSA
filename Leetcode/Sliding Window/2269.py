# https://leetcode.com/problems/find-the-k-beauty-of-a-number/?envType=problem-list-v2&envId=sliding-window

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        n = len(s)
        count = 0

        window = s[:k]
        divisor = int(window)
        if divisor and num % divisor == 0:
            count += 1

        for i in range(n - k):
            window = window[1:] + s[i + k]

            divisor = int(window)
            if divisor and num % int(window) == 0:
                    count += 1

        return count
    
sol = Solution()
sol.divisorSubstrings(num = 430043, k = 2)