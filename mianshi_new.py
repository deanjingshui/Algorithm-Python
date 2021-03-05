#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Tested with : Python 3.7.0
# Created date : Mar 5, 2021


def convert_format(_input_list):
    """
    将列表转换为树状结构
    """
    result = {}
    root_list = map(lambda x: x['name'], filter(lambda x: 'parent' not in x, _input_list))
    for root in root_list:
        node = find_node(root, _input_list)
        if root in node:
            result[root] = node[root]
    return result


def find_node(parent, _input_list):
    data = {}
    for node in _input_list:
        if 'parent' in node and node['parent'] == parent:
            nodes = find_node(node['name'], _input_list)
            if parent not in data:
                data[parent] = {}
            if node['name'] in nodes:
                data[parent][node['name']] = nodes.get(node['name'])
            else:
                data[parent][node['name']] = nodes
    return data


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
