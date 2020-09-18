# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 
# 
#  示例: 
# 
#  输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 316 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        res = []

        def dfs(root, depth):
            if not root:
                return
            if len(res) <= depth:
                res.append(0)
            res[depth] = root.val

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)


        dfs(root, 0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
