"""
the quick-sort algorithm consists of the following three steps :
1. Divide: If S has at least two elements (nothing needs to be done if S has
zero or one element), select a specific element x from S, which is called the
pivot. As is common practice, choose the pivot x to be the last element in S.
Remove all the elements from S and put them into three sequences:
    • L, storing the elements in S less than x
    • E, storing the elements in S equal to x
    • G, storing the elements in S greater than x
Of course, if the elements of S are distinct, then E holds just one element—
the pivot itself.
2. Conquer: Recursively sort sequences L and G.
3. Combine: Put back the elements into S in order by first inserting the elements
of L, then those of E, and finally those of G.
"""


def quick_sort(s):
    """
    sort the elements of list s using the quick-sort algorithm
    Complexity: best O(n*log(n)) avg O(n*log(n)), worst O(n^2)
    """
    n = len(s)
    if n < 2:
        return
    # divide
    # using the last element as the arbitrary pivot
    p = s[-1]
    l, e, g = [], [], []
    while len(s) > 0:
        if s[-1] < p:
            l.append(s.pop())
        elif s[-1] > p:
            g.append(s.pop())
        else:
            e.append(s.pop())
    # conquer (recursion)
    quick_sort(l)
    quick_sort(g)
    # concatenate
    s.extend(l)
    s.extend(e)
    s.extend(g)
    return s


# improved method (saving memory)
def inplace_quick_sort(s):
    if len(s) < 2:
        return s
    return inplace_quick_sort_recur(s, 0, len(s)-1)


def inplace_quick_sort_recur(s, l, r):
    if l >= r:
        return
    p = s[r]
    left = l
    right = r-1
    while left <= right:
        while left <= right and s[left] < p:
            left += 1
        while left <= right and s[right] > p:
            right -= 1
        if left <= right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
    s[left], s[r] = s[r], s[left]
    inplace_quick_sort_recur(s, l, left-1)
    inplace_quick_sort_recur(s, left+1, r)
    return s


if __name__ == '__main__':
    ul = [85, 24, 63, 45, 17, 31, 96, 50]
    print(quick_sort(ul))

    print(inplace_quick_sort(ul))
