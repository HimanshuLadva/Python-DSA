# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree_from_array(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None

    root = TreeNode(arr[i])
    root.left = create_tree_from_array(arr, 2*i + 1)
    root.right = create_tree_from_array(arr, 2*i + 2)

    return root

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        max_level = 1
        max_sum = float('-inf')
        queue = [root]
        count = 1
        while queue:
            level_sum = 0
            next_level = []

            for node in queue:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = count
            
            count += 1
            queue = next_level
        return max_level
    
    def maxLevelSumV1(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        max_sum = float('-inf')

        queue = deque([root])
        count = 0
        while queue:
            level_size = len(queue)
            count += 1

            temp_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                # print(node.val, end=" ")
                temp_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # print(f"temp_sum = {temp_sum}")
            if temp_sum > max_sum:
                # print(f"operation = {temp_sum}, {max_sum}")
                max_sum = temp_sum
                max_level = count
            # print("\n---------------------")
        return max_level
    
sol = Solution()

arr =  [1,7,0,7,-8,None, None]
arr = [989,None,10250,98693,-89388,None,None,None,-32127]
arr = [-100,-200,-300,-20,-5,-10,None]
root = create_tree_from_array(arr)
print(sol.maxLevelSum(root))