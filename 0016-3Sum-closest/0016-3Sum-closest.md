# LeetCode 第 16 号问题：最接近的三数之和

### 题目描述

给定一个包括 *n* 个整数的数组 `nums` 和 一个目标值 `target`。找出 `nums` 中的三个整数，使得它们的和与 `target` 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

**示例：**

```
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
```

### 题目解析

本题目与15题类似，采用`升序数组`+`双指针方法`

### 算法流程

1. 特判，对于数组长度n，如果数组为null，或者数组长度小于 3，返回null。
2. 对数组进行排序。
3. 遍历排序后数组：
   - 对于第一重遍历：选取第一个数，确定左右指针left与right
   - 计算sum_val = nums[i]+nums[left]+nums[right]
   - **存储结果：**每次根据abs(sum_val-target)的大小，选取最小值动态更新结果res
   - **控制移动：**1.sum_val小于target，left+=1；2.sum_val大于target，right-=1

### 代码实现

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[0:3])     # res的初始化

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while(left<right):
                sum_val = nums[i] + nums[left] + nums[right]
            
                if abs(res-target) > abs(sum_val-target):    # 随时进行更新
                    res = sum_val
                if sum_val == target:    # 控制移动：正好两者相等
                    return sum_val
                elif sum_val<target:    # 控制移动：和小于目标值
                    left +=1
                else:    # 控制移动：和大于目标值
                    right-=1
        return res
```
