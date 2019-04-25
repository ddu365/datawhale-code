# 逆序对个数
# 解题思路:
# 首先将给定的数组列表按索引递归的分成左右两部分，然后比较分割后的左右两部分，
# 当左边列表的元素大于右边的，往左移动左列表的索引，并记录逆序对个数
# 当右边列表的元素大于左边的，往左移动右列表的索引
# 最终将两个列表合成一个有序的列表
# 重复上述过程，直到将所有的左右列表合成一个列表。

global count
count = 0


def inverse_pairs(data):
    return merge_sort(data)


def merge_sort(lists):
    global count
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[0:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


# left right两个列表都是有序的
def merge(left, right):
    global count
    r = len(right) - 1
    l = len(left) - 1
    result = []
    while l >= 0 and r >= 0:
        if left[l] > right[r]:
            result.insert(0, left[l])
            l -= 1
            count += r + 1
        else:
            result.insert(0, right[r])
            r -= 1

    if l >= 0:
        left = left[0: l + 1]
        result = left + result

    if r >= 0:
        right = right[0: r + 1]
        result = right + result
    return result


if __name__ == '__main__':
    data = [1, 2, 3, 4, 0]
    inverse_pairs(data)
    print(count)

