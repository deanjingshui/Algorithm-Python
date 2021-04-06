"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
"""


class Solution:
    """
    author；fenghao
    date:2021.4.6
    思路：双指针对撞
         注意：题目要求“只考虑字母和数字字符”，故对特殊字符需要跳过
    考点：语言中常用字符（串）相关 API 的使用：s.isalnum(), s.capitalize()
    时间：O(n)
    空间：O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            while left < n and not s[left].isalnum():   # 注：2个逻辑判断的先后顺序，互换会出现index out of range错误
                left += 1
            while right > -1 and not s[right].isalnum():
                right -= 1
            if left > right:  # 说明没有一个字母和数字
                return True
            elif s[left].capitalize() != s[right].capitalize():
                return False
            else:
                left += 1
                right -= 1
        return True


# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = ",,,, ?"
my_sol = Solution()
print(my_sol.isPalindrome(s))
