# https://leetcode.com/problems/count-good-numbers/description/

class Solution:
    # Recursion version
    #howtowork
    #revision
    #implogic
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(base, exp):
            if exp == 0:
                return 1

            half = power(base, exp // 2)

            if exp % 2 == 0:
                return (half * half) % MOD
            else:
                return (half * half * base) % MOD

        even_count = (n + 1) // 2
        odd_count = n // 2

        return (power(5, even_count) * power(4, odd_count)) % MOD

    #TLE
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        even_count = (n + 1) // 2
        odd_count = n // 2

        ans = 1

        for i in range(even_count):
            ans = (ans * 5) % MOD # here we are using 5 because [0,2,4,6,8]

        for i in range(odd_count):
            ans = (ans * 4) % MOD # here we are suing 4 because [1,3,5,7]

        return ans

    # Ruff approach
    def countGoodNumbersV1(self, n: int) -> int:
        start = 10 ** (n-1)
        end = 10 ** (n)
        prime_numbers = {'2','3','5','7'}

        ans = []

        for i in range(start, end):
            flag = True
            for idx,j in enumerate(list(str(i))):
                if idx % 2 == 0 and int(j) % 2 != 0:
                    flag = False
                    break
                elif idx % 2 != 0 and j not in prime_numbers:
                    flag = False
                    break

            if flag:
                ans.append(i)

        print(len(ans))
        return len(ans)

sol = Solution()
print(sol.countGoodNumbers(4))