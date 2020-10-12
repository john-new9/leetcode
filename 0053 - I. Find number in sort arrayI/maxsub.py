def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return maxSum(nums, 0, len(nums))

def maxSum(nums, lo, hi):

    mi = (lo + hi) // 2
    if (hi - lo ==1):
        return nums[lo]

    reL = nums[mi - 1]
    i = mi - 1
    temp = 0
    while (lo <= i):
        temp += nums[i]
        if reL < temp:
            reL = temp
        i -= 1

    reR = nums[mi]
    j = mi
    temp1 = 0
    while (j < hi):
        temp1 += nums[j]
        if reR < temp1:
            reR = temp1
        j += 1
    return max(reR + reL, max(maxSum(nums, lo, mi), maxSum(nums, mi, hi)))

arr = [2,0,3,-2]
print(maxSubArray(arr))