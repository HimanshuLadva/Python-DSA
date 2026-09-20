# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    #howtowork
    #revision
    def removeAnagrams(self, words: list[str]) -> list[str]:
        result = [words[0]]

        def get_key(word):
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - 97] += 1

            return freq

        prev = get_key(words[0])
        for word in words[1:]:
            curr = get_key(word)

            if curr != prev:
                prev = curr
                result.append(word)

        return result
    
    def removeAnagramsV1(self, words: list[str]) -> list[str]:
        result = [words[0]]

        for word in words[1:]:
            if sorted(word) != sorted(result[-1]):
                result.append(word)
            
        return result

    # myself
    def removeAnagramsV1(self, words: list[str]) -> list[str]:
        n = len(words)
        i = 0
        j = 1

        while i < n-1 and j < n:
            curr = "".join(sorted(words[i]))
            next = "".join(sorted(words[j]))

            if curr == next:
                words[j] = ""
                j += 1
            else:
                i = j 
                j += 1

        return [x for x in words if x != '']

sol = Solution()
print(sol.removeAnagrams(words = ["abba","baba","bbaa","cd","cd"]))