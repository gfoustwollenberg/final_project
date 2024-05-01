from person import Person


# personnode class created to hold instance of person being added to the list
class PersonNode:
    def __init__(self, data=Person()):
        self.data = data


class PersonLinkedList:
    # constructor for linked list creating the class list and variable for top of list
    def __init__(self):
        self.top = -1
        self.list_items = []

    # is empty method verifies if list is empty
    def is_empty(self):
        return self.top == -1

    # get method returns position of needed item
    def get(self, position):
        if not self.is_empty():
            return self.list_items[position]
        raise ValueError("List is empty!")

    # size method returns size of list
    def size(self):
        list_size = self.top + 1
        return list_size

    # insert method allows entry of list item
    def insert(self, node):
        self.list_items.append(node)
        self.top += 1
        return

    # remove at method allows removal of person from linked list
    def remove_at(self, position):
        if not self.is_empty():
            self.list_items.pop(position)
            self.top -= 1
            return
