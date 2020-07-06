import numpy as np


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        temp = target-nums[i]
        if temp in nums and nums.index(temp) != i:
            return [i,nums.index(temp)]
        else:
            continue
    return []


if __name__ == '__main__':
    nums= [5,3,4,2]
    target = 10

    print(twoSum(nums, target))

