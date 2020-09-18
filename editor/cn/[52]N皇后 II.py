# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回 n 皇后不同的解决方案的数量。 
# 
#  示例: 
# 
#  输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N
# -1 步，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法 
#  👍 146 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 生成N*N的棋盘，填充棋盘，每个格子默认是“。”表示没有放置皇后
        arr = [["." for _ in range(n)] for _ in range(n)]
        res = []

        # 检查当前的行和列是否可以放置皇后
        def check(x, y):
            # 检查竖着的一列是否有皇后
            for i in range(x):
                if arr[i][y] == "Q":
                    return False
            # 检查左上到右下的斜边是否有皇后
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                if arr[i][j] == "Q":
                    return False
                i, j = i - 1, j - 1
            # 检查左下到右上的斜边是否有皇后
            i, j = x - 1, y + 1
            while i >= 0 and j < n:
                if arr[i][j] == "Q":
                    return False
                i, j = i - 1, j + 1
            return True

        def dfs(x):
            # x是从0开始计算的
            # 当x==n时所有行的皇后都放置完毕，此时记录结果
            if x == n:
                res.append(["".join(arr[i]) for i in range(n)])
                return
                # 遍历每一列
            for y in range(n):
                # 检查[x,y]这一坐标是否可以放置皇后
                # 如果满足条件，就放置皇后，并继续检查下一行
                if check(x, y):
                    arr[x][y] = "Q"
                    dfs(x + 1)
                    arr[x][y] = "."

        dfs(0)
        return len(res)
# leetcode submit region end(Prohibit modification and deletion)
