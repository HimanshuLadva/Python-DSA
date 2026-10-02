# https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    # MLE
    def kthGrammarV1(self, n: int, k: int, arr: list[int] = [0]) -> int:
        # print(arr)
        if n == 1:
            return arr[k-1]
        
        temp = []
        c = k
        for num in arr:
            if c <= 0:
                break
            if num == 0:
                temp.append(0)
                temp.append(1)
            else:
                temp.append(1)
                temp.append(0)

            c -= 2
        return self.kthGrammar(n-1,k,temp)

sol = Solution()
# print(sol.kthGrammar(n = 1, k = 1))
print(sol.kthGrammar(n = 2, k = 2))










