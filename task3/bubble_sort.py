def bubble_sort(s):
    """
    sort the elements of list s using the bubble-sort algorithm
    Complexity: best O(n) avg O(n^2), worst O(n^2)
    """
    for i in range(0, len(s)):
        for j in range(1, len(s)-i):
            if s[j-1] > s[j]:
                s[j-1], s[j] = s[j], s[j-1]
    return s


if __name__ == '__main__':
    ul = [85, 24, 63, 45, 17, 31, 96, 50]
    print(bubble_sort(ul))
