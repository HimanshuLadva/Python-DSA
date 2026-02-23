# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/?envType=daily-question&envId=2026-02-23

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()

        for i in range(len(s) - k + 1):
            seen.add(s[i:i+k])

        return len(seen) == 2**k
    # TLE
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            b = format(i, f'0{k}b')
            if b not in s:
                return False

        return True
    # TLE
    def hasAllCodesV1(self, s: str, k: int) -> bool:
        all_combination = []
        for i in range(2**k):
            all_combination.append(format(i, f'0{k}b'))

        # print(all_combination)

        for x in all_combination:
            if x not in s:
                return False
        return True

sol = Solution()
s = "00110110"
k = 2
print(sol.hasAllCodes(s, k))