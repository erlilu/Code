from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], res:List[list]):
            if node is None:
                res.append(None)
                return
            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)

        res1, res2 = [], []
        dfs(p, res1)
        dfs(q, res2)

        return res1 == res2
