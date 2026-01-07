# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree?envType=daily-question&envId=2026-01-07
# #method
# #newlearn-topic
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)
        
        S = total_sum(root)
        self.max_prod = 0

        def postorder(node):
            if not node:
                return 0
            
            left = postorder(node.left)
            right = postorder(node.right)
            
            sub_tree = left + right + node.val
            self.max_prod = max(self.max_prod, sub_tree * (S - sub_tree))

            return sub_tree
        
        postorder(root)
        return self.max_prod % MOD
    
sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
print(f"ans = {sol.maxProduct(root)}")