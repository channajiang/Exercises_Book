"""
示例:

给定 n = 5，并且 version = 4 是第一个错误的版本。

调用 isBadVersion(3) -> false
调用 isBadVersion(5) -> true
调用 isBadVersion(4) -> true

所以，4 是第一个错误的版本。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-bad-version
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

list = ['a', 'B', ' ', 'C', 'A', 'b', 'A']
right = len(list)
left = 0
while left < right:
    mid = (right + left) // 2
    if list[mid].isupper():
        right = mid
        # print('第一个错误的版本是在列表中的第 % d 个元素 % d' % (list.index(mid), list[mid]))
    else:
        left = mid + 1
print('第一个错误的版本是在列表中的第 % d 个元素 % s' % (left, list[left]))


