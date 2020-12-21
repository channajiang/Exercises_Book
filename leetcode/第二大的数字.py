# a = [1, 2, 3]
# b = [1, 2, 4]
# print(id(a[1]))
# print(id(b[1]))

# num_list = [98, 12, 45, 1, 2, 32, 90, 45, 23, 121, 121, 11]
# tmp_dict = set(num_list)
# print(tmp_dict)
# tmp_list = sorted(tmp_dict)
# print(tmp_list)
# print('第二大的数是：', tmp_list[-2])


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [90, 64, 34, 25, 12, 22, 11]

bubbleSort(arr)

print(bubbleSort(arr))
for i in range(len(arr)):
    print("%d" % arr[i])

# def find_second_large_num(num_list):
#     # 方法二
#     # 设置两个标志位一个存储最大数一个存储次大数
#     # two 存储次大值，one 存储最大值，遍历一次数组即可，先判断是否大于 one，若大于将 one 的值给 two，
#     # 将 num_list[i] 的值给 one，否则比较是否大于two，若大于直接将 num_list[i] 的值给two，否则pass
#     one = num_list[0]
#     two = num_list[0]
#     for i in range(1, len(num_list)):
#         if num_list[i] > one:
#             two = one
#             one = num_list[i]
#         elif num_list[i] > two and num_list[i] != one:
#             two = num_list[i]
#     print("第二个大的数是 :", two)
#
#
# num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5, 78]
# find_second_large_num(num_list)

# 冒泡程序找到数组列表中第二大的数字
#  https://blog.csdn.net/weixin_38819889/article/details/93488557
num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5, 78]
max_one = num_list[0]
max_two = num_list[0]
for index in range(len(num_list)):
    if num_list[index] > max_one:
        max_one, max_two = num_list[index], max_one
    elif num_list[index] > max_two and num_list[index] != max_one:
        max_two = num_list[index]
    else:
        continue
print("第二个大的数是 :", max_two)


