class Solution:
    # 2ms
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        return len(directions) - directions.count('S')
    # 291ms
    def countCollisionsV1(self, directions: str) -> int:
        temp = []
        count = 0
        dlen = len(directions)
        dirarr = list(directions)
        
        for i in range(dlen):
            if i != 0:
                if dirarr[i] == 'L' and temp[-1] != 'L':
                    if temp[-1] == 'R':
                        count += 2
                    else:
                        count += 1
                    dirarr[i] = 'S'
                    temp[-1] = 'S'
            temp.append(dirarr[i])

        # print(f"first temp = {temp}")
        temp.reverse()
        # print(f"second temp = {temp}")
        dirarr = temp
        temp = []
        for i in range(dlen):
            if i != 0:
                if dirarr[i] == 'R' and temp[-1] != 'R':
                    if temp[-1] == 'L':
                        count += 2
                    else:
                        count += 1
                    dirarr[i] = 'S'
                    temp[-1] = 'S'
            temp.append(dirarr[i])
        
        # print(f"final temp = {temp}")
        return count
    
sol = Solution()
directions = "RLRSLL"
directions = "LLRR"
directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
print(sol.countCollisions(directions))