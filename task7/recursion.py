from time import time
from functools import lru_cache

# 题目链接: https://leetcode-cn.com/problems/climbing-stairs/
# 递推公式: f(n) = f(n-1) + f(n-2) (f(1)=1,f(2)=2)

# 当n较大时，用递归会存在大量重复的存储与计算，效率低

# 自定义装饰器
# 参考链接: https://blog.csdn.net/mp624183768/article/details/79522231
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

# @memo
# def climbStairs(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#
#     return climbStairs(n - 1) + climbStairs(n - 2)

# 系统级装饰器
@lru_cache()
def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return climbStairs(n - 1) + climbStairs(n - 2)


# 带缓存的递归
# def climbStairs(n, cache=None):
#     if cache is None:
#     # if not cache:  #  这样写有问题
#         cache = {}
#     if n in cache:
#         return cache[n]
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     cache[n] = climbStairs(n-1, cache) + climbStairs(n-2, cache)
#
#     return cache[n]

# 动态规划
# def climbStairs(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         i = 1
#         j = 2
#         for _ in range(2, n):
#             i, j = j, i+j
#     return j

start = time()
print('[use time]', time()-start, '[result]', climbStairs(35))  # time s
