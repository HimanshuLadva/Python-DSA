# https://leetcode.com/problems/count-the-number-of-special-characters-ii/?envType=daily-question&envId=2026-05-27
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        for ch in "abcdefghijklmnopqrstuvwxyz":
            lower = ch
            upper = ch.upper()

            if lower in word and upper in word:
                last_lower = word.rfind(lower)
                first_upper = word.find(upper)

                if first_upper > last_lower:
                    count += 1
        return count

    def numberOfSpecialCharsV2(self, word: str) -> int:
        seen = set()
        # cCceDC

        ans = []
        for w in word:
            if w.isupper() and (w.upper() not in seen) and (w.lower() in seen):
                ans.append(w.lower())
        
            if w.islower() and (w.upper() in seen):
                if w.lower() in ans:
                    ans.remove(w.lower())
            seen.add(w)

        # print(seen, ans)
        return len(ans)
    
    def numberOfSpecialCharsV1(self, word: str) -> int:
        seen = set()

        ans = []
        for w in word:
            # print(f"word = {w}")
            if w.isupper() and w.lower() in seen:
                # print(f"veri 1")
                if w not in ans:
                    ans.append(w)
                seen.add(w)
            elif w.islower() and w.upper() in seen:
                # print(f"veri 2")
                if w.upper() in ans:
                    ans.remove(w.upper())
                seen.add(w)
            else:
                # print(f"veri 3")
                seen.add(w)
            
        # print(seen, ans)
        return len(ans)
    
sol = Solution()
# print(sol.numberOfSpecialChars(word = "aaAbcBC"))
# print(sol.numberOfSpecialChars(word = "abc"))
# print(sol.numberOfSpecialChars(word = "AbBCab"))
# print(sol.numberOfSpecialChars(word = "dcbCC"))
print(sol.numberOfSpecialChars(word = "cCceDC"))