# 给定一个含有 n 个正数的数组 x。从点 (0,0) 开始，先向北移动 x[0] 米，然后向西移动 x[1] 米，向南移动 x[2] 米，向东移动 x[3]
#  米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。 
# 
#  编写一个 O(1) 空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。 
# 
#  
# 
#  示例 1: 
# 
#  ┌───┐
# │   │
# └───┼──>
#     │
# 
# 输入: [2,1,1,2]
# 输出: true 
#  
# 
#  示例 2: 
# 
#  ┌──────┐
# │      │
# │
# │
# └────────────>
# 
# 输入: [1,2,3,4]
# 输出: false 
#  
# 
#  示例 3: 
# 
#  ┌───┐
# │   │
# └───┼>
# 
# 输入: [1,1,1,1]
# 输出: true 
#  
#  Related Topics 数学 
#  👍 34 👎 0
from itertools import chain
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        x0, x1, x2, x3, x4, x5 = 1 / 2, 1 / 2, 1 / 4, 1 / 4, 1 / 8, 1 / 8  # 初始值, 避免边界条件
        for i in x:
            x0, x1, x2, x3, x4, x5 = i, x0, x1, x2, x3, x4
            if (x2 <= x0 and x1 <= x3) or (x4 <= x2 <= x0 + x4 and x1 <= x3 <= x1 + x5):  # 交点判定条件
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)
x = [3,3,4,2,2]
print(Solution().isSelfCrossing(x))
