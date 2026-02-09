# https://leetcode.com/problems/balance-a-binary-search-tree/?envType=daily-question&envId=2026-02-09
from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nums = []
        def inorder_traversal(node: Optional[TreeNode]):
            if not node:
                return
            inorder_traversal(node.left)
            nums.append(node.val)
            inorder_traversal(node.right)

        inorder_traversal(root)
        nums.sort()

        def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
            n = len(nums)
            if n == 0:
                return None
            
            mid = n // 2
            root = TreeNode(nums[mid])
        
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])
            return root
        
        root = sortedArrayToBST(nums)
        return root

sol = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(4)
sol.balanceBST(root)