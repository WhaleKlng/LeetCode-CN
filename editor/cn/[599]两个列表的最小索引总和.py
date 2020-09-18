# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。 
# 
#  你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。 
# 
#  示例 1: 
# 
#  输入:
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
#  
# 
#  示例 2: 
# 
#  输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
#  
# 
#  提示: 
# 
#  
#  两个列表的长度范围都在 [1, 1000]内。 
#  两个列表中的字符串的长度将在[1，30]的范围内。 
#  下标从0开始，到列表的长度减1。 
#  两个列表都没有重复的元素。 
#  
#  Related Topics 哈希表 
#  👍 82 👎 0

from typing import List
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = defaultdict(int)
        for index, item in enumerate(list1):
            res[item] += index
        for index, item in enumerate(list2):
            res[item] += index
        unio = set(list1) & set(list2)
        # print(unio)  # {'KFC', 'Burger King', 'Shogun'}
        min_sum = float('inf')
        for key, val in res.items():
            if key in unio:
                if val <= min_sum:
                    min_sum = val
        return [k for (k, v) in res.items() if v == min_sum and k in unio]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().findRestaurant(list1, list2))
