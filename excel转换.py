"""
将数字转换为excel字母表头
A B C D ... Z. AA AB AC .... AZ BA BB BC ... BZ CA... ZZZ ..

1  -> A
2 -> B
26 -> Z
27 -> AA
....
10000 -> ZZZB
"""


def trans(num):
    result = ""
    mapping = dict()
    for i in range(26):
        mapping[i] = ord(i)
    while num > 26:
        num, other = divmod(num, 26)
        result += mapping[other]
    if other == 0:
        result += 'Z'
    return result



a = [[]]*3
a[1].append(1)
print(a)