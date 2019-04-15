class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class ChainHashTable:
    """
    HashTable Data Type [Array + LinkedList]:
    By having each bucket contain a linked list of elements that are hashed to that bucket.
    Usage:
    >>> table = ChainHashTable() # Create a new, empty map.
    >>> table.put('hello', 'world') # Add a new key-value pair.
    >>> len(table) # Return the number of key-value pairs stored in the map.
    1
    >>> table.get('hello') # Get value by key.
    'world'
    >>> del table['hello'] # Equivalent to `table.del_('hello')`, deleting key-value pair.
    >>> table.get('hello') is None # Return `None` if a key doesn't exist.
    True
    """
    def __init__(self, capacity=10):
        self.capacity = capacity
        self._len = 0
        self._table = [None] * self.capacity

    def hash(self, key):
        return hash(key) % self.capacity

    def __len__(self):
        return self._len

    def put(self, key, value):
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        if node_ is None:
            self._table[hash_] = Node(key, value)
        else:
            while node_.next is not None:
                if node_.key == key:
                    node_.value = value
                    return
                node_ = node_.next
            node_.next = Node(key, value)
        self._len += 1

    def get(self, key):
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        while node_ is not None:
            if node_.key == key:
                return node_.value
            node_ = node_.next
        return None

    def del_(self, key):
        hash_ = self.hash(key)
        node_ = self._table[hash_]
        p = None
        while node_ is not None:
            if node_.key == key:
                if p is None:
                    self._table[hash_] = node_.next
                else:
                    p.next = node_.next
                self._len -= 1
            p = node_
            node_ = node_.next

    def __getitem__(self, key):
        return self.get(self, key)

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __delitem__(self, key):
        return self.del_(key)


if __name__ == '__main__':
    table = ChainHashTable()
    table.put('hello', 'world')
    table.put('c', 'you')
    table.put('python', 'good')
    table.put('what', 'fuck')

    print(len(table))
    print(table.get('c'))

    del table['c']

    print(len(table))
    print(table.get('c'))
