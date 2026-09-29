class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # --------------------------------
    # INSERT AT BEGINNING
    # --------------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # --------------------------------
    # INSERT AT END
    # --------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # --------------------------------
    # INSERT AT POSITION
    # --------------------------------
    def insert_at_position(self, data, position):

        # Invalid position
        if position < 0:
            return False

        # Position 0 means beginning
        if position == 0:
            self.insert_at_beginning(data)
            return True

        new_node = Node(data)

        current = self.head

        # Move to node before required position
        for _ in range(position - 1):

            if current is None:
                return False

            current = current.next

        # Position is outside the list
        if current is None:
            return False

        # Connect new node
        new_node.next = current.next
        current.next = new_node

        return True

    # --------------------------------
    # DELETE FROM BEGINNING
    # --------------------------------
    def delete_from_beginning(self):

        if self.head is None:
            return None

        deleted_value = self.head.data

        self.head = self.head.next

        return deleted_value

    # --------------------------------
    # DELETE FROM END
    # --------------------------------
    def delete_from_end(self):

        # Empty list
        if self.head is None:
            return None

        # Only one node
        if self.head.next is None:

            deleted_value = self.head.data

            self.head = None

            return deleted_value

        current = self.head

        # Move to second-last node
        while current.next.next is not None:
            current = current.next

        deleted_value = current.next.data

        current.next = None

        return deleted_value

    # --------------------------------
    # DELETE AT POSITION
    # --------------------------------
    def delete_at_position(self, position):

        # Empty list or invalid position
        if self.head is None or position < 0:
            return None

        # Delete first node
        if position == 0:
            return self.delete_from_beginning()

        current = self.head

        # Move to node before target
        for _ in range(position - 1):

            if current.next is None:
                return None

            current = current.next

        # Position doesn't exist
        if current.next is None:
            return None

        deleted_value = current.next.data

        # Remove node
        current.next = current.next.next

        return deleted_value

    # --------------------------------
    # SEARCH
    # --------------------------------
    def search(self, target):

        current = self.head

        while current is not None:

            if current.data == target:
                return True

            current = current.next

        return False

    # --------------------------------
    # DISPLAY
    # --------------------------------
    def display(self):

        values = []

        current = self.head

        while current is not None:

            values.append(current.data)

            current = current.next

        return values

    # --------------------------------
    # SIZE
    # --------------------------------
    def size(self):

        count = 0

        current = self.head

        while current is not None:

            count += 1

            current = current.next

        return count

def traversal_steps(self):
    steps = []

    current = self.head
    index = 0

    while current is not None:

        steps.append({
            "index": index,
            "value": current.data,
            "message": f"Visiting node {index}: {current.data}"
        })

        current = current.next
        index += 1

    steps.append({
        "index": -1,
        "value": None,
        "message": "Traversal completed. Reached NULL."
    })

    return steps  
# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    linked_list = LinkedList()

    # Insert at end
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)

    print("Initial Linked List:")
    print(linked_list.display())

    # Insert at beginning
    linked_list.insert_at_beginning(5)

    print("\nAfter inserting 5 at beginning:")
    print(linked_list.display())

    # Insert at position
    result = linked_list.insert_at_position(25, 2)

    print("\nAfter inserting 25 at position 2:")
    print(linked_list.display())

    print("Insert successful:", result)

    # Delete from beginning
    deleted = linked_list.delete_from_beginning()

    print("\nDeleted from beginning:", deleted)
    print("List:")
    print(linked_list.display())

    # Delete from end
    deleted = linked_list.delete_from_end()

    print("\nDeleted from end:", deleted)
    print("List:")
    print(linked_list.display())

    # Delete at position
    deleted = linked_list.delete_at_position(1)

    print("\nDeleted from position 1:", deleted)
    print("List:")
    print(linked_list.display())

    # Search
    print("\nSearch 20:", linked_list.search(20))
    print("Search 100:", linked_list.search(100))

    # Size
    print("\nSize:", linked_list.size())