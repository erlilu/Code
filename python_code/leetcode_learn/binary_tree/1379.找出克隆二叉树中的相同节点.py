from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return

        # 目标结果
        if original == target:
            return cloned

        left_res = self.getTargetCopy(original.left, cloned.left, target)
        if left_res:
            return left_res

        right_res = self.getTargetCopy(original.right, cloned.right, target)
        if right_res:
            return right_res