from collections import Counter
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        comman = Counter(words[0])

        for word in words[1:]:
            comman &= Counter(word)

        # print(comman)
        res = []
        for ch,count in comman.items():
            # print(ch, count)
            res.extend([ch] * count)

        return res

sol = Solution()
print(sol.commonChars(words = ["bella","label","roller"]))
# print(sol.commonChars(words = ["cool","lock","cook"]))