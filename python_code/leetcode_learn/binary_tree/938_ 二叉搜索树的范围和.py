'''
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
'''
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        # 左子节点
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        # 右子节点
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root

# 遍历 + 排序 + 求值
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        total = 0
        for val in arr:
            if low <= val <= high:
                total += val
        return total



if __name__ == "__main__":
    vals = [10,5,15,3,7,None,18]
    root = build_tree(vals)
    sol = Solution()
    print(sol.rangeSumBST(root, 7, 15))