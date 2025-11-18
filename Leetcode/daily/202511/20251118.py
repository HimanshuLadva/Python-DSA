# https://leetcode.com/problems/1-bit-and-2-bit-characters?envType=daily-question&envId=2025-11-18

from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        while i < n-1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2

        return i == n-1