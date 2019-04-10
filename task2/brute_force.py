def find_brute(t, p):
    """
    字符串匹配--bf 暴力搜索
    :param t: 主串
    :param p: 模式串
    :return: 返回 子串p开始的t的最低索引（没找到则为-1）
    """
    n, m = len(t), len(p)
    for i in range(n-m+1):
        k = 0
        while k < m and t[i+k] == p[k]:
            k += 1
        if k == m:
            return i
    return -1


if __name__ == '__main__':
    T = 'abacaabaccabacabaabb'
    P = 'abacab'
    print(find_brute(T, P))
