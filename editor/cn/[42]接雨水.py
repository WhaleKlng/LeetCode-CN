# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1646 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        # 边界条件
        if not height: return 0
        n = len(height)
        left = [0] * n
        right = [0] * n
        ans = 0
        # 初始化
        left[0] = height[0]
        right[n - 1] = height[n - 1]
        # 设置备忘录，分别存储左边和右边最高的柱子高度
        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])
        for j in range(n - 2, -1, -1):
            right[j] = max(height[j], right[j + 1])
        # 一趟遍历，比较每个位置可以存储多少水
        for i in range(n):
            if min(left[i], right[i]) > height[i]:
                ans += min(left[i], right[i]) - height[i]
        return ans
# leetcode submit region end(Prohibit modification and deletion)
