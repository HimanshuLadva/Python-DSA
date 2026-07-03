# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/?envType=problem-list-v2&envId=two-pointers

from itertools import combinations
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        palindrome_range = []
        for i in range(n):
            for j in range(i+1, n+1):
                temp = s[i:j]
                if (j - i) % 2 != 0 and temp == temp[::-1]:
                    palindrome_range.append((i, j-1))
                    print(temp)
        
        print(palindrome_range)

        def top_two_non_overlapping(intervals):
            sorted_by_len = sorted(intervals, key=lambda x: -(x[1]-x[0]))
            first = sorted_by_len[0]
            for cand in sorted_by_len[1:]:
                if cand[1] <= first[0] or first[1] <= cand[0]:
                    return [first, cand]
            return [first]  
        
        print(top_two_non_overlapping(palindrome_range))
        return 0
 
sol = Solution()
print(sol.maxProduct(s = "ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"))