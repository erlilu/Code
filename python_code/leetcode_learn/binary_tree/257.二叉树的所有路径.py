from platform import node
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node: Optional[TreeNode], path: str):
            if node is None:
                return

            if path:        # 空时不执行，空不是None，""
                path += "->"
            path += str(node.val)

            # 如果没有叶子节点，路径结束，加入结果
            if not node.left and not node.right:
                res.append(path)
                return

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return res
