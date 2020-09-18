# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。 
# 
#  假定 BST 有如下定义： 
# 
#  
#  结点左子树中所含结点的值小于等于当前结点的值 
#  结点右子树中所含结点的值大于等于当前结点的值 
#  左子树和右子树都是二叉搜索树 
#  
# 
#  例如： 
# 给定 BST [1,null,2,2], 
# 
#     1
#     \
#      2
#     /
#    2
#  
# 
#  返回[2]. 
# 
#  提示：如果众数超过1个，不需考虑输出顺序 
# 
#  进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内） 
#  Related Topics 树 
#  👍 141 👎 0
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        queue = [root]  # 定义一个栈，用于广度遍历
        d = defaultdict(int)  # 定义字典，用于存放元素以及其出现的次数
        while queue:
            node = queue.pop(0)
            d[node.val] += 1  # 将元素加入到字典中，并统计其出现的个数
            # if node.val not in d:
            #     d[node.val] = 1
            # else:
            #     d[node.val] += 1
            if node.left is not None:  # 分别遍历当前节点的左右元素
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        m = max(d.values())  # 找到元素最多出现的次数
        # l = []
        # for k, v in d.items():
        #     if v == m:
        #         l.append(k)  # 将最多出现的元素加入到列表中
        return [k for k, v in d.items() if v == m]
# leetcode submit region end(Prohibit modification and deletion)
