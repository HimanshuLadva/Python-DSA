# https://leetcode.com/problems/balanced-binary-tree/description/?envType=daily-question&envId=2026-02-08
#howtowork
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]):
            if not node:
                return 0
            
            print(f"Checking node: {node.val}") 
            left_height = check(node.left)
            if left_height == -1:
                return -1
            
            right_height = check(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        if check(root) == -1:
            return False
        else:
            return True
        
sol = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(3)

root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
sol.isBalanced(root)