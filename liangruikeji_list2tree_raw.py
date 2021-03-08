#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Tested with : Python 3.7.0
# Created date : Mar 5, 2021
import copy


def convert_format(input_list):
    """
    功能：将列表转换为树状结构
    思路：第一次遍历先找到根节点（可多个）。。。遍历查找以上一次节点为父节点的节点，即从根节点向叶子节点方向遍历
          注意，为降低时间复杂度，每次遍历就去除捕获到的节点，并记忆上一层的节点
    时间复杂度：O(h) h为遍历次数，树的高度
    空间复杂度：O(n)
    """
    nodes_list = copy.deepcopy(input_list)  # 不修改入参
    ret = dict()

    parent_nodes = []   # 记忆上一次遍历的节点
    # 查找根节点（可多个）
    for item in nodes_list:
        if "parent" not in item.keys():
            name = item["name"]
            parent_nodes.append(name)
            ret[name] = {}
            nodes_list.remove(item)
    # 遍历查找非根节点
    while len(nodes_list) != 0:
        new_parent_nodes = []
        for item in nodes_list:
            parent = item["parent"]
            name = item["name"]
            if parent in parent_nodes:
                parent_nodes[name] = {}
                new_parent_nodes.append(parent_nodes[name])
        parent_nodes = new_parent_nodes

    return ret

input_list = [
    {
        "parent": "交易所",
        "name": "中国外汇交易中心"
    },
    {
        "name": "交易所"
    },
    {
        "parent": "交易所",
        "name": "聚合交易所",
    },
    {
        "parent": "交易所",
        "name": "森浦Quebee",
    },
    {
        "name": "交易模式"
    },
    {
        "parent": "交易模式",
        "name": "报价驱动模式",
    },
    {
        "parent": "报价驱动模式",
        "name": "可执行持续报价(ESP)",
    }
]
output = convert_format(input_list)
expect = {
    "交易所": {
        "中国外汇交易中心": {},
        "聚合交易所": {},
        "森浦Quebee": {}
    },
    "交易模式": {
        "报价驱动模式": {
            "可执行持续报价(ESP)": {}
        }
    }
}
assert (output == expect)
