# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones?envType=daily-question&envId=2025-11-15
# #newlearn

import math as mt
class Solution:
    # 0ms
    def numberOfSubstrings(self, s: str) -> int:
            n = len(s)
            cumZeros = [0] * (n + 1) # DP-ish for count of zeros; cumZeros[i+1] = cumulative zeros up to i
            posZeros = [-1] # index positions of zeros in s
            posOnes = [-1] # index positions of ones in s

            res = 0

            for i, c in enumerate(s):
                if c == '1':
                    posOnes.append(i)
                    res += 1
                    curZeros = cumZeros[i] # cumulative zeros before i
                    curOnes = i - curZeros + 1 # number of ones we have is current index minus the zeros plus one
                    left = posZeros[curZeros - 1] # position before last zero
                else:
                    posZeros.append(i)
                    curZeros = cumZeros[i] + 1 # cumulative zeros before i, +1 for the current zero 
                    curOnes = i - curZeros + 1 # number of ones we have is current index minus the zeros plus one
                    left = posOnes[curOnes] # position before the last one

                cumZeros[i + 1] = curZeros # set the next cumulative zeros count, cumZeros[i+1] represents s[:i]

                right = i
                while left >= 0:
                    countZero = curZeros - cumZeros[left] # Zeros in range [left, i]
                    countOne = i - left + 1 - countZero # Ones in range [left, i]

                    sqZero = countZero * countZero
                    if sqZero <= countOne:
                        if s[left] == "1": # if jump ended on a 1, only count current full substring [left, right]
                            res += 1
                        else:
                            res += right - left # if jump ended on a 0, count all substrings in [left, right]

                        right = left

                        nextZero = curZeros - mt.ceil(mt.sqrt(countOne + 1)) + 1 # index in posZeros to jump to next that's valid (enough ones to satisfy the condition)
                        left = posZeros[nextZero] if nextZero >= 0 else -1

                    else:
                        if s[left] == "0":
                            res += right - left - 1 # if jump ended on a 0, count all substrings in [left, right], excluding the full substring due to the jump logic

                        right = left
                        nextOne = curOnes - sqZero + 1 # at least sqZero ones to satisfy condition
                        left = posOnes[nextOne] if nextOne >= 0 else -1

                if curZeros * curZeros <= curOnes: # if entire range is dominant, count all remaining valid substrings up to right from s[0]
                    res += right
            return res
    
    # 6487ms
    def numberOfSubstringsV2(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res
    
    # time limit exceeded
    def numberOfSubstringsV1(self, s: str) -> int:
      slen = len(s)
      count = i = 0
      while i <= slen:
         for j in range(slen - i + 1):
            count_of_zeros = s[j:j+i].count('0')
            count_of_ones = s[j:j+i].count('1')

            if(count_of_ones == 0 and count_of_zeros == 0):
               continue

            if (count_of_zeros > 0 or count_of_ones > 0) and count_of_ones >= (count_of_zeros) ** 2:
               count += 1
         i += 1
      return count
    
sol = Solution()
s = "00011"
# s = "101101"
print(sol.numberOfSubstrings(s))