class Array:
    def __init__(self):
        self.array = []

    def insert(self, index, value):
        self.array.insert(index, value)

    def delete(self, index):
        if 0 <= index < len(self.array):
            return self.array.pop(index)
        else:
            raise IndexError("Index out of bounds")

    def access(self, index):
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of bounds")

# Matrix
class Matrix:
    def __init__(self, rows, cols):
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def update(self, row, col, value):
        self.matrix[row][col] = value

    def access(self, row, col):
        return self.matrix[row][col]


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next

    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self):
        print(self.value)
        for child in self.children:
            child.traverse()

