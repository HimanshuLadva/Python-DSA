# https://leetcode.com/problems/maximum-number-of-balloons?envType=problem-list-v2&envId=counting

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)

        b_count = counter['b']
        a_count = counter['a']
        l_count = counter['l'] // 2
        o_count = counter['o'] // 2
        n_count = counter['n']

        return min(b_count, a_count, l_count, o_count, n_count)

        
    def maxNumberOfBalloonsV1(self, text: str) -> int:
        word = "balloon"
        set1 = set(word)
        set2 = set(text)
        counter_w = Counter(word)
        counter_t = Counter(text)

        if not set1.issubset(set2):
            return 0
        else:
            count = 0
            for key,value in counter_t.most_common():
                if key in word:
                    count = counter_t[key]
            return count



sol = Solution()
# text = "nlaebolko"
# text = "loonbalxballpoon"
text = "balon"
print(sol.maxNumberOfBalloons(text))