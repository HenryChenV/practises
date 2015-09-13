#!/usr/bin/env python
#-*-encoding=utf-8-*-

'''
有四个数组,每个数组的元素都包含1到13个数,
从每个数组里随便选4个数字(有些数可能重复),
通过+-*/(),生成结果为24的等式.
比如3+4+4+13,(有些组合可能没有结果),操作加减乘除和括号都可以重复。
'''


from itertools import combinations, combinations_with_replacement


def calculate(num_list, op_list, result=24):
    expression = '((' + num_list[0] + op_list[0] + num_list[1] + ')' + \
            op_list[1] + num_list[2] + ')' + op_list[2] + num_list[3]
    if eval(expression) == result:
        return expression


def getAllCom():
    nums = combinations(range(1, 14), 4)
    nums = [[str(j) for j in i] for i in nums]
    ops = list(combinations_with_replacement('+-*/', 3))
    return [calculate(i, j) for i in nums for j in ops if calculate(i, j)]


if __name__ == '__main__':
    print getAllCom()
