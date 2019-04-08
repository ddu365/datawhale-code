""""
Pros
Linked Lists have constant-time insertions and deletions in any position,
in comparison, arrays require O(n) time to do the same thing.
Linked lists can continue to expand without having to specify
their size ahead of time (remember our lectures on Array sizing
form the Array Sequence section of the course!)

Cons
To access an element in a linked list, you need to take O(k) time
to go from the head of the list to the kth element.
In contrast, arrays have constant time operations to access
elements in an array.
"""
from abc import ABCMeta, abstractmethod


class AbstractLinkedList(metaclass=ABCMeta):
    def __init__(self):
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        return " ".join(map(str, self))

    def __len__(self):
        return self._size

    @abstractmethod
    def add_first(self, value):
        pass

    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def insert(self, pos, value):
        pass

    @abstractmethod
    def remove_first(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass


class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SinglyLinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __iter__(self):
        p = self
        while True:
            yield p.value
            p = p.next
            if p is None:
                return


class SinglyLinkedList(AbstractLinkedList):
    def __init__(self):  # , node=None
        super().__init__()
        self._head = None
        self._tail = None

    # 头部插入
    def add_first(self, value):
        n = SinglyLinkedListNode(value)
        if self.is_empty():
            self._head = n
            self._tail = n
        else:
            n.next = self._head
            self._head = n
        self._size += 1
        return self._head

    # 尾部插入
    def append(self, value):
        n = SinglyLinkedListNode(value)
        if self.is_empty():
            self._head = n
            self._tail = n
        else:
            self._tail.next = n
            self._tail = n
            # without self._tail version
            # p = self._head
            # while p.next is not None:
            #     p = p.next
            # p.next = n
        self._size += 1
        return self._head

    # 任意位置插入 从零开始计数
    def insert(self, pos, value):
        if pos <= 0:
            self.add_first(value)
            return
        if pos >= len(self):
            self.append(value)
            return
        count = 0
        n = SinglyLinkedListNode(value)
        p = self._head
        while count < pos - 1:
            count += 1
            p = p.next
        n.next = p.next
        p.next = n
        self._size += 1
        return self._head

    # 头部删除
    def remove_first(self):
        if self.is_empty():
            return
        self._head = self._head.next
        self._size -= 1
        return self._head

    # 任意位置删除 从零开始计数
    def delete(self, pos):
        if pos <= 0:
            self.remove_first()
            return
        if pos >= len(self):
            pos = len(self)
        count = 0
        p = self._head
        while count < pos - 1:
            count += 1
            p = p.next
        p.next = p.next.next
        self._size -= 1
        return self._head

    def __iter__(self):
        h = self._head
        while True:
            if h is None:
                return
            yield h.value
            h = h.next


class SinglyCircularLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    # 头部插入
    def add_first(self, value):
        n = SinglyLinkedListNode(value)
        if self.is_empty():
            self._head = n
            self._tail = n
            self._tail.next = self._head  # add tail-to-head
        else:
            n.next = self._head
            self._head = n
            self._tail.next = self._head  # add tail-to-head
        self._size += 1

    # 尾部插入
    def append(self, value):
        n = SinglyLinkedListNode(value)
        if self.is_empty():
            self._head = n
            self._tail = n
            self._tail.next = self._head  # add tail-to-head
        else:
            self._tail.next = n
            self._tail = n
            self._tail.next = self._head  # add tail-to-head
        self._size += 1

    # 头部删除
    def remove_first(self):
        if self.is_empty():
            return
        self._head = self._head.next
        self._tail.next = self._head  # add tail-to-head
        self._size -= 1

    def __iter__(self):
        h = self._head
        while True:
            yield h.value
            h = h.next
            if h is self._head:
                return


class DoublyLinkedList(AbstractLinkedList):
    def __init__(self):
        super().__init__()
        self._header = DoublyLinkedListNode(None)
        self._trailer = DoublyLinkedListNode(None)
        self._header.next = self._trailer
        self._trailer.prev = self._header

    # 头部插入
    def add_first(self, value):
        n = DoublyLinkedListNode(value)
        if self.is_empty():
            self._header.next = n
            self._trailer.prev = n
            n.prev = self._header
            n.next = self._trailer
        else:
            header_next_node = self._header.next
            self._header.next = n
            header_next_node.pre = n
            n.prev = self._header
            n.next = header_next_node
        self._size += 1

    # 尾部插入
    def append(self, value):
        n = DoublyLinkedListNode(value)
        if self.is_empty():
            self._header.next = n
            self._trailer.prev = n
            n.prev = self._header
        else:
            trailer_prev_node = self._trailer.prev
            self._trailer.prev = n
            trailer_prev_node.next = n
            n.prev = trailer_prev_node
        n.next = self._trailer
        self._size += 1

    # 任意位置插入 从零开始计数
    def insert(self, pos, value):
        if pos <= 0:
            self.add_first(value)
            return
        if pos >= len(self):
            self.append(value)
            return
        count = 0
        n = DoublyLinkedListNode(value)
        p = self._header.next
        while count < pos - 1:
            count += 1
            p = p.next
        n.next = p.next
        p.next = n
        p.next.prev = n
        n.prev = p
        self._size += 1

    # 头部删除
    def remove_first(self):
        if self.is_empty():
            return
        header_node = self._header.next
        self._header.next = header_node.next
        header_node.next.prev = self._header

        # error writing
        # self._header.next = self._header.next.next
        # self._header.next.next.prev = self._header
        self._size -= 1

    # 任意位置删除 从零开始计数
    def delete(self, pos):
        if pos <= 0:
            self.remove_first()
            return
        if pos >= len(self):
            pos = len(self)
        count = 0
        p = self._header
        while count < pos:
            count += 1
            p = p.next
        delete_node = p.next
        p.next = delete_node.next
        delete_node.next.prev = p
        self._size -= 1

    def __iter__(self):
        h = self._header
        while True:
            if h.next.value is None:
                return
            yield h.next.value
            h = h.next



