# https://leetcode.com/problems/count-binary-substrings/?envType=daily-question&envId=2026-02-19
#howtowork
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr_group = 1
        prev_group = 0
        count = 0

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                curr_group += 1
            else:
                count += min(curr_group, prev_group)
                prev_group = curr_group
                curr_group = 1
        
        count += min(prev_group, curr_group)
        return count
    # tle
    def countBinarySubstrings(self, s: str) -> int:
        s_len = len(s)
        count = 0
        for i in range(s_len):
            for j in range(i+1, s_len):
                n = (j-i+1)
                if n % 2 != 0:
                    continue
                
                temp = s[i:(j+1)]
                # print('-------------------------------')
                # print(temp)
                if temp.count('1') != temp.count('0'):
                    continue
                
                mid = i + (j - i + 1)//2
                first_half = s[i:mid]
                second_half = s[mid:j+1]
                # print(f"first = {first_half}, second = {second_half}")

                count_1_f = first_half.count('1')
                count_1_s = second_half.count('1')
                count_0_f = first_half.count('0')
                count_0_s = second_half.count('0')

                if (count_0_f and count_1_f) or (count_1_f and count_1_s):
                    continue

                # print(f"temp = {temp}")
                count += 1
        return count
    
sol = Solution()
s = "00110011"
sol.countBinarySubstrings(s)