# https://leetcode.com/problems/maximum-number-of-balloons/?envType=daily-question&envId=2026-06-22

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        char_counter = Counter([x for x in text if x in word])
        
        if any(t not in char_counter for t in word):
            return 0
        else:
            return min(char_counter['b'] // 1,char_counter['a'] // 1,char_counter['l'] // 2, char_counter['o'] // 2, char_counter['n'] // 1)

        if len(c) != 5:
            return 0

        print(f"min char = {min(c)}")
        min_char,min_value = min(c.items(), key=lambda x: x[1])

        print(f"two count = {c['l'] // 2}, {c['o'] // 2}")
        two_time_char_count = min(c['l'] // 2, (c['o'] // 2))
        print(f"two_time_char_count = {two_time_char_count}")
        print(min_char, min_value)

        if min_char in ['b','a','n']:
            return min(min_value, two_time_char_count)
        else:
            return two_time_char_count

    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter([x for x in text if x in ['b','a','l','o','n']])
        print(c)

        if len(c) != 5:
            return 0

        print(f"min char = {min(c)}")
        min_char,min_value = min(c.items(), key=lambda x: x[1])

        print(f"two count = {c['l'] // 2}, {c['o'] // 2}")
        two_time_char_count = min(c['l'] // 2, (c['o'] // 2))
        print(f"two_time_char_count = {two_time_char_count}")
        print(min_char, min_value)

        if min_char in ['b','a','n']:
            return min(min_value, two_time_char_count)
        else:
            return two_time_char_count

sol = Solution()
# print(sol.maxNumberOfBalloons(text = "loonbalxballpoon"))
print(sol.maxNumberOfBalloons(text = "loonbalxballpoonballoo"))