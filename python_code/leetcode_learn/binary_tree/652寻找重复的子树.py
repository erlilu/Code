from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
方法：
1. 字符串拼接：开销大，直观易懂
2. UID整数映射：开销n，避免字符串操作，更高效【本质：字符串序列化的优化版】
思路：后续遍历
1. 
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        count = defaultdict(int)
        res = []   # 存储重复子树的根节点

        """后序遍历，返回当前子树的序列化字符串"""
        def dfs(node: Optional[TreeNode]):
            if not node:
                return "#"

            left_serial = dfs(node.left)
            right_serial = dfs(node.right)

            # 构造当前子树的序列化字符串
            serial = f"{node.val},{left_serial},{right_serial}"
            count[serial] += 1  # 更新出现次数

            # 出现两次时，加入序列
            if count[serial] == 2:
                res.append(node)
            #  返回 serial，父节点用子节点的 serial 来拼自己的 serial
            return serial
        dfs(root)
        return res


