from person import Person


# plan node creates storage for person and priority number of plan
class PlanNode:
    def __init__(self, data=Person(), priority=0):
        self.data = data
        self.priority = priority


class PlanPriorityQueue:
    # constructor creates the priority queue for the class
    def __init__(self):
        self.priority_queue = []

    # is empty method returns if priority queue is empty or not
    def is_empty(self):
        return self.priority_queue == []

    # is full method always returns false because there is no limit on this priority queue
    def is_full(self):
        return False

    # peek method allows the ability to return data at beginning of priority queue
    def peek(self):
        if not self.is_empty():
            return self.priority_queue[self.size() - 1].data
        raise ValueError('Queue is empty!')

    # size method returns the length of the priority queue
    def size(self):
        return len(self.priority_queue)

    # enqueue method adds priority queue member based on their priority ranking
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

    # dequeue method allows the removal and return of the first priority queue member
    def dequeue(self):
        if not self.is_empty():
            return self.priority_queue.pop()
        raise ValueError('Queue is empty!')

    # print queue method allows queue data to be returned for potential printing
    def print_queue(self):
        stack_str = ""

        if not self.is_empty():
            for i in range(0, self.size()):
                stack_str += str(self.priority_queue[i].data)
                stack_str += "\n"
            return stack_str
        raise ValueError("Queue is empty!")
