# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        return self.getHeight(root.left) - self.getHeight(root.right) < 2
        
    def getHeight(self, node):
        if node is None:
            return 0

        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1
