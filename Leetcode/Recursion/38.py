# https://leetcode.com/problems/count-and-say/description/

class Solution:
    def countAndSay(self, n: int, s:str = "1") -> str:
        if n == 0:
            return s
        
        ans = ""
        l = len(s)
        i = 0

        while i < l:
            count = 1
            for j in range(i + 1, l):
                if s[j] != s[i]:
                    break
                count += 1
            ans += str(count) + s[i]
            i += count

        
        return self.countAndSay(n-1, ans)
    
    def countAndSayV1(self, n: int) -> str:
        s = "11"
        l = len(s)
        ans = ""
        i = 0

        while i < l:
            count = 1
            for j in range(i + 1, l):
                print(f"j = {j}")
                if s[j] != s[i]:
                    break
                count += 1
            ans += str(count) + s[i]
            i += count

        print(ans)
            

        # for i in range(l):
        #     count = 1
        #     for j in range(i+1,l):
        #         if s[j] != s[i]:
        #             break
        #         count += 1
        #     print(j - i, count)
        
        return ""

sol = Solution()
print(sol.countAndSay(5))
