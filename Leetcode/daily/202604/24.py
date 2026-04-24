# Furthest Point From Origin
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        blank = 0

        for move in moves:
            if move == 'L':
                left += 1
            elif move =='R':
                right += 1
            else:
                blank += 1

        return abs(left - right) + blank
    # 0ms 
    def furthestDistanceFromOriginV1(self, moves: str) -> int:
        moves_l = list(moves)

        count_L = sum(1 for x in moves_l if x == 'L')
        count_R = sum(1 for x in moves_l if x == 'R')

        
        if count_L >= count_R:
            moves = moves.replace('_', 'L')
        else:
            moves = moves.replace('_', 'R')

        # print(f"first = {moves_l} ,count_L = {count_L}, count_R = {count_R}")
        moves_l = list(moves)

        count_L = sum(1 for x in moves_l if x == 'L')
        count_R = sum(1 for x in moves_l if x == 'R')

        # print(f"second = {moves_l} ,count_L = {count_L}, count_R = {count_R}")
        return abs(count_R - count_L)
    
sol = Solution()
print(sol.furthestDistanceFromOrigin(moves = "L_RL__R"))
print(sol.furthestDistanceFromOrigin(moves = "_R__LL_"))