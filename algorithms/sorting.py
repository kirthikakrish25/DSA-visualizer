# ============================================================
# BUBBLE SORT
# ============================================================

def bubble_sort_steps(arr):

    working = arr.copy()
    steps = []

    comparisons = 0
    swaps = 0

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": "Starting Bubble Sort."
    })

    n = len(working)

    for i in range(n):

        swapped = False

        for j in range(n - i - 1):

            comparisons += 1

            steps.append({
                "array": working.copy(),
                "active": [j, j + 1],
                "message": (
                    f"Compare {working[j]} and {working[j + 1]} | "
                    f"Comparisons: {comparisons}"
                )
            })

            if working[j] > working[j + 1]:

                working[j], working[j + 1] = (
                    working[j + 1],
                    working[j]
                )

                swapped = True
                swaps += 1

                steps.append({
                    "array": working.copy(),
                    "active": [j, j + 1],
                    "message": (
                        f"Swap indexes {j} and {j + 1} | "
                        f"Swaps: {swaps}"
                    )
                })

        if not swapped:
            break

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": (
            f"Array is sorted! | "
            f"Comparisons: {comparisons} | "
            f"Swaps: {swaps}"
        )
    })

    return steps


# ============================================================
# SELECTION SORT
# ============================================================

def selection_sort_steps(arr):

    working = arr.copy()
    steps = []

    comparisons = 0
    swaps = 0

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": "Starting Selection Sort."
    })

    n = len(working)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            comparisons += 1

            steps.append({
                "array": working.copy(),
                "active": [min_index, j],
                "message": (
                    f"Compare {working[min_index]} and {working[j]} | "
                    f"Comparisons: {comparisons}"
                )
            })

            if working[j] < working[min_index]:

                min_index = j

                steps.append({
                    "array": working.copy(),
                    "active": [i, min_index],
                    "message": (
                        f"New minimum: {working[min_index]} "
                        f"at index {min_index}"
                    )
                })

        if min_index != i:

            working[i], working[min_index] = (
                working[min_index],
                working[i]
            )

            swaps += 1

            steps.append({
                "array": working.copy(),
                "active": [i, min_index],
                "message": (
                    f"Swap indexes {i} and {min_index} | "
                    f"Swaps: {swaps}"
                )
            })

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": (
            f"Array is sorted! | "
            f"Comparisons: {comparisons} | "
            f"Swaps: {swaps}"
        )
    })

    return steps


# ============================================================
# INSERTION SORT
# ============================================================

def insertion_sort_steps(arr):

    working = arr.copy()
    steps = []

    comparisons = 0
    shifts = 0

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": "Starting Insertion Sort."
    })

    n = len(working)

    for i in range(1, n):

        key = working[i]
        j = i - 1

        steps.append({
            "array": working.copy(),
            "active": [i],
            "message": f"Take {key} as current element."
        })

        while j >= 0:

            comparisons += 1

            steps.append({
                "array": working.copy(),
                "active": [j, j + 1],
                "message": (
                    f"Compare {working[j]} and {key} | "
                    f"Comparisons: {comparisons}"
                )
            })

            if working[j] > key:

                working[j + 1] = working[j]

                shifts += 1

                steps.append({
                    "array": working.copy(),
                    "active": [j, j + 1],
                    "message": (
                        f"Shift element to index {j + 1} | "
                        f"Shifts: {shifts}"
                    )
                })

                j -= 1

            else:
                break

        working[j + 1] = key

        steps.append({
            "array": working.copy(),
            "active": [j + 1],
            "message": (
                f"Insert {key} at index {j + 1}"
            )
        })

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": (
            f"Array is sorted! | "
            f"Comparisons: {comparisons} | "
            f"Shifts: {shifts}"
        )
    })

    return steps


# ============================================================
# MERGE SORT
# ============================================================

def merge_sort_steps(arr):

    working = arr.copy()
    steps = []

    comparisons = 0

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": "Starting Merge Sort."
    })

    def merge(left, mid, right):

        nonlocal comparisons

        left_part = working[left:mid + 1]
        right_part = working[mid + 1:right + 1]

        i = 0
        j = 0
        k = left

        while i < len(left_part) and j < len(right_part):

            comparisons += 1

            steps.append({
                "array": working.copy(),
                "active": [
                    left + i,
                    mid + 1 + j
                ],
                "message": (
                    f"Compare {left_part[i]} and {right_part[j]} | "
                    f"Comparisons: {comparisons}"
                )
            })

            if left_part[i] <= right_part[j]:

                working[k] = left_part[i]
                i += 1

            else:

                working[k] = right_part[j]
                j += 1

            steps.append({
                "array": working.copy(),
                "active": [k],
                "message": (
                    f"Place {working[k]} at index {k}"
                )
            })

            k += 1

        while i < len(left_part):

            working[k] = left_part[i]

            steps.append({
                "array": working.copy(),
                "active": [k],
                "message": (
                    f"Place {working[k]} at index {k}"
                )
            })

            i += 1
            k += 1

        while j < len(right_part):

            working[k] = right_part[j]

            steps.append({
                "array": working.copy(),
                "active": [k],
                "message": (
                    f"Place {working[k]} at index {k}"
                )
            })

            j += 1
            k += 1

    def merge_sort(left, right):

        if left >= right:
            return

        mid = (left + right) // 2

        steps.append({
            "array": working.copy(),
            "active": list(range(left, right + 1)),
            "message": (
                f"Divide array from index {left} to {right}"
            )
        })

        merge_sort(left, mid)

        merge_sort(mid + 1, right)

        merge(left, mid, right)

    if len(working) > 1:
        merge_sort(0, len(working) - 1)

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": (
            f"Array is sorted using Merge Sort! | "
            f"Comparisons: {comparisons}"
        )
    })

    return steps

# ============================================================
# QUICK SORT
# ============================================================

def quick_sort_steps(arr):

    working = arr.copy()
    steps = []

    comparisons = 0
    swaps = 0

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": "Starting Quick Sort."
    })

    def partition(low, high):

        nonlocal comparisons, swaps

        pivot = working[high]

        steps.append({
            "array": working.copy(),
            "active": [high],
            "message": (
                f"Choose {pivot} as pivot "
                f"at index {high}"
            )
        })

        i = low - 1

        for j in range(low, high):

            comparisons += 1

            steps.append({
                "array": working.copy(),
                "active": [j, high],
                "message": (
                    f"Compare {working[j]} with pivot {pivot} | "
                    f"Comparisons: {comparisons}"
                )
            })

            if working[j] <= pivot:

                i += 1

                if i != j:

                    working[i], working[j] = (
                        working[j],
                        working[i]
                    )

                    swaps += 1

                    steps.append({
                        "array": working.copy(),
                        "active": [i, j],
                        "message": (
                            f"Swap indexes {i} and {j} | "
                            f"Swaps: {swaps}"
                        )
                    })

        if i + 1 != high:

            working[i + 1], working[high] = (
                working[high],
                working[i + 1]
            )

            swaps += 1

            steps.append({
                "array": working.copy(),
                "active": [i + 1, high],
                "message": (
                    f"Place pivot {pivot} at "
                    f"index {i + 1}"
                )
            })

        return i + 1

    def quick_sort(low, high):

        if low < high:

            pivot_index = partition(low, high)

            steps.append({
                "array": working.copy(),
                "active": [pivot_index],
                "message": (
                    f"Pivot {working[pivot_index]} "
                    f"is now in its correct position."
                )
            })

            quick_sort(
                low,
                pivot_index - 1
            )

            quick_sort(
                pivot_index + 1,
                high
            )

    if len(working) > 1:
        quick_sort(0, len(working) - 1)

    steps.append({
        "array": working.copy(),
        "active": [],
        "message": (
            f"Array is sorted using Quick Sort! | "
            f"Comparisons: {comparisons} | "
            f"Swaps: {swaps}"
        )
    })

    return steps


# ============================================================
# TEST MERGE SORT
# ============================================================

if __name__ == "__main__":

    arr = [8, 3, 5, 1, 7, 2]

    steps = quick_sort_steps(arr)

    for step in steps:

        print(step["message"])
        print(step["array"])
        print()