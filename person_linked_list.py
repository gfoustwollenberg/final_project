from person import Person


class PersonNode:
    def __init__(self, data=Person()):
        self.data = data


class PersonLinkedList:
    def __init__(self):
        self.top = -1
        self.list_items = []

    def is_empty(self):
        return self.top == -1

    def get(self, position):
        if not self.is_empty():
            return self.list_items[position]
        raise ValueError("List is empty!")

    def size(self):
        list_size = self.top + 1
        return list_size

    def insert(self, node):
        self.list_items.append(node)
        self.top += 1
        return

    def remove_at(self, position):
        if not self.is_empty():
            self.list_items.pop(position)
            self.top -= 1
            return
