def insert_sort(s):
    """
    sort the elements of list s using the insert-sort algorithm
    Complexity: best O(n) avg O(n^2), worst O(n^2)
    """
    for i in range(1, len(s)):
        cur = s[i]
        j = i
        while j > 0 and cur < s[j-1]:
            s[j] = s[j-1]
            j -= 1
        s[j] = cur
    return s


if __name__ == '__main__':
    ul = [85, 24, 63, 45, 17, 31, 96, 50]
    print(insert_sort(ul))
