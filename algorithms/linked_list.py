class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            return None

        deleted_value = self.head.data
        self.head = self.head.next

        return deleted_value

    def delete_from_end(self):
        if self.head is None:
            return None

        if self.head.next is None:
            deleted_value = self.head.data
            self.head = None
            return deleted_value

        current = self.head

        while current.next.next is not None:
            current = current.next

        deleted_value = current.next.data
        current.next = None

        return deleted_value

    def search(self, target):
        current = self.head

        while current is not None:
            if current.data == target:
                return True

            current = current.next

        return False

    def display(self):
        values = []

        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values

    def size(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count


if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    print("Linked List:")
    print(linked_list.display())

    linked_list.insert_at_beginning(5)

    print("After inserting at beginning:")
    print(linked_list.display())

    linked_list.delete_from_beginning()

    print("After deleting from beginning:")
    print(linked_list.display())

    print("Search 20:", linked_list.search(20))
    print("Size:", linked_list.size())