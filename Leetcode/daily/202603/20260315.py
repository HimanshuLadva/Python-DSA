# https://leetcode.com/problems/fancy-sequence/description/?envType=daily-question&envId=2026-03-15
class Fancy:
    MOD = int(1e9 + 7)
    def __init__(self):
        self.arr = []
        self.add = 0
        self.mul = 1
        
    def append(self, val: int) -> None:
        #howtowork
        val = (val - self.add) * pow(self.mul, -1, self.MOD)
        val %= self.MOD
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        #howtowork
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] * self.mul + self.add) % self.MOD
    
class Fancy:
    MOD = int(1e9 + 7)
    def __init__(self):
        self.arr = []
        
    def append(self, val: int) -> None:
        self.arr.append(val)

    def addAll(self, inc: int) -> None:
        for x in range(len(self.arr)):
            self.arr[x] += inc

    def multAll(self, m: int) -> None:
        for x in range(len(self.arr)):
            self.arr[x] *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return self.arr[idx] % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)