"""
https://www.nowcoder.com/practice/c178e3f5cc4641dfbc8b020ae79e2b71?tpId=107&&tqId=33319&rp=1&ru=/ta/beginner-programmers&qru=/ta/beginner-programmers/question-ranking
变种水仙花数 - Lily Number：把任意的数字，从中间拆分成两个数字，比如1461 可以拆分成（1和461）,（14和61）,（146和1),如果所有拆分后的乘积之和等于自身，则是一个Lily Number。

例如：

655 = 6 * 55 + 65 * 5

1461 = 1*461 + 14*61 + 146*1

求出 5位数中的所有 Lily Number。
"""

class Solution:
    def LilyNumber(self):
        res = []
        for num in range(10000, 100000):
            sum1 = 0
            for i in range(1, 5):
                sum_1 = num % (10 ** i)
                print(sum_1)
                sum_2 = (num // 10 ** i)
                print(sum_2)
                sum_3 = num % (10 ** i) * (num // 10 ** i)
                print(sum_3)
                sum1 = sum1 + num % (10 ** i) * (num // 10 ** i)
            if sum1 == num:
                res.append(num)
        for x in res:
            print(x, end=' ')


if __name__ == '__main__':
    num = 655
    d = Solution()
    d.LilyNumber()
