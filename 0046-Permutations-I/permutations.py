import numpy as np

'''
给定不重复的一组数字array, 给出它的所有全排列组合
利用全排列数字的特性建立树，之后使用回溯法进行剪枝
'''

def backtrack(arr,len,depth,path,res):

    '''
    :输入数组 arr:
    :输入数组长度 len:
    :当前填充的位置 depth:
    :树结构中走过的路径 path:
    :是否被使用过的标记 used:
    :返回结果 res:
    '''
    if len == 0:
        return []
    '''方法1 使用used'''
    # for i in range(len):
    #     if depth == len:    # 递归终止条件, 当填充的数已经满时, 递归终止
    #         res.append(path[:])
    #         return
    #     if not used[i]:
    #         used[i] = True
    #         path.append(arr[i])
    #         backtrack(arr, len, depth+1,path,used,res)
    #
    #         used[i] = False
    #         path.pop()

    '''方法2 在原数组本身进行维护'''
    if depth == len:    # 递归终止条件, 当填充的数已经满时, 递归终止
        res.append(path[:])
        return
    for i in range(depth, len):
        path.append(arr[i])    # 进行选择
        arr[depth], arr[i] = arr[i], arr[depth]    # 交换 使得选择过的数值arr[i]交换到原来的第depth位置, 确保前depth位置都被选择过了
        backtrack(arr, len, depth+1,path,res)
        arr[depth], arr[i] = arr[i], arr[depth]    # 撤销选择
        path.pop()    # 撤销选择


arr = [1,2,3]
len = len(arr)
res = []
path = []

backtrack(arr,len,0,path,res)
print(res)