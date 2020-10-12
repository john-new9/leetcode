## LeetCode第1143号问题：最长公共子序列

题目描述

```txt
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。
```

### 题目分析
![image-20200812183419882](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200812183419882.png)

注意：子序列必须按照原相对次序构成。

### 解法分析

> **方法一：递归+减而治之，递归+分而治之**

对于序列A[0,n)与B[0,m)来讲，要求LCS(n,m):

- 若n=-1 或 m=-1，则取空序列("")      //递归基
- 若A[n-1]='X'=B[m-1]，则减而治之，把最后一个元素截取掉，取LCS(n-1,m-1)+1
  - ![image-20200812184312775](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200812184312775.png)
- 若A[n-1]!=B[m-1]，则分而治之。
  - ![image-20200812184349464](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200812184349464.png)
  - 分为两种情况 ①Y对整个公共序列没有贡献，则将Y截取掉，即LCS(n,m-1) ②Y对整个公共序列有贡献，则X一定不会有贡献，则将X截取掉，即LCS(n-1,m) 
  - 取max(LCS(n,m-1) ,LCS(n-1,m))

```python
def longestCommonSubsequence(text1, text2):
    if len(text1) == 0 or len(text2) == 0:
        return ''
    res = 0
    return digui(text1, len(text1) - 1, text2, len(text2) - 1, res)

def digui(text1, n, text2, m, res):
    if n == -1 or m == -1:
        return res  # 递归基

    if text1[n] == text2[m]:    # 减而治之
        res = digui(text1, n - 1, text2, m - 1, res) + 1

    else:
        res += max(digui(text1, n - 1, text2, m, res), digui(text1, n, text2, m - 1, res))    # 分而治之

    return res
```

**方法一复杂度分析：**

- 最好情况：每次都减而治之，则只需要O(m+n)的时间。比如，一个序列是另一个的后缀时，不涉及到分而治之
- 最坏情况：分而治之的情况下，子任务会出现大量的雷同情况，是非常糟糕的
- ![image-20200812190153074](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200812190153074.png)
- 比如说在解决(n,m)时，一定会大量重复调用(a,b)，根据组合的原理，重复次数为$\left(\begin{array}{c}n+m-a-b \\ n-a\end{array}\right)$ 在总的路径中选取n-a个水平路径。如果全部都是分而治之，则对(0,0)利用次数可达到$2^m$，这是指数级的复杂度。

> **方法二：动态规划**

将所有子问题假想成一张表格（DP table），之后计算方向为从左上角到右下角，从LCS(0,0)出发，依次计算出所有项。(n+1,m+1)的表格

![image-20200812190625830](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200812190625830.png)

表格每个元素代表当前解决的子问题，比如L(3,2)代表A(0,3)与B(0,2)的最长子序列。

对于表中所有元素共有两种情况

- 如果A[i]=B[j]，则说明需要减而治之，则`dp[i][j]=dp[i-1][j-1]+1` ，即与对角线有关系。
- 如果A[i]!=B[j]，则说明需要分而治之，则`dp[i][j]=max(dp[i-1][j]],dp[i][j-1])`

## 代码：

```java
public int tribonacci(int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1 || n == 2) {
        return 1;
    }
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n -3);
}
```

### 动态规划

```python
def df(text1, text2):
    m, n = len(text1), len(text2)
    # 构建 DP table 和 base case
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    print(dp)
    # 利用动态规划表格完成状态转移
    for i in range(1,m+1):
        for j in range(1,n+1):
            if text1[i - 1] == text2[j - 1]:
                # 找到一个 lcs 中的字符
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]
```
