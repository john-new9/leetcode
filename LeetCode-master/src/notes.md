
# LeetCode Notes

50题一格

[部分付费题目](https://www.raychase.net/4593)

[TOC]
---

### 1、两数之和[Easy]

==哈希表==
* 方法一
  * 两层循环,一层i,一层j(j从i开始到尾),和是目标值.
* 方法二
  * 创建字典,字典的key是数组值,value是位置.
  * 数组位置和值对调保存,再排序.从两端开始向中间靠近直到和是目标.

### 2、两数相加[Medium]

* 每次移动输入的链表时候,余数赋值,商进位.
* 建两个链表,一个保存值,一个实时移动.
* 返回时候去掉链表的第一个空值0

### 3、无重复字符的最长子串[Medium]

==滑动窗==

* ASCII码8位 256个
* 用滑动窗记录
* 每次遍历的过程中记录当前遍历到的元素之前,离当前位置最近的重复元素位置
* 遍历j, 滑动窗 [i,j] j往右边移动 若遇到重复的 i比s[j]右移一位

### 4、寻找两个有序数组的中位数[Hard]

* 分奇偶个数的情况(奇数中间那个,偶数取中间两个数的平均)
* 转化成两个数组找第k大问题
* 二分递归查找两个数组,查找时取两个数组的中间数
  - 若两个左端长度不够,往右边找
  - 两个左端长度超了,往右边找

### 5、最长回文子串[Medium]

* $P[i,j]$用以表示$S_i…S_j$是回文(true)或不是回文(false)
* 那么可知状态转移方程:$P[i,j] = ( (j-i < 2 || P[i + 1, j - 1]) \& S_i == S_j)$
* 初始条件是:$P[i, i] = true$
* $P[i,j]=true$并且长度大于之前的再进行操作

### 6、Z字形变换[Medium]

==具体场景==

* z前半个(|/)个数两行减2, i.e. $p = 2\times(row-1)$
* 字符的位置在$i\%p$上,
* 在/上部分是$row -1 -[i\%p - (row -1)] = p - i\%p$
* 最后多行字符串join在一起

### 7、整数反转[Easy]

* 符号单独记录
* 循环内容:res = res * 10 + x %10;x = x//10

### 8、字符串转换整数(atoi)[Medium]

* strip去空格
* 讨论第一位的符号,置标志位.同时需要去除这个符号
* 字符串0-9之内的进行运算,超过这个区间**break**退出

### 9、回文数[Easy]

==技巧性很强==

* 取最高位最低位对比
* 设置一个数d ,用以取最高位(x // d >= 10,一直乘10乘上去)
* x //d 和 x %10对应最高位最低位
* **x = x % d // 10 ;d //= 100** x 去掉最高位,去掉最低位,d也减两位

### 10、正则表达式匹配[Hard]

$\color{red}{绕},重要$

* 递归
  - s和pattern都为空,匹配成功
  - pattern是空串,而s不是,匹配失败
  - s,pattern均不是空串(长度至少为1)

    - pattern的第二个字符是‘ * ’:
      * s与pattern的第一个字符匹配(即s与pattern的第一个字符相等或者pattern第一个字符为‘ . ’)
        - s后移一位,相当于认为‘*’前的字符在s中出现不止一次 ==eg. "aabbba"和"aab\*a"==
        - pattern后移两位,相当于认为‘*’前的字符在s中只出现一次 ==eg. "ab"和"a\*ab"==
      * s与pattern的第一个字符不匹配,模式串pattern后移两位,相当于认为‘ * ’前的字符在s中出现了0次

    - 如果pattern的第二个字符不是‘ * ’:
      * s与pattern的第一个字符匹配(含义同上),s和pattern同时后移一位
      * 匹配失败

* 动态规划
  [图解](https://blog.csdn.net/vivian_ll/article/details/87936420)

### 11、盛最多水的容器[Medium]

* min(height[left], height[right]) * (right - left) 取左边和右边的高当中的最小值, 下标right-left为宽,两者相乘为最大面积
* 判断哪条高小,小的那边下标进行操作(左边小,左边右移一)

### 12、整数转罗马数字[Medium]

==贪心算法==

* 先建立字符和数字的字典(有限个),数字按从大到小排
* 遍历字典,输入的数字比当前字典的value大的话,结果加上多个字符
* 输入数字减去已有字符代表的数字(num %= number)

### 13、罗马数字转整数[Easy]

* 选择性替换掉所有的左边大于右边的情况,总共6种(一位、二位、三位各二)
* eg. "IV"换成"IIII"
* 或者遇到左边比右边大的情况就减去左边的两倍(eg. 40 = 50 + 10 - 2 * 10,加照旧只是需要减去两倍来补偿)

### 14、最长公共前缀[Easy]

* 方法一
  * 先压缩,每个字符串的对应位置合在一起
  * 取set一直到不一样(len(set)>1)

* 方法二
  * 输入的字符串列表按长度进行排序,确保最短的排在前面(最大的公共可能就是最短的那个) 
  * 扫描,对每一个位置的值,遍历所有元素,出现不一样就返回
  * 否则返回第一个(最短的那个)

### 15、三数之和[Medium]

* 第一个数遍历
* 从第一个数右边的范围内,两端往中间靠拢
* 遇到连着相同的需要跳过(不重复)

### 16、最接近的三数之和[Medium]

* 第一个数遍历
* 从第一个数右边的范围内,两端往中间靠拢
* 记录最靠近的值并更新

### 17、电话号码的字母组合[Medium]

==递归==

* 建立数字和字母对应的字典
* 分成最后一个和前面的
* 前面的再调用函数递归 

### 18、四数之和[Medium]

* 15、三数之和的延伸,排序数组
* 外两层循环固定i,j.四个数的和降成两个数的和 
* 两个数的和向中间靠拢
* 遇到连着相同的需要跳过(不重复)

### 19、删除链表的倒数第N个节点[Medium]

* 两个指针,一个先走N步,再两个同时走
* 第一个走到尾的时候第二个就到该删的地方了

### 20、有效的括号[Easy]

- Python replace
  * 判断是否是奇数或空字符
  * 将其中的(){}[] 都换成空字符,然后判断是否有剩余
- 栈操作
  * 用栈压缩'({[',用字典记录它们对应的部分')}]'
  * 遇到')}]'就查看栈顶元素是不是匹配

### 21、合并两个有序链表[Easy]

* 类似数组合并

### 22、括号生成[Medium]

==深度优先搜索==

* 递归函数记录path,res,和当前字符串和当前左右括号各自的数目
* 终止条件:如果当前总数目已经达到要求,则直接添加到res
* 如果当前左括号个数合法(小于n),可以再添加一个左括号
* 如果当前右括号个数合法(小于左括号个数),可以再添加一个右括号

### 23、合并K个排序链表[Hard]

* 利用21、合并两个有序列表
* 列表递归二分合并,前一半、后一半各自递归,然后合并两个列表

### 24、两两交换链表中的节点[Medium]

* 记录连着的三个节点
* 图示prev,a,b -> prev,b,a.很直观

### 25、K个一组翻转链表[Hard]

==**烦**==、$\color{red}{挺有代表意义的}$

* 循环,如果计数器不是k的整数倍,节点往下走一步
* 否则局部反转,反转输入是反转区间的(前一个点、后一个点),并且end需要在start后一个点
* 反转函数不仅需要反转,还需要将一首一尾连起来.最后返回尾部的前一个(和前面对应起来)

### 26、删除排序数组中的重复项[Easy]

* 从左往右剔除相同的
* 从左往右遍历的过程,将不同的放左边,并把位置索引往右移

### 27、移除元素[Easy]

* 从两端往中间(主要还是从左往右)
* 不是val就右移左指针
* 遇到val就往右交换,右边的索引同时往左移.此时左指针不能右移,不知道换过来的是不是等于val

### 28、实现 strStr()[Easy]

* not needle or haystack == needle:返回0
* len(haystack)<= len(needle):返回-1 ==包含:两个字符串等长但是不相同==
* 从左往右匹配,匹配了返回.否则-1

### 29、两数相除[Medium]

* 两层大while,一个判断**被除数>=除数**,另一个判断**被除数>=加倍的除数**
* 除数的时候,可以把被除数乘以2,商一下子也加上2
* 除数不能加到超过了余量(被除数>加倍的除数)






### 31、下一个排列[Medium]

* 从后往前遍历, 找到第一个位置i,使得A[i] < A[i+1] (第一次断崖).
* 在A[i+1,…, N-1]中, 从后往前遍历, 找第一个位置j,使得A[j] > A[i].
* 交换A[i]和A[j];
* 将 A[i+1,…, N-1] 逆序.

e.g. [5, 3, 4, 7, 6, 2, 1].在4的位置, 4 < 7;

在从[4,7,6,2,1]中, 从左到右,找出比4大的第一个数是6.交换4和6, [6,7,4,2,1].

再将[7,4,2,1]逆序成[1,2,4,7].得出[5,3,6,1,2,4,7]

### 32、最长有效括号[Hard]

- 方法一:栈
  * 遇到"(",索引i压入栈
  * 遇到")",栈非空的情况下,栈尾值和当前索引一起压入数组
  * 数组排序后计算最长连续值即可
  * 使用栈的目的:去除不匹配的括号,如"("多或者")"多
- 方法二:动态规划($\color{red}{技巧性}$)
  * 当前是")",上一个是"("组成的()对,$dp[i] = dp[i-2] + 2$
  * 当前和上一个连着两个))
    - 判断上一个(i-1)往前dp[i-1]处的s[i-1-dp[i-1]]是不是"(".和当前的")"匹配
    - $dp[i] = dp[i-dp[i-1]-2] + dp[i-1] + 2$表示几串连在一起

### 33、搜索旋转排序数组[Medium]

==二分查找的思路==

* mid在前半段 或者l mid r 都在右边
  - nums[l] <= target <= nums[mid]
* l 在左半段 、mid 在后半段
  - nums[mid] <= target <= nums[r]

### 34、在排序数组中查找元素的第一个和最后一个位置[Medium]

* 先二分法查出一个等于target的位置
* 位置往两端找最大最小位置(此时搜索区间为缩小后的区间)

### 35、搜索插入位置[Easy]

* 二分法

### 36、有效的数独[Medium]

* 行列块都判断一次
* 判断行最简单,每行非"."元素拉出来取set看长度变不变
* 判断列的时候用zip把列转化成行
* 判断块把块区域的值拉成行,判断9个块

### 37、解数独[Hard]

==看懂了,但是不会写的==

* **深度优先搜索**
* 对每行每列中"."的位置进行填充尝试"123456789",并进行判断是否合法
* 填完这个值后填完了所有的元素并且合法就能返回
* 判断合法的函数需要(行判断、列判断、块判断)

### 38、外观数列[Easy]

* 顺序计算下来(n=1,2,3,...)
* 计算某个s时,先后判断是否遇到不同的,结果中加(个数,值)
* 结果元组用''(空)链接
* ==因为有前后的判断(m[j] != m[i]),加一个后面不会溢出(随便加一个就行)==

### 39、组合总和[Medium]

**深度优先搜索**

* 数组排序
* 记录path和res: 一条子路和已经加起来的和
* 终止条件: target < 0(不满足) 和target == 0(添加path)
* 因为数字可以重复,递归时索引index不用加一

### 40、组合总和II[Medium]

**深度优先搜索**

* 与 39、组合总和的区别在于不能重复
* 经过一个值起点加1,路径加点,目标值减小
* 递归时候,遇到nums[i] == nums[i - 1]需要跳过

### 41、缺失的第一个正数[Hard]

$\color{red}{桶排序}$ ==索引为 i 的位置上应该存放的数字是 i + 1==

* 先进行一轮排序
  * 当nums[i]!= i+1时候,将nums[i]与nums[nums[i]-1]交换,直到nums[i]== nums[nums[i]-1] (或者越界大于length、小于0)交换终止
* 最后进行判断,排序好的数组哪里开始nums[i]!= i+1,这就是第一个不存在的正整数,否则就是length+1

### 42、接雨水[Hard]

==结合图去理解==

* 双指针法,左右两边哪边短操作哪边
* 移动的过程中需要更新最大值(两个,左右分开)
* 同时蓄水为l_max/r_max - height[l],要更新到结果上

### 43、字符串相乘[Medium]

* 数反转,按位相乘
* 对结果进行取余数,进位操作
* 在另一个结果列表0位置插入当前值
* 从头开始去0,再将list join在一起






### 45、跳跃游戏II[Hard]

==贪心算法==

* 先初始化(start,end,step,maxDis)
* 在当前位置和最远能达到的位置之间进行尝试,看下一步最远能走到哪(maxDis)
* 每尝试一步,步数(step)加一,其他参数更新

### 46、全排列[Medium]

==深度优先搜索==

* nums的值递归一步步压入path
* 终止条件:nums为空将path压入结果中

### 47、全排列II[Medium]

* 同46,加一个path是否在res里的判断(重复数字可能导致相同的path)

### 48、旋转图像[Medium]

* 对$\frac{1}{4}$部分的矩阵进行旋转,一次旋转4对值
* 从外围到内围, $begin, end = i, ls - 1 - i$
* 此时一圈中 **上->右->下->左** 这个顺时针圈中的4个值
$m[begin][begin+k],m[begin+k][end],m[end][end-k],m[end-k][begin] $ 

### 49、字母异位词分组[Medium]

* 建一个字典:key是单词中各个字母排序重组,value是单词列表
* 返回字典的values

### 50、Pow(x, n)[Medium]

==分冶法==

* 递归
  - n为0,返回1
  - n为负数,1/pow(x,-n)
  - n偶数: x*x n //=2
  - n奇数: 结果先乘一个ｘ出来,再调用偶数

---

### 51、N皇后[Hard]

==深度优先搜索==

* C[i]表示第i行皇后在哪一列
* 一行一行操作,操作到$row+1$行时候,列的选择遍历j = 1->$N$,先判断 1、填充值不在C里面(作用是剪枝); 2、与前面$row$行都不冲突,再进行操作下一行
* 是否冲突的函数注意:与之前的是不是同一列(C[i] == col);与前面的是否对角线冲突(abs(i-row) == abs(C[i]-col))
* 终止条件即判断$row$是不是len(C),按格式插入res,(这里字符串不支持修改,可以用列表join的形式)

### 52、N皇后II[Hard]

* 同51

### 53、最大子序和[Easy]

==阿里面试题==

- 方法一
  * 对于数组中的其中一个元素,它只有两个选择:
   1. 要么加入之前的数组加和之中(跟别人一组)
   2. 要么自己单立一个数组(自己单开一组)
  * $f[j]=\max \{f[j-1]+S[j], S[j]\}$
- 方法二
  * 如果没有遇到负数,那么可以将数组值累和下去,$nums[i] += nums[i-1]$
  * 遇到负数重新开始
  * 维护区间

### 54、螺旋矩阵[Medium]

- 普通方法
  * 顺时针操作,操作完对应的边需要缩一
  * while True循环里面,不满足左右上下关系即可break
- $\color{red}{技巧性操作}$
  * 初始化$dx,dy,di$和访问过位置的数组visited
  * 行列的循环一起操作(range(m * n))
  * 矩阵值加到结果,访问过的坐标加到visited
  * 根据$dx,dy,di$(代表的是走向)计算下一个位置
  * 如果下一个坐标没有越界 并 没有访问过,就下一步
  * 否则di = (di+1)%4,换个方向继续

### 55、跳跃游戏[Medium]

* end = max(end, nums[start] + start)
* start += 1

### 56、合并区间[Medium]

* 利用自定义函数对区间进行排序,排序标准按左值
* 初始化[s,e]为第一个区间的前后
  - 后边跟着的区间和[s,e]的交叉,相当于合并
  - 紧跟着的区间在[s,e]后面,压入[s,e],并重新置新的[s,e]

### 57、插入区间[Hard]

* 在新区间左右两边部分单独记录
* 和新区间的交叉部分合并,左边端点取小,右边端点取大
* 左、右、新三个区间最后加在一起

### 58、最后一个单词的长度[Easy]

* split()拆分后组成列表
* 注意最后元素是' '空的情况
* 返回最后一个单词的len,注意空列表情况

### 59、螺旋矩阵II[Medium]

* 比54好一点,此处只能是方阵
* 按顺序赋值,并同时加一(横、竖、横、竖)
* begin,end两个变量是同时变化一的,一圈结束,b += 1;e -= 1
* 若n为奇数,中间还有一个值需要while循环外面赋予

### 60、第k个排列[Medium]

==烦,自己写不出来==$\color{red}{大体思路是从第一位到尾,先后确定数字}$

* 排列是从小到大排列的,首位是1,2,3这样的排列,次位类似
* 先建立['1','2',...'n']和0!, 1!, ..., (n - 1)!
* **第几个转化为第几个的索引(减1)**
* 第一个区间首位是1,第二个区间首位是2
* 首位所在的区间 k//(n-1)! **(n-1)!**表示一个区间有多少个数
* k减去多个区间对应的值   
* 结果值添加对应的数字
* 因为排列不重复,之前的字符数组需要去掉对应元素 

### 61、旋转链表[Medium]

==链表成环==

* 遍历
* 计算链长,并计算左部分的个数,指针在尾部
* 把链表连成环,指针(在尾部)的next是head
* 计算左边该几个,指针处跑到该断的位置断开

### 62、不同路径[Medium]

* 边界处理好,第一行和第一列的初始化
* 当前位置的路径和为左边点和上边点的路径可能的和

### 63、不同路径II[Medium]

* 和62类似的动态规划
* obstacleGrid矩阵元素(1-obstacleGrid[i][j])作为系数判断mat[i][j]是否置0

### 64、最小路径和[Medium]

* 动态规划
* 左边或者上面的最小加当前
* mat[r][c] = min(mat[r-1][c] , mat[r][c-1])+grid[r][c]

### 65、有效数字[Hard]

* 没看懂 

### 66、加一[Easy]

- 方法一:数值操作
  * 先将列表计算成数
  * 数加一并取余添加进列表,列表反转输出
- 方法二:列表操作
  * 先将列表尾部加一,头部填0(进位)
  * 从尾到头处理进位
  * 计算结束看头部是不是0,是的话去掉

### 67、二进制求和[Easy]

==递归==

* 终止条件:a,b其中有一个是空的
* 按a、b最后位分三种情况,递归求去最后一位的a、b
  * 最后都是1 前面的相加 再加1 字符串尾部补0;
  * 最后都是0 补0
  * 最后一个1、一个0: 补1





### 69、x 的平方根[Easy]

* 二分查找
* 递归提取4出来,输入/4,逐渐将输入限制到4以内

### 70、爬楼梯[Easy]

**斐波那契数列**

* f(n) = f(n-1) + f(n-2)

### 71、简化路径[Medium]

* 按'/'拆分开
  * ''或'.',不用操作
  * '..' pop掉结果的最后一个元素(相当于抵消)
  * 否则添加入尾部
* join在一起,用"/"连

### 72、编辑距离[Hard]

==动态规划经典==

* 行列处理 对应从空到一个字符串 或 一个字符串到空
* 三个分别对应于加、减、替换
* 要是word1[i-1]==word2[j-1],那么dp[i][j] = dp[i-1][j-1]
* 不然dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1 三种情况取小,对应三种操作取一种

### 73、矩阵置零[Medium]

- 直接
  * 直接查找是0的位置,记录0的行列,并取set.然后对每个位置行列各置为零
- 稍微麻烦点
  * 第一行第一列做标记,行:从上倒下,列:**从右往左**置0(以防第一列需要置0但是被之前的标记污染)
  * **记得回来处理一下第一行,全部置成0**

### 74、搜索二维矩阵[Medium]

$\color{red}{想法很牛逼的}$

* 对角搜索思想
* 从右上角开始往左下移动
  - 小了,就往下找
  - 大了,就往左找

### 75、颜色分类[Medium]

$\color{red}{计数排序}$

* 先遍历一遍数组nums,进行三个值的个数count (初始化[0,0,0])
* 再遍历range(3)和range(count[i]),nums对应位置赋予i

### 76、最小覆盖子串[Hard]

==很烦==

* 建立字典统计目标串的字母分布(t串的为正,其他默认值0)
* 从左往右遍历s串
  - 要是字典大于0,计数器就减一(又包含了一个t串元素)
  - 先找到一个区间能包含t(判断条件为计数器为0),但长度不一定是最短的
    - 此时左端往右移动直到need[c]==0,再移下去就不够了
    - 更新区间
    - 此时还需要将区间左侧往右移,字典对应值加一,计数器加一
    - 下一步迭代

### 77、组合[Medium]

==深度优先搜索==

* 终止条件:需要的数为0
* 从当前索引往n找数添加到路径

### 78、子集[Medium]

==深度优先搜索==

* 和前面77类似
* 没有终止添加,dfs搜索一来就将路径添加到结果

### 79、单词搜索[Medium]

==深度优先搜索== + **剪枝**

* 需要一个与二维网格等大的矩阵,记录是否已经遍历过
* 终止条件:word整个都搜索到
* 递归迭代:若当前位置的元素与当前单词位置相同,则按它的上下左右四个方向匹配下一个
* **特殊场景下剪枝:遍历的过程中越过边界、遍历到的位置之前遍历过了、或者当前位置的元素和单词对应的位置不同**

### 80、删除排序数组中的重复项II[Medium]

* 从前往后遍历
* 若遇到和上一个相同情况
  - 计数器加一
  - 若计数器大于2,需要pop当前元素
* 如果和上一个不一样,计数器重置为1即可

### 81、搜索旋转排序数组II[Medium]

* 和33、搜索旋转排序数组类似.但是存在一个特殊情况 eg. [1,3,1,1,1]
* 差别修改有两处
  * 遇到mid相关的地方,判断符号去掉等号(>= 改成 >)
  * 判断nums[mid]与nums[l]的关系时候,多了一个等号的情况,这时候的操作不是左右区间的压缩,==**l+=1,左边往右移一**==

### 82、删除排序链表中的重复元素II[Medium]

* 最外面一层循环判断有没有到尾
* 内部一层循环跳过多个相同的,到达不同的位置为止(很重要的)

### 83、删除排序链表中的重复元素[Easy]

* 因为已经排序好了,往后推进就行
* 当前的值与下一个节点的值相等
* ==覆盖的是下一个节点的值不是当下的==

### 84、柱状图中最大的矩形[Hard]

[牛逼了](https://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html),看懂写不出来

* 建立==递增栈==,在递增的块内求面积最大
* 当前如果是递增,压入栈;否则弹出栈并计算面积情况
* h是短的,w是当前位置和h的位置差
* ==此处较为巧妙: 若heights数组中元素都是单增序列,则最后无法出栈stack,也就无法计算最大面积.可以在高度列表补个0,使之最后可以出栈==

### 85、最大矩形[Hard]

* 方法一
  - 按行遍历,每行往上看都是一道84题的延伸
* 方法二:动态规划 ==看懂了,但是写不出来==
  - [参考](https://zhuanlan.zhihu.com/p/102357584)
  - 每遍历到一个点,考虑向上、向左、向右能延伸到的最远的地方
  - 高: 行遍历,遇到0 height就变成0,否则为height+1
  - 左: left  = max("当前行向左延伸最大列" , 上一行这列的left )
  - 右: right = min( "当前行向右延伸最大列", 上一行这列的right )
  - 遇到0,向左延伸和向右延伸的最大列都要向中间靠拢

### 86、分隔链表[Medium]

* 四个指针,两个指向头不动
* 两个指针动,对应左右两部分
* 最后串起来





### 88、合并两个有序数组[Easy]

* ==**从后往前填**==,一直填到两个数组一个空了
* 第一个没空无所谓,反正要返回
* 第二个没空继续填

### 89、格雷编码[Medium]

==看具体形式凑的==

* 设$n$阶格雷码集合为$G(n)$,则$G(n+1)$阶格雷码为:
  * 给$G(n)$阶格雷码每个元素二进制形式前面添加0,得到$G^′(n)$ ($G(n+1)$的前一半 )
  * 设$G(n)$倒序(反过来)为$R(n)$,给$R(n)$每个元素二进制形式前面添加1(**程序操作为1<< n**),得到$R^′(n)$ ($G(n+1)$的后一半 )
  * $G(n+1)=G^′(n)\cup R^′(n)$,拼接两个集合即可得到下一阶格雷码
* 实现上,外循环实现$G(0)$到$G(n)$,内循环实现$G(n)$倒序

### 90、子集II[Medium]

==深度优先搜索==

- 去除重复子集的方法
  * 78 append新元素的时候,加一个判断
  * 78 append遍历start->end的时候,若nums[i] = nums[i-1],跳过

### 91、解码方法[Medium]

$\color{red}{特定条件下的斐波那契}$

* dp[i] 表示i的字符的合法编码数量,取决于当前字符 
* dp[i] = dp[i-1] + dp[i-2] (满足if条件)
  - dp[i] += dp[i-1],if s[i-1] ~(‘0’–‘9’) 
  - dp[i] += dp[i-2],if s[i-2] == ‘1’ || (s[i-2]==’2’ && s[i-1]>=’0’ && s[i-1]<=’6’)

### 92、反转链表II[Medium]

* 前面先走m-1步
* 反转中间部分
* 接上最后一段和中间一段

### 93、复原IP地址[Medium]

==深度优先搜索,烦==

* ip每部分最多3位,一个循环体range(3),选择这样的子串成为ip的一部分,但是==允许单个0,但是不允许0开头的一串,比如025==.所以子串长度大于1时,需要判断
* **特殊场景下可以剪枝(==ip的形式决定==),剩下的子串太长(剩下的ip位都超过了3位)或太短(剩下的ip位都小于1位了)**
* 上一条既是剪枝,也是条件.如果剩下的太短,添加的时候容易溢出

### 94、二叉树的中序遍历[Medium]

**left->root->right**

* 一直往左,并压入栈
* 看栈尾节点的值弹出并添加进结果(此时这个节点左边和当前节点都已经压入结果中),节点往右
* 或者递归,[左子树]+[当前root]+[右子树]

### 95、不同的二叉搜索树II[Medium]

* 定义函数fun(start,end)
* 对[start,end]进行遍历,遍历值为root
* 递归生成左右子树,将root添加到结果去

### 96、不同的二叉搜索树[Medium]

* 数组的值是$1,2,\cdots,n$. 若以$i$为root,左子树就是$1,2,\cdots,i-1$,右子树就是$i+1,\cdots,n$,即:$f(i-1) \times f(n-i)$
* 递归: $f(n) = \sum_{i=1}^{n} f(i-1) \times f(n-i)$
* 两个循环,外循环计算$f[n]$

### 97、交错字符串[Hard]

==动态规划==

* f[i][j]表示s1[i]和s2[j]匹配s3[i+j]
* s1的最后一个字符等于s3的最后一个字符,则 f[i][j]=f[i-1][j]
* s2的最后一个字符等于s3的最后一个字符,则 f[i][j]=f[i][j-1]
* 总结:
  - f[i][j] = (s1[i-1]==s3[i+j-1] and f[i - 1][j]) or (s2[j-1] == s3[i+j-1] and f[i][j-1])
* 注意边界条件

### 98、验证二叉搜索树[Medium]

* 给子树一个限定的值域范围
* 在当前节点满足要求的前提下,缩小子树的时候变化值域范围,如左子树($-\infty,root.val$)
* 否则 False

### 99、恢复二叉搜索树[Hard]

==看懂,写不出==$\color{red}{中序遍历}$
**实际写自己举个例子理解**

* 二分搜索树的中序遍历是一个单调递增的数组
* 遍历的过程中判断之前访问的节点pre.val是不是大于当前访问的节点cur.val
  - 是:我们就要记录pre,pre就是要交换的第一个元素
  - 然后继续遍历
  - 直到再也没有出现pre.val > cur.val.此时最后一次出现的cur就是要交换的第二个元素
* 中序遍历可以递归或者栈法

### 100、相同的树[Easy]

* 都空[真]
* 都不空并判断[递归]
* 一个空[false]

---

### 101、对称二叉树[Easy]

* 根相同
* 左子树右子数的根值相同并左子树的左子树～右子树的右子树、左子树的右子树～右子树的左子树

### 102、二叉树的层次遍历[Medium]

==深度搜索,不是深度优先搜索==

* 定义递归函数fun(root,level,result)
* 如果递归的层level加深了,result加入空列表[]
* 递归调用函数,root变为它的子节点,深度加深

### 103、二叉树的锯齿形层次遍历[Medium]

* 在102的基础上加一个标志位flag(bool)
* flag根层时候是(True),flag加一层,flag翻转一下

### 104、二叉树的最大深度[Easy]

* 递归
* 空树深度为0
* 左右支路比较长短
* 只有一支树考虑一边

### 105、从前序与中序遍历序列构造二叉树[Medium]

* 前序的头就是root,查询完需要pop掉,否则无法下一步
* 查询索引的函数index
* 中序中,root值左边就是左子树,右边是右子树
* 递归构造子树先left后right

### 106、从中序与后序遍历序列构造二叉树[Medium]

* 后序的尾部就是root,查询完需要pop掉,否则无法下一步
* 中序中,root值左边就是左子树,右边是右子树
* ==递归构造子树先right后left==

### 107、二叉树的层次遍历II[Easy]

- 方法一
  * 利用栈的思想,栈中只有一个元素(初始化:[root])
  * 栈中元素取出,将所有节点的值压入列表,最后压入res的0索引位置(题目需要倒序)
  * 对栈中取出的元素(节点组成的列表),子节点组合成列表后装入栈,向下新一轮扫描并压入栈
- 方法二
  * 102、二叉树的层次遍历加一个反转

### 108、将有序数组转换为二叉搜索树[Easy]

* 数组对半分
* 一半给左右子树

### 109、有序链表转换二叉搜索树[Medium]

- 方法一
  * 利用快慢指针进行中点判断
  * 左列表给left,右列表给right
- 方法二
* 把list的值压入Array,然后同108

### 110、平衡二叉树[Easy]

* 递归计算left和right的深度,不为空的情况下返回最大的那个+1
* 若异常则返回-1
* 左右子树深度差超过1也算异常
* 非异常情况下就满足要求

### 111、二叉树的最小深度[Easy]

* min(left,right) + 1

### 112、路径总和[Easy]

* 每到一个子节点,sum-=root.val
* sum为0并是叶子节点(没有子节点了)
* 不是叶子节点就返回左右的或(or)

### 113、路径总和II[Medium]

==深度优先搜索==

* 终止条件:左右子树都空(最下面的),并sum == root.val的时候该路径满足,路径添加到result
* 递归调用的时候,sum -= root.val,path + [root.val]

### 114、二叉树展开为链表[Medium]

* 左右字树分别递归
* 递归到当前节点,左子树插到root和root.right之间.(其中重要的一步是查找左字树的最右节点)

### 115、不同的子序列[Hard]

* 动态规划,s、t分别对应行列表
* 初始化
  - 当母串子串都是0长度时,次数是1
  - 当子串长度为0时,所有次数都是1
  - 当母串长度为0时,所有次数都是0 (默认是0,不用重复了)
* 假设S已经匹配了i-1个字符,得到匹配个数为dp[i-1][j].现在无论S[i]是不是和T[j]匹配,dp[i][j] 至少是 dp[i-1][j]

* 总结:
  - dp[0][0] = 1 # T和S都是空串
  - dp[i][0] = 1 # T是空串
  - dp[0][j] = 0 # S是空串,T不是空串,S没有子序列匹配
  - dp[i][j] = dp[i-1][j] + (s[i-1] == t[j-1] ? dp[i-1][j-1]:0)

### 116、填充每个节点的下一个右侧节点指针[Medium]

* 当前节点的左右子树链接
* 同一行之间的链接,右子树的下一个root.right.next 
  - root有next:root.next.left
  - root没有next(右边没有了):None
* 递归链接子树

### 117、填充每个节点的下一个右侧节点指针II[Medium]

==看懂,写不出==

* 建立一个节点dummyHead,它的next始终指向当前行最左子节点
* 通过next遍历当前行,将每个子节点用next相连
* 当前行遍历完毕时,通过dummyHead.next到达下一行的最左节点,同时将dummyHead.next置为None.(当前行的尾部为None)
* 如果这一行的节点都没有子节点的话,会停止循环下去

### 118、杨辉三角[Easy]

* 先用全1的列表组填,再用循环的方法计算,根据上一行计算下一行

### 119、杨辉三角II[Easy]

==滑动窗==

* 直接用118的可以
* 定义多行,一上一下,类似于滑动窗一样往下滑
* 直接定义最后一行,==从后往前==,从上往下覆盖

### 120、三角形最小路径和[Medium]

==特殊场景下,动态规划==

* 将类山形状的集合想象成左下凸三角形|_\
* 从下往上,从左往右 递归
* **从下到上的逆序有个优点:不用边界判断**
* $f(i, j)=\min \{f(i+1, j), f(i+1, j+1)\}+f(i, j)$:(下面和右下面)
* 可以直接在原始数组上修改,返回[0][0]处元素

### 121、买卖股票的最佳时机[Easy]

* 线性扫描,从左往右扫描出最小的值记录
* 描到第i个元素时,如果在这一天卖股票,盈利就是profit = prices[i] - minelement
* 记录最大值

### 122、买卖股票的最佳时机II[Easy]

* 当前价格比昨天高就加入收益

### 123、买卖股票的最佳时机III[Hard]

- **牛逼的方法**
  * 对于任意一天考虑四个变量:
      fstBuy: 在该天第一次买入股票可获得的最大收益 
      fstSell: 在该天第一次卖出股票可获得的最大收益
      secBuy: 在该天第二次买入股票可获得的最大收益
      secSell: 在该天第二次卖出股票可获得的最大收益
      分别对四个变量进行相应的更新, 最后secSell就是最大
- 规划
  * $f(i)$是$[0, i]$的最大利益, $g(i)$是$[i, n-1]$的最大利益
  * $\max \{f (i) + g(i)\}$是两次买卖的最大收益
  * 分两步,一步前向找最大收益,一步反向找收益并加上之前前向的值

### 124、二叉树中的最大路径和[Hard]

==看懂,写不出来==

* 递归 
* 定义全局变量记录结果
* 递归函数return的时候只需要一个方向的值,因为在递归过程中,子树只有向父节点返回(L->root或R->root),**不存在L->root->R**

### 125、验证回文串[Easy]

* 检测字符串是否由字母和数字组成:isalnum()
* 两侧像中间靠拢

### 126、单词接龙II[Hard]

==没看懂==

* 使用collections.defaultdict(set)构造后向的字典(end:{prev}的形式)
* 使用迭代 **res = [ [p]+r for r in res for p in parents[ r[0] ] ]** 生成路径,避免递归

### 127、单词接龙[Medium]

$\color{red}{广度优先搜索}$ ==技巧:list转化为set可以省时==

* 队列格式为(word,level),加词的话(newWord, length + 1)
* newWord的构造为在队列最左边的元素各个位置分别插入26个字母(可以认为:26个方向的棋盘搜索)
* 一旦搜索到目标立即返回level,此时是最短的,否则将出现更长的路径
* 队列中可能存在类似的元素[(xx,len),(xxx,len),(x,len+1),(ix,len+1)]

### 128、最长连续序列[Hard]

==技巧性==

* 遍历数组,对于当前值,往大处搜索和往小处搜索
* 一直搜索到不在数组里面的数,i1-i2(需要对应具体写法加减1)
* 最大长度和全局最大长度取大
* 循环过程一直到数组都剔除完

### 129、求根到叶子节点数字之和[Medium]

* 一层一层递归
* 下一次递归的时候sum * 10+root.val
* 左右子树都空的时候终止

### 130、被围绕的区域[Medium]

==特殊场景下的深度优先搜索==

* 任何不在边界上,或不与边界上的‘O’相连的‘O’最终都会被填充为‘X’
* 在边界上的O或与边界上O相邻的O(能从边界到达(深度遍历))都不会改变
* 可以从边界上的O出发,通过深度遍历找出与他们相邻的O,并将这些O先全部改成T.
* 这样,还在矩阵中的O就是需要改成X的O,而T需要改回O

### 131、分割回文串[Medium]

==深度优先搜索==

* 单独的回文判断函数
* 终止条件: 索引和字符串长度相同,意思是遍历完
* 在start到len(s)之间判断是否合法,合法的话加入path继续搜索

### 132、分割回文串II[Hard]

* 动态规划
* f(i)表示[i,n-1]之间的最小的裁剪数目(n+1个数)
* f的初始化的场景:单个元素都是回文串 f[n] = -1,f[n-1] = 0,...f[0] = n-1(n个元素n-1到裁剪完)
* ==从右往左== , $f(i)=\min\{f(i),f(j+1)+1\}$,$[i,j]$之间是一个回文串
* 回文状态:$DP[i][j]= (\operatorname{str}[i]=\operatorname{str}[j]) \quad\&\&\quad DP[i+1][j-1]$
* ==dp (i 往左更新,j往右更新)==

### 133、克隆图[Medium]

==看懂,但是写不出==
**深度搜索和广度搜索**

* 建立字典和栈,栈初始化为输入node,字典{srcnode:dstnode} 
* 对栈中元素进行邻近遍历,邻近已经在字典里了,那就链接邻居关系;不在里面,那新建节点并链接邻居关系,还要压入栈

### 134、加油站[Medium]

* 一个变量判断整个数组有没有解$\sum (gas - cost) >= 0$
* 一个变量判断当前位置开始的有效性,否则记录下一个为有效点

### 135、分发糖果[Hard]

* res 初始化为全1
* 前向遍历
  - 右边比左边大,**res[i] = res[i-1] + 1**
* 后向遍历
  - 左边大的话,左边为 在右边的基础上加一,同时与当前的必大,**res[i-1] = max(res[i]+1 ,res[i-1])**

### 136、只出现一次的数字[Easy]

* 方法一
  * $2\sum(set(nums)) - \sum(nums)$
* 方法二:异或
  * 位运算中异或的性质:两个相同数字异或=0,一个数和0异或还是它本身
  * 当只有一个数出现一次时,我们把数组中所有的数,依次异或运算,最后剩下的就是落单的数,因为成对儿出现的都抵消了

### 137、只出现一次的数字II[Medium]

* $\frac{1}{2}[3\sum(set(nums)) - \sum(nums)]$

### 138、复制带随机指针的链表[Medium]

$\color{red}{链表重复两份,再拆分出来}$

* 复制next部分
* 复制random部分
* 拆分两个单链表,间隔取节点

### 139、单词拆分[Medium]

* 动态规划
* $f(i)$表示$s[0,i]$是否可以拆分
* $f(i) = \forall j : (f(j) \quad\&\&\quad s[j+1,i] \in dict), 0 \leq j < i$
* 一旦检测到有一个j满足条件,递推关系可以 延续下去

### 140、单词拆分II[Hard]

==深度优先搜索+动态规划==

* 和139一样的动态规划,预加一个矩阵判断**prev[i][j] = true 表示s[j,i)是一个合法单词,从j处切开**
* 深度搜索后向进行,i->cur的子串在字典里(prev[cur][i])就压入path 并迭代
* 当搜索到0处,即处理path拼接之后压入res

### 141、环形链表[Easy]

* 一个就是设置两个指针slow和fast,一个步长为1,一个步长为2进行遍历
* 如果有环,则slow和fast总会在某一点相遇.如果没有环,则fast会先为空,或者fast.next为空.

### 142、环形链表II[Medium]

$\color{red}{技巧性很强}$

* 链长$L$,环入口到fast与slow相遇点距离$a$,起点到环入口距离$x$
* fast与slow相遇时候,fast比slow多走$n$个圈,即$2s = s + nr,\Delta = s = nr$长度
* $ \begin{aligned}
{\color{red}{x+a = s = nr}}\Longrightarrow x &= nr - a \\
&= (n-1)r + r - a \quad // r = L - x \\
&= (n-1)r + (L - x - a) \quad // 后面部分是slow下一次到入口的距离 \end{aligned} $
* 新建一个指针res走$x$步,slow也走$x$步就会到达入口,所以res和slow会**在入口相遇**

### 143、重排链表[Medium]

* 快慢指针分出来前后部分
* 后半部分反转
* 两个链表合并

### 144、二叉树的前序遍历[Medium]

**root->left->right**

* 用一个栈记录节点
* 当前的root结果记录到输出,**right和left**先后压入栈中(left整个左支路先压完的)
* 一直循环到栈为空

### 145、二叉树的后序遍历[Hard]

**left->right->root**

* 前序的修正版
* 先按root->right->left的反顺得到结果(类似前序)
* 结果压入root,栈中先后压入left->right(相当于**root->right->left**的顺序)
* 结果逆序输出

### 146、LRU缓存机制[Medium]

* 一个字典,一个列表
* 字典进行操作,列表记录
* 列表左边表示操作过的,操作过的左移.万一满了,列表尾部去掉

### 147、对链表进行插入排序[Medium]

==烦,看懂,写不出==

* 若下一个节点的值比这个节点的值大,下一个
* p找到小于的最后一个节点
* 右边的节点插入到左边去

### 148、排序链表[Medium]

* 分冶
* 快慢指针将列表分成两半,各自递归调用排序
* 再将两个有序列表按序合并(21题)

### 149、直线上最多的点数[Hard]

$\color{red}{最大公约数}$ ==看懂,写不出==

* 直线是y = ax + b,$a,b$对相同即同一直线,转化为考虑($dx,dy$)相同(因为求斜率容易出现非整数,精度对判断有影响,这里求**最大公约数**)(**好像只考虑斜率,不知道为什么不用考虑截距**)
* 两重循环,相当于先后取两个点 
* 建立两重哈希表,key分别是$dx$和$dy$
* 需要实时更新最大值
* **本题还有一种特殊场景:就是dx = dy = 0(同一个点),这需要单独考虑**

### 150、逆波兰表达式求值[Medium]

* 数字放在列表中(模拟栈),如果遇到运算符号,就从数字栈尾部拿出两个进行运算,算完压入栈
* **在 / 除法时候,若存在负数,不能整除时候需要加一** eg. 1//-22 is -1 in python but 0 for needed

---

### 151、翻转字符串里的单词[Medium]

* 将字符串按" "拆分
* 拆分的列表去掉" "
* 列表反转后用空字符join在一起
* 不用拆分的话:遍历字符串,遇到空字符进行操作
  - 左端不等于当前索引(中间有单词),添加入栈
  - 左端等于索引(空字符),跳过(不操作)
  - 栈反转再join
* ==技巧:尾部加个空字符,否则最后一个单词加不进去==

### 152、乘积最大子序列[Medium]

* 三个指针:一个当前最小、一个当前最大、一个返回的最大(因为可能存在负数,负负得正)
* 往右推移的过程比较nums[i] , nums[i]\*max ,nums[i]\*min三个的大小

### 153、寻找旋转排序数组中的最小值[Medium]

* 二分查找
* mid值比左端大的话,mid在左部分,否则在右边部分
* 特殊场景:纯升序排列

### 154、寻找旋转排序数组中的最小值II[Hard]

* 设置l,r指针在数组两端,mid为每次二分的中点:
  - 当 $nums[mid] > nums[r]$时,mid一定在左部分,i一定满足 mid < i <= r,l = mid + 1
  - 当 $nums[mid] < nums[r]$时,mid一定在右部分,i一定满足l < i <= mid,r = mid
  - 当 $nums[mid] == nums[r]$时,是此题对比153题的难点(去除可重复元素),r -= 1

### 155、最小栈[Easy]

* 使用两个栈,一个压值
* 一个压最小值,若压入的数比当前最小值大,则压入min_stack[-1]

### 160、相交链表[Easy]

==技巧性==

* 我们同样使用双指针进行判别,不过步长都是一步,让两个指针分别从两个链表头结点开始向后移动
* 当其中一个指针走到链表末尾后,换到另一个链表的头结点上,另一个指针也是如此
* 这样如果两个链表相交,则一定可以相遇,且根据数量关系可知,首次相遇的结点即为相交结点

### 162、寻找峰值[Medium]

* O(logn),采用二分查找
* 首先找到中间节点mid
  - 如果大于两边就返回当前下标index
  - 如果左边的结点比mid大,那么继续在左半区间查找,这里面一定存在一个峰值元素,因为nums[-1]为负无穷大- 反之就继续在右半区间查找





### 165、比较版本号[Medium]

* 先用"."把两个字符串拆分一下
* 两者较短的那个在尾部用 0 串补上
* 逐位比较, 1 -1 的情况可以提前return.否则就是0






### 167、两数之和 II - 输入有序数组[Easy]

* 一左一右向内部靠拢,大了往左,小了往右

### 168、Excel表列名称[Easy]

* 26进制表示
* 取完余数,考虑上一位的
* 结果需要反转后join

### 169、多数元素[Easy]

* 小到大排序,取后半段的值:len(nums)//2位置值

### 171、Excel表列序号[Easy]

* 26进制反表示 

### 172、阶乘后的零[Easy]

==具体例子画画看==

* 有乘因子有5的数字时会有零出现
* 有些数字如25、125等里面5的因子不止一个,有几个因子5就加几
* 相当于加 n//5

### 173、二叉搜索树迭代器[Medium]

* **递增排序<=>中序遍历**
* 遍历完存数组
* 索引初始化-1,一个next加一

### 174、地下城游戏[Hard]

==特殊场景下的动态规划==

* 倒过来走
* 每一步都和1比较,max(1,res[r][c])
* 初始化
  - 判段最后一个元素是否小于0
  - 最后一行,一列$max(res[r+1][n-1] -dungeon[r][n-1] ,1)$
* 递归时候下面和右边两个数取小的那个

### 179、最大数[Medium]

==Python的技巧.==**Python的富比较方法包括__lt__、__gt__分别表示:小于、大于,对应的操作运算符为:“<”、“>”**

```
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y < y+x
```
* 将列表转化成字符串列表,再排序
* 将列表按一点规则join在一起就行
* 一个特殊case:原数组列表set是{0}的话说明原来都是0

### 187、重复的DNA序列[Medium]

==技巧性==

* 建立一个很啰嗦的字典:从首位开始的连续十个字符串作为key,每出现一次加一
* key一直往右边推移
* 字典中的key的value大于1说明出现超过一次,加入一个结果集合(set).有重复会自动消去
* 集合返回成列表

### 188、买卖股票的最佳时机IV[Hard]

==牛逼==

* 拆解成之前的子问题解决
* 2k较大(大于股价数组长)时使用贪婪算法(只要后一个比前一个大就能买卖),2k较小时使用动态规划
* ==max==有效不能是空列表,有一个地方是k+1

### 189、旋转数组[Easy]

* 每次都把最后一个元素取出,前面元素往后移,循环k次
* 先反转前n-k个元素,再反转后k个元素,在全部反转
* 利用(i+k)%numsSize从第一个开始确定该元素旋转后的位置,直到所有元素归位

### 190、颠倒二进制位[Easy]

* res加上(n的尾部左移多位)的结果
* n右移一位

### 191、位1的个数[Easy]

* 常规
* 移位



### 198、打家劫舍[Easy]

**斐波那契数列**

* $f(i)= max(f(i-1),f(i-2)+nums[i])$

### 199、二叉树的右视图[Medium]

==深度优先搜索==

* 类似层次遍历,记录深度
* 深度大于res的长度的时候,添加一个元素(不妨是0,后面覆盖)
* **先进行左子树的迭代,右子树迭代出来的值会覆盖到之前的上面去**

### 200、岛屿数量[Medium]

==深度优先搜索==

* 连通域问题
* 遍历矩阵,遇到1的时候,计数器加一,深度迭代的置位
* 四个方向在合法的条件下将1置为0

---

### 201、数字范围按位与[Medium]

$\color{red}{技巧性}$

* 因为只要有一个0,那么无论有多少个1都是0
  - 不妨 m < n,所以至少会有两个数字,所以最低位相与结果一定是0
  - 当 m == n 的时候,很明显,结果就是m了
* 解决了低位的问题,我们只需要把 m 和 n 同时右移一位.然后继续按照上边的思路考虑新的最低位的结果即可
* ==此题本质:比较的其实是m和n从左侧起,最长的相同部分==

### 202、快乐数[Easy]

* 反复求和,结果记录下来,
* 如果结果第二次被记录,那就陷入死循环了,直接false

### 203、移除链表元素[Easy]

* 从头到位遍历
* 两个指针,一个指针指向源链表,一个指向目标链表
* 遇到相同的就跳过 

### 204、计数质数[Easy]

$\color{red}{技巧性}$

* res初始化成1,非质数置成0
* i,j循环(j最大是(n-1)//i),res[i * j]置成0
* 质数的位置都是1,然后求和就是个数

### 205、同构字符串[Easy]

$\color{red}{技巧性}$

* 两个字典key是自己当前字符,value是对方字符
* 相互指直到指向不一致

### 206、反转链表[Easy]

* 左边的子串记录下来
* 往右的串的位置要记录下来

### 207、课程表[Medium]

==特殊场景的深度优先搜索==

* 先建立前后关系的大List[List]
* flags标志
```
 0:未访问 
 1:已被当前节点启动的访问
-1:已被其他节点启动的访问
```
* 深度搜索
  - flags[i] == -1:已经被其他点包括进去了,返回True
  - flags[i] ==  1:第二次碰到这个点,存在环,返回False
  - 对前后关系列表进行下一个课进行遍历,同时更改flags





### 209、长度最小的子数组[Medium]

* 滑动窗
* 一直往右滑动并累加值
* 一旦超过目标s,滑动窗左指针往右,并在累和上减去左边值

### 210、课程表II[Medium]

看懂,写不出

* 和207、课程表类似
* 主要采用flags标志,同时dfs返回是否有环





### 213、打家劫舍II[Medium]

* 奇偶串nums[0:-1]和nums[1:]取大即可
* 两个指针,一个now、一个prev

### 214、最短回文串[Hard]

* 暴力法
  - s反转成r,匹配r的后部分边和s的前部分边
  - 两部分重合之外还有一部分r[:i]+s
* 双指针法
  - [解答](https://leetcode-cn.com/problems/shortest-palindrome/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--44/)
* KMP
  - 没看懂


### 215、数组中的第K个最大元素[Medium]

==快排==

* 类似二分法
* 在排序算法中,先找一个参照值(可以为数组尾值)
* 循环范围,比参照大的都移到左边去,最后参照值也拉倒左边去
* 判断左边的个数够没(从0开始到k-1,共k个)
  - 够了:找到了
  - 不够:往右边搜索
  - 超了:往左边搜索

### 216、组合总和III[Medium]

==深度优先搜索==

* 终止条件: 剩下的目标为0并且长度符合
* 从start->10去搜索,并添加元素入path
* 剪枝条件: 目标小于0了;长度超了;或者遍历的值超过10了

### 217、存在重复元素[Easy]

* 判断set长和原长是不是一样




### 219、存在重复元素II[Easy]

==哈希表==

* 建立哈希表,判断是不是存在相同并且距离小于k

### 220、存在重复元素III[Medium]

==牛逼了,看懂写不出==

* 桶思想
* 设置一个桶的大小是$t+1$, num//bucket_size为桶的位子
  - 若已经有元素,返回True
  - 否则把当前值放到桶中
  - 值的前后覆盖,确保当前是最新的
* 同时检查前后桶满不满足要求
* **如果不构成返回条件,那么当i >= k 的时候就要删除旧桶了,以维持桶中的元素索引跟下一个i+1索引只差不超过k**
* ==也就是说,当前存在的桶都是满足索引差的==

### 221、最大正方形[Medium]

==动态规划==

* 判断边长,结果就是最大边长的平方
* $matrix[i,j] == "1", dp[i,j] = min(dp[i - 1,j], dp[i,j - 1], dp[i - 1,j - 1]) + 1$
* $matrix[i][j] == "0", dp[i,j] = 0$

### 222、完全二叉树的节点个数[Medium]

* 直接法[不一定完全二叉树,通用]
  - 递归1+左右子树
* 间接法
  - 计算左子树深度(h_l),一直left就行
  - 计算右子树深度(h_r),第一步right,之后一直left
  - 最后一层停止在左子树还是右子树
  - h_l与h_r相同,左满了($2^{h\_l}$-1),右边递归
  - h_l比h_r大一,右边满了($2^{h\_r}$-1),左边递归
  - 返回左右子树节点和+1

### 223、矩形面积[Medium]

* 两个矩形减去IOU
* IOU可能为0,不存在相交面积

### 224、基本计算器[Hard]

* 遍历,会遇到(数字、'+'、'-'、'('、')')五种可能:
  - 遇到数字,往后取到这个数字为止,乘以符号加到结果上
  - 遇到加减号,符号修改为+-1
  - 遇到'(',当前的结果和符号压入栈中,**此时的符号其实是对括号里面的结果的操作**,res和sign 重置
  - 遇到')',符号和结果取出来运算
* 因为取数字的时候可能有多位,所以不能用for 语句,用while语句
* 每次遍历索引会加1,取数字不满足while的时候此时的i已经不是数字,需要回退一步,和后边加1对冲

### 225、用队列实现栈[Easy]

==用C重新理解==

* 用一个list
* 尾部压入,尾部弹出

### 226、翻转二叉树[Easy]

* 递归调用翻转函数
* 树的右枝用左边的翻转去替换




### 228、汇总区间[Medium]

* 从左往右,建立两个指针
* 如果相连两个差小于1,右指针右移动
  - 两个指针位置一样:单个值
  - 指针位置不一样:左指针值->右指针值

### 229、求众数II[Medium]

$\color{red}{摩尔投票法}$

* 摩尔投票法:抵消法
* 超过$⌊n/3⌋$次的元素最多有2个
* 在使用摩尔算法时,同时记录两个大多数,得到一个大多数,和一个出现次数仅次于大多数的数
* 检查它们出现的次数是否符合条件

### 230、二叉搜索树中第K小的元素[Medium]

- 方法一
  * 递归的搜索树,返回[root.left] + [root.val] + [root.right] 
  * 从排序列表中输出索引为[k-1]的值
- 方法二
  * 定义节点数计算的函数
  * 计算当前左子树的节点数
    - 数量为k-1,那么当前节点就是第k个
    - 数量大于k-1,递归到左子树
    - 递归到右子树

### 231、2的幂[Easy]

* 循环除,看余数
* $2^n$相当于二进制的移位,可以二进制化,看一个的个数是不是只有一个

### 232、用栈实现队列[Easy]

==用C重新理解==

* 用list
* 尾部压入,头部弹出

### 233、数字1的个数[Hard]

==没看懂==

* [参考](https://www.cnblogs.com/grandyang/p/4629032.html)

### 234、回文链表[Easy]

* fast,slow两个指针,一个速度2,一个速度1.
* fast到尾部,slow到中部
* slow开始向两端走
* ==前半部分需要建链表,反着走 : rev, rev.next = slow, rev==
* **重要:奇链表slow需要再走一步**

### 235、二叉搜索树的最近公共祖先[Easy]

* 从上往下找
* 如果p、q的值都比root的小,那么在左子树找;同样比root的大就在右子树找
* 否则就就是它了,返回

### 236、二叉树的最近公共祖先[Medium]

* 递归
* 若root为空或者root为p或者root为q,说明找到了p和q其中一个
* 左右子树递归的找p,q
* 若左子树找到了p,右子树找到了q,说明此时的root就是公共祖先
* 若左子树是none右子树不是,说明右子树找到了p或q

### 237、删除链表中的节点[Easy]

**题目有问题**

* 把下一个的值赋给当前
* 删除下一个(原本要删除当前这个的)

### 238、除自身以外数组的乘积[Medium]

* 从左往右 和 从右往左 各来一次
  * 从左往右:res[i] = res[i - 1] * nums[i - 1],即当前数左边的累积
  * 从右往左:res[i] * = right, right * = nums[i],right是当前数右边的累积,乘到结果上去

### 239、滑动窗口最大值[Hard]

* 双向队列,队列存索引值,左边的索引对应的值比右边的大
* 队列操作
 - 左边的索引超出了滑动窗,去掉
 - 队列填充填充大数的原则,尾部对应的值比当前的值小就去掉
 - 队列左端就是大的数,压入结果
* 注意: 结果中先后压入的可能是同一个值(队列设置导致)

### 240、搜索二维矩阵II[Medium]

* 左下角开始,往右增、往上减
  * 小了右移
  * 大了上移
* ==本质找一个点,这个点往不同的方向增减趋势不一样==





### 242、有效的字母异位词[Easy]

* 两个字典,key & value都一样就行

---

### 257、二叉树的所有路径[Easy]

==深度优先搜索==

* 终止条件:没有子节点
* 用箭头将结果join在一起

### 258、各位相加[Easy]

* 将数字转化成字符数组,相加. 直到加出来的数字小于10

### 260、只出现一次的数字III[Medium]

* 先得到这两个数的异或(x^y) 这个结果肯定不为0
* 上述结果值按二进制位进行判断(先找出一个是1的位置)
* 如果num并这个数
  * 0:这是一类,类内只有一个数出现了一次  
  * 1:这是一类,类内只有一个数出现了一次 
* 转化成前面的题





### 263、丑数[Easy]

* 一直除以2、3、5除到不能整除

### 264、丑数II[Medium]

==想法很好==

* 只找丑数的值,(一个基数乘以2、3、5得来)
* ugly[i2]\*2 , ugly[i3]\*3 ,ugly[i5]\*5中的最小为连着的丑数
* i2、i3、i5指针跟着走

### 268、缺失数字[Easy]

$ \frac{n(n+1)}{2} - \sum(List) $






### 274、H指数[Medium]

* H值从0开始增加,一直增到数组长度(文章篇数)
* 被引列表先排序
* $citations[len(citations)-1-i]>i$ : 意思是从高引往回数$i$篇,看这篇的被引数是不是大于现在遍历到的H值

### 275、H指数II[Medium]

* 同274
* 不需要排序

### 278、第一个错误的版本[Easy]

* 二分法
* 边界好烦

### 279、完全平方数[Medium]

==Lagrange 四平方定理: 任何一个正整数都可以表示成不超过四个整数的平方之和.==

* $dp[i]$表示i最少可以由几个平方数构成
* 初试化$dp=[0,1,2,\cdots,n]$,长度为$n+1$,最多次数就是全由1构成
* 遍历dp,对于i,遍历区间$[2,n+1)$
  - 遍历所有平方数小于i的数j,遍历区间$[1,int(\sqrt{i})+1)$
  - $dp[i]=min(dp[i],dp[i−j∗j]+1)$
  - 始终保存所有可能情况中的最小值






### 283、移动零[Easy]

- 方法一
  * 记录0的位置,再一边删0一遍补0
- 方法二
  * 从前往后,非0的地方$nums[j] = nums[i],j+=1$
  * j 到nums尾部置0


### 287、寻找重复数[Medium]

==二分法==

* 数组值域的范围[0,n-1]
* 二分法:遍历数组,统计小于等于mid的个数
  * 个数大于mid,说明重复的值在左边
  * 否则重复值在右边

### 289、生命游戏[Medium]

* 方法一:使用卷积的思想
  - 拷贝出一个矩阵并在四周填充一圈0
  - 使用卷积核$\begin{bmatrix}
              1 & 1 & 1\\ 
              1 & 0 & 1\\ 
              1 & 1 & 1
              \end{bmatrix} $
  - 如果该位置是1(活的),并且卷积和<2或>3,则置0(死)
  - 否则判断卷积和是3,则置1(活)
* 方法二:两次遍历
  - 写个数个数的函数,原来活的都计入进去(1,-1)
  - 第一次遍历时也是分两种情况：
    - 若活细胞变成了死细胞,由1->-1
    - 若死细胞变成了活细胞,由0->2
  - 第二次遍历则是将2(活)->1, -1(死)->0

### 290、单词规律[Easy]

- 方法一
  * 看索引一不一样
- 方法二
  * 一一对应
  * 第一步 key为pattern, value为words, 遍历pattern, 检查同一个patten是否对应相同的word
  * 第二步 key为words, value为pattern, 遍历words, 检查同一个word是否对应相同的patter

### 292、Nim游戏[Easy]

==智力题==

* n不是4的余数就赢,是就输 




### 295、数据流的中位数[Hard]

* 维护大小顶堆 分为大小部分
* 堆顶元素是最小的元素 一个堆用负值压入
* 偶数就取平均 奇数就取其中一个堆的堆顶




### 297、二叉树的序列化与反序列化[Hard]

* 广度优先搜索


### 299、猜数字游戏[Easy]

* 遍历,secret和guess相等的位置A就加一
* 第一轮遍历建立字典,记录secret中出现的数字
* 第二轮遍历guess数字在字典里并值大于0的,B就加一并更新字典(减一)
* B最后需要减去A的部分(b -= a)

### 300、最长上升子序列[Medium]

- 方法一:动态规划
  * 两层循环,外循环遍历元素,内循环遍历[0,i)区间
  * 如果内循环值比外循环值小,执行动态规划
  * $dp[i] = max(dp[i] , dp[j] + 1 ),0\leq j < i$
- 方法二 $\color{red}{技巧性}$
  * 新建数组,用于保存最长上升子序列
  * 对原序列进行遍历,将每位元素二分插入数组中.如果数组中元素都比它小,将它插到最后,否则用它覆盖掉比它大的元素中最小的那个. eg. [1,2,3,5,4],将4覆盖掉5,升序长度为4
  * 这样数组未必是真实的最长上升子序列,但长度是对的

---






### 303、区域和检索-数组不可变[Easy]

* 累加值新建成一个数组
* 累和减累和(如前五个减前三个,就是中间两个的和)

### 304、二维区域和检索-矩阵不可变[Medium]

* 初始化时候在新建和矩阵(比原矩阵多一行多一列)
* 新的矩阵代表从左上角开始的位置到(row,col)覆盖的矩阵元素和:可以递推的构建
* $sums[i][j] = matrix[i-1][j-1] + sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1]$
* 调用函数访问:$sums[row2][col2] - sums[row2][col1-1] - sums[row1-1][col2] + sums[row1-1][col1-1]$
* 注意和矩阵和原矩阵索引差个1

### 306、累加数[Medium]

* 题意解读:确认前两个数字,后面即被确认
* 思路:遍历前两个数字,优化是遍历不超过num_str的一半即可
* 限制:开头不可为0--->但有'000'的情况,len(num)至少为3
* 先生成num1和num2,这两个不能是0开头的数字(单独0可以)
* 再由num1和num2生成后面的,递推的判断合法与否








### 309、最佳买卖股票时机含冷冻期[Medium]

* cool[i]就是sale[i-1]的状态,因为冷冻期的上一个状态一定是卖出
* sale[i]:
  - 在sale[i-1]之前卖出了
  - sale[i]的时候卖出
  - 就是考虑当天是否要或者可以卖出
* buy[i]考虑今天是否买入
  - 如果今天买入就是用上一次冷冻期的价格减去当天的股票交易
  - 因为从上一次冷冻期开始到此次买入之间不会存在其他交易,
  - 如果此次不买入,则价格就为上一次的买入价格










### 313、超级丑数[Medium]

* 和丑数2类似,只不过指针需要定义多个,定义成和primes等长的数组











### 319、灯泡开关[Medium]

==智力题==

* 平方数




### 322、零钱兑换[Medium]

==动态规划== 
**背包问题**

* $dp[j] = min(dp[j], dp[j - coin] + 1)$
* 遍历硬币值,当前硬币值下只能影响大于硬币值的 dp
* 当$f(amount)>amount$ 无解,返回-1

### 324、摆动排序II[Medium]

$\color{red}{技巧性}$

* 排序
* 大的一半和小的一半奇偶排序 

### 326、3的幂[Easy]

* 循环除,看余数
* $3^n$的最大可能除以输入,看能不能整除




### 329、矩阵中的最长递增路径[Hard]

==深度优先搜索==

* 一个等大的矩阵cache用于记录每个点的最长递增路径的长度
* 主函数循环矩阵位置,计算长度并更新最大值
* dfs函数搜索4个方向,记录最大长度
* 最大长度一方面赋值给矩阵cache,一方面返回
* **终止条件即cache位置有值**
* 写法比较特殊



### 335、路径交叉[Hard]

==画图,场景有限.看懂写不出==

* [图解](https://leetcode-cn.com/problems/self-crossing/solution/335lu-jing-jiao-cha-by-zhangll/)








### 342、4的幂[Easy]

* 循环除,看余数
* $4^n$类如下面,先考虑是不是100...00的结构,再看后面0的个数是偶数(4的倍数)
```
# bin(4**0) '0b1'
# bin(4**1) '0b100'
# bin(4**2) '0b10000'
# bin(4**3) '0b1000000'
```

### 343、整数拆分[Medium]

- 方法一(dp)
  * $i$ 可以拆分成$j$ 和$i-j$
  * 判断$i-j$还要不要继续拆分 即 max(i-j,dp[i-j])
  * $dp[i] = max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]) )$
- 方法二(贪心)
  * 根据数学推导可得需要更多的3的段
    - 余数是0：$3^a$
    - 余数是1：3段 + 2 段+ 2段 (2 * 2>3 * 1) $3^{a-1} * 4 $
    - 余数是2：3 段 2 段 $3^a * 2 $

### 344、反转字符串[Easy]

* 两侧往中间靠

### 345、反转字符串中的元音字母[Easy]

* 两侧往中间靠






### 349、两个数组的交集[Easy]

* set的并

### 350、两个数组的交集II[Easy]

* 数组排序
* 两个数组分别给一个指针,从头遍历
* 值相同的时候指针都往右移,否则小的那个右移

---







### 354、俄罗斯套娃信封问题[Hard]

==LIS(最长上升子序列)==

* 300题最长上升子序列 的二维形式
* **按w升序,h降序排列**,找h上最长递增子序列的长度
* eg. [ [1,5],[1,4],[1,2],[2,3] ],则提取h为[5,4,2,3].对h进行LIS算法将得到[2,3]
* ==在L中查找x,x存在时返回x左侧的位置,x不存在返回应该插入的位置==,使用(from bisect import bisect_left)










### 367、有效的完全平方数[Easy]

* 二分查找,逐步逼近mid位置,再判断是不是能 $ x * 2 = num$
* 收敛法 $ x = \frac{1}{2}(x+\frac{num}{x}) $ 收敛下去就是$\sqrt{num}$.而且这个过程$x>\sqrt{num}$,即正向收敛过来

### 368、最大整除子集[Medium]

==特殊的动态规划==

* 先按顺序排序
* dp,每个元素填充单个nums的值
* $nums[i]\%nums[j] == 0$(i在j右边),并且$len(dp[j])+1 > len(dp[i])$更新
  - $dp[i] = dp[j] + [nums[i]]$
* 返回最长的dp元素





### 371、两整数之和[Easy]

**二进制运算** 看懂写不出







### 374、猜数字大小[Easy]

* 二分查找,用函数返回值判断











### 383、赎金信[Easy]

==哈希表==

* 遍历杂志建字典
* 遍历绑架信减去字典








### 386、字典序排数[Medium]

==深度优先搜索==

```
class LargerNumKey(int):
    def __lt__(x, y):
        return str(x) < str(y)
```

* 方法一
  - 自定义排序规则,整形转化字符串进行比较(字符串逐位比较)
* 方法二:dfs
  - 从1->10各自进行搜索,结果就是[1,1x,1xx,2,2x,...]
  - 在搜索时,如i,搜索$10*i+d$
  - 终止条件:搜索值需要小于n,要是超过了,深搜也停止


### 387、字符串中的第一个唯一字符[Easy]

* 遍历建字典
* 按索引遍历,按索引值判断是不是只有一个








### 393、UTF-8编码验证[Medium]

==烦==

* cnt表示后面接几个字节字符
* cnt 从0到0表示一个字符
* cnt为0时候表示在字符头,数据进行移位判断它表示的是几位字节字符,cnt设置为后面跟几个字节字符
* cnt不是0的话判断后面跟着的是不是10开头,并递减
* 遍历完之后看cnt是不是0,是0的话就是合理的









---


### 400、第N个数字[Medium]

* [图解](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/)
* 起点 区间的数字的位数 区间的个数
* 更新区间
* 判断n对应的数字是多少
* 判断n对应的当前数字是哪一位




### 410、分割数组的最大值[Hard]

* 先编写计算函数,在最大值是val情况下,需要多少次
* 二分查找,left,right 分别是单个最大,整体和
* 查阅的次数大于设定m,那就left右移动(mid+1)



### 414、第三大的数[Easy]

* 取set去重复
* 短于3的话返回最大的数
* 排序后返回List[-3]

### 415、字符串相加[Easy]

* 大数相加
* 逐位相加

### 416、分割等和子集[Medium]

==动态规划==
**背包问题**

* 两子集相等,只要找到一个集合是其一半就行
* 转化成子集中找目标值(target//2)
* 动态规划:横列代表求得的值和索引到的nums
* 遇到一个数,只有加/不加两种情况:$dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]$








### 432、全O(1)的数据结构[Hard]

* 字典 




### 434、字符串中的单词数[Easy]

* 连续两个字符一个空一个非空







### 442、数组中重复的数据[Medium]

* 取出每个数字的绝对值x,检查索引为x-1位的数字,若此数字已经为负,则这是x第二次被访问,将其加入返回数列,若此数字还是正,则这是x第一次访问,将索引为x-1位的数字取负

### 443、压缩字符串[Easy]

* 两个变量
 - 一个跟踪字符往后移动
 - 一个跟踪写入的位置







### 448、找到所有数组中消失的数字[Easy]

* 直接判断会时间溢出
* 对出现过的值的位置反转(* = -1),那大于0的位置就是没出现过的









---



### 470、用Rand7()实现Rand10()[Medium]

* (Rand7()-1) * 7得到的范围{0,7,14,21,28,35,42}
* Rand7()得到的范围{1,2,3,4,5,6,7}
相加得到的范围1-49,均匀
* 去除超过40的部分,1-40中选一个映射到1-10





### 474、一和零[Medium]

==二维动态规划== 
**背包问题**
不太懂,写不出

* $dp(i, j) = max(1 + dp(i - cost\_zero[k], j - cost\_one[k])) \quad i >= cost\_zero[k] \& j >= cost\_one[k]$





















### 485、最大连续1的个数[Easy]

* 遇到0就重新统计一下,遇到1就累计值
















### 494、目标和[Medium]

==动态规划== 
**背包问题**

* 相当于取一部分值,使其和为$\frac{sum+S}{2}$
* 创建数组,含义是和为i的个数为mem[i],当前值的时候,mem[i] += mem[i-num]









---




### 509、斐波那契数[Easy]

* 常规迭代


### 518、零钱兑换II[Medium]

==背包问题==

* coin硬币可以使用或者不使用
* $dp[j] += dp[j-coin]$
















### 532、数组中的K-diff数对[Easy]

==哈希表==

* 建立字典,{val:number}:
  k < 0,提前去掉
  k = 0,number>1的个数
  k > 0,判断num-k的个数是不是大于0的











### 541、反转字符串II[Easy]

==递归==

* 大于2k长的先拉2k长出来
* 小于k全部反转
* 大于k,小于2k反转前面部分

















### 547、朋友圈[Medium]

==深度优先搜索==

- 方法一
  * 建立数组表示每个人是否被包括,遍历每个人,遍历到过置1
  * 等于1表示被别的圈包进去了,等于0表示再开一个圈
  * 开圈的时候深度优先搜索,遍历所有人,$j != i and visited[j] == 0 and M[i][j] == 1$ 表示$i,j$是一个圈的,递归的包括下去
  * **此题不需要终止条件**
- 方法二
  * 建立列表,不同位置放置一个set,eg. (1,2,3)
  * 建立索引搜索函数,输入目标元素,返回所在集合在列表中的索引
  * 遍历矩阵,遇到1的时候查认识的两个人在列表里的索引,不存在就返回-1
  * 两个人都不在,列表加新元素
  * 其中一个在,将另一个添加上去
  * 两个都在:若两个相同pass;若两个不同,一个union到另一个上去,消灭当前这个

---

### 551、学生出勤记录I[Easy]

* 遍历












### 557、反转字符串中的单词III[Easy]

* 按空格拆分成列表
* 列表分别反转
* 用空格join在一起





### 560、和为K的子数组[Medium]

==字典去重法==

* 初始化字典{0:1},表示累加和为0,出现了1次
* 遍历数组,数组更新累加和sum
* 若sum−k存在于字典中,说明存在连续序列使得和为k,res += dict[sum-k]
* 更新字典








### 561、数组拆分I[Easy]

* 取顺序排列后的奇数就行















### 566、重塑矩阵[Easy]

* dst的(r,c) <--> src的(r,c)对应

### 567、字符串的排列[Medium]

==滑动窗==

* s1、s2串的字母对消
* 建一个26个值的数组list,记录对消结果(可能是1,-1,0等)
* 通过滑动窗滑动更新对消结果
* 对消之后全都是0就返回 True
* 建两个数组进行对比也行



### 575、分糖果[Easy]

* 糖果样数和糖果数量的一半,两个值取小





### 581、最短无序连续子数组[Easy]

* 拷贝出来一组数据,排序
* 两端向中间移动,判断是不是改值了,改了那就不是





























---












### 605、种花问题[Easy]

* 边界连着两个是0
* 非边界连着三个是0,就能种
* 可以在两边补两个0代替边界



















### 628、三个数的最大乘积[Easy]

* 最大值可能两个情况出现,取大
  - 最后三个
  - 最后一个和最前面两个(负的)





### 638、大礼包[Medium]

==深度优先搜索==

* 终止条件:needs降到全0就买完了
* 一个一个买,某个产品需求减一,价格加上对应的价格
* 买套装,加上套装价格

这种想法超时,优化:

* 一个一个买换成全部都是单独买,计算一个总价格,然后对比
* 对需求建个全局字典,记录.避免重复递归计算





### 643、子数组最大平均数I[Easy]

* 滑动窗,判断窗口值是否最大,更新







---








### 661、图片平滑器[Easy]

* ==它和图像中值滤波不同,边缘是/1 /4等的,不全是/9==
* 遍历坐标点,在当前点前后链接的3位中累和,并计数
* 边缘条件好烦,可以利用是否越界判断






### 665、非递减数列[Easy]

* 判断是否出现逆序
  判断nums[i-1] <= nums[i+1]
  - 变相去掉nums[i]
  - 变相去掉nums[i+1]

















### 674、最长连续递增序列[Easy]

* 递增就加,不增就重新计数







### 680、验证回文字符串Ⅱ[Easy]

* 删掉之后看一不一样







### 695、岛屿的最大面积[Medium]

==特殊场景下,深度优先搜索==

* 遇到1深度搜索一次
* 终止条件: 越界或者遇到0
* 自己置成0,向四周延伸 
* 与之前的深度搜索区别: **此处的返回值不是路径或者res,需要返回数量.定义数量然后加上迭代值. 终止时返回0**





---






### 754、到达终点数字[Medium]

```
步数        能到达的位置
1:          1
2:          3, 1
3:          6, 4, 2, 0
4:          10, 8, 6, 4, 0
5:          15, 13, 11, 9, 7, 5, 3, 1
...
max(f(n)) = max(f(n-1)) + n
f(n) = [max(f(n)),  max(f(n)) - 2, max(f(n)) - 4, ....]
```
* 每一步能到达的最大位置是上一步最大位置加上步数,而每一步所能达到的位置之间间隔都为2
* 如果target可以在第n步达到,那么target一定小于等于max(f(n))且max(f(n))与taget同奇同偶 




###　796、旋转字符串[Easy]

* 字符串Ａ在两倍字符串Ｂ里面　
* 同时两段等长












---






### 836、矩形重叠[Easy]

- 排除四种情况即可:
  * rec1的右边在rec2的左边
  * rec1的上边在rec2的下边
  * rec1的左边在rec2的右边
  * rec1的下边在rec2的上边







---



### 885、螺旋矩阵III[Medium]

* 四个方向搜索,可分为两部分
  - 一部分x y 先后增加
  - 一部分x y 先后减少
* 在范围内添加到结果里面










### 874、模拟行走机器人[Easy]

* 北 东 南 西 四个方向 顺时针描述
* 左右转分别是di = (di + 3)%4 di = (di + 1)%4
* 否则就是多步模拟前进,一旦遇到障碍就停止
* list转成set可以省时





### 887、鸡蛋掉落[Hard]

没看懂

* 状态可以表示成 $(K,N)$, $K$ 为鸡蛋数,$N$ 为楼层数
  - 如果鸡蛋不碎,那么状态变成 $(K,N−X)$
  - 我们鸡蛋的数目不变,但答案只可能在上方的 $N−X$ 层楼了
  - 如果鸡蛋碎了,那么状态变成 $(K−1,X−1)$
  - 我们少了一个鸡蛋,但我们知道答案只可能在第 $X$ 楼下方的 $X−1$ 层楼中了
* $d p(K, N)=1+\min _{1 \leq X \leq N}(\max (d p(K-1, X-1), d p(K, N-X)))$
* 二分查找




### 889、根据前序和后序遍历构造二叉树[Medium]

* 前序遍历为：(根结点) (前序遍历左分支) (前序遍历右分支)
* 后序遍历为：(后序遍历左分支) (后序遍历右分支) (根结点)
* 查索引的时候是查第二个点





---


### 946、验证栈序列[Medium]

* 遍历压栈列表
* 判断栈顶和弹出列表头是否相同,同就弹出






---



### 974、和可被K整除的子数组[Medium]

* $(sums[j] - sums[i-1])\%K == 0$,同余定理$sums[j]\%K == sums[i-1]\%K$
* 从左往右求累和,并取K的余数
* 建立字典{余数:个数}
* 个数中两两组合就是子序列区间数$C_n^2 = \frac{n(n-1)}{2} $



---




### 1015、可被K整除的最小整数[Medium]

==数学题==

- 一方面:
设$x = pk+q \Rightarrow x\%k = q \\
x_{i+1}=10x_i+1\Rightarrow x_{i+1}\%k=(10x_i+1)\%k =(10(pk+q)+1)\%k = (10q+1)\%k \xrightarrow[]{x_i \%k = q} = (10x_i \%k+1)\%k \\
 \Rightarrow \color{red}{(10x_i+1)\%k = (10x_i \%k+1)\%k}
$
所以$x * 10 + 1$和$(x \% K) * 10 + 1$在后续判断$x \% K != 0$时是没有任何区别的
- 另一方面:
考虑==死循环==:$(s_i * 10 + 1)\%k = (s_j * 10 + 1)\%k \Rightarrow s_i-s_j = \frac{tk}{10} \in [0,k](s_i,s_j在处理过程中有\%操作)$
所以$\color{red}{t\in [0,10].k=2或5时有t使其死循环.所以不能整除的关键在于分母10}$

* 是2或5的倍数就返回-1
* $temp = (temp \% K) * 10 + 1$迭代公式
* 一直到 $temp \% K != 0$

---

### 1109、航班预订统计[Medium]

* 为每个航班人数定义计数器列表
* 上车加、下车减的原则.计数器为(1,1,0,0,-1,-1)形式
* 从头到尾累和























### 1147、段式回文[Hard]

==贪心==

* 左右指针,往中间走
* 如果两个子串相同,段数加2
* 注意奇数位的情况或者偶数位但是str1不为空情况加一段





---


### 1293、网格中的最短路径[Hard]

==广度优先搜索==

* 用三元组 (x, y, rest)(位置,剩下能遇障碍物个数) 表示一个搜索状态. 初始状态 (0, 0, k)
* 再来一个记录走过的位置visited
* 对于当前的状态 (x, y, rest),它可以向最多四个新状态进行搜索
  - 如果该位置为障碍物,那么新的状态为 (mx + dx, my + dy, rest - 1)
  - 新的状态为 (mx + dx, my + dy, rest)
* 优化:考虑一条从 (0, 0) 向下走到 (m - 1, 0) 再向右走到 (m - 1, n - 1) 的路径,它经过了 m + n - 1 个位置,其中起点 (0, 0) 和终点 (m - 1, n - 1) 没有障碍物,那么这条路径上最多只会有 m + n - 3 个障碍物.因此我们可以将 k 的值设置为 m + n - 3 与其本身的较小值 min(k, m + n - 3)








































