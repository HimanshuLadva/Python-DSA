class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        reminder = 0
        while True:
            reminder = (reminder * 10 + 1)
            if reminder % k == 0:
                break

        return len(str(reminder))
    
sol = Solution()
k = 1
print(sol.smallestRepunitDivByK(k))