# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/?envType=daily-question&envId=2026-07-16

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a: int, b: int):
            while b != 0:
                temp = b
                b = a % b
                a = temp
            
            return a
        
        max_num = []
        prefixGcd = []
        n = len(nums)

        for i in range(n):
            if i == 0:
                max_num.append(nums[i])
                prefixGcd.append(gcd(nums[i], nums[i]))
            else:
                max_num.append(max(nums[i], max_num[-1]))
                prefixGcd.append(gcd(nums[i], max(nums[i], max_num[-1])))
        
        # print(prefixGcd)
        prefixGcd.sort()

        i = 0
        j = len(prefixGcd) - 1
        res = 0
        while i < j:
            res += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return res

sol = Solution()
print(sol.gcdSum(nums = [2,6,4]))