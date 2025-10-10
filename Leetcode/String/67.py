# https://leetcode.com/problems/add-binary?envType=problem-list-v2&envId=string

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        sum = ""
        carry = 0

        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for x in range(max_len):
            index = -1*(x+1)
            if a[index] == b[index] == '1':
                if carry:
                    sum += "1"
                    carry = 1
                else:
                    sum += "0"
                    carry = 1
            elif a[index] == b[index] == '0':
                if carry:
                    sum += "1"
                    carry = 0
                else:
                    sum += "0"
            else:
                if carry:
                    sum += "0"
                    carry = 1
                else:
                    sum += "1"
        if carry:
            sum += "1"
        
        return sum[::-1]
 
sol = Solution()
a = "1111"
b = "1111"
print(sol.addBinary(a, b))