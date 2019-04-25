# 0-1背包问题
# 递推关系: c[i][m]=max{c[i-1][m-w[i]]+p[i] (m>w[i]), c[i-1][m]}
# 参考链接: https://blog.csdn.net/superzzx0920/article/details/72178544

# n：物品件数；c:最大承重为c的背包；w:各个物品的重量；v:各个物品的价值
# 第一步建立最大价值矩阵(横坐标表示[0,c]整数背包承重):(n+1)*(c+1)
# 技巧:python 生成二维数组(数组)通常先生成列再生成行


def bag(n, c, w, p):
    res = [[-1 for _ in range(c+1)]for _ in range(n+1)]
    for j in range(c+1):
        # 第0行全部赋值为0，物品编号从1开始.为了下面赋值方便
        res[0][j] = 0
    for i in range(1, n+1):
        for j in range(1, c+1):
            res[i][j] = res[i-1][j]
            # 生成了n*c有效矩阵，以下公式w[i-1],p[i-1]代表从第一个元素w[0],p[0]开始取。
            if j >= w[i-1] and res[i-1][j-w[i-1]] + p[i-1] > res[i][j]:
                res[i][j] = res[i-1][j-w[i-1]] + p[i-1]
    return res


# 以下代码功能：标记出有放入背包的物品
# 反过来标记，在相同价值情况下，后一件物品比前一件物品的最大价值大，则表示物品i#有被加入到背包，x数组设置为True。设初始为j=c。
def show(n, c, w, res):
    print('最大价值为:', res[n][c])
    x = [False for _ in range(n)]
    j = c
    for i in range(1, n+1):
        if res[i][j] > res[i-1][j]:
            x[i-1] = True
            j -= w[i-1]
    print('选择的物品为:')
    for i in range(n):
        if x[i]:
            print('第', i, '个')


# 最小路径和
# 题目地址: https://leetcode-cn.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid):
        r = len(grid)
        c = len(grid[0])
        path = [[0] * c for _ in range(r)]
        path[0][0] = grid[0][0]  # save the sum of each position
        for _r in range(1, r):
            path[_r][0] = path[_r - 1][0] + grid[_r][0]
        for _c in range(1, c):
            path[0][_c] = path[0][_c - 1] + grid[0][_c]
        for _r in range(1, r):
            for _c in range(1, c):
                path[_r][_c] = min(path[_r - 1][_c], path[_r][_c - 1]) + grid[_r][_c]

        return path[r - 1][c - 1]


    # 莱文斯坦最短编辑距离
    # 题目地址: https://leetcode-cn.com/problems/edit-distance/
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)

        steps = [[0 for _ in range(w2 + 2)] for _ in range(w1 + 2)]  # the first position represent space
        # w1=a w2=sc
        #   #  s c
        # # 0  1 2
        # a 1  1 2

        for i in range(w1 + 1):
            steps[i][0] = i
        for j in range(w2 + 1):
            steps[0][j] = j
        for i in range(1, w1 + 1):
            for j in range(1, w2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    steps[i][j] = steps[i - 1][j - 1]
                else:
                    steps[i][j] = 1 + min(steps[i - 1][j - 1], min(steps[i][j - 1], steps[i - 1][j]))  # representing replace、delete and add

        return steps[w1][w2]

    # 最长上升子序列
    # 题目链接: https://leetcode-cn.com/problems/longest-increasing-subsequence/
    # dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    # 那么题目要求的，就是这个 dp 数组中的最大者
    # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例：
    # dp 的值： 1  1  1  2  2  3  4    4
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# 最长公共子序列
# 求两个字符串的最大公共子序列（可以不连续）的长度，并输出这个子序列。
# 例如：
# 输入 googleg 和 elgoog 输出 goog 4
# 输入 abcda 和 adcba 输出 aba 3
# 参考:
# https://blog.csdn.net/zszszs1994/article/details/78208488
# https://www.cnblogs.com/AndyJee/p/4465696.html

def longest_common_subsequence(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    res = []
    dp = [[0 for _ in range(l2+2)] for _ in range(l1+2)]

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # res.append(s1[i-1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 记录最长公共子序列
    for i in range(1, l1 + 1):
        if dp[i][j] > dp[i - 1][j]:
            res.append(s1[i-1])

    return dp[l1][l2], ''.join(res)


if __name__ == '__main__':
    n = 5
    c = 10
    w = [2, 2, 6, 5, 4]
    p = [6, 3, 5, 4, 6]
    res = bag(n, c, w, p)
    show(n, c, w, res)
    print(longest_common_subsequence('googleg', 'elgoog'))

