from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node: Optional[TreeNode], cur: int):
            nonlocal total
            if not node:
                return

            cur = (cur << 1) | node.val  # 等价于 cur * 2 + node.val
            if not node.left and not node.right:
                total += cur
                return

            dfs(node.left, cur)
            dfs(node.right, cur)

        dfs(root, total)
        return total