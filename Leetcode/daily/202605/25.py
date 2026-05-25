# https://leetcode.com/problems/jump-game-vii/?envType=daily-question&envId=2026-05-25

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        i = 0
        while i < n-1:
            max_jump = min(i + maxJump, n-1)
            min_jump = min(i + minJump, n-1)

            if min_jump == n - 1 and s[n-1] == '0':
                return True
            
            if s[min_jump] != '0':
                is_found = False
                next_i = i 

                for j in range(max_jump, min_jump - 1, -1):
                    if s[j] == '0':
                        is_found = True
                        next_i = j

                if not is_found:
                    return False
                
                if next_i == i:
                    return False
                
                i = next_i
            else:
                i = min_jump

        return i == n-1
    # 129 testcase pass
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        """ for i,x in enumerate(s):
            print((i,x), end=" ")
            print()
        print("============================================") """

        i = 0
        while i < n:
            max_jump = (i + maxJump) if (i + maxJump) < n else n-1
            min_jump = (i+minJump) if (i+minJump) < n else n-1
            # print(i, min_jump, max_jump)
            if s[min_jump] != '0':
                is_find = False
                for j in range(min_jump, max_jump+1):
                    # print(f"in loop = {s[j]}")
                    if s[j] == '0':
                        is_find = True
                        i = j
                
                if is_find == False:
                    return False
            else:
                i += min_jump
        return True
    
sol = Solution()
print(sol.canReach(s = "011010", minJump = 2, maxJump = 3))   
print(sol.canReach(s = "01101110", minJump = 2, maxJump = 3))
print(sol.canReach(s = "011111000111000001011111010", minJump = 6, maxJump = 8))
print(sol.canReach(s = "00111010", minJump = 3, maxJump = 5))