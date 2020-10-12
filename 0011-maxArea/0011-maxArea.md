## LeetCode第11号问题：盛水最多的容器

**本题选自leetcode的第11题，medium级别**

**题目描述：**

```txt
给你n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i,ai)。在坐标内画n条垂直线，
垂直线i的两个端点分别为(i,ai)和(i,0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且n的值至少为2。
示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
```

我们都应该听说过**木桶原理**，一个木桶可以装入多少水取决于最短的那块板；而这道题也可以与木桶装水的问题对应上。
 很容易的可以得到---->**容器可以容纳水的容量=两条垂直线中最短的那条*两条线之间的距离**
 现在的情况是，有很多条线，让你计算两两之间能装的最多的水，其实暴力法之间就能解决这个问题，但是它的时间复杂度也达到了**O(n^2)**

ok，那我们先试试用**暴力法**来解 决问题：

### 1.暴力法

直接上代码：

```java
public int maxArea(int[] height) {
    int res = 0;
    for(int i = 0;i < height.length;i++){
      for(int j = i+1;j < height.length;j++){
        int temp = Math.min(height[i],height[j]) * (j-i);
        res = Math.max(res,temp);
      }
    }
    return res;
}
```

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        temp = 0
        for i in range(len(height)):
            for j in range(1,len(height)):
                area = (j-i)*min(height[i],height[j])
                if temp<area:
                    temp = area
        return temp
```

暴力法是可以通过测试的，但是可以看到**程序执行用时**并不理想

```
执行用时 :440 ms, 在所有 Java 提交中击败了17.44% 的用户
内存消耗 :39.9 MB, 在所有 Java 提交中击败了37.86%的用户
```

### 2.双指针

思路：使用两个指针（**resource**和**last**）分别指向数组的第一个元素和最后一个元素，然后我们计算这两条“线”之间能容纳的水的容量，并更新最大容量（初始值为0）；接着我们需要将指向元素值小的那个指针前移一步，然后重复上面的步骤，直到**resource = last**循环截止。

双指针代表了什么？

**双指针代表的是 可以作为容器边界的所有位置的范围**。在一开始，双指针指向数组的左右边界，表示 数组中所有的位置都可以作为容器的边界，因为我们还没有进行过任何尝试。在这之后，我们每次将对应的数字较小的那个指针往另一个指针的方向移动一个位置，就表示我们认为这个指针不可能再作为容器的边界了。

为什么对应的数字较小的那个指针不可能再作为容器的边界了？

在上面的分析部分，我们对这个问题有了一点初步的想法。这里我们定量地进行证明。

考虑第一步，假设当前左指针和右指针指向的数分别为 $x$ 和 $y$，不失一般性，我们假设 $x\leq y$。同时，两个指针之间的距离为 $t$。那么，它们组成的容器的容量为：
$$
\min(x, y) * t = x * t
$$
我们可以断定，如果我们保持左指针的位置不变，那么无论右指针在哪里，这个容器的容量都不会超过 $x * t$ 了。注意这里右指针只能向左移动，因为我们考虑的是第一步，也就是指针还指向数组的左右边界的时候。

我们任意向左移动右指针，指向的数为$ y_1$ ，两个指针之间的距离为 $t_1$。那么显然有 $t_1 < t$，并且$ \min(x, y_1) \leq \min(x, y)$

如果 $y_1 \leq y$，那么 $\min(x, y_1) \leq \min(x, y)$

如果 $ y_1 > y$，那么$ \min(x, y_1) = x = \min(x, y)$

因此有：

$$
\min(x, y_t) * t_1 < \min(x, y) * t
$$
即**无论我们怎么移动右指针，得到的容器的容量都小于移动前容器的容量**。也就是说，**这个左指针对应的数不会作为容器的边界了，那么我们就可以丢弃这个位置，将左指针向右移动一个位置，此时新的左指针于原先的右指针之间的左右位置，才可能会作为容器的边界**。

这样以来，我们将问题的规模减小了$1$，被我们丢弃的那个位置就相当于消失了。此时的左右指针，就指向了一个新的、规模减少了的问题的数组的左右边界，因此，我们可以继续像之前 考虑第一步那样考虑这个问题：

求出当前双指针对应的容器的容量；

对应数字较小的那个指针以后不可能作为容器的边界了，将其丢弃，并移动对应的指针。

最后的答案是什么？

答案就是我们每次以双指针为左右边界（也就是「数组」的左右边界）计算出的容量中的最大值。

**GIF动画演示：**

![maxArea](F:\project\leetcode\0011-maxArea\maxArea.gif)

**来看看代码：**

**java实现**

```java
public int maxArea(int[] height) {
    int resource = 0;
    int last = height.length - 1;
    int res = 0;
    while (resource < last) {
        if (height[resource] >= height[last]) {
            res = Math.max(res, (last - resource) * height[last]);
            last--;
        } else {
            res = Math.max(res, (last - resource) * height[resource]);
            resource++;
        }
    }
    return res;
}
```

**python实现**

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, result = 0, 0
        right = len(height) - 1

        while(left<right):

            temp = min(height[left],height[right])*(right-left)
            result = max(temp,result)
            if height[left]<height[right]:
                left = left + 1
            else:
                right = right - 1
        return result
```

**C++实现**

```c++
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left,result, temp;
        left = result = temp = 0;
        int right = height.size()-1;
        while(left<right){
            temp = min(height[left],height[right])*(right-left);
            result = max(result,temp);
            height[left]<height[right]?left++:right--;
        }
        return result;
    };
};
```



**可以很明显的看到，虽然内存消耗两者是差不多的，但是双指针的速度比暴力解法的速度可是高出好多倍。**

时间复杂度：**O(n)**	空间复杂度：**O(1)**

```
执行用时 :3 ms, 在所有 Java 提交中击败了92.69% 的用户
内存消耗 :40.3 MB, 在所有 Java 提交中击败了7.86%的用户
```

[视频演示](../0011-maxArea/maxArea.mp4)