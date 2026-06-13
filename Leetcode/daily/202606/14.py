# https://leetcode.com/problems/weighted-word-mapping/description/?envType=daily-question&envId=2026-06-13

from typing import List
from collections import defaultdict
import string
class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        master = {
            0: 'z',
            1: 'y',
            2: 'x',
            3: 'w',
            4: 'v',
            5: 'u',
            6: 't',
            7: 's',
            8: 'r',
            9: 'q',
            10: 'p',
            11: 'o',
            12: 'n',
            13: 'm',
            14: 'l',
            15: 'k',
            16: 'j',
            17: 'i',
            18: 'h',
            19: 'g',
            20: 'f',
            21: 'e',
            22: 'd',
            23: 'c',
            24: 'b',
            25: 'a'
        }

        frm_weight = defaultdict(str)
        for letter, weight in zip(string.ascii_lowercase, weights):
            frm_weight[letter] = weight

        ans = ""
        for word in words:
            word_sum = 0
            for ch in word:
                word_sum += frm_weight[ch]
            ans += master[word_sum % 26]

        return ans
    
sol = Solution()
print(sol.mapWordWeights(words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))