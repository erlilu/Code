import queue
from asyncio.windows_events import NULL
from collections import deque, Counter
from encodings import cp437
from statistics import mode
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


# 搜索二叉树的众数
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        fin_nums = []
        def inorder(node: Optional[TreeNode]):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
            return
        inorder(root)

        if not res:
            return
        counter = Counter(res)   # 统计每个元素出现的次数
        max_count = max(counter.values())   # 获取最高出现次数

        for item, count in counter.items():
            if count == max_count:
                fin_nums.append(item)
        return fin_nums





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
    vals = [1,None,2,2]
    root = build_tree(vals)
    sol = Solution()
    print(sol.findMode(root))