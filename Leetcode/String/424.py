# https://leetcode.com/problems/longest-repeating-character-replacement/description/

#howtowork
#revision
#implogic
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        count = {}
        left = 0
        maxFreq = 0
        answer = 0

        for right in range(n):
            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            print(count)

            # Maximum frequency inside the window
            maxFreq = max(maxFreq, count[s[right]])

            # window size 
            windowSize = right - left + 1
            # No of character we need to replace
            replacements = windowSize - maxFreq

            # Window is invalid
            if replacements > k:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)    
            
        return answer

sol = Solution()
sol.characterReplacement(s = "AABABBA", k = 1)