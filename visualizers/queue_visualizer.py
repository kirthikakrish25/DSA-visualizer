import streamlit as st

from algorithms.queue import Queue


def display_queue(queue):

    if queue.is_empty():

        st.info("Queue is empty.")

        return

    st.subheader("Queue")

    cols = st.columns(len(queue.items))

    for i, value in enumerate(queue.items):

        with cols[i]:

            if i == 0:
                label = "FRONT"
            elif i == len(queue.items) - 1:
                label = "REAR"
            else:
                label = ""

            st.markdown(
                f"""
                <div style="
                    padding: 20px 5px;
                    border: 2px solid;
                    border-radius: 10px;
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


def show_queue_visualizer():

    st.header("Queue Visualizer")

    st.write(
        "Visualize Queue operations using FIFO "
        "(First In, First Out)."
    )

    # ========================================================
    # SESSION STATE
    # ========================================================

    if "queue" not in st.session_state:

        st.session_state.queue = Queue()

    queue = st.session_state.queue

    # ========================================================
    # ENQUEUE
    # ========================================================

    st.subheader("Enqueue")

    value = st.number_input(
        "Enter a value:",
        step=1,
        key="queue_value"
    )

    if st.button(
        "Enqueue",
        key="enqueue_button"
    ):

        queue.enqueue(value)

        st.rerun()

    # ========================================================
    # DEQUEUE
    # ========================================================

    if st.button(
        "Dequeue",
        key="dequeue_button"
    ):

        if queue.is_empty():

            st.warning("Queue Underflow!")

        else:

            removed = queue.dequeue()

            st.success(
                f"Dequeued: {removed}"
            )

            st.rerun()

    # ========================================================
    # FRONT
    # ========================================================

    if st.button(
        "Front",
        key="front_button"
    ):

        if queue.is_empty():

            st.warning("Queue is empty.")

        else:

            st.info(
                f"Front element: {queue.front()}"
            )

    # ========================================================
    # REAR
    # ========================================================

    if st.button(
        "Rear",
        key="rear_button"
    ):

        if queue.is_empty():

            st.warning("Queue is empty.")

        else:

            st.info(
                f"Rear element: {queue.rear()}"
            )

    # ========================================================
    # SIZE
    # ========================================================

    st.write(
        f"**Queue Size:** {queue.size()}"
    )

    # ========================================================
    # VISUALIZATION
    # ========================================================

    st.divider()

    display_queue(queue)

    # ========================================================
    # CLEAR
    # ========================================================

    if st.button(
        "Clear Queue",
        key="clear_queue"
    ):

        st.session_state.queue = Queue()

        st.rerun()