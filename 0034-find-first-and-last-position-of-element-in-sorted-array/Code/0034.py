def binsearch(nums, target, lo, hi):
    while(lo<hi):
        mi = (lo + hi) // 2
        if (target<nums[mi]):
            hi = mi
        else:
            lo = mi+1
    right = lo-1
    if nums[right] != target:
        return [-1,-1]
    left = right

    while(left>=0 and nums[right]==nums[left]):
        left-=1
    return [left+1, right]


# nums = [1,3,4,5,5,8,9,10]
# target = 5

nums = [2]
target = 1

# nums = [1,1]
# target = 1

if len(nums)==0:
    print([-1,-1])
else:
    print(binsearch(nums, target, 0, len(nums)))
