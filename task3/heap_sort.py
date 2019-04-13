"""
堆是一种完全二叉树的数据结构
算法流程：
1.将待排序列表构建成完全二叉树
2.调整完全二叉树节点的顺序，使其成为最大堆(初始无序区)，即父节点大于孩子节点[从最后一个父节点开始从右往左从下往上地调整，调整后还需反向检查调整后的节点是否满足最大堆的性质]
3.将堆顶元素L[1]与最后一个元素L[n]交换,得到新的无序区(L[1],L[2]...,L[n-1])和新的有序区L[n]
4.将新得到的无序区调整为最大堆,然后再次将调整后的最大堆的堆顶元素L[1]与最后一个元素L[n-1]交换,得到新的无序区(L[1],L[2]...,L[n-2])和新的有序区L[n-1],L[n]
5.重复上述过程直到有序区元素的个数为n-1
参考链接: http://www.cnblogs.com/0zcl/p/6737944.html
"""


def max_heap_sort(s):
    """
    sort the elements of list s using the max-heap-sort algorithm
    Complexity: best O(n*log(n)) avg O(n*log(n)), worst O(n*log(n))
    """
    for i in range(len(s)-1, 0, -1):
        max_heapify(s, i)
    return s


def max_heapify(s, end):
    last_parent = (end - 1) // 2
    for parent in range(last_parent, -1, -1):
        current_parent = parent
        while current_parent <= last_parent:
            child = 2 * current_parent + 1
            if child + 1 <= end and s[child] < s[child + 1]:
                child += 1

            if s[child] > s[current_parent]:
                s[current_parent], s[child] = s[child], s[current_parent]
                current_parent = child
            else:
                break
    s[0], s[end] = s[end], s[0]


if __name__ == '__main__':
    ul = [85, 24, 63, 45, 17, 31, 96, 50]
    print(max_heap_sort(ul))

