# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1, n+1))
        l = len(arr)
        ele = k

        def findlast(arr:list[int], l: int, ele: int):
            if l <= 1:
                return arr[0]
            
            idx = arr.index(ele)
            arr.remove(ele)
            l = len(arr)
            next = (idx + (k-1)) % l
            ele = arr[next]

            return findlast(arr, l, ele)

        return findlast(arr, l, ele)


    def findTheWinnerV1(self, n: int, k: int) -> int:
        arr = list(range(1, n+1))
        l = len(arr)
        ans = []
        ele = k

        while l > 1:
            ans.append(ele)
            idx = arr.index(ele)
            arr.remove(ele)
            print(arr)
            l = len(arr)
            next = (idx + (k-1)) % l
            ele = arr[next]

        return arr[0]

sol = Solution()
print(sol.findTheWinner(n = 6, k = 5))
print(sol.findTheWinner(n = 5, k = 2))