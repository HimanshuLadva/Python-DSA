# https://leetcode.com/problems/longest-palindromic-substring?envType=problem-list-v2&envId=two-pointers
# MMIMP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0  # indices of longest palindrome found

        def expandAroundCenter(left: int, right: int) -> tuple[int, int]:
            # expand as long as characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # return bounds of palindrome (exclusive right)
            return left + 1, right - 1

        for i in range(len(s)):
            # odd length palindrome
            l1, r1 = expandAroundCenter(i, i)
            print(f"odd = {l1},{r1}")
            # even length palindrome
            l2, r2 = expandAroundCenter(i, i + 1)
            print(f"even = {l2},{r2}")

            # update max palindrome if found bigger
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
            
            print(f"start-end = {start}-{end}")

        return s[start:end + 1]

    
    def longestPalindromeV1(self, s: str) -> str:
        i = 0
        len_s = len(s)
        max = -1
        result = ""

        for i in range(len_s):
            for j in range(i, len_s):
                if s[i:j+1] == s[i:j+1][::-1]  and (j - i) > max:
                    max = (j - i)
                    result = s[i:j+1]

        return result
    
sol = Solution()
s = "babad"
# s = "a"
print(f"answer={sol.longestPalindrome(s)}")