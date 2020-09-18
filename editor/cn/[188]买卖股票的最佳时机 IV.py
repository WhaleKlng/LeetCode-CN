# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。 
# 
#  注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  示例 1: 
# 
#  输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#  
# 
#  示例 2: 
# 
#  输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 
# 。
#  
#  Related Topics 动态规划 
#  👍 286 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMax(self, prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += (prices[i] - prices[i - 1])
        return res

    # def maxProfit(self, k: int, prices: List[int]):
    #     n = len(prices)
    #     if n < 2 or k < 1:
    #         return 0
    #     if k >= n / 2:
    #         return self.getMax(prices)
    #     buy = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
    #     sell = [[0] * (k + 1) for _ in range(n + 1)]
    #     # buy[0][0] = float('-inf')
    #     # sell[1][0] = 0
    #     for i in range(1, n + 1):
    #         for j in range(1, k + 1):
    #             buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i - 1])
    #             sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i - 1])
    #     return sell[-1][k]
    def maxProfit(self, k: int, prices: List[int]):
        n = len(prices)
        if n < 2 or k < 1:
            return 0
        if k >= n / 2:
            return self.getMax(prices)
        buy = [float('-inf') for _ in range(k + 1)]
        sell = [0 for _ in range(k + 1)]
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - prices[i - 1])
                sell[j] = max(sell[j], buy[j] + prices[i - 1])
        return sell[k]


# leetcode submit region end(Prohibit modification and deletion)
lst = [3, 3, 5, 0, 0, 3, 1, 4]
print(Solution().maxProfit(2, lst))
