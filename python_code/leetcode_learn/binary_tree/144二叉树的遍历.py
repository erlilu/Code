from typing import Optional, List
from collections import deque

# 二叉树节点定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def f(node: Optional[TreeNode]):
            if node is None:
                return

            f(node.left)
            res.append(node.val)
            f(node.right)

        f(root)
        return res

# 辅助函数：根据层序遍历列表构建二叉树
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

# --- 正确调用 ---
if __name__ == "__main__":
    vals = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
    root = build_tree(vals)                     # 先构造树
    sol = Solution()                            # 创建实例
    print(sol.preorderTraversal(root))          # 输出前序遍历结果