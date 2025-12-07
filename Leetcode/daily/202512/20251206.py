# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k?envType=daily-question&envId=2025-12-06
# #new-learn
from typing import List
from collections import deque
from sortedcontainers import SortedList

class Solution:
    # 328ms
    def countPartitions(self, nums: List[int], k: int) -> int:

        left, cnt, mod_ = 0, 1, 1_000_000_007
        mnQueue, mxQueue, dp = deque(), deque(), [cnt]
        
        for rght, num in enumerate(nums):
            while mxQueue and num > mxQueue[-1]:
                mxQueue.pop()
            while mnQueue and num < mnQueue[-1]:
                mnQueue.pop()

            mxQueue.append(num)    
            mnQueue.append(num)
            # print("Max", mxQueue)
            # print("Min", mnQueue)
            while mxQueue[0] - mnQueue[0] > k:
                cnt-= dp[left]
                if nums[left] == mxQueue[0]: mxQueue.popleft()
                if nums[left] == mnQueue[0]: mnQueue.popleft()
                left+= 1

            dp.append(cnt)
            cnt*= 2
            cnt%= mod_

        return dp[-1] %mod_
    
    # 1551ms
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        cnt = SortedList()

        dp[0] = 1
        prefix[0] = 1

        j = 0
        for i in range(n):
            cnt.add(nums[i])
            # adjust window
            while j <= i and cnt[-1] - cnt[0] > k:
                cnt.remove(nums[j])
                j += 1
            dp[i + 1] = (prefix[i] - (prefix[j - 1] if j > 0 else 0)) % mod
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % mod

        return dp[n]