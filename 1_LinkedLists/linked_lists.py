class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None) -> None:
        self.head = None
        self.tail = None
        self.length = 0

        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        value = None

        if self.length == 0:
            return value

        if self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next.next:
                current = current.next

            value = current.next.value
            current.next = None
            self.tail = current

        self.length -= 1
        return value

    def prepend(self, value):
        if self.length == 0:
            self.append(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True


# Code for test
my_linked_list = LinkedList()

""" my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7) """

my_linked_list.pop()
my_linked_list.pop()

my_linked_list.prepend(3)
my_linked_list.prepend(2)
my_linked_list.prepend(1)

my_linked_list.print_list()

print("Length:", my_linked_list.length)
# print("Head:", my_linked_list.head.value)
# print("Tail:", my_linked_list.tail.value)
