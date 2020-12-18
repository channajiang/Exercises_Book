# def putInfoToDict(fileName):
#     record = list(fileName)
#     dic = {}
#     for element in record:
#         print(element)
#         print("checkTime: %s " % element[0])
#         # print("lessonid: %d " % element[1])
#         # print("studentid: %d " % element[2])
#         list = ["lessonid: %d " % element[1],"checkTime: %s " % element[0]]
#         print(list)
#         if element[0] not in dic:
#             dic[element[2]] = list
#         else:
#             dic[element[2]]= list.extend(list)
#
#     return dic
#
# if __name__ == '__main__':
#     fileName = "('2017-03-13 11:50:09', 271, 131), " \
#                "('2017-03-13 11:50:09', 271, 171)," \
#                "('2017-03-13 11:50:09', 278, 171)"
#     print(putInfoToDict(fileName))

# fileName = "('2017-03-13 11:50:09', 271, 131), " \
#            "('2017-03-13 11:50:09', 271, 171)," \
#            "('2017-03-13 11:50:09', 278, 171)"
# print(list(fileName))
# #
# list = []
# a = {'a': 1, 'b': 2}
# list.append(a)
# print(list)


import re


def putInfoToDict(fileName):
    dic = {}
    dict_list = []
    e_list = []
    f_list = []
    for i in range(len(fileName)):
        key_01 = "lessonid"
        key_00 = "checkTime"
        small_dict_vlaue = {key_01: fileName[i][1], key_00: fileName[i][0]}
        # dic = {fileName[i][2]: small_dict_vlaue}
        # print(dic)
        dict_list.append(small_dict_vlaue)
        print(dict_list)
        if fileName[i][2] not in dic:
            dic[fileName[i][2]] = [dict_list[i]]
        else:
            f_list.append(dic[fileName[i][2]])
            f_list.append(dict_list[i])
            dic[fileName[i][2]] = f_list
    return dic


if __name__ == '__main__':
    fileName = [('2017-03-13 11:50:09', 271, 131),
                ('2017-03-13 11:50:09', 272, 171),
                ('2017-03-13 11:50:09', 277, 171),
                ('2017-03-13 11:50:09', 277, 171)]
    print(putInfoToDict(fileName))
