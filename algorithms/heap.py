class MinHeap:

    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, value):

        self.heap.append(value)

        self._heapify_up(len(self.heap) - 1)

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

    def peek(self):

        if not self.heap:
            return None

        return self.heap[0]

    def extract_min(self):

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._heapify_down(0)

        return minimum

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

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        return self.heap.copy()


# =================================
# MAX HEAP
# =================================

class MaxHeap:

    def __init__(self):
        self.heap = []

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

            if self.heap[index] > self.heap[parent_index]:

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
    # Extract Maximum
    # --------------------------------

    def extract_max(self):

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]

        self.heap[0] = self.heap.pop()

        self._heapify_down(0)

        return maximum

    # --------------------------------
    # Heapify Down
    # --------------------------------

    def _heapify_down(self, index):

        size = len(self.heap)

        while True:

            left = self.left_child(index)
            right = self.right_child(index)

            largest = index

            if (
                left < size
                and self.heap[left] > self.heap[largest]
            ):
                largest = left

            if (
                right < size
                and self.heap[right] > self.heap[largest]
            ):
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = (
                self.heap[largest],
                self.heap[index]
            )

            index = largest

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


# =================================
# TEST
# =================================

if __name__ == "__main__":

    print("MIN HEAP")

    min_heap = MinHeap()

    for value in [40, 20, 30, 10, 50, 15]:
        min_heap.insert(value)

    print("Heap:", min_heap.display())
    print("Minimum:", min_heap.peek())
    print("Extracted:", min_heap.extract_min())
    print("After extraction:", min_heap.display())

    print()

    print("MAX HEAP")

    max_heap = MaxHeap()

    for value in [40, 20, 30, 10, 50, 15]:
        max_heap.insert(value)

    print("Heap:", max_heap.display())
    print("Maximum:", max_heap.peek())
    print("Extracted:", max_heap.extract_max())
    print("After extraction:", max_heap.display())