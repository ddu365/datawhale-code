from queue import PriorityQueue
from task5.heap import MinHeap

# built-in PriorityQueue using heapq and thread safe
que = PriorityQueue()

que.put(85)
que.put(24)
que.put(63)
que.put(45)
que.put(17)
que.put(31)
que.put(96)
que.put(50)


print('[built-in PriorityQueue]', [que.get() for _ in range(que.qsize())])


# my simple priority queue
class MyPriorityQueue:
    def __init__(self):
        self._heap = MinHeap()
        self._size = 0

    def put(self, value):
        self._heap.insert(value)
        self._size += 1

    def get(self):
        self._size -= 1
        return self._heap.remove_min()

    def __len__(self):
        return self._size


que = MyPriorityQueue()

que.put(85)
que.put(24)
que.put(63)
que.put(45)
que.put(17)
que.put(31)
que.put(96)
que.put(50)


print('[MyPriorityQueue]', [que.get() for _ in range(len(que))])


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists):
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val, node))
    while not q.empty():
        # 取出堆顶(最小堆)元组的节点
        curr.next = q.get()[1]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, curr.next))
    return dummy.next


if __name__ == '__main__':
    l = []
    merge_v = []
    l1 = ListNode(2)
    l1.next = ListNode(5)
    l1.next.next = ListNode(7)

    l2 = ListNode(3)
    l2.next = ListNode(4)
    l2.next.next = ListNode(9)

    l3 = ListNode(0)
    l3.next = ListNode(6)
    l3.next.next = ListNode(8)

    l.append(l1)
    l.append(l2)
    l.append(l3)

    res = merge_k_lists(l)
    while res:
        merge_v.append(res.val)
        res = res.next
    print('[merge k lists]', merge_v)
