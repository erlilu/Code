"""
给你一个二叉树的根节点 root ，计算并返回 整个树 的坡度 。
节点的坡度 = ｜该节点左子树的节点之和 - 右子树节点之和｜ 。【绝对值abs】
- 如果没有左子树的话，左子树的节点之和为 0 ；
- 没有右子树的话也是一样。空结点的坡度是 0 。

整个树 的坡度就是其所有节点的坡度之和。
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 后续遍历
class Solution1:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal total_tilt
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            title = abs(left_sum - right_sum)
            total_tilt += title     # 此处计算完成，total_title

            # 返回以node为根节点的子树的所有总和（供父节点使用）
            return left_sum + right_sum + node.val

        dfs(root)
        return total_tilt


    # 前序遍历【不推荐，无法直接获取左右子树，仍需要进行一次后续遍历，把节点存入字典】
    class Solution2:
        def findTilt(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            subtree_sum = {}

            # 一次遍历----后序遍历：计算所有节点子树
            def compute_sum(node: Optional[TreeNode]):
                if not node:
                    return 0
                left_sum = compute_sum(node.left)
                right_sum = compute_sum(node.right)
                s = left_sum + right_sum + node.val
                subtree_sum[node] = s
                return s

            compute_sum(root)
            total_tilt = 0

            # 二次遍历----前序遍历累加坡度
            def dfs_preorder(node: Optional[TreeNode]) -> int:
                nonlocal total_tilt
                if not node:
                    return
                left_sum = subtree_sum.get(node.left, 0)
                right_sum = subtree_sum.get(node.right, 0)
                total_tilt += abs(left_sum - right_sum)

                dfs_preorder(node.left)
                dfs_preorder(node.right)

            dfs_preorder(root)
            return total_tilt