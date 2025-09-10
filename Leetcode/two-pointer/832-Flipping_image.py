# https://leetcode.com/problems/flipping-an-image?envType=problem-list-v2&envId=two-pointers
from typing import List

class Solution:
    def flipAndInvertImageV1(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for x in image:
            temp = [y^1 for y in x]
            result.append(temp[::-1])

        return result
    
s = Solution()
image = [[1,1,0],[1,0,1],[0,0,0]]
print(s.flipAndInvertImage(image))