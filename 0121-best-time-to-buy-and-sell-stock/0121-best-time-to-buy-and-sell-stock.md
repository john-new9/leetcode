# LeetCode 第 121 号问题：买卖股票的最佳时机

题目来源于 LeetCode 上第 121 号问题：买卖股票的最佳时机。题目难度为 Easy


### 题目描述

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 5
```

解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

**示例 2:**

```
输入: [7,6,4,3,1]
输出: 0
```

解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

### 题目解析

股票问题的方法就是 **动态规划**，因为它包含了重叠子问题，**即买卖股票的最佳时机是由之前买或不买的状态决定的，而之前买或不买又由更早的状态决定的...** 这种动态问题，很容易想到动态规划实现。

#### 动态规划

给定一个数组，去求最大值-最小值。**前提是：最大值的索引应该比最小值的索引要大。**

该题目显然可以用动态规划来解，可以参考Leetcode第53题，最长子序和。

* 定义一个新的数组，数组元素代表在当前时刻卖出能够获得的最大收益。

* 显然，当前元素可能取值：①在之前时刻卖出，获得更大收益，②在当前时刻卖出，price[i]减去前面时刻price的最小值

* 状态递推方程

  ```python
  dp[i] = max(dp[i-1], price[i]-minprice)
  # minprice:代表[0:i]的最小价格
  # dp[i]代表在第i天卖出时，获得的最大利益
  ```

##### 实现

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        minprice = prices[0]
        profit = [0]*len(prices)

        for i in range(1,len(prices)):
            minprice = min(minprice, prices[i])
            profit[i] = max(profit[i-1],prices[i]-minprice)
        return max(profit)
```

##### 复杂度分析

时空复杂度从代码中都清晰可见，一次遍历。时间复杂度：$\mathcal{O}(n)$， 空间复杂度：$\mathcal{O}(1)$

由于本题只有一笔交易（买入卖出），因此除了动态规划，我们还可以使用更加简便的方法实现。

#### 一次遍历

遍历一遍数组，计算每次 **到当天为止** 的**最小股票价格**和最大利润。

<img src="https://pic.leetcode-cn.com/4eaadab491f2bf88639d66c9d51bb0115e694ae08d637841ac18172b631cb21f-0121.gif" alt="img" style="zoom:50%;" />

此处需要注意：**最小股票价格需要通过跟随遍历元素进行比较**，更新。

为了防止出现输入: [7,6,4,3,1]即股票一直跌落的情况，**需要将maxprofit初始值设置为0，**这样能保证最小的收益为0。

##### 实现

```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        minprice = prices[0]    # 最小价格, 每次都会更新
        maxprofit = 0    # 最大利润, 不允许亏损

        for i in range(0,len(prices)):
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit, prices[i]-minprice)
        return maxprofit
```

##### 复杂度分析

- 时间复杂度：$\mathcal{O}(n)$。
- 空间复杂度：$\mathcal{O}(n)$。