# ============================================================
# QUEUE
# ============================================================

class Queue:

    def __init__(self):
        self.items = []

    # --------------------------------------------------------
    # ENQUEUE
    # --------------------------------------------------------

    def enqueue(self, value):

        self.items.append(value)

    # --------------------------------------------------------
    # DEQUEUE
    # --------------------------------------------------------

    def dequeue(self):

        if self.is_empty():
            return None

        return self.items.pop(0)

    # --------------------------------------------------------
    # FRONT
    # --------------------------------------------------------

    def front(self):

        if self.is_empty():
            return None

        return self.items[0]

    # --------------------------------------------------------
    # REAR
    # --------------------------------------------------------

    def rear(self):

        if self.is_empty():
            return None

        return self.items[-1]

    # --------------------------------------------------------
    # IS EMPTY
    # --------------------------------------------------------

    def is_empty(self):

        return len(self.items) == 0

    # --------------------------------------------------------
    # SIZE
    # --------------------------------------------------------

    def size(self):

        return len(self.items)

    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    def display(self):

        return self.items.copy()


# ============================================================
# TEST QUEUE
# ============================================================

if __name__ == "__main__":

    queue = Queue()

    print("Initial queue:")
    print(queue.display())

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("\nAfter enqueue:")
    print(queue.display())

    print("\nFront:")
    print(queue.front())

    print("\nRear:")
    print(queue.rear())

    print("\nDequeued:")
    print(queue.dequeue())

    print("\nQueue after dequeue:")
    print(queue.display())

    print("\nQueue size:")
    print(queue.size())