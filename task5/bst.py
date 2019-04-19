
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self._root = None

    def get_root(self):
        return self._root

    def insert(self, data):
        if self._root is None:
            self._root = Node(data)
            return True
        else:
            self.insert_recur(self._root, data)

    def insert_recur(self, root, data):
        if data == root.data:
            return False
        elif data < root.data:
            if root.left is None:
                root.left = Node(data)
                return True
            else:
                return self.insert_recur(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
                return True
            else:
                return self.insert_recur(root.right, data)

    def delete(self, data):
        if self._root is None:
            return None
        return self.delete_recur(self._root, data)

    def delete_recur(self, root, data):
        if root.data == data:
            if root.left:
                # Find the right most leaf of the left sub-tree
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                # Attach right child to the right of that leaf
                left_right_most.right = root.right
                # Return left child instead of root, a.k.a delete root
                return root.left
            else:
                return root.right
            # If left or right child got deleted, the returned root is the child of the deleted node.
        elif root.data > data:
            root.left = self.delete_recur(root.left, data)
        else:
            root.right = self.delete_recur(root.right, data)
        return root

    def search(self, data):
        return self.search_recur(self._root, data)

    def search_recur(self, root, data):
        if root is None:
            return False
        if data == root.data:
            return True
        elif data < root.data:
            return self.search_recur(root.left, data)
        else:
            return self.search_recur(root.right, data)

    def size(self):
        return self.size_recur(self._root)

    def size_recur(self, root):
        if root is None:
            return 0
        else:
            return 1 + self.size_recur(root.left) + self.size_recur(root.right)

    # 前序遍历[深度遍历-栈]: 根结点 ---> 左子树 ---> 右子树
    def pre_order_recur(self, root):
        if root is not None:
            print(str(root.data), end=' ')
            self.pre_order_recur(root.left)
            self.pre_order_recur(root.right)

    def pre_order_iter(self, root):
        node_stack = []
        cur_node = root
        while cur_node or node_stack:
            while cur_node:
                print(str(cur_node.data), end=' ')
                node_stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = node_stack.pop()
            cur_node = cur_node.right
            # 第二种写法
            # if cur_node is not None:
            #     print(str(cur_node.data), end=' ')
            #     node_stack.append(cur_node)
            #     cur_node = cur_node.left
            # else:
            #     tmp_node = node_stack.pop()
            #     cur_node = tmp_node.right

    # 中序遍历[深度遍历-栈]: 左子树 ---> 根结点 ---> 右子树
    def in_order_recur(self, root):
        if root is not None:
            self.in_order_recur(root.left)
            print(str(root.data), end=' ')
            self.in_order_recur(root.right)

    def in_order_iter(self, root):
        node_stack = []
        cur_node = root
        while cur_node or node_stack:
            while cur_node:
                node_stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = node_stack.pop()
            print(str(cur_node.data), end=' ')
            cur_node = cur_node.right

            # 第二种写法
            # if cur_node is not None:
            #     node_stack.append(cur_node)
            #     cur_node = cur_node.left
            # else:
            #     tmp_node = node_stack.pop()
            #     print(str(tmp_node.data), end=' ')
            #     cur_node = tmp_node.right

    # 后序遍历[深度遍历-栈]: 左子树 ---> 右子树 ---> 根结点
    def post_order_recur(self, root):
        if root is not None:
            self.post_order_recur(root.left)
            self.post_order_recur(root.right)
            print(str(root.data), end=' ')

    def post_order_iter(self, root):
        node_stack_forward = []
        node_stack_reverse = []
        cur_node = root
        node_stack_forward.append(cur_node)
        while node_stack_forward:
            cur_node = node_stack_forward.pop()
            if cur_node.left:
                node_stack_forward.append(cur_node.left)
            if cur_node.right:
                node_stack_forward.append(cur_node.right)
            node_stack_reverse.append(cur_node)
        while node_stack_reverse:
            cur_node = node_stack_reverse.pop()
            print(str(cur_node.data), end=' ')


    # 层级遍历[广度遍历-队列] 每层一个列表
    def level_order2(self, root):
        res = []
        if root is None:
            return res
        node_queue = []
        node_queue.append(root)
        while node_queue:
            level_value = []
            level_node_nums = len(node_queue)
            for _ in range(level_node_nums):
                node = node_queue.pop(0)
                if node.left is not None:
                    node_queue.append(node.left)
                if node.right is not None:
                    node_queue.append(node.right)
                level_value.append(node.data)
            res.append(level_value)
        return res

    # 层级遍历[广度遍历-队列] 整个层一个列表
    def level_order(self, root):
        res = []
        if root is None:
            return res
        node_queue = []
        node = root
        node_queue.append(node)
        while node_queue:
            node = node_queue.pop(0)
            res.append(node.data)
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)
        return res

    # 后继节点: 节点data值大于该节点data值并且值最小的节点
    def successor_node(self, data):
        successor = None
        cur_node = self._root
        while cur_node:
            if data < cur_node.data:
                successor = cur_node
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return successor.data

    # 前驱节点: 节点data值小于该节点data值并且值最大的节点
    def predecessor_node(self, data):
        predecessor = None
        cur_node = self._root
        while cur_node:
            if data > cur_node.data:
                predecessor = cur_node
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        return predecessor.data


if __name__ == '__main__':
    bst = BST()
    bst.insert(44)
    bst.insert(17)
    bst.insert(88)
    bst.insert(8)
    bst.insert(32)
    bst.insert(65)
    bst.insert(97)
    bst.insert(28)
    bst.insert(54)
    bst.insert(82)
    bst.insert(93)
    bst.insert(29)
    bst.insert(76)
    bst.insert(68)
    bst.insert(80)

    print('++++++before deleting node[88]++++++')
    print(bst.search(88))
    print(bst.size())
    print('[pre_order_recur]', end='\t')
    bst.pre_order_recur(bst.get_root())
    print()
    print('[pre_order_iter]', end='\t')
    bst.pre_order_iter(bst.get_root())
    print()
    print('[in_order_recur]', end='\t')
    bst.in_order_recur(bst.get_root())
    print()
    print('[in_order_iter]', end='\t\t')
    bst.in_order_iter(bst.get_root())
    print()
    print('[post_order_recur]', end='\t')
    bst.post_order_recur(bst.get_root())
    print()
    print('[post_order_iter]', end='\t')
    bst.post_order_iter(bst.get_root())
    print()
    print('[level_order]', end='\t')
    print(bst.level_order(bst.get_root()))
    print('[level_order2]', end='\t')
    print(bst.level_order2(bst.get_root()))

    print()
    print('[successor_node[29]]', end='\t')
    print(bst.successor_node(29))

    print()
    print('[predecessor_node[29]]', end='\t')
    print(bst.predecessor_node(29))

    bst.delete(88)
    print()

    print('++++++after deleting node[88]++++++')
    print(bst.search(88))
    print(bst.size())
    print('[pre_order_recur]', end='\t')
    bst.pre_order_recur(bst.get_root())
    print()
    print('[in_order_recur]', end='\t')
    bst.in_order_recur(bst.get_root())
    print()
    print('[post_order_recur]', end='\t')
    bst.post_order_recur(bst.get_root())
    print()
    print('[level_order]', end='\t')
    print(bst.level_order(bst.get_root()))
