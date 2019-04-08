import task1.linkedlist as ll
import math


# 题目链接 https://leetcode-cn.com/problems/middle-of-the-linked-list/
def middle_node(head):
    count = 0
    d = {}
    while head:
        count += 1
        d[count] = head
        head = head.next
    return d[math.ceil((count - 1) / 2) + 1].value


def reverse_singly_linked_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    prev = None
    while head:
        # current = head
        # head = head.next
        # current.next = prev
        # prev = current
        current, head = head, head.next
        current.next, prev = prev, current
    return prev


def merge_two_list(l1, l2):
    ret = cur = ll.SinglyLinkedListNode(None)
    while l1 and l2:
        if l1.value < l2.value:
            # cur.next = l1
            # l1 = l1.next
            cur.next, l1 = l1, l1.next
        else:
            # cur.next = l2
            # l2 = l2.next
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 or l2
    return ret.next


if __name__ == '__main__':
    try:
        # SinglyLinkedList
        print('-'*20, 'SinglyLinkedList', '-'*20)
        sLinkedList = ll.SinglyLinkedList()
        header = sLinkedList.append(3)
        sLinkedList.append(5)
        sLinkedList.remove_first()
        sLinkedList.append(9)
        sLinkedList.add_first(8)
        print(sLinkedList)
        sLinkedList.insert(2, 2)
        print(sLinkedList)
        print(len(sLinkedList))
        sLinkedList.delete(3)
        print(sLinkedList)
        # SinglyCircularLinkedList
        print('o' * 20, 'SinglyCircularLinkedList', '0' * 20)
        scLinkedList = ll.SinglyCircularLinkedList()
        scLinkedList.append(3)
        scLinkedList.append(5)
        scLinkedList.remove_first()
        scLinkedList.append(9)
        scLinkedList.add_first(8)
        print(scLinkedList)
        scLinkedList.insert(2, 2)
        print(scLinkedList)
        print(len(scLinkedList))
        scLinkedList.delete(3)
        print(scLinkedList)
        # DoublyLinkedList
        print('=' * 20, 'SinglyCircularLinkedList', '=' * 20)
        dLinkedList = ll.DoublyLinkedList()
        dLinkedList.append(3)
        dLinkedList.append(5)
        dLinkedList.remove_first()
        dLinkedList.append(9)
        dLinkedList.add_first(8)
        print(dLinkedList)
        dLinkedList.insert(2, 2)
        print(dLinkedList)
        print(len(dLinkedList))
        dLinkedList.delete(3)
        print(dLinkedList)
        # reverse_singly_linked_list
        print('#' * 20, 'reverse_singly_linked_list', '#' * 20)
        print('before reverse')
        print([value for value in header])
        reverse_header = reverse_singly_linked_list(header)
        print('after reverse')
        print([value for value in reverse_header])
        # merge_two_list
        s1 = ll.SinglyLinkedList()
        s1.append(1)
        s1.append(2)
        l1 = s1.append(6)
        s2 = ll.SinglyLinkedList()
        s2.append(5)
        s2.append(7)
        l2 = s2.append(9)
        print(f'l1:{s1} l2:{s2}')
        l12 = merge_two_list(l1, l2)
        print(f'merge l1 l2 --> {[value for value in l12]}')
        # middle_node
        print(f'middle_node of l12:{middle_node(l12)}')
    except Exception as e:
        print(f'test happen a error:{e}')
