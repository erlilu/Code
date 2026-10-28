# Definition for a binary tree node.

from idlelib.tree import TreeNode
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []  # 存结点，而不是节点值
        def preorder(node: Optional[TreeNode]):
            if node:
                nodes.append(node)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        # 原地串成链表
        for i in range(1, len(nodes)):
            pre, curr = nodes[i-1], nodes[i]
            pre.left = None
            pre.right = curr

        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None
            



