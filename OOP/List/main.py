class List:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def get_node_by_index(self, index):
        if index >= 0:
            node = self.head
            cur_index = 0

            while True:
                if cur_index == index:
                    return node

                node = node.next
                cur_index += 1
        else:
            raise Exception('Поки не готово для від`ємних індексів')

    def __getitem__(self, index):  # []
        node = self.get_node_by_index(index)
        return node.value

    def __setitem__(self, index, value):
        node = self.get_node_by_index(index)
        node.value = value

    def append(self, value):
        new_node = Node(value)

        if self.head is None:  # якщо список був пустий
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node

    def __len__(self):
        elements_amount = 0

        node = self.head
        while True:
            if node is None:
                return elements_amount
            elements_amount += 1
            node = node.next

    def __str__(self):
        text = '['

        node = self.head
        while node is not None:
            text += f'{node.value.__repr__()}, '
            node = node.next
        return text[:-2] + ']'


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


lst = List()
lst.append('a')
lst.append('b')
lst.append('c')
lst.append('d')
lst.append('e')
lst.append(3)
lst.append(':)')

lst[2] = ':('
print(lst)
