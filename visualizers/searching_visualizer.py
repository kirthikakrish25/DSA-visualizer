import streamlit as st

from algorithms.searching import (
    linear_search_steps,
    binary_search_steps
)


def display_search_array(arr, active=None):
    """
    Display the array and highlight active indexes.
    """

    if active is None:
        active = []

    if not arr:
        st.warning("Array is empty.")
        return

    cols = st.columns(len(arr))

    for i, value in enumerate(arr):

        with cols[i]:

            if i in active:
                st.markdown(
                    f"""
                    <div style="
                        background-color:#2563eb;
                        color:white;
                        padding:20px 5px;
                        border-radius:10px;
                        text-align:center;
                        font-size:22px;
                        font-weight:bold;
                    ">
                        {value}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.markdown(
                    f"""
                    <div style="
                        background-color:#e2e8f0;
                        color:#0f172a;
                        padding:20px 5px;
                        border-radius:10px;
                        text-align:center;
                        font-size:22px;
                        font-weight:bold;
                    ">
                        {value}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.caption(f"Index {i}")


def show_searching_visualizer():

    st.header("Searching Visualizer")

    st.write(
        "Visualize Linear Search and Binary Search "
        "step by step."
    )

    # -------------------------
    # ARRAY
    # -------------------------

    if "search_array" not in st.session_state:
        st.session_state.search_array = [
            10, 20, 30, 40, 50
        ]

    arr = st.session_state.search_array

    st.subheader("Array")

    display_search_array(arr)

    st.divider()

    # -------------------------
    # ALGORITHM
    # -------------------------

    algorithm = st.selectbox(
        "Choose searching algorithm:",
        [
            "Linear Search",
            "Binary Search"
        ]
    )

    target = st.number_input(
        "Enter value to search:",
        value=30,
        step=1
    )

    # -------------------------
    # START SEARCH
    # -------------------------

    if st.button("Start Search"):

        if algorithm == "Linear Search":

            st.session_state.search_steps = (
                linear_search_steps(
                    arr,
                    int(target)
                )
            )

        else:

            # Binary Search requires sorted data.
            sorted_arr = sorted(arr)

            st.session_state.search_array = sorted_arr

            st.session_state.search_steps = (
                binary_search_steps(
                    sorted_arr,
                    int(target)
                )
            )

        st.session_state.search_step_index = 0

    # -------------------------
    # STEP STATE
    # -------------------------

    if "search_steps" not in st.session_state:
        st.session_state.search_steps = []

    if "search_step_index" not in st.session_state:
        st.session_state.search_step_index = 0

    steps = st.session_state.search_steps

    # -------------------------
    # VISUALIZATION
    # -------------------------

    if steps:

        index = st.session_state.search_step_index

        current_step = steps[index]

        st.subheader("Visualization")

        display_search_array(
            current_step["array"],
            current_step["active"]
        )

        st.info(
            current_step["message"]
        )

        st.progress(
            (index + 1) / len(steps)
        )

        st.caption(
            f"Step {index + 1} of {len(steps)}"
        )

        # -------------------------
        # CONTROLS
        # -------------------------

        previous, next_step, reset = st.columns(3)

        with previous:

            if st.button(
                "Previous",
                disabled=index == 0
            ):

                st.session_state.search_step_index -= 1

                st.rerun()

        with next_step:

            if st.button(
                "Next",
                disabled=index == len(steps) - 1
            ):

                st.session_state.search_step_index += 1

                st.rerun()

        with reset:

            if st.button("Reset"):

                st.session_state.search_steps = []

                st.session_state.search_step_index = 0

                st.rerun()

    # -------------------------
    # COMPLEXITY
    # -------------------------

    st.divider()

    st.subheader("Algorithm Information")

    if algorithm == "Linear Search":

        st.write("Time Complexity: O(n)")
        st.write("Space Complexity: O(1)")

        st.info(
            "Linear Search checks elements one by one."
        )

    else:

        st.write("Time Complexity: O(log n)")
        st.write("Space Complexity: O(1)")

        st.info(
            "Binary Search repeatedly divides the "
            "search space in half."
        )