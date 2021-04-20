"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
"""


def convertToTitle(num):
    """
    ASCII  1--->498  A--->65
    """
    result = ""
    mapping = dict()
    for i in range(1, 26):
        mapping[i] = chr(i+64)
    while num > 26:
        num, mod = divmod(num, 26)
        result = mapping[mod] + result  # 倒叙
    if mod == 0:
        result += 'Z'
    return result


num = 1
print(convertToTitle(num))
