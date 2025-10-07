# https://leetcode.com/problems/valid-anagram?envType=problem-list-v2&envId=sorting

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
    def isAnagramV1(self, s: str, t: str) -> bool:
        s = s.replace(" ", "")
        t = t.replace(" ", "")

        if len(s) != len(t):
            return False

        s_arr = []    
        t_arr = []

        for x,y in zip(s, t):
            s_arr.append(x)
            t_arr.append(y)

        s_arr.sort()
        t_arr.sort()

        for x,y in zip(s_arr, t_arr):
            if x != y:
                return False
        
        return True

sol = Solution()
s = "anagram"
t = "nagaram"
# s = "car"
# t = "rat"
print(sol.isAnagram(s, t))