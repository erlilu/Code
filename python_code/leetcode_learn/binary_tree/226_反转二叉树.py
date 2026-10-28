import queue
from asyncio.windows_events import NULL
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# 按层构建二叉树
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


# 反转二叉树
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    # 层序遍历
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        res = []

        # 队列不为空，继续处理
        while queue:    # while len(queue)>0:
            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res




if __name__ == "__main__":
    vals = [4,2,7,1,3,6,9]
    root = build_tree(vals)
    sol = Solution()
    print(sol.levelOrder(root))
    res_root = sol.invertTree(root)
    print(sol.levelOrder(res_root))