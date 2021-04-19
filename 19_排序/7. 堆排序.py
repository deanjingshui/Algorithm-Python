"""
堆排序
"""

import heapq


def heap_sort(nums):
    result = list()
    heapq.heapify(nums)
    while nums:
        num = heapq.heappop(nums)
        result.append(num)
    return result


if __name__ == "__main__":
    nums = [54, 36, 12, 29, 50]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', heap_sort(nums)))
