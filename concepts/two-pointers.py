# when to use: when problem asking about finding pairs or triplets. use it for problems
# that require checking something from both ends of the array.

# Problem - Sum of Pair Equal to Target
def findPair(nums:list[int], target:int) -> bool:
    start = 0
    end = len(nums) - 1

    while start < end:
        sum = nums[start] + nums[end]
        
        if sum == target:
            return True
        elif sum < target:
            start += 1
        else:
            end -= 1

    return False

arr = [10,20,35,50]
target = 70

print(findPair(arr, target))