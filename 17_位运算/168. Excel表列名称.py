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


def convertToTitle(columnNumber: int)-> str:
    """
    author:fenghao
    date:2021.4.20
    思路：本质是26进制
         另外，还考察了ASCII表： A--->65
    结果：大用例错误  num = 701
    """
    result = ""
    mapping = dict()
    for i in range(1, 27):
        mapping[i] = chr(i+64)
    while columnNumber > 0:
        columnNumber, mod = divmod(columnNumber, 26)
        if mod != 0:
            result = mapping[mod] + result  # 倒序
    return result


def convertToTitle_leetcode(columnNumber: int)-> str:
    """
    author:leetcode
    date:2021.4.20
    思路：
    """
    result = ""
    while columnNumber > 0:
        columnNumber -= 1
        columnNumber, mod = divmod(columnNumber, 26)
        result = chr(mod+65) + result  # 倒序
    return result

# num = 1
# num = 27     # AA
# num = 28     # AB
num = 701      # AY ？ ZY
print(convertToTitle(num))
print(convertToTitle_leetcode(num))
