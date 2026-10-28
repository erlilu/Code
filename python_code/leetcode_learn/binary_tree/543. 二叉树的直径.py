from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node: Optional[TreeNode]):
            if not node:
                return 0

            l = depth(node.left)
            r = depth(node.right)

            self.ans = max(self.ans, l+r)  # 经过当前节点的路径长度

            return max(l, r) + 1        # 返回当前子树的最大深度
        
        depth(root)
        return self.ans