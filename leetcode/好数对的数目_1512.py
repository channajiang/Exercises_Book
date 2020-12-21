"""
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

示例 1：

输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始

示例 2：

输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对

示例 3：

输入：nums = [1,2,3]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-good-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# # nums = [1, 2, 3, 1, 1, 3]
# # nums = [1, 1, 1, 1]
# nums = [1, 2, 3]
# count = 0
# for i in range(0, len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j] and i < j:
#             count += 1
# print(count)
from typing import List


class Solution(object):
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        print(count)
        return count


nums = [1, 1, 1, 1]
d = Solution()
result = d.numIdenticalPairs(nums)
