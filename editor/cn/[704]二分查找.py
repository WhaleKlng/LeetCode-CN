# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否
# 则返回 -1。 
# 
#  
# 示例 1: 
# 
#  输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
#  
# 
#  示例 2: 
# 
#  输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#  
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设 nums 中的所有元素是不重复的。 
#  n 将在 [1, 10000]之间。 
#  nums 的每个元素都将在 [-9999, 9999]之间。 
#  
#  Related Topics 二分查找 
#  👍 149 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1  # [left,right]
        while left <= right:  # left+1 = right-1时跳出 [left,right)区间为空
            mid = int(left + (right - left) / 2)
            if nums[mid] == target:
                # right = mid
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1
        # leetcode submit region end(Prohibit modification and deletion)


nums = [-1, 0, 3, 5, 9, 12]
target = 13
left = 0
right = len(nums)
while left < right:  # left = right时跳出 [left,right)区间为空
    mid = int((right + left) / 2)
    if nums[mid] == target:
        print(mid)
    elif nums[mid] < target:
        left = mid + 1
    elif nums[mid] > target:
        right = mid
print(left)
print(nums[left])
print('{}'.format(left if nums[left] == target else -1))
