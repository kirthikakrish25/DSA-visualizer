
import streamlit as st

from algorithms.arrays import create_array
from algorithms.array_steps import (
    insertion_steps,
    deletion_steps,
    search_steps
)


def display_array(arr, active=None):
    """Display array elements as colored boxes."""
    if active is None:
        active = []

    if not arr:
        st.info("The array is empty.")
        return

    # Use up to 8 columns per row.
    for start in range(0, len(arr), 8):
        chunk = arr[start:start + 8]
        cols = st.columns(len(chunk))

        for offset, value in enumerate(chunk):
            i = start + offset
            highlighted = i in active

            background = (
                "#2563eb" if highlighted else "#e2e8f0"
            )
            foreground = (
                "#ffffff" if highlighted else "#0f172a"
            )

            label = "Empty" if value is None else str(value)

            with cols[offset]:
                st.markdown(
                    f"""
                    <div style="
                        background:{background};
                        color:{foreground};
                        text-align:center;
                        padding:16px 4px;
                        border-radius:8px;
                        font-size:20px;
                        font-weight:bold;
                    ">
                        {label}
                    </div>
                    <p style="text-align:center">
                        Index {i}
                    </p>
                    """,
                    unsafe_allow_html=True
                )


def show_array_visualizer():
    st.header("Array Visualizer")
    st.write("Learn array operations step by step.")

    # Initialize persistent application state.
    if "array" not in st.session_state:
        st.session_state.array = create_array()

    if "array_steps" not in st.session_state:
        st.session_state.array_steps = []

    if "step_index" not in st.session_state:
        st.session_state.step_index = 0

    arr = st.session_state.array

    st.subheader("Current Array")
    display_array(arr)

    st.divider()

    operation = st.radio(
        "Choose an operation",
        ["Insert", "Delete", "Search"],
        horizontal=True
    )

    if operation == "Insert":
        position_type = st.selectbox(
            "Insert at",
            ["Beginning", "End", "Position"]
        )

        value = st.number_input(
            "Value to insert",
            value=25,
            step=1
        )

        if position_type == "Beginning":
            position = 0
        elif position_type == "End":
            position = len(arr)
        else:
            position = st.number_input(
                "Index",
                min_value=0,
                max_value=len(arr),
                step=1
            )

        if st.button("Visualize insertion"):
            st.session_state.array_steps = insertion_steps(
                arr, int(value), int(position)
            )
            st.session_state.step_index = 0

    elif operation == "Delete":
        if arr:
            position_type = st.selectbox(
                "Delete from",
                ["Beginning", "End", "Position"]
            )

            if position_type == "Beginning":
                position = 0
            elif position_type == "End":
                position = len(arr) - 1
            else:
                position = st.number_input(
                    "Index to delete",
                    min_value=0,
                    max_value=len(arr) - 1,
                    step=1
                )

            if st.button("Visualize deletion"):
                st.session_state.array_steps = deletion_steps(
                    arr, int(position)
                )
                st.session_state.step_index = 0
        else:
            st.warning("Nothing to delete.")

    elif operation == "Search":
        target = st.number_input(
            "Value to search",
            value=30,
            step=1
        )

        if st.button("Visualize search"):
            st.session_state.array_steps = search_steps(
                arr, int(target)
            )
            st.session_state.step_index = 0

    st.divider()

    # Display the animation frames.
    steps = st.session_state.array_steps

    if steps:
        index = st.session_state.step_index
        current = steps[index]

        st.subheader("Step-by-step visualization")

        st.progress((index + 1) / len(steps))
        st.caption(f"Step {index + 1} of {len(steps)}")

        display_array(
            current["array"],
            current["active"]
        )

        st.info(current["message"])

        previous, next_step, finish = st.columns(3)

        with previous:
            if st.button(
                "Previous",
                disabled=index == 0
            ):
                st.session_state.step_index -= 1
                st.rerun()

        with next_step:
            if st.button(
                "Next",
                disabled=index == len(steps) - 1
            ):
                st.session_state.step_index += 1
                st.rerun()

        with finish:
            if st.button("Apply result"):
                if index != len(steps) - 1:
                    st.warning(
                        "Go to the final step before applying."
                    )
                else:
                    st.session_state.array = (
                        steps[-1]["array"].copy()
                    )
                    st.session_state.array_steps = []
                    st.session_state.step_index = 0
                    st.rerun()

    st.divider()

    if st.button("Reset array"):
        st.session_state.array = create_array()
        st.session_state.array_steps = []
        st.session_state.step_index = 0
        st.rerun()