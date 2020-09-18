# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
#  Related Topics 动态规划 
#  👍 528 👎 0

from typing import List


# 在一天当中，只能进行“买”，“卖”或者“什么都不干”中的一种操作
# 在“卖”掉股票之后，必须“什么都不干”一天
# dp[i][0]表示在i天买入最大利益
#
# dp[i][1]表示在i天卖出最大利益
#
# dp[i][2]表示在经过卖出的后一天冷冻期的最大利益
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n < 2:
            return 0
        # dp = [[0] * 2] * n + 1  # 我透遇到了深浅拷贝的问题
        dp = [[0, 0] for _ in range(n + 1)]
        dp[1][0] = 0
        dp[1][1] = -prices[1 - 1]
        dp[2][0] = max(dp[1][0], dp[1][1] + prices[1])
        dp[2][1] = max(dp[1][1], dp[1][0] - prices[1])

        for i in range(3, n + 1):
            dp[i][0] = max(dp[i - 1][1] + prices[i - 1], dp[i - 1][0])
            dp[i][1] = max(dp[i - 2][0] - prices[i - 1], dp[i - 1][1])
        return dp[-1][0]


# leetcode submit region end(Prohibit modification and deletion)
prices = [1, 2, 3, 0, 2]
print(Solution().maxProfit(prices))
