# def longestCommonSubsequence(text1, text2):
#     """
#     :type text1: str
#     :type text2: str
#     :rtype: int
#     """
#     if len(text1) == 0 or len(text2) == 0:
#         return ''
#
#     res = 0
#     return digui(text1, len(text1) - 1, text2, len(text2) - 1, res)

def digui(text1, n, text2, m, res):

    if n == -1 or m == -1:
        return res

    if text1[n] == text2[m]:
        res = digui(text1, n - 1, text2, m - 1, res) + 1

    else:
        res += max(digui(text1, n - 1, text2, m, res), digui(text1, n, text2, m - 1, res))

    return res

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


text1 = "ylqpejgqee"
text2 = "yrkzavgdgsae"
res = 0
# print(digui(text1, len(text1) - 1, text2, len(text2) - 1, res))
print(df(text1, text2))