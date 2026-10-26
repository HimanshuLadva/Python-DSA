# https://leetcode.com/problems/happy-number/
#implogic
#revision
#howtowork
class Solution:
    def getNext(self, n):
        sum = 0

        while n > 0:
            digit = n % 10
            sum += (digit * digit)
            n //= 10

        return sum
    
    def isHappy(self, n: int) -> bool:
        slow = self.getNext(n)
        fast = self.getNext(self.getNext(n))

        while slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return slow == 1

sol = Solution()
sol.isHappy(19)