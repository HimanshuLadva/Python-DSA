# https://leetcode.com/problems/decode-string/description/

#howtowork
#revision
class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i):
            result = ""
            num = 0

            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    num = 0

                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                elif s[i] == '[':
                    decoded,i = decode(i + 1)
                    result += decoded * num
                    num = 0
                    i += 1
                else:
                    result += s[i]
                    i += 1

            return result,i
        
        return decode(0)[0]

sol = Solution()
sol.decodeString(s = "3[a]2[bc]")