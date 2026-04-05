# https://leetcode.com/problems/robot-return-to-origin/?envType=daily-question&envId=2026-04-05

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')
    # 166ms
    def judgeCircle(self, moves: str) -> bool:
        res = []
        for i,move in enumerate(moves):
            if i != 0:
                if move == 'L' and 'R' in res:
                    res.remove('R')
                elif move == 'R' and 'L' in res:
                    res.remove('L')
                elif move == 'U' and 'D' in res:
                    res.remove('D')
                elif move == 'D' and 'U' in res:
                    res.remove('U')
                else:
                    res.append(move)
            else:
                res.append(move)

        # print(res)
        return not len(res)
    
sol = Solution()
# sol.judgeCircle(moves = "LL")
# sol.judgeCircle(moves = "RRDD")
# sol.judgeCircle(moves = "LDRRLRUULR")
sol.judgeCircle(moves = "UDUDUDLRLRLRR")