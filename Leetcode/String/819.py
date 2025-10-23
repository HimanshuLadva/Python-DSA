# https://leetcode.com/problems/most-common-word?envType=problem-list-v2&envId=counting

from typing import List
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        text = paragraph.lower()
        words = re.findall(r'\b\w+\b', text)
        counter = Counter(words)

        for key,value in counter.most_common():
            if key not in banned:
                return key
        return ""
    
sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))