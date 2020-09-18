# 这里有 n 个航班，它们分别从 1 到 n 进行编号。 
# 
#  我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座
# 位。 
# 
#  请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。 
# 
#  
# 
#  示例： 
# 
#  输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
#  
# 
#  
# 
#  提示：
# 
#  
#  1 <= bookings.length <= 20000 
#  1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000 
#  1 <= bookings[i][2] <= 10000 
#  
#  Related Topics 数组 数学 
#  👍 84 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0 for _ in range(n + 2)]  # 后面地比前面多多少 [45,-10,-20,0,0]
        for i, j, k in bookings:
            ans[i] += k
            ans[j+1] -= k  # 后面的比前面的多了个负数
        # print(ans)
        for i in range(n + 1):
            ans[i + 1] += ans[i]
        return ans[1:-1]

    # leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    bookings, n = [[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5
    print(Solution().corpFlightBookings(bookings=bookings, n=n))
