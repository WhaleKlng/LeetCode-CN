# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树[3, 9, 20, null, null, 15, 7],
#
# 3
# / \
#     9
# 20
# / \
#     15
# 7
#
# 返回锯齿形层次遍历如下：
#
# [
#     [3],
#     [20, 9],
#     [15, 7]
# ]
#
# Related
# Topics
# 栈
# 树
# 广度优先搜索
# 👍 265 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        sign = 1
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level[::sign])
            sign *= -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))

    # def BFS(root):
    #     '''广度优先'''
    #     if root == None:
    #         return
    #     # queue队列，保存节点
    #     queue = []
    #     # res保存节点值，作为结果
    #     # vals = []
    #     queue.append(root)
    #
    #     while queue:
    #         # 拿出队首节点
    #         currentNode = queue.pop(0)
    #         # vals.append(currentNode.val)
    #         print(currentNode.val, end=' ')
    #         if currentNode.left:
    #             queue.append(currentNode.left)
    #         if currentNode.right:
    #             queue.append(currentNode.right)
    #
    #
    # BFS(root)
