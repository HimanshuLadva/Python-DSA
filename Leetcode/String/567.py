# https://leetcode.com/problems/permutation-in-string/

class Solution:
    #revision
    def checkInclusion(self, s1: str, s2: str) -> bool:
       if len(s1) > len(s2):
           return False

       s1_count = [0] * 26
       window_count = [0] * 26

       for ch in s1:
           s1_count[ord(ch) - 97] += 1

       for i in range(len(s1)):
           window_count[ord(s2[i]) - 97] += 1

       if s1_count == window_count:
           return True

       for i in range(len(s1), len(s2)):
           window_count[ord(s2[i]) - 97] += 1
           window_count[ord(s2[i - len(s1)]) - 97] -= 1

           print(f"loop idx = {i}, {i - len(s1)}")

           if window_count == s1_count:
               return True
           
       return False
    
    def checkInclusionV1(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = ''.join(sorted(s1))
        

        for i in range(len(s2) - n + 1):
            # print(s2[i:i+n])
            temp = ''.join(sorted(s2[i:i+n]))
            if s1 == temp:
                return True

        return False

sol = Solution()
sol.checkInclusion(s1 = "ab", s2 = "eidbaooo")