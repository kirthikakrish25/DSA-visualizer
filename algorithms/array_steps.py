
def make_step(arr, active, message):
    """Save an independent snapshot of the array."""
    return {
        "array": arr.copy(),
        "active": active.copy(),
        "message": message
    }


def insertion_steps(arr, value, position):
    """Generate the steps for insertion at an index."""
    if not 0 <= position <= len(arr):
        raise ValueError("Invalid insertion position")

    working = arr.copy()
    steps = [make_step(working, [], "Original array")]

    # Create an extra slot at the end.
    working.append(None)
    steps.append(
        make_step(working, [len(working) - 1],
                  "Create an empty slot")
    )

    # Shift elements one position to the right.
    for i in range(len(working) - 2, position - 1, -1):
        working[i + 1] = working[i]
        working[i] = None

        steps.append(
            make_step(
                working,
                [i, i + 1],
                f"Shift {working[i + 1]} to index {i + 1}"
            )
        )

    # Insert the new value.
    working[position] = value

    steps.append(
        make_step(
            working,
            [position],
            f"Inserted {value} at index {position}"
        )
    )

    return steps


def deletion_steps(arr, position):
    """Generate the steps for deletion at an index."""
    if not 0 <= position < len(arr):
        raise ValueError("Invalid deletion position")

    working = arr.copy()
    steps = [make_step(working, [], "Original array")]

    deleted = working[position]
    working[position] = None

    steps.append(
        make_step(
            working, [position],
            f"Remove {deleted} from index {position}"
        )
    )

    # Shift the remaining elements to the left.
    for i in range(position, len(working) - 1):
        working[i] = working[i + 1]
        working[i + 1] = None

        steps.append(
            make_step(
                working, [i, i + 1],
                f"Shift element to index {i}"
            )
        )

    working.pop()

    steps.append(
        make_step(
            working, [],
            f"Deleted {deleted} successfully"
        )
    )

    return steps


def search_steps(arr, target):
    """Record each comparison during linear search."""
    working = arr.copy()
    steps = [make_step(working, [], "Start searching")]

    for i, value in enumerate(working):
        steps.append(
            make_step(
                working, [i],
                f"Comparing {value} with {target}"
            )
        )

        if value == target:
            steps.append(
                make_step(
                    working, [i],
                    f"Found {target} at index {i}"
                )
            )
            return steps

    steps.append(
        make_step(
            working, [],
            f"{target} was not found"
        )
    )

    return steps