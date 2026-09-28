import streamlit as st

from algorithms.sorting import (
    bubble_sort_steps,
    selection_sort_steps,
    insertion_sort_steps,
    merge_sort_steps,
    quick_sort_steps
)


def display_sorting_array(arr, active=None):

    if active is None:
        active = []

    if not arr:
        st.warning("Array is empty.")
        return

    cols = st.columns(len(arr))

    for i, value in enumerate(arr):

        with cols[i]:

            if i in active:
                background = "#2563eb"
                foreground = "white"
            else:
                background = "#e2e8f0"
                foreground = "#0f172a"

            st.markdown(
                f"""
                <div style="
                    background-color: {background};
                    color: {foreground};
                    padding: 20px 5px;
                    border-radius: 10px;
                    text-align: center;
                    font-size: 22px;
                    font-weight: bold;
                ">
                    {value}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(f"Index {i}")


def show_sorting_visualizer():

    st.header("Sorting Visualizer")

    st.write(
        "Visualize sorting algorithms step by step."
    )

    # -----------------------------------------
    # SESSION STATE
    # -----------------------------------------

    if "sorting_array" not in st.session_state:
        st.session_state.sorting_array = [
            5, 2, 8, 1, 3
        ]

    if "sorting_steps" not in st.session_state:
        st.session_state.sorting_steps = []

    if "sorting_step_index" not in st.session_state:
        st.session_state.sorting_step_index = 0

    arr = st.session_state.sorting_array

    # -----------------------------------------
    # CURRENT ARRAY
    # -----------------------------------------

    st.subheader("Current Array")

    display_sorting_array(arr)

    st.divider()

    # -----------------------------------------
    # ALGORITHM SELECTION
    # -----------------------------------------

    algorithm = st.selectbox(
    "Choose sorting algorithm:",
    [
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort"
    ],
    key="sorting_algorithm"
)
    # -----------------------------------------
    # START SORTING
    # -----------------------------------------

    if st.button(
        "Start Sorting",
        key="start_sorting"
    ):

        if algorithm == "Bubble Sort":

            st.session_state.sorting_steps = (
                bubble_sort_steps(arr)
            )

        elif algorithm == "Selection Sort":

            st.session_state.sorting_steps = (
                selection_sort_steps(arr)
            )

        elif algorithm == "Insertion Sort":

            st.session_state.sorting_steps = (
                insertion_sort_steps(arr)
            )

        elif algorithm == "Merge Sort":

            st.session_state.sorting_steps = (
                merge_sort_steps(arr)
            )

        elif algorithm == "Quick Sort":

            st.session_state.sorting_steps = (
                 quick_sort_steps(arr)
            )

        st.session_state.sorting_step_index = 0

        st.rerun()

    # -----------------------------------------
    # GET STEPS
    # -----------------------------------------

    steps = st.session_state.sorting_steps

    if not steps:

        st.info(
            "Choose an algorithm and click "
            "'Start Sorting' to begin."
        )

    # -----------------------------------------
    # VISUALIZATION
    # -----------------------------------------

    if steps:

        index = st.session_state.sorting_step_index

        # Safety check
        if index < 0:
            index = 0
            st.session_state.sorting_step_index = 0

        if index >= len(steps):
            index = len(steps) - 1
            st.session_state.sorting_step_index = index

        current_step = steps[index]

        st.subheader(
            "Step-by-Step Visualization"
        )

        display_sorting_array(
            current_step["array"],
            current_step["active"]
        )

        st.info(
            current_step["message"]
        )

        # Progress bar
        progress = (index + 1) / len(steps)

        st.progress(progress)

        st.caption(
            f"Step {index + 1} of {len(steps)}"
        )

        st.divider()

        # -----------------------------------------
        # BUTTONS
        # -----------------------------------------

        col1, col2, col3, col4 = st.columns(4)

        # Previous
        with col1:

            if st.button(
                "Previous",
                key="sorting_previous",
                disabled=(index == 0)
            ):

                st.session_state.sorting_step_index = (
                    index - 1
                )

                st.rerun()

        # Next
        with col2:

            if st.button(
                "Next",
                key="sorting_next",
                disabled=(index == len(steps) - 1)
            ):

                st.session_state.sorting_step_index = (
                    index + 1
                )

                st.rerun()

        # Apply
        with col3:

            if st.button(
                "Apply Result",
                key="sorting_apply"
            ):

                if index == len(steps) - 1:

                    st.session_state.sorting_array = (
                        steps[-1]["array"].copy()
                    )

                    st.session_state.sorting_steps = []

                    st.session_state.sorting_step_index = 0

                    st.rerun()

                else:

                    st.warning(
                        "Go to the final step before "
                        "applying the result."
                    )

        # Reset
        with col4:

            if st.button(
                "Reset",
                key="sorting_reset"
            ):

                st.session_state.sorting_array = [
                    5, 2, 8, 1, 3
                ]

                st.session_state.sorting_steps = []

                st.session_state.sorting_step_index = 0

                st.rerun()

    # -----------------------------------------
    # ALGORITHM INFORMATION
    # -----------------------------------------

    st.divider()

    st.subheader("Algorithm Information")

    if algorithm == "Bubble Sort":

        st.write("Best Case: O(n)")
        st.write("Average Case: O(n²)")
        st.write("Worst Case: O(n²)")
        st.write("Space Complexity: O(1)")

        st.info(
            "Bubble Sort compares adjacent elements "
            "and swaps them when they are in the wrong order."
        )

    elif algorithm == "Selection Sort":

        st.write("Best Case: O(n²)")
        st.write("Average Case: O(n²)")
        st.write("Worst Case: O(n²)")
        st.write("Space Complexity: O(1)")

        st.info(
            "Selection Sort finds the minimum element "
            "and places it in the correct position."
        )

    elif algorithm == "Insertion Sort":

        st.write("Best Case: O(n)")
        st.write("Average Case: O(n²)")
        st.write("Worst Case: O(n²)")
        st.write("Space Complexity: O(1)")

        st.info(
            "Insertion Sort builds the sorted portion "
            "one element at a time."
        )

    elif algorithm == "Merge Sort":

        st.write("Best Case: O(n log n)")
        st.write("Average Case: O(n log n)")
        st.write("Worst Case: O(n log n)")
        st.write("Space Complexity: O(n)")

        st.info(
            "Merge Sort divides the array into smaller "
            "parts and merges them in sorted order."
        )