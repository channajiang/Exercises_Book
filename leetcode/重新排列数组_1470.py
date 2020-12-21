"""
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-the-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7]
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，
所以答案为 [2,3,5,4,1,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-the-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# class Solution(object):
#     def __init__(self):
#         self.list = []
#         l, r = 0, len(nums)
#         self.mid = int((l + r) / 2)
#
#     def sort_list(self, nums):
#         if len(nums) % 2 == 0:
#             list_1 = nums[:self.mid]
#             print(list_1)
#             list_2 = nums[self.mid:]
#             print(list_2)
#             a = 0
#             for i in list_1:
#                 for j in list_2:
#                     if list_1.index(i) == list_2.index(j):
#                         self.list.append(i)
#                         self.list.append(j)
#             print(self.list)
#         else:
#             print('The list is not 2n elements')
#
#
# if __name__ == '__main__':
#     nums = [1, 1, 2, 2]
#     d = Solution()
#     d.sort_list(nums)

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) % 2 == 0:
            for i in range(n):
                temp = nums.pop()
                nums.insert(n - i, temp)
            return nums


if __name__ == '__main__':
    nums = [2, 3, 5, 4, 1, 7]
    l, r = 0, len(nums)
    n = int((l + r) / 2)
    d = Solution()
    d.shuffle(nums, n)
    print(nums)

# arg = {'a':1, 'b':2}
# print(arg.values())
# k = (i for i in range(len(arg)))
# print(k)
# for k in arg:
#     print(k, arg[k])