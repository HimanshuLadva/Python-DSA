# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/?envType=daily-question&envId=2026-02-21
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n <= 3:
                return n > 1
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        ans = 0
        for n in range(left, right + 1):
            count = bin(n)[2:].count('1')
            ans += 1 if is_prime(count) else 0
    
        return ans