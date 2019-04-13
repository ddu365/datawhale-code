def bs(s, t):
    """
    标准二分查找
    :param s: 有序数组
    :param t: target
    :return: target在s中的索引
    """
    l, r = 0, len(s) - 1
    while l <= r:
        m = (l + r) // 2
        if t < s[m]:
            r = m - 1
        elif t > s[m]:
            l = m + 1
        else:
            return m
    return -1


def bs_fist_ge(s, t):
    """
     查找第一个大于等于给定值的元素(模糊二分查找)
    :param s: 有序数组
    :param t: target
    :return: 第一个大于等于target的索引,没有返回-1
    """
    l, r = 0, len(s) - 1
    while l <= r:
        m = (l + r) // 2
        if t <= s[m]:
            if m == 0 or s[m-1] < t:
                return m
            else:
                r = m - 1
        else:
            l = m + 1
    return -1


def bs_last_le(s, t):
    """
     查找最后一个小于等于给定值的元素(模糊二分查找)
    :param s: 有序数组
    :param t: target
    :return: 最后一个小于等于target的索引,没有返回-1
    """
    l, r = 0, len(s) - 1
    while l <= r:
        m = (l + r) // 2
        if t >= s[m]:
            if m == r or s[m + 1] > t:
                return m
            else:
                l = m + 1
        else:
            r = m - 1
    return -1


if __name__ == '__main__':
    s = [-1, 0, 2, 5, 9, 12, 23]
    t = 3
    print(bs(s, t))
    print(bs_fist_ge(s, t))
    print(bs_last_le(s, t))
