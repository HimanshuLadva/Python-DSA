# https://leetcode.com/problems/make-array-elements-equal-to-zero?envType=daily-question&envId=2025-10-28
# #MIMP
from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # Calculate the total sum of all elements
        total_sum = sum(nums)
        
        # Initialize counters
        valid_count = 0
        left_sum = 0
        
        # Iterate through each element
        for num in nums:
            if num != 0:
                # Add non-zero elements to left sum as we move right
                left_sum += num
            else:
                # At a zero position, check if it's a valid starting point
                right_sum = total_sum - left_sum
                
                if left_sum == right_sum:
                    # Perfect balance: both directions work
                    valid_count += 2
                elif abs(left_sum - right_sum) == 1:
                    # Near balance: only one direction works
                    valid_count += 1
                # If difference > 1, no valid selections from this position
        
        return valid_count

def test_solution():
    solution = Solution()
    
    # Test case 1: [1,0,2,0,3]
    nums1 = [1, 0, 2, 0, 3]
    result1 = solution.countValidSelections(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2: [2,3,4,0,4,1,0]
    nums2 = [2, 3, 4, 0, 4, 1, 0]
    result2 = solution.countValidSelections(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print()
    
    # Test case 3: Simple case [0, 1, 0]
    nums3 = [0, 1, 0]
    result3 = solution.countValidSelections(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print()

if __name__ == "__main__":
    test_solution()
