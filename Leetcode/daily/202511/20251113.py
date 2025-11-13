# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end?envType=daily-question&envId=2025-11-13

class Solution:
    def maxOperations(self, s: str) -> int:
        slen = len(s)
        temp = []
        for i in range(slen):
            if s[i] == '0':
                temp.append(i)

        count = 0
        if len(temp):
            prev = temp[0]
            for i in range(len(temp)):
                if temp[i] != prev + 1:
                    count += (temp[i] - i)
                prev = temp[i]

        return count