def create_array():
    """Create and return a sample array."""
    return [10, 20, 30, 40, 50]


def insert_at_beginning(arr, value):
    """Insert a value at the beginning of the array."""
    arr.insert(0, value)
    return arr


def insert_at_end(arr, value):
    """Insert a value at the end of the array."""
    arr.append(value)
    return arr


def insert_at_position(arr, value, position):
    """Insert a value at a specific position."""
    if position < 0 or position > len(arr):
        return None

    arr.insert(position, value)
    return arr


def delete_at_beginning(arr):
    """Delete the first element."""
    if len(arr) == 0:
        return None

    arr.pop(0)
    return arr


def delete_at_end(arr):
    """Delete the last element."""
    if len(arr) == 0:
        return None

    arr.pop()
    return arr


def delete_at_position(arr, position):
    """Delete an element from a specific position."""
    if position < 0 or position >= len(arr):
        return None

    arr.pop(position)
    return arr


def search_array(arr, target):
    """Search for a value using linear search."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":

    arr = create_array()

    print("Original array:", arr)

    insert_at_beginning(arr, 5)
    print("After beginning insertion:", arr)

    insert_at_end(arr, 60)
    print("After end insertion:", arr)

    insert_at_position(arr, 25, 2)
    print("After position insertion:", arr)

    delete_at_beginning(arr)
    print("After beginning deletion:", arr)

    delete_at_end(arr)
    print("After end deletion:", arr)

    delete_at_position(arr, 1)
    print("After position deletion:", arr)

    result = search_array(arr, 40)
    print("Index of 40:", result)

    """
Array Operation Complexities

Access by index       : O(1)
Search                : O(n)

Insert at beginning   : O(n)
Insert at end         : O(1) average
Insert at position    : O(n)

Delete beginning      : O(n)
Delete end            : O(1)
Delete position       : O(n)
"""