# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/?envType=daily-question&envId=2026-02-24

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        all_sum = 0
        #howtowork
        def allLeaves(node: Optional[TreeNode], path:str):
            nonlocal all_sum
            if not node:
                return
            
            path += str(node.val)
            if not node.left and not node.right:
                all_sum += int(path, 2)
                return
            
            allLeaves(node.left, path)
            allLeaves(node.right, path)

        allLeaves(root, "")
        return all_sum

sol = Solution()

root = TreeNode(1)

root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(0)
root.left.right = TreeNode(1)

root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
sol.sumRootToLeaf(root)