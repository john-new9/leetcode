# LeetCode 第 1 号问题：两数之和

题目来源于 LeetCode 上第 1 号问题：两数之和。题目难度为 Easy 。

### 题目描述

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例:**

```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

### 题目解析

使用查找表来解决该问题。

设置一个 map 容器 record 用来记录元素的值与索引，然后遍历数组 nums。

* 每次遍历时使用临时变量 complement 用来保存目标值与当前值的差值
* 在此次遍历中查找 record ，查看是否有与 complement 一致的值，如果查找成功则返回查找值的索引值与当前变量的值 i
* 如果未找到，则在 record 保存该元素与索引值 i

### 动画描述

![Animation](F:\project\leetcode\0001-Two-Sum\Animation.gif)

### 代码实现

**java实现**

```java
// 1. Two Sum
// https://leetcode.com/problems/two-sum/description/
// 时间复杂度：O(n)
// 空间复杂度：O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> record;
        for(int i = 0 ; i < nums.size() ; i ++){
       
            int complement = target - nums[i];
            if(record.find(complement) != record.end()){
                int res[] = {i, record[complement]};
                return vector<int>(res, res + 2);
            }

            record[nums[i]] = i;
        }
        return {};
    }
};
```

**python实现**

使用哈希表（字典）进行查找。仅需进行一遍遍历，时间复杂度为O(n)。

对原始数组nums进行遍历时，记录当前与target的差值为another_num，之后判断字典中有没有该key，如果没有将another_num作为key，index作为value存储到字典中，如果有的话，则返回其value值。

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
```

**C++实现**

使用哈希表（map）进行查找。仅需进行一遍遍历，时间复杂度为O(n)。

对原始数组nums进行遍历时，记录当前与target的差值为another_num，之后判断map中有没有该key，如果没有将another_num作为key，index作为value存储到map中，如果有的话，则返回其value值。

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> hashmap;//提供一对一的hash，数据结构hashmap
        vector<int> result(2,-1);//用来承载结果，初始化一个大小为2，值为-1的容器
        for(int i=0;i<nums.size();i++)
        {	
            if(hashmap.count(target-nums[i])>0)  // 查找target-nums[i]出现次数
            {
                result[0]=hashmap[target-nums[i]];
                result[1]=i;
                break;
            }
            hashmap[nums[i]]=i;  //反过来放入map中，为了获取结果下标
        }
        return result;
    };
};
```

