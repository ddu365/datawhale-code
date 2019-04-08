import task1.queue as queue
from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._array = [None] * k
        self._front = 0
        self._rear = 0
        self._size = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self._front = self._dec_p(self._front)
        self._array[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self._array[self._rear] = value
        self._rear = self._inc_p(self._rear)
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._array[self._front] = None
        self._front = self._inc_p(self._front)
        self._size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self._rear = self._dec_p(self._rear)
        self._array[self._rear] = None
        self._size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self._array[self._front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        # ac 只取值
        return self._array[self._dec_p(self._rear)]

        # error 取值的同时移动了尾指针
        # self._rear = self._dec_p(self._rear)
        # return self._array[self._rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._size == len(self._array)

    def _inc_p(self, index):
        return (index + 1) % len(self._array)

    def _dec_p(self, index):
        return (index - 1 + len(self._array)) % len(self._array)

    def __str__(self):
        return " ".join(map(str, self))

    def __iter__(self):
        s = self._front
        while True:
            yield self._array[s]
            # s += 1
            s = (s + 1) % len(self._array)
            if s == self._rear:
                return


if __name__ == '__main__':
    try:
        # built-in deque
        d = deque(maxlen=5)
        d.appendleft(5)
        d.appendleft(7)
        d.appendleft(4)
        d.appendleft(3)
        d.append(1)
        d.append(9)  # insert success
        print(f'rear----{d[-1]}')
        print(d)
        # custom deque
        obj = MyCircularDeque(5)
        obj.insertFront(5)
        obj.insertFront(7)
        obj.insertFront(4)
        obj.insertFront(3)
        obj.insertLast(1)
        # obj.deleteLast()
        obj.insertLast(9)  # insert error
        print(f'rear----{obj.getRear()}')
        print(obj)

        # test ArrayQueue
        aq = queue.ArrayQueue(3)
        aq.enqueue(5)
        aq.enqueue(3)
        aq.dequeue()
        aq.enqueue(6)
        aq.enqueue(9)

        print(f'aq.first:{aq.first()}')
        print(aq)
        # ArrayQueue inner
        print(len(aq._array))
        print(aq._array)

        # test LinkedListQueue
        lq = queue.LinkedListQueue()
        lq.enqueue(5)
        lq.enqueue(3)
        lq.dequeue()
        lq.enqueue(6)
        lq.enqueue(9)

        print(f'lq.first:{lq.first()}')
        print(lq)

        lq.dequeue()
        lq.dequeue()
        lq.dequeue()

        # print(f'lq.first:{lq.first()}')
        print(lq)




    except Exception as e:
        print(f'test happen error:{e}')
