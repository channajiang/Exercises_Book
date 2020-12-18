"""'
KiKi学会了printf在屏幕输出信息，他想输出一架小飞机。请帮他编写程序输出这架小飞机。


"""

# 4 行 12列

for i in range(6):
    str = ' '
    for j in range(12):
        if i in range(2) and j in range(5, 7):
            str += '*'
        elif i in range(2, 4):
            str += '*'
        elif i in range(4, 6) and (j == 4 or j == 7):
            str += '*'
        else:
            str += ' '

        str += ''
    print(str)
