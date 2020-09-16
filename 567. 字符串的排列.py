"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-in-string
"""


class Solution_force:
    """
    date:2020.9.16
    author:fenghao
    思路：
        朴素解法
        <1 枚举s1字符的所有排列组合的字符串
        <2 判断字符串是否在s2中
    时间复杂度：O(n!)  n是s1的长度
    空间复杂度：O(n)
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass


class Solution:
    """
    date:2020.9.16
    author:fenghao
    思路：
        # 滑窗
        #     z注意：
        #         需要字符是连续的
        #     算法步骤：
        #         1、先移动右指针，直到窗口满足条件
        #         2、然后，移动左指针，直到窗口不满足条件，
        #         3、记录刚刚好满足条件的窗口（记录“局部最优解”）
        #         4、判断右指针是否已经到尾部，否则继续前面的3个步骤
        不需要用滑窗，不要死搬硬套
        一个指针遍历，同时维护一个缓存记录子串的状态。这里没有用双指针
            1、遇到非s1字符，清空缓存
            2、遇到s1字符，且个数未溢出，缓存增加1，并判断是否满足要求
            3、遇到s1字符，但个数溢出，清空缓存，缓存增加1

    时间复杂度：O(n)  n是s2的长度
    空间复杂度：O(n)  n是s1的长度
    """

    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 构建s1的“字符频次字典”
        s1_count_dict = dict()
        for char in s1:
            s1_count_dict[char] = s1.count(char)

        # 构建窗口“字符频次字典”
        window_count_dict = dict()

        len_window_s1 = 0  # 窗口中含有s1字符的个数.用于判断是否满足要求
        len_s1 = len(s1)
        for char in s2:
            if char in s1:
                if char not in window_count_dict:
                    window_count_dict[char] = 1
                    len_window_s1 += 1
                    if len_window_s1 == len_s1:
                        return True
                else:
                    if window_count_dict[char] < s1_count_dict[char]:
                        window_count_dict[char] += 1
                        len_window_s1 += 1
                        if len_window_s1 == len_s1:
                            return True
                    else:
                        window_count_dict = dict()  # 清空缓存   bug
                        window_count_dict[char] = 1
                        len_window_s1 = 1
            else:
                window_count_dict = dict()  # 清空缓存
                len_window_s1 = 0
        return False


# s1 = "ab"
# s2 = "eidbaooo"
# s2 = "eidboaoo"

s1 = "adc"
s2 = "dcda"

my_sol = Solution()
print(my_sol.checkInclusion(s1, s2))