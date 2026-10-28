from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], res: List[list]):
            if node is None:
                return

            if not node.right and not node.left:
                res.append(node.val)

            dfs(node.left, res)
            dfs(node.right, res)
            return

        res1, res2 = [], []
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2
