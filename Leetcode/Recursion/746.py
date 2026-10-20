# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    #revision
    #implogic
    #howtowork
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        memo = {}

        def solve(i:int) -> int:
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(solve(i+1), solve(i+2))

            return memo[i]

        return min(solve(0), solve(1))

    # TLE
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        def solve(i:int, ans:int = 0):
            if i >= n:
                return ans

            # one step
            one = solve(i+1, ans + cost[i])

            # two step
            two = solve(i+2, ans + cost[i])

            return min(one, two)
        
        return min(solve(0), solve(1))
    
    def minCostClimbingStairsV1(self, cost: list[int]) -> int:
        print(f"cost = {cost}")
        def findMin(i:int, j:int):
            if cost[i] <= cost[j]:
                return (i, cost[i])
            else:
                return (j, cost[j])

        n = len(cost)
        # start from 0
        def solve(i:int, fidx: int, ans:int = 0):
            if i+2 >= n:
                return ans
            
            ele = findMin(i+1, i+2)
            print(f"idx = {ele[0]}, ele = {ele[1]}, fidx = {fidx}")
            if fidx == i:
                ans += (cost[i] + ele[1])
            else:
                ans += ele[1]
            print(f"ans = {ans}")
            idx = ele[0]
            return solve(idx, fidx, ans)

        x = solve(0, 0, cost[0])
        print("----------------------------")
        y = solve(1, 1, cost[1])
        # return min(solve(0, 0), solve(1, 0))
        return min(x, y)

sol = Solution()
print(sol.minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]))
print(sol.minCostClimbingStairs([0,1,1,0]))