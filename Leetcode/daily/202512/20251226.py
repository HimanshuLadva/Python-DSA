# https://leetcode.com/problems/minimum-penalty-for-a-shop?envType=daily-question&envId=2025-12-26
# #method
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        accum = 0
        result = 0
        resultIndex = -1

        for i in range(n):
            if customers[i] == 'Y':
                accum += 1
            else:
                accum -= 1
            
            if accum > result:
                result = accum
                resultIndex = i
        return resultIndex + 1
    # 247ms
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        ans = []
        current_count = 0
        prefix_Y = [0] * (n+1)
        prefix_N = [0] * (n+1)

        for i,c in enumerate(customers):
            prefix_Y[i+1] = prefix_Y[i] + (c == 'Y')
            prefix_N[i+1] = prefix_N[i] + (c == 'N')

        for i in range(n):
            current_count = 0

            # current element
            if customers[i] == 'Y':
                current_count += 1

            # Y customers after i
            current_count += prefix_Y[n] - prefix_Y[i + 1]

            # N customers before i
            current_count += prefix_N[i]

            ans.append(current_count)

        ans.append(prefix_N[n])
        min_count = min(ans)
           
        return ans.index(min_count)
    
    # TLE
    def bestClosingTimeV1(self, customers: str) -> int:
        n = len(customers)
        
        ans = []
        current_count = 0
        for i in range(n):
            current_count = 0
            if customers[i] == 'Y':
                current_count += 1

            # will comming customer count
            current_count += len([x for x in range(i+1, n) if customers[x] == 'Y'])
            # was not comming customer count
            current_count += len([x for x in range(i) if customers[x] == 'N'])
            ans.append(current_count)

        ans.append(len([x for x in range(n) if customers[x] == 'N']))
        min_count = min(ans)
        # print(ans)
           
        return ans.index(min_count)
    
sol = Solution()
customers = "YYNYNNYYYNY"
customers = "YYYY"
customers = "YYNY"
print(sol.bestClosingTime(customers))