# https://leetcode.com/problems/count-square-sum-triples?envType=daily-question&envId=2025-12-08
from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c = int(sqrt(a**2 + b**2 + 1))
                if c <= n and c**2 == a**2 + b**2:
                    count += 1
        return count

sol = Solution()
# print(sol.countTriples(5))
print(sol.countTriples(10))
""" 
Why We Use +1 in Pythagorean Triple Code

**Problem:** Floating-point errors can cause `sqrt(a² + b²)` to return slightly less than the correct integer (e.g., 4.9999999 instead of 5.0), making `int()` truncate to the wrong value.

**Solution:** Adding +1 before taking `int()` acts as a rounding buffer:
- Valid triple: `int(sqrt(25 + 1)) = int(5.099...) = 5` ✓
- Invalid case: Still rejected by the check `c² == a² + b²`

**Result:** We safely capture all valid Pythagorean triples without false positives, because the equality check filters out any incorrect values that the +1 might produce.

**In short:** +1 prevents us from losing correct answers due to floating-point precision issues, while the subsequent validation ensures we don't accept wrong answers.
 """