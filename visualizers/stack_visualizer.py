import streamlit as st

from algorithms.stack import Stack


def display_stack(stack):

    if stack.is_empty():

        st.info("Stack is empty.")

        return

    st.subheader("Stack")

    # Show from TOP to BOTTOM
    for i in range(stack.size() - 1, -1, -1):

        value = stack.items[i]

        if i == stack.size() - 1:

            label = "TOP"

        else:

            label = ""

        st.markdown(
            f"""
            <div style="
                padding: 15px;
                margin: 5px auto;
                max-width: 300px;
                border: 2px solid;
                border-radius: 8px;
                text-align: center;
                font-size: 20px;
                font-weight: bold;
            ">
                {value}
                <br>
                <small>{label}</small>
            </div>
            """,
            unsafe_allow_html=True
        )


def show_stack_visualizer():

    st.header("Stack Visualizer")

    st.write(
        "Visualize Stack operations using LIFO "
        "(Last In, First Out)."
    )

    # --------------------------------------------------------
    # SESSION STATE
    # --------------------------------------------------------

    if "stack" not in st.session_state:

        st.session_state.stack = Stack()

    stack = st.session_state.stack

    # --------------------------------------------------------
    # PUSH
    # --------------------------------------------------------

    st.subheader("Push")

    value = st.number_input(
        "Enter a value:",
        step=1,
        key="stack_value"
    )

    if st.button(
        "Push",
        key="push_button"
    ):

        stack.push(value)

        st.rerun()

    # --------------------------------------------------------
    # POP
    # --------------------------------------------------------

    if st.button(
        "Pop",
        key="pop_button"
    ):

        if stack.is_empty():

            st.warning("Stack Underflow!")

        else:

            removed = stack.pop()

            st.success(
                f"Popped: {removed}"
            )

            st.rerun()

    # --------------------------------------------------------
    # PEEK
    # --------------------------------------------------------

    if st.button(
        "Peek",
        key="peek_button"
    ):

        if stack.is_empty():

            st.warning("Stack is empty.")

        else:

            st.info(
                f"Top element: {stack.peek()}"
            )

    # --------------------------------------------------------
    # SIZE
    # --------------------------------------------------------

    st.write(
        f"**Stack Size:** {stack.size()}"
    )

    # --------------------------------------------------------
    # VISUALIZATION
    # --------------------------------------------------------

    st.divider()

    display_stack(stack)

    # --------------------------------------------------------
    # CLEAR
    # --------------------------------------------------------

    if st.button(
        "Clear Stack",
        key="clear_stack"
    ):

        st.session_state.stack = Stack()

        st.rerun()