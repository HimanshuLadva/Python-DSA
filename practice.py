class Solution:
    def check_len(self, arr:list[int]):
        print("check len")
        return len(arr)
    
    def display(self,arr: list[int]):
        i = 0

        while i < self.check_len(arr):
            print(arr[i])
            i += 1

s = Solution()
s.display([1,2,3,4,5])