# https://leetcode.com/problems/elimination-game/description/

class Solution:
    #howtowork
    #revision
    def lastRemaining(self, n: int) -> int:
        head = 1               # First remaining number
        step = 1               # Gap between numbers
        remaining = n          # Number of remaining elements
        left_to_right = True   # Initial direction

        while remaining > 1:

            # Update head if the first number is eliminated
            if left_to_right or remaining % 2 == 1:
                head += step

            # Half the elements survive
            remaining //= 2

            # Gap between survivors doubles
            step *= 2

            # Reverse direction for the next round
            left_to_right = not left_to_right

        return head

    # 3375 / 3377 testcase passed
    def lastRemaining(self, n: int) -> int:

        def findNo(arr: list[int], dir:str):
            if len(arr) <= 1:
                return arr[0]
            
            # print(arr)

            if dir == 'l':
                for i in range(0,len(arr),2):
                    arr[i] = 0
                arr = [x for x in arr if x != 0]

                return findNo(arr, 'r')
        
            else:
                for i in range(len(arr)-1,-1,-2):
                    arr[i] = 0
                arr = [x for x in arr if x != 0]

                return findNo(arr, 'l')
                    
        return findNo(list(range(1,n+1)), 'l')

sol = Solution()
print(sol.lastRemaining(n = 9))