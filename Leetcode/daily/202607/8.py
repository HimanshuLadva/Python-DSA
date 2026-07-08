# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/description/?envType=daily-question&envId=2026-07-08

from typing import List
import sys
class Solution:
    #implogic
    #revision
    #howtowork
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        print(list(s))
        MOD = 10**9 + 7
        pow10 = [1] * 100001
        for i in range(1, 100001):
            pow10[i] = pow10[i - 1] * 10 % MOD

        sum = [0] * (n + 1)
        x = [0] * (n + 1)
        cnt = [0] * (n + 1)

        for i, c in enumerate(s):
            d = int(c)
            sum[i+1] = sum[i] + d
            x[i+1] = (x[i] * 10 + d) % MOD if d > 0 else x[i]
            cnt[i+1] = cnt[i] + (d > 0)

        m = len(queries)
        res = [0] * m
        for i in range(m):
            l = queries[i][0]
            r = queries[i][1] + 1
            length = cnt[r] - cnt[l]
            res[i] = (x[r] - x[l] * pow10[length]) * (sum[r] - sum[l]) % MOD
        
        # print(sum)
        # print(x)
        # print(cnt)

        return res
    # 506 testcase pass
    def sumAndMultiplyv1(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        prefix = [0]
        MOD = 10**9 + 7

        for ch in s:
            prefix.append(prefix[-1] + int(ch))

        print(prefix)
        sys.set_int_max_str_digits(0)

        for x,y in queries:
            # sub_str = s[x:y+1]
            digit_sum = prefix[y+1] - prefix[x]

            num = 0
            for c in s[x:y+1]:
                if c != '0':
                    num = num * 10 + (ord(c) - ord('0'))

            
            # without_zero = sub_str.replace('0','')
            # if not without_zero:
            #     without_zero = 0
            # temp = int(without_zero)
            # print(digit_sum)
            # print(temp)        
            res.append((digit_sum * num) % MOD)

        return res
    
sol = Solution()
print(sol.sumAndMultiply(s = "10203004", queries = [[0,7],[1,3],[4,6]]))
# print(sol.sumAndMultiply(s = "9876543210", queries = [[0,9]]))