# LeetCode 第 94 号问题：二叉树的中序遍历

题目来源于 LeetCode 上第 94 号问题：二叉树的中序遍历。题目难度为 Medium

### 题目描述

给定一个二叉树，返回它的*中序* 遍历。

**示例:**

```
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
```

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

### 题目解析

用**栈(Stack)**的思路来处理问题。

中序遍历的顺序为**左-根-右**，具体算法为：

- 从根节点开始，先将根节点压入栈
- 然后再将其所有左子结点压入栈，取出栈顶节点，保存节点值
- 再将当前指针移到其右子节点上，若存在右子节点，则在下次循环时又可将其所有左子结点压入栈中



### 动画描述

![](https://blog-1257126549.cos.ap-guangzhou.myqcloud.com/blog/v17b8.gif)

### 代码实现

**java版本实现**

```java
class Solution {
        public List<Integer> inorderTraversal(TreeNode root) {
            List<Integer> list = new ArrayList<>();
            Stack<TreeNode> stack = new Stack<>();
            TreeNode cur = root;
            while (cur != null || !stack.isEmpty()) {
                if (cur != null) {
                    stack.push(cur);
                    cur = cur.left;
                } else {
                    cur = stack.pop();
                    list.add(cur.val);
                    cur = cur.right;
                }
            }
            return list;
        }
}
```



**python版本实现**

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        S = []
        result = []
        while(True):
            if root!=None:   
                S.append(root)    # 对每一个树，左侧所有节点堆入栈中
                root = root.left    # 左侧一直向下操作
            elif S == []:   # 检测栈是否已空
                break                
            else:
                root = S.pop()    # 之后从下往上进行迭代
                result.append(root.val)    # 
                root = root.right    # 遍历右子树
        return result
```

**c++版本实现**

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
     vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode*> S;
        vector<int> v;
        TreeNode* rt = root;
        while(rt || S.size()){
            while(rt){
                S.push(rt);
                rt=rt->left;
            }
            rt=S.top();S.pop();
            v.push_back(rt->val);
            rt=rt->right;
        }
        return v;        
    }

};
```

