from person import Person


class PlanNode:
    def __init__(self, data=Person(), priority=0):
        self.data = data
        self.priority = priority


class PlanPriorityQueue:
    def __init__(self):
        self.priority_queue = []

    def is_empty(self):
        return self.priority_queue == []

    def is_full(self):
        return False

    def peek(self):
        if not self.is_empty():
            return self.priority_queue[self.size() - 1].data
        raise ValueError('Queue is empty!')

    def size(self):
        return len(self.priority_queue)

    def enqueue(self, node):
        if self.size() == 0:
            self.priority_queue.append(node)
        else:
            for x in range(0, self.size()):
                if node.priority >= self.priority_queue[x].priority:
                    if x == (self.size() - 1):
                        self.priority_queue.insert(x+1, node)
                    else:
                        continue
                else:
                    self.priority_queue.insert(x, node)
                    return True

    def dequeue(self):
        if not self.is_empty():
            return self.priority_queue.pop()
        raise ValueError('Queue is empty!')

    def print_queue(self):
        stack_str = ""

        if not self.is_empty():
            for i in range(0, self.size()):
                stack_str += str(self.priority_queue[i].data)
                stack_str += "\n"
            return stack_str
        raise ValueError("Queue is empty!")
