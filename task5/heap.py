"""
Min Heap. A min heap is a complete binary tree where each node is smaller
its children. The root, therefore, is the minimum element in the tree. The min
heap use array to represent the data and operation. For example a min heap:
     4
   /   \
  50    7
 / \   /
55 90 87
Heap [4, 50, 7, 55, 90, 87]
Method in class: insert, remove_min
For example insert(2) in a min heap:
     4                     4                     2
   /   \                 /   \                 /   \
  50    7      -->     50     2       -->     50    4
 / \   /  \           /  \   / \             /  \  /  \
55 90 87   2         55  90 87  7           55  90 87  7
For example remove_min() in a min heap:
     4                     87                    7
   /   \                 /   \                 /   \
  50    7      -->     50     7       -->     50    87
 / \   /              /  \                   /  \
55 90 87             55  90                 55  90
"""

from abc import ABCMeta, abstractmethod


class AbstractHeap(metaclass=ABCMeta):
    """Abstract Class for Binary Heap."""
    def __init__(self):
        self._size = 0
        self.heap = []

    def __len__(self):
        return self._size

    """
    Method insert always start by inserting the element at the bottom.
    it inserts rightmost spot so as to maintain the complete tree property
    Then, it fix the tree by swapping the new element with its parent,
    until it finds an appropriate spot for the element. It essentially
    adjust_up the min/max element
    Complexity: O(logN)
    """
    def insert(self, val):
        self.heap.append(val)
        self._size += 1
        self.adjust_up(self._size - 1)

    @abstractmethod
    def adjust_up(self, i):
        pass

    @abstractmethod
    def adjust_down(self, i):
        pass


class MinHeap(AbstractHeap):
    def __init__(self):
        super().__init__()

    def adjust_up(self, i):
        # 存在父节点
        while (i+1) // 2 > 0:
            # 当前节点比父节点小
            if self.heap[i] < self.heap[(i-1) // 2]:
                # Swap value of child with value of its parent
                self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1) // 2

    """
    Method min_child returns index of smaller 2 children of its parent
    """
    def min_child(self, i):
        if 2 * (i+1) + 1 > self._size:  # No right child
            return 2 * i + 1
        else:
            # left child > right child
            if self.heap[2 * i + 1] > self.heap[2 * (i + 1)]:
                return 2 * (i + 1)
            else:
                return 2 * i + 1

    def adjust_down(self, i):
        # 存在子节点
        while 2 * (i+1) <= self._size:
            min_child = self.min_child(i)
            if self.heap[min_child] < self.heap[i]:
                # Swap min child with parent
                self.heap[min_child], self.heap[i] = self.heap[i], self.heap[min_child]
            i = min_child

    """
    Remove Min method removes the minimum element and swap it with the last
    element in the heap( the bottommost, rightmost element). Then, it
    adjust_down this element, swapping it with one of its children until the
    min heap property is restored
    Complexity: O(logN)
    """
    def remove_min(self):
        ret = self.heap[0]      # the smallest value at beginning
        self.heap[0] = self.heap[self._size-1]  # Replace it by the last value
        self._size -= 1
        self.heap.pop()
        self.adjust_down(0)
        return ret


class MaxHeap(AbstractHeap):
    def __init__(self):
        super().__init__()

    def adjust_up(self, i):
        # 存在父节点
        while (i+1) // 2 > 0:
            # 当前节点比父节点大
            if self.heap[i] > self.heap[(i-1) // 2]:
                # Swap value of child with value of its parent
                self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1) // 2

    """
    Method max_child returns index of larger 2 children of its parent
    """
    def max_child(self, i):
        if 2 * (i + 1) + 1 > self._size:  # No right child
            return 2 * i + 1
        else:
            # left child > right child
            if self.heap[2 * i + 1] > self.heap[2 * (i + 1)]:
                return 2 * i + 1
            else:
                return 2 * (i + 1)

    def adjust_down(self, i):
        # 存在子节点
        while 2 * (i+1) <= self._size:
            max_child = self.max_child(i)
            if self.heap[max_child] > self.heap[i]:
                # Swap min child with parent
                self.heap[max_child], self.heap[i] = self.heap[i], self.heap[max_child]
            i = max_child

    """
    Remove Max method removes the max element and swap it with the last
    element in the heap( the bottommost, rightmost element). Then, it
    adjust_down this element, swapping it with one of its children until the
    max heap property is restored
    Complexity: O(logN)
    """
    def remove_max(self):
        ret = self.heap[0]  # the largest value at beginning
        self.heap[0] = self.heap[self._size - 1]  # Replace it by the last value
        self._size -= 1
        self.heap.pop()
        self.adjust_down(0)
        return ret


if __name__ == '__main__':
    min_heap = MinHeap()

    min_heap.insert(85)
    min_heap.insert(24)
    min_heap.insert(63)
    min_heap.insert(45)
    min_heap.insert(17)
    min_heap.insert(31)
    min_heap.insert(96)
    min_heap.insert(50)

    print('[min_heap]', [min_heap.remove_min() for _ in range(len(min_heap))])

    import heapq
    heap = []
    heapq.heappush(heap, 85)
    heapq.heappush(heap, 24)
    heapq.heappush(heap, 63)
    heapq.heappush(heap, 45)
    heapq.heappush(heap, 17)
    heapq.heappush(heap, 31)
    heapq.heappush(heap, 96)
    heapq.heappush(heap, 50)

    print('[heap top k(k=3)]', heapq.nlargest(3, heap))
    print('[built-in heap]', [heapq.heappop(heap) for _ in range(len(heap))])

    max_heap = MaxHeap()

    max_heap.insert(85)
    max_heap.insert(24)
    max_heap.insert(63)
    max_heap.insert(45)
    max_heap.insert(17)
    max_heap.insert(31)
    max_heap.insert(96)
    max_heap.insert(50)

    print('[max_heap]', [max_heap.remove_max() for _ in range(len(max_heap))])
