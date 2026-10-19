# https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        def calculate(temp:int,idx:int):
            if len(b) == idx:
                return temp

            return calculate((pow(temp, 10, 1337) * pow(a,b[idx],1337)) % 1337, idx+1)

        return calculate(1, 0)

        for x in b:
            # print(temp ** 10)
            temp = (temp ** 10 * 2 ** x) % 1337
            # temp = (pow(temp, 10, 1337) * pow(a,x,1337)) % 1337
            print(temp)
        return temp

sol = Solution()
sol.superPow(a = 2, b = [4,3,3,8,5,2])       