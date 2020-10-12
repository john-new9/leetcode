# LeetCode 第 144 号问题：二叉树的前序遍历

题目来源于 LeetCode 上第 144 号问题：二叉树的前序遍历。题目难度为 Medium，目前通过率为 59.8% 。

### 题目描述

给定一个二叉树，返回它的 *前序* 遍历。

 **示例:**

```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
```

**进阶:** 递归算法很简单，你可以通过迭代算法完成吗？

### 题目解析

用**栈(Stack)**的思路来处理问题。

前序遍历的顺序为**根-左-右**，具体算法为：

- 把根节点 push 到栈中
- 循环检测栈是否为空，若不空，则取出栈顶元素，保存其值
- 看其右子节点是否存在，若存在则 push 到栈中
- 看其左子节点，若存在，则 push 到栈中。



### 动画描述

![Animation](F:\project\leetcode\0144-Binary-Tree-Preorder-Traversal\Animation.gif)

### 代码实现

**普通迭代版本——Java 实现**

```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        //非递归前序遍历，需要借助栈
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> list = new LinkedList<>();
        //当树为空树时，直接返回一个空list
        if(root == null){
            return list;
        }
        //第一步是将根节点压入栈中
        stack.push(root);
        //当栈不为空时，出栈的元素插入list尾部。
        //当它的孩子不为空时，将孩子压入栈，一定是先压右孩子再压左孩子
        while(!stack.isEmpty()){
            //此处的root只是一个变量的复用
            root = stack.pop();
            list.add(root.val);
            if(root.right != null) stack.push(root.right);
            if(root.left != null) stack.push(root.left);
        }
        return list;
    }
}
```

**普通迭代版本——python实现**

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        stack = [root]

        while(stack):    # 在栈变空前反复循环
            temp = stack.pop()
            result.append(temp.val)   # 先弹出并访问根节点
            if temp.right:     # 右孩子先进后出
                stack.append(temp.right)
            if temp.left:      # 左孩子后进先出
                stack.append(temp.left)
        return result

```

**普通迭代版本——C++实现**

```c++
 
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> s;
        if (!root)    // 退化情况
            return ans;

        s.push(root);
        while(!s.empty()){
            TreeNode* r=s.top();
            s.pop();
            ans.push_back(r->val);    // 对根节点进行访问,之后先压入右孩子，再压入左孩子
            if (r->right)  s.push(r->right);
            if (r->left)  s.push(r->left);     
        }
        return ans;
    }
};
```

**改进版本——python实现** 沿左侧分支从上而下**访问**，之后对于右子树从下而上进行**遍历**

```python
# 定义该函数一直沿着沿左侧分支从上而下访问，同时将右孩子压入栈中
def visitalongvine(root,stack,result):
    while(root):
        result.append(root.val)
        stack.append(root.right)
        root = root.left

# 主函数，从root开始，一只调用上个函数，之后对于右子树从下而上进行遍历
class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []
        result = []
        stack = [root]
        while(stack):    # 在栈变空前反复循环
            visitalongvine(root,stack,result)
            root = stack.pop()
        return result
```




