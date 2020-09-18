# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例： 
# 
#  输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  Related Topics 回溯算法 
#  👍 600 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
        return res
# leetcode submit region end(Prohibit modification and deletion)
