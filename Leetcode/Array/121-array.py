# Best Time to Buy and Sell Stock
from typing import List

class Solution:

    def maxProfitOld(self, prices: List[int]) -> int:
        max_profit = 0
        for i,_ in enumerate(prices):
            for y in range(i+1, len(prices)):
                if prices[y] > prices[i] and max_profit < (prices[y] - prices[i]):
                    max_profit = (prices[y] - prices[i])

        return max_profit  

    def maxProfit1(self, prices: List[int]) -> int:
        max_profit = 0
        start_index = 0
        end_index = (len(prices)-1)

        while start_index < end_index:
            if prices[end_index] > prices [start_index]:
                if (max_profit < (prices[end_index] - prices [start_index])):
                    max_profit = (prices[end_index] - prices [start_index])
                    start_index += 1
                    end_index -= 1
                else:
                    start_index += 1
                    end_index -= 1
            else:
                end_index -= 1

        return max_profit    
    
    def maxProfit2(self, prices: List[int]) -> int:
        start_index = 0
        end_index = (len(prices)-1)
        my_set = {0}

        while start_index != len(prices):
            if prices[end_index] > prices[start_index] and start_index != end_index:
                my_set.add(prices[end_index] - prices[start_index])
                end_index -= 1
            else:
                if start_index == end_index:
                    start_index += 1
                    end_index = (len(prices) - 1)
                else:
                    end_index -= 1
        return sorted(my_set)[-1]
    
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price

            if profit > max_price:
                max_price = profit
        return max_price

s = Solution()
nums = [1,2]
# nums = [2,1,4]
# nums = [7,1,5,3,6,4]
# nums = [1,5,9,10,3]
num = s.maxProfit(nums)
print(num)