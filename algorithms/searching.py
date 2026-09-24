def linear_search_steps(arr, target):
    """
    Generate steps for Linear Search.
    """

    steps = []

    for i in range(len(arr)):

        steps.append({
            "array": arr.copy(),
            "active": [i],
            "message": f"Checking index {i}: {arr[i]} == {target}?"
        })

        if arr[i] == target:

            steps.append({
                "array": arr.copy(),
                "active": [i],
                "message": f"Found {target} at index {i}!"
            })

            return steps

    steps.append({
        "array": arr.copy(),
        "active": [],
        "message": f"{target} was not found in the array."
    })

    return steps


def binary_search_steps(arr, target):
    """
    Generate steps for Binary Search.

    The array must be sorted.
    """

    steps = []

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        steps.append({
            "array": arr.copy(),
            "active": [left, mid, right],
            "message": (
                f"Left = {left}, "
                f"Middle = {mid}, "
                f"Right = {right}"
            )
        })

        if arr[mid] == target:

            steps.append({
                "array": arr.copy(),
                "active": [mid],
                "message": f"Found {target} at index {mid}!"
            })

            return steps

        elif arr[mid] < target:

            steps.append({
                "array": arr.copy(),
                "active": [mid],
                "message": (
                    f"{arr[mid]} < {target}. "
                    f"Search the right half."
                )
            })

            left = mid + 1

        else:

            steps.append({
                "array": arr.copy(),
                "active": [mid],
                "message": (
                    f"{arr[mid]} > {target}. "
                    f"Search the left half."
                )
            })

            right = mid - 1

    steps.append({
        "array": arr.copy(),
        "active": [],
        "message": f"{target} was not found."
    })

    return steps

if __name__ == "__main__":

    arr = [10, 20, 30, 40, 50]

    print("LINEAR SEARCH")

    linear_steps = linear_search_steps(arr, 40)

    for step in linear_steps:
        print(step["message"])

    print("\nBINARY SEARCH")

    binary_steps = binary_search_steps(arr, 40)

    for step in binary_steps:
        print(step["message"])