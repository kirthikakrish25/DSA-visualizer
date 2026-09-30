class MinHeap:

    def __init__(self):
        self.heap = []

    # --------------------------------
    # Parent / Child Index
    # --------------------------------

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    # --------------------------------
    # Insert
    # --------------------------------

    def insert(self, value):

        self.heap.append(value)

        self._heapify_up(len(self.heap) - 1)

    # --------------------------------
    # Heapify Up
    # --------------------------------

    def _heapify_up(self, index):

        while index > 0:

            parent_index = self.parent(index)

            if self.heap[index] < self.heap[parent_index]:

                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index]
                )

                index = parent_index

            else:
                break

    # --------------------------------
    # Peek
    # --------------------------------

    def peek(self):

        if not self.heap:
            return None

        return self.heap[0]

    # --------------------------------
    # Extract Minimum
    # --------------------------------

    def extract_min(self):

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._heapify_down(0)

        return minimum

    # --------------------------------
    # Heapify Down
    # --------------------------------

    def _heapify_down(self, index):

        size = len(self.heap)

        while True:

            left = self.left_child(index)
            right = self.right_child(index)

            smallest = index

            if (
                left < size
                and self.heap[left] < self.heap[smallest]
            ):
                smallest = left

            if (
                right < size
                and self.heap[right] < self.heap[smallest]
            ):
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index]
            )

            index = smallest

    # --------------------------------
    # Size
    # --------------------------------

    def size(self):
        return len(self.heap)

    # --------------------------------
    # Empty
    # --------------------------------

    def is_empty(self):
        return len(self.heap) == 0

    # --------------------------------
    # Display
    # --------------------------------

    def display(self):
        return self.heap.copy()


# --------------------------------
# Test
# --------------------------------

if __name__ == "__main__":

    heap = MinHeap()

    values = [40, 20, 30, 10, 50, 15]

    for value in values:
        heap.insert(value)

    print("Heap:")
    print(heap.display())

    print()

    print("Minimum:")
    print(heap.peek())

    print()

    print("Extracted:")
    print(heap.extract_min())

    print()

    print("Heap after extraction:")
    print(heap.display())