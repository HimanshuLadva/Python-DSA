# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = s.split()

        # print(arr)
        n = len(arr)

        i = 0
        j = n-1

        while i < j:
            arr[i],arr[j]=arr[j],arr[i]

            i += 1
            j -= 1

        # print(arr)
        return " ".join(arr)
    
    def reverseWordsV1(self, s: str) -> str:
        s = s.strip()

        arr = s.split()
        arr.reverse()

        return " ".join(arr)

sol = Solution()
print(sol.reverseWords(s = "the sky is blue"))