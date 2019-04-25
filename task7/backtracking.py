# N皇后

# 解题思路：
# 判断棋盘上某一行某一列的皇后与之前行上的皇后 是否在同列或同对角线上，
# 如果在，移动当前行的皇后至下一列,再判断是否在同列或同对角线上，如果移动到最后仍然在，则回溯到上一行，重复上述移动与判断的过程。
# 总结: 走不通，就掉头[采用深度优先的策略去搜索问题的解]


def place(x, k):  # 判断是否冲突
    for i in range(1, k):
        # x[i] == x[k]判断i行皇后与k行皇后是否在同一列
        # abs(x[i] - x[k]) == abs(i - k)判断i行的皇后与k行的皇后是否在对角线上
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):
            return False
    return True


# get one solution
def queens(n):
    k = 1   # 设置初始皇后为第一个
    x = [0 for _ in range(n + 1)]  # 设置x列表初始值为0
    while k > 0:
        x[k] = x[k] + 1  # 在当前列的下一列开始
        while x[k] <= n and not place(x, k):  # 不满足条件，继续搜索下一列位置
            x[k] = x[k] + 1
        if x[k] <= n:  # 判断是否为最后一个，不是就执行下一行
            if k == n:  # 是最后一个皇后，退出
                break
            else:  # 不是，则处理下一行皇后
                k = k + 1   # 执行下一行
                x[k] = 0    # 初始化，从第一列开始
        else:  # n列均不满足，回溯到上一行
            x[k] = 0    # 初始化列到第一列
            k = k - 1   # 回溯到上一行
    return x[1:]    # 返回1-8个皇后的位置


print(queens(4))


# problems: https://leetcode-cn.com/problems/n-queens/
# get all solutions
class Solution:
    def solveNQueens(self, n):
        res = []
        a = [0 for _ in range(n)]  # save the position of queen each row

        def back(a, k):  # k: the row to be checked
            if k >= n:
                l = []
                for pos in a:
                    s = ['.' for _ in range(len(a))]
                    s[pos - 1] = 'Q'
                    l.append(''.join(s))
                res.append(l)
            else:
                for i in range(1, n + 1):
                    a[k] = i
                    if self.is_safe(a, k):
                        back(a, k + 1)  # 递归回溯

        back(a, 0)
        return res

    # rows before k are judged with k
    def is_safe(self, a, k):  # k: the row to be checked
        for i in range(k):
            if a[i] == a[k] or abs(a[i] - a[k]) == k - i:
                return False
        return True


# 0-1背包
# 回溯法 通过采用深度优先的策略去搜索所有的可行解，取其中最优的一种解

bestV = 0
curW = 0
curV = 0
bestx = None


def backtrack(i):
    global bestV, curW, curV, x, bestx
    if i >= n:
        if bestV < curV:
            bestV = curV
            bestx = x[:]
    else:
        if curW+w[i] <= c:
            x[i] = True
            curW += w[i]
            curV += v[i]
            backtrack(i+1)
            curW -= w[i]
            curV -= v[i]
        x[i] = False
        backtrack(i+1)


if __name__ == '__main__':
    n = 5
    c = 10
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    x = [False for i in range(n)]
    backtrack(0)
    print(bestV)
    print(bestx)



# if __name__ == '__main__':
#     solution = Solution()
#     print(solution.solveNQueens(4))
