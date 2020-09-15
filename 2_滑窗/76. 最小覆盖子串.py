"""
给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。


示例：

输入：S = "ADOBECODEBANC", T = "ABC"
输出："BANC"
 

提示：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
"""


class Solution_sliding_window:
    """
    date:2020.9.14
    author:fenghao
    思路：滑窗
        关键点如下
        <1 窗口是一个试图包含 T 字符的字符串
        <2 维护一个字典，保存每个 T 中字符出现的最右侧的位置   {A:index_A, B:[index_B_1, index_B_2], C:index_C}
        <3 字典中位置根据滑过字符，当字符是 T 中字符时，更新字典
        <4 同时判断是否收集齐 T 中的字符，如果收集齐，计算一次当前窗口的长度，如果比之前小就更新一下结果

        S = "aa"
        T = "aa"
        预期结果是 "aa"，不是"a"，即重复的字符不算做一个字符
        故当T = "ABBC", mapping 的结构类似 {A:index_A, B:[index_B_1, index_B_2], C:index_C}


    时间复杂度：O(n)  1828 ms
    """
    def minWindow(self, s: str, t: str) -> str:
        len_t = len(t)
        result = s
        left = right = 0  # 窗口的左右端
        mapping = {}
        len_mapping = 0
        for index, char in enumerate(s):
            if char in t:
                if char in mapping:        # 如果窗口中已有该字符，需要更新位置
                    if len(mapping[char]) == t.count(char):
                        mapping[char].pop(0)
                    mapping[char].append(index)
                else:
                    mapping[char] = [index]

                left = mapping[list(mapping.keys())[0]][0]
                right = index
                len_mapping = 0
                for char in mapping:   # 待优化点：计算收集到的字符的个数；计算左指针
                    len_mapping += len(mapping[char])
                    left = min(left, mapping[char][0])
                if len_mapping == len_t:  # 如果字符集齐，需要更新结果
                    result = s[left: right+1] if right - left + 1 < len(result) else result
        if len_mapping < len_t:
            return ""
        return result


class Solution_sliding_window_optimize:
    """
    date:2020.9.14
    author:fenghao
    思路：滑窗     {A:index_A, B:[index_B_1, index_B_2], C:index_C}
          优化，提高效率

          效率提升的难点，左指针left的更新
          目标 ABBC
          B A B   此时left指向第一个B
          B A B B 此时left指针需要指向A


    时间复杂度：O(n*m)   924ms
    """
    def minWindow(self, s: str, t: str) -> str:
        len_t = len(t)
        result = s
        left = right = 0  # 窗口的左右端
        mapping = {}
        len_mapping = 0
        t_count = {}
        for char in t:     # t中字符出现的频次
            t_count[char] = t.count(char)
        for index, char in enumerate(s):
            if char in t:
                if char in mapping:        # 如果窗口中已有该字符，需要更新位置
                    if len(mapping[char]) == t_count[char]:
                        mapping[char].pop(0)
                        len_mapping -= 1
                    mapping[char].append(index)
                    # 更新left指针
                    tmp = mapping[list(mapping.keys())[0]][0]
                    for i in mapping:       # 低效
                        tmp = min(tmp, mapping[i][0])
                    left = tmp
                else:
                    mapping[char] = [index]
                    left = index if len_mapping == 0 else left
                len_mapping += 1

                right = index
                if len_mapping == len_t:  # 如果字符集齐，需要更新结果
                    result = s[left: right+1] if right - left + 1 < len(result) else result
        if len_mapping < len_t:
            return ""
        return result


class Solution_sliding_window_optimize_2:
    """
    date:2020.9.14
    author:fenghao
    思路：滑窗     {A:index_A, B:[index_B_1, index_B_2], C:index_C} (删)
          优化，提高效率

          效率提升的难点，左指针left的更新
          目标 ABBC
          B A B   此时left指向第一个B
          B A B B 此时left指针需要指向A

          同时使用3种数据机构：
            <1  字典      window_count_dict        窗口中t字符包含的个数 {A:1, B:2}
            <2  字典列表  window_dict_list      窗口中t字符出现的顺序，并带有索引映射关系 [{A:1}, {B:2}, {B:3}]   可方便的获得left指针
            <3  列表      window_list         窗口中t字符出现的顺序，[A,B,B]

    时间复杂度：O()   1336ms
    """
    def minWindow(self, s: str, t: str) -> str:
        len_t = len(t)
        result = s
        left = right = 0  # 窗口的左右端
        t_count = {}
        for char in t:     # t中字符出现的频次
            t_count[char] = t.count(char)

        len_mapping = 0
        window_count_dict = {}   # {A:1, B:2}
        window_dict_list = []    # [{A:1}, {B:2}, {B:3}]
        window_list = []         # [A,B,B]
        for index, char in enumerate(s):
            if char in t:
                if char in window_count_dict:        # 如果窗口中已有该字符，需要更新位置
                    if window_count_dict[char] == t_count[char]:
                        # 将栈中第一个char删除
                        char_remove_index = window_list.index(char)
                        window_list.remove(char)
                        window_dict_list.pop(char_remove_index)
                        len_mapping -= 1
                        window_count_dict[char] -= 1
                    window_count_dict[char] += 1
                else:
                    window_count_dict[char] = 1
                window_list.append(char)
                window_dict_list.append({char: index})
                len_mapping += 1

                if len_mapping == len_t:  # 如果字符集齐，需要更新结果
                    # 更新指针
                    left = window_dict_list[0][list(window_dict_list[0].keys())[0]]
                    right = index
                    result = s[left: right+1] if right - left + 1 < len(result) else result
        if len_mapping < len_t:
            return ""
        return result


class Solution_sliding_window_leetcode:
    """
    date:2020.9.15
    author:力扣 + fenghao
    思路：滑窗
        https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/

        滑窗算法的关键点：
            双指针（对应滑窗的左右边界）
            选择合适的数据结构记录滑窗的关键特征

        算法步骤：
            1、先移动右指针，直到窗口满足条件
            2、然后，移动左指针，直到窗口不满足条件，
            3、记录刚刚好满足条件的窗口（记录“局部最优解”）
            4、判断右指针是否已经到尾部，否则继续前面的3个步骤
        如何判断窗口满足条件？需要选择合适的数据结构来存储滑窗的“关键特征”
            统计t的字符个数(len_window_t)，当len_window_t等于t的字符个数len_t时，满足条件。注意处理窗口中多余的t字符，比如目标ABBC 当滑窗含有超过2个B时，还算2个
        构建2个数据结构：
            t每个字符的出现频次          t_count_dict       {A:1, B:2, C:1}
            窗口中的t每次字符出现频次    window_count_dict  {A:1, B:2}
            注：推荐看官方解法视频，提到了“词频数组”

    时间复杂度：O(n)   192ms
    """

    def minWindow(self, s: str, t: str) -> str:

        result = ""
        len_s = len(s)
        len_t = len(t)
        len_window_t = 0    # 统计窗口中t字符个数，超出的个数不累计
        t_count_dict = {}   # t中字符出现的频次  {A:1, B:2, C:1}
        for char in t:
            t_count_dict[char] = t.count(char)

        window_count_dict = {}   # 窗口中t字符出现频次  {A:1, B:2}
        left = right = 0         # 窗口的左右指针
        while right < len_s:
            # 右指针右移，直到窗口满足条件
            while len_window_t != len_t and right < len_s:
                char = s[right]
                if char in t:
                    if char in window_count_dict:
                        window_count_dict[char] += 1
                    else:
                        window_count_dict[char] = 1
                    if window_count_dict[char] < t_count_dict[char] + 1:
                        len_window_t += 1
                right += 1

            # 若窗口满足条件，左指针右移
            if len_window_t == len_t:
                while len_window_t == len_t:
                    char = s[left]
                    if char in t:
                        window_count_dict[char] -= 1
                        if window_count_dict[char] < t_count_dict[char]:
                            len_window_t -= 1
                    left += 1

                # 记录当前满足要求时的滑窗（记录当前“局部最优解”）
                tmp = s[left-1: right]
                result = tmp if len(tmp) < len(result) or len(result) == 0 else result

        return result


# S = "ADOBECODEBANC"
# T = "ABC"
S = "a"
T = "aa"
# S = "cabefgecdaecf"
# T = "cae"

my_sol = Solution_sliding_window_leetcode()
print(my_sol.minWindow(S, T))
