def selection_sort(s):
    """
    sort the elements of list s using the selection-sort algorithm
    Complexity: best O(n^2) avg O(n^2), worst O(n^2)
    """
    for i in range(len(s)):
        min_index = i
        for j in range(i+1, len(s)):
            if s[j] < s[min_index]:
                min_index = j
        s[i], s[min_index] = s[min_index], s[i]
    return s


if __name__ == '__main__':
    ul = [85, 24, 63, 45, 17, 31, 96, 50]
    print(selection_sort(ul))
