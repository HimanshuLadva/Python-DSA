# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy?envType=daily-question&envId=2025-12-18
# #newlearn-topic
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        base_profit = 0
        A = [0] * n
        for i in range(n):
            A[i] = strategy[i] * prices[i]
            base_profit += A[i]
        
        prefix_A = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_A[i] = prefix_A[i - 1] + A[i - 1]
            
        prefix_P = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_P[i] = prefix_P[i - 1] + prices[i - 1]
            
        half = k // 2
        max_delta = -10**18
        
        for i in range(0, n - k + 1):
            orig_i = prefix_A[i + k] - prefix_A[i]
            new_i = prefix_P[i + k] - prefix_P[i + half]
            delta = new_i - orig_i
            if delta > max_delta:
                max_delta = delta
                
        return base_profit + max(0, max_delta)

    # editorial
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        profitSum = [0] * (n + 1)
        priceSum = [0] * (n + 1)
        for i in range(n):
            profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
            priceSum[i + 1] = priceSum[i] + prices[i]
        res = profitSum[n]
        for i in range(k - 1, n):
            leftProfit = profitSum[i - k + 1]
            rightProfit = profitSum[n] - profitSum[i + 1]
            changeProfit = priceSum[i + 1] - priceSum[i - k // 2 + 1]
            res = max(res, leftProfit + changeProfit + rightProfit)
        return res
    
    # TLE
    def maxProfitV1(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        max_profit = 0
        total = sum(p * s for p,s in zip(prices, strategy))
        max_profit = total

        need = k//2
        replacement = [0] * need + [1] * (k - need)
        for i in range(n-k+1):
            new_strategy = strategy[:]
            new_strategy[i:i+k] = replacement
            total = sum(p * s for p,s in zip(prices, new_strategy))
            if max_profit < total:
                max_profit = total

        return max_profit

sol = Solution()
prices = [4,2,8]
strategy = [-1,0,1]
k = 2
sol.maxProfit(prices, strategy,k)
