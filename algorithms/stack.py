# ============================================================
# STACK
# ============================================================

class Stack:

    def __init__(self):
        self.items = []

    # --------------------------------------------------------
    # PUSH
    # --------------------------------------------------------

    def push(self, value):

        self.items.append(value)

    # --------------------------------------------------------
    # POP
    # --------------------------------------------------------

    def pop(self):

        if self.is_empty():
            return None

        return self.items.pop()

    # --------------------------------------------------------
    # PEEK
    # --------------------------------------------------------

    def peek(self):

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
# TEST STACK
# ============================================================

if __name__ == "__main__":

    stack = Stack()

    print("Initial stack:")
    print(stack.display())

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("\nAfter pushing 10, 20, 30:")
    print(stack.display())

    print("\nTop element:")
    print(stack.peek())

    print("\nPopped element:")
    print(stack.pop())

    print("\nStack after pop:")
    print(stack.display())

    print("\nStack size:")
    print(stack.size())