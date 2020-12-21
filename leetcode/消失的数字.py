# -*-coding:utf-8-*-
"""
数组包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。
你有办法在o(n)时间内完成吗

示例 1：

输入：nums = [3,0,1]
输出：2

示例 2：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8


"""
from typing import List


class Solution:
    def disappearNum(self, nums: List[int]) -> int:
        a = list(range(len(nums) + 1))
        # print(a)
        if len(nums) < len(a):
            if sum(nums) - sum(a) == 0:
                if len(nums) < len(a):
                    # print('缺失的整数为：0')
                    return 0
            else:
                # print(sum(a) - sum(nums))
                return sum(a) - sum(nums)
        else:
            print('输入有问题')

    def disappear(self, nums: List[int]) -> int:
        print(sum(range(len(nums) + 1)) - sum(nums))
        return sum(range(len(nums) + 1)) - sum(nums)

    def disappearDigit(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                print(i)
                return i
        # print(nums[-1]+1)
        # return nums[-1]+1


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    d = Solution()
    d.disappearDigit(nums)
