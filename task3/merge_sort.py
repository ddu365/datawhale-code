"""
the merge-sort algorithm proceeds as follows:
1. Divide: If S has zero or one element, return S immediately; it is already
sorted. Otherwise (S has at least two elements), remove all the elements
from S and put them into two sequences, S1 and S2 , each containing about
half of the elements of S; that is, S1 contains the first n/2 elements of S,
and S2 contains the remaining n/2 elements.
2. Conquer: Recursively sort sequences S1 and S2 .
3. Combine: Put back the elements into S by merging the sorted sequences S1
and S2 into a sorted sequence.
"""


def merge_sort(s):
    """sort the elements of list using the merge-sort algorithm."""
    n = len(s)
    if n < 2:
        return
    # divide
    mid = n // 2
    s1 = s[:mid]
    s2 = s[mid:]
    # conquer (recursion)
    merge_sort(s1)
    merge_sort(s2)
    # combine (merge results)
    merge(s1, s2, s)
    return s


def merge(s1, s2, s):
    """
    merge two sorted list s1 and s2 into a proper size list s
    Complexity: best O(n*log(n)) avg O(n*log(n)), worst O(n*log(n))
    """
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1


if __name__ == '__main__':
    ul = [85, 24, 63, 45, 17, 31, 96, 50]
    print(merge_sort(ul))
