#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root :
            return 0
        elif not root.left:
            return 1 + self.maxDepth(root.right)
        elif not root.right:
            return 1 + self.maxDepth(root.left)
        elif root.left and root.right:
            return 1 + max(
                self.maxDepth(root.left),
                self.maxDepth(root.right)
                ) 

