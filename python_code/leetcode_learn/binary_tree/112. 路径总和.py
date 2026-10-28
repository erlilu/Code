from hmac import digest_size
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0

        def dfs(node: Optional[TreeNode], sum):
            if node is None:
                return False

            sum += node.val

            if not node.left and not node.right:
                return sum == targetSum
            return dfs(node.left, sum) or dfs(node.right, sum)

        return dfs(root, sum)


"""
错误	后果
未接收递归返回值	找到路径也无法返回 True
非叶子节点就判断 sum == targetSum	中途满足条件时误判
空节点返回 None 而非 False	逻辑不清晰
判断时机错误（左子树后判断，右子树后判断）	路径混乱
修正的核心就是：仅在叶子节点判断，且用递归返回值的 or 向上传递结果。
"""