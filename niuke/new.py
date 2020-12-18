import re
# #
# # record = [('2017-03-13 11:50:09', 271, 131),
# #           ('2017-03-13 11:50:09', 272, 171),
# #           ('2017-03-13 11:50:09', 277, 171)]
# # dic = {}
# # # small_dic = {}
# # list = []
# # for element in record:
# #     print(element)
# #     print("checkTime: %s " % element[0])
# #     print("lessonid: %d " % element[1])
# #     print("studentid: %d " % element[2])
# #     # small_dic['lessonid'] = element[1]
# #     # small_dic['checkTime'] = element[0]
# #     key_01 = "lessonid"
# #     key_02 = "checkTime"
# #     small_dict = {key_01: element[1], key_02: element[0]}
# #     # dic[element[2]] = list
# #     list.append(small_dict)
# #     print(list)
# #     if element[2] not in dic:
# #         dic[element[2]] = list
# #     else:
# #         pass
# #
# #
# # print(dic)
# #
# # # time = re.findall(r"'(.*)", record)
# # # print(time)
# # # id = re.findall(r"'([0-9]*)\)", record)
# # # print(id)
#
#
#
# import re
#
# record = [('2017-03-13 11:50:09', 271, 131),
#           ('2017-03-13 11:50:09', 272, 171),
#           ('2017-03-13 11:50:09', 277, 171)]
# dic = {}
# small_dict = {}
# dict_list = []
# f_list = []
# for i in range(len(record)):
#     print(record[i])
#     print("checkTime: %s " % record[i][0])
#     print("lessonid: %d " % record[i][1])
#     print("studentid: %d " % record[i][2])
#     # list.append(small_dict)
#     # print(list)
#     # print(list[i])
#     key_01 = "lessonid"
#     key_02 = "checkTime"
#     small_dict = {key_01: record[i][1], key_02: record[i][0]}
#     # list[i]["lessonid"] = record[i][1]
#     # list[i]["checkTime"] = record[i][0]
#     dict_list.append(small_dict)
#     print(dict_list)
#     if record[i][2] not in dic:
#         dic[record[i][2]] = [dict_list[i]]
#     else:
#         f_list.append(dic[record[i][2]])
#         f_list.append(dict_list[i])
#         dic[record[i][2]] = f_list
# # print(small_dic)
#     # list.append(small_dic)
#     # dic[element[2]] = list
#     # list.append(small_dic)
#     # print(list)
#     # if element[2] not in dic:
#     #     dic[element[2]] = list
#     # else:
#     #     pass
#
# print(dic)
# #
# # # time = re.findall(r"'(.*)", record)
# # # print(time)
# # # id = re.findall(r"'([0-9]*)\)", record)
# # # print(id)


fileName = "('2017-03-13 11:50:09', 271, 131)," \
           "('2017-03-13 11:50:09', 272, 171)," \
           "('2017-03-13 11:50:09', 277, 171)"
record = fileName.split(",")
print(record)