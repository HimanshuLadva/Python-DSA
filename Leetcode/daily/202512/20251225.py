from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0

        for i in range(k):
            gain = happiness[i] -i

            if gain <= 0:
                return ans
            
            ans += gain
        
        return ans
    
    def maximumHappinessSumV1(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = happiness[0]
        # print(f"start = {happiness}")
        for i in range(1, k):
            for j in range(i, k):
                if happiness[j] == 0:
                    break
                happiness[j] -= 1
            ans += happiness[i]
            # print(happiness)
        
        # print(f"end = {happiness}")
        return ans
    
sol = Solution()
happiness = [1,2,3]
happiness = [7,50,3]
happiness = [12,1,42]
k = 2
k = 3
print(sol.maximumHappinessSum(happiness, k))