# https://leetcode.com/problems/ransom-note?envType=problem-list-v2&envId=counting

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)

        print(f"Counter 1 = {counter1}")
        print(f"Counter 2 = {counter2}")
        print(f"result = {counter1 - counter2}")

        return not (counter1 - counter2)
    
    def canConstructV1(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)

        for x in counter1:
            if x in counter2:
                if counter2[x] >= counter1[x]:
                    continue
                else:
                    return False
            else:
                return False

        return True
    
sol = Solution()
ransomNote = "aabb"
magazine = "aab"
sol.canConstruct(ransomNote, magazine)