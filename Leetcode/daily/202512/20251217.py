# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v?envType=daily-question&envId=2025-12-17
# #newlearn
from typing import List
from functools import cache
import sys
class Solution:
    # 760ms
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp_buy, dp_sell, dp_normal = [-sys.maxsize] * (k + 1), [0] * (k + 1), [0] * (k + 1)
        dp_buy[0] = -prices[0]
        dp_sell[0] = prices[0]
        for i, price in enumerate(prices):
            #print(f"i: {i} price: {price} dp_buy: {dp_buy} dp_sell: {dp_sell} dp_normal: {dp_normal}")
            if i == 0:
                continue
            for j in range(k, -1, -1):
                if dp_normal[j] - price > dp_buy[j]:
                    dp_buy[j] = dp_normal[j] - price
                if dp_sell[j] < dp_normal[j] + price:
                    dp_sell[j] = dp_normal[j] + price
                if j > 0:
                    if dp_buy[j - 1] + price > dp_normal[j]:
                        dp_normal[j] = dp_buy[j - 1] + price
                    if dp_sell[j - 1] - price > dp_normal[j]:
                        dp_normal[j] = dp_sell[j - 1] - price
        return max(dp_normal)
    # 3978ms
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        @cache
        def dfs(i, j, state):
            if j == 0:
                return 0
            if i == 0:
                return (
                    0 if state == 0 else -prices[0] if state == 1 else prices[0]
                )
            p = prices[i]
            if state == 0:
                res = max(
                    dfs(i - 1, j, 0), dfs(i - 1, j, 1) + p, dfs(i - 1, j, 2) - p
                )
            elif state == 1:
                res = max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - p)
            else:
                res = max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + p)

            return res

        ans = dfs(n - 1, k, 0)
        dfs.cache_clear()
        return ans
    # not working
    def maximumProfitV1(self, prices: List[int], k: int) -> int:
        n = len(prices)
        comman_arr = {}
        print(prices)
        for i in range(n-1):
            max_sell_price = max(prices[i+1:])
            min_buy_price = min(prices[i+1:])

            if prices[i] < max_sell_price:
                max_index = prices[i+1:].index(max_sell_price)
                if max_index not in comman_arr:
                    comman_arr[max_index] = []
                comman_arr[max_index].append(max_sell_price - prices[i])
            if prices[i] > min_buy_price:
                if i not in comman_arr:
                    comman_arr[i] = []
                comman_arr[i].append(prices[i] - min_buy_price)
            
        print(comman_arr)
        max_arr = []
        for x in comman_arr:
            max_arr.append(max(comman_arr[x]))

        print(max_arr)
        print(max_arr[-k:])
        max_arr.sort()
        return sum(max_arr[-k:])
    
sol = Solution()
prices = [12,16,19,19,8,1,19,13,9]
k = 3
# prices = [1,7,9,8,2]
# k = 2
# prices = [20,19,12,10,5,10,9]
# k = 1
print(sol.maximumProfit(prices, k))