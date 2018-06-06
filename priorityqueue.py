'''
    def enqueue(self, item, priority):
        newNode = Node(item, priority)
        if self.head is None:
            self.head = self.last = newNode
        if priority > self.head.get_priority():
            newNode.set_next(self.head)
            self.head = newNode
        else:
            curr = self.head.next
            while curr is not None and curr.priority < priority:
                self.head = self.head.next
            newNode.set_next(curr)
            curr = newNode
'''


class Node:
    def __init__(self, item: object, priority: int, next=None):
        self.item = item
        self.priority = priority
        self.next = next

    def get_priority(self: 'Node') -> int:
        return self.priority

    def set_priority(self: 'Node', priority: int) -> None:
        self.priority = priority

    def set_next(self, next):
        self.next = next

    def set_item(self, item):
        self.item = item

    def get_next(self):
        return self.next

    def get_item(self):
        return self.item

    def __str__(self):
        return str(self.item)

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, item, priority):
        newNode = Node(item, priority)
        if self.head is None:
            self.head = self.last = newNode
        if priority > self.head.get_priority():
            newNode.set_next(self.head)
            self.head = newNode
        elif priority == self.head.get_priority():
            self.head.set_next(newNode)
        else:
            curr = self.head.next
            while curr is not None and curr.priority < priority:
                self.head = self.head.next
            newNode.set_next(curr)
            curr = newNode

    def front(self):
        if self.isEmpty():
            raise RuntimeError('Attempt to access front of empty queue')
        print(self.head.item)
        return self.head.item

    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError('Attempt to access front of empty queue')
        item = self.head.item
        del self.head.item
        return item
        

