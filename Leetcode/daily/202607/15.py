# https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/?envType=daily-question&envId=2026-07-15

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        e_sum = 2
        o_sum = 1
        e_sum_arr = [2]
        o_sum_arr = [1]

        #implogic - for find GCD of two number
        #revision
        #formula
        def gcd(a, b) -> int:
            while b != 0:
                temp = b
                b = a % b
                a = temp
            
            return a
        
        for i in range(n-1):
            e_sum += 2
            o_sum += 2
            e_sum_arr.append(e_sum)
            o_sum_arr.append(o_sum)

        # print(e_sum_arr,o_sum_arr)
        return gcd(sum(e_sum_arr), sum(o_sum_arr))
    
sol = Solution()
print(sol.gcdOfOddEvenSums(n = 4))