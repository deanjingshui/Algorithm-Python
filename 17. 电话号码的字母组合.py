"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

字符串、回溯算法

"""
from typing import List
from copy import deepcopy


class Solution:
    """
    author:fenghao
    date:2020.7.12
    """
    def __init__(self):
        self.mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        for index, num in enumerate(digits):
            chars = self.mapping[num]
            if index == 0:
                ret.extend(list(chars))
            else:
                ret_tmp = deepcopy(ret)
                ret = []
                for i in ret_tmp:
                    for char in chars:
                        ret.append(i+char)
        return ret


class Solution:
    """
    author:fenghao
    date:2020.7.12
    思路：多叉树
    """


test_1 = "23"
my_sol = Solution()
print(my_sol.letterCombinations(test_1))


test_1 = "2"
my_sol = Solution()
print(my_sol.letterCombinations(test_1))


test_1 = "232"
my_sol = Solution()
print(my_sol.letterCombinations(test_1))
print(len(my_sol.letterCombinations(test_1)))

test_1 = "239"
my_sol = Solution()
print(my_sol.letterCombinations(test_1))
print(len(my_sol.letterCombinations(test_1)))
