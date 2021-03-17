"""
面试
2021.3.17 蚂蚁集团-资深测试工程师/专家

判断一个字符串，能否通过一个字符的变更（增删改），变成另一个给定的字符串
输入：xyz, xz  输出
true
输入：xyz, xyyz  输出
true
输入：xyz, xyx  输出
true
输入：xyz, xxx  输出
false

"""


def judge_two_strs(str1, str2):
    """
    author: 面试官提示 + fenghao
    date:2021.3.17
    思路：
        两个指针分别指向两个字符串的头部
        删除和增加的判断逻辑类似
    """
    str1_len = len(str1)
    str2_len = len(str2)
    if abs(str1_len - str2_len) > 1:
        return False
    elif str1_len == str2_len:
        diff_count = 0
        for index in range(str1_len):
            if str1[index] != str2[index]:
                diff_count += 1
        if diff_count > 1:
            return False
    else:
        diff_count = 0
        str_long = str1 if str1_len > str2_len else str2
        str_short = str2 if str1_len > str2_len else str1
        short_len = len(str_short)
        for index in range(short_len):
            if str_long[index + diff_count] != str_short[index]:
                diff_count += 1
        if diff_count > 1:
            return False
    return True


str1 = "xyz"
str2 = "xz"
print(judge_two_strs(str1, str2))

str1 = "xyz"
str2 = "xyyz"
print(judge_two_strs(str1, str2))

str1 = "xyz"
str2 = "xyx"
print(judge_two_strs(str1, str2))

str1 = "xyz"
str2 = "xxx"
print(judge_two_strs(str1, str2))