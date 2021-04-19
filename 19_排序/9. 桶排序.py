"""
桶排序
"""


def bucket_sort(nums, bucketSize):
    """
    author:https://zhuanlan.zhihu.com/p/120833227
    date:2021.4.19
    """
    if len(nums) < 2:
        return nums
    _min = min(nums)
    _max = max(nums)
    # 需要桶个数
    bucketNum = (_max - _min) // bucketSize + 1
    buckets = [[] for _ in range(bucketNum)]
    for num in nums:
        # 放入相应的桶中
        buckets[(num - _min) // bucketSize].append(num)
    res = []

    for bucket in buckets:
        if not bucket: continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            # 当都装在一个桶里,说明桶容量大了
            if bucketNum == 1:
                bucketSize -= 1
            res.extend(bucket_sort(bucket, bucketSize))
    return res


if __name__ == "__main__":
    nums = [54, 36, 12, 29, 50, 12, 54]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', bucket_sort(nums, 5)))
