import queue
from asyncio.windows_events import NULL
from collections import deque
from idlelib import rpc
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(val=root_val)

        root_idx = inorder.index(root_val)

        root.left = self.buildTree(preorder[1: root_idx+1], inorder[: root_idx])
        root.right = self.buildTree(preorder[root_idx+1: ], inorder[root_idx+1: ])

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
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    sol = Solution()
    root = sol.buildTree(preorder, inorder)
    print(sol.levelOrder(root))
'''
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
'''