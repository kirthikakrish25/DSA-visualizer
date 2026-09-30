import streamlit as st
import streamlit.components.v1 as components

from algorithms.heap import MinHeap


def display_heap(heap):

    values = heap.heap

    if not values:
        st.info("Heap is empty. Insert some values.")
        return

    positions = {}

    # --------------------------------
    # Calculate node positions
    # --------------------------------

    levels = {}

    for index, value in enumerate(values):

        level = index.bit_length()

        if level not in levels:
            levels[level] = []

        levels[level].append(index)

    max_level = max(levels.keys())

    for level, indexes in levels.items():

        count = len(indexes)

        spacing = 800 / (count + 1)

        y = 70 + level * 100

        for position, index in enumerate(indexes):

            x = spacing * (position + 1)

            positions[index] = (x, y)

    svg_elements = []

    # --------------------------------
    # Draw edges
    # --------------------------------

    for index in range(len(values)):

        left = 2 * index + 1
        right = 2 * index + 2

        x1, y1 = positions[index]

        if left < len(values):

            x2, y2 = positions[left]

            svg_elements.append(
                f"""
                <line
                    x1="{x1}"
                    y1="{y1}"
                    x2="{x2}"
                    y2="{y2}"
                    stroke="#888888"
                    stroke-width="3"
                />
                """
            )

        if right < len(values):

            x2, y2 = positions[right]

            svg_elements.append(
                f"""
                <line
                    x1="{x1}"
                    y1="{y1}"
                    x2="{x2}"
                    y2="{y2}"
                    stroke="#888888"
                    stroke-width="3"
                />
                """
            )

    # --------------------------------
    # Draw nodes
    # --------------------------------

    for index, value in enumerate(values):

        x, y = positions[index]

        svg_elements.append(
            f"""
            <circle
                cx="{x}"
                cy="{y}"
                r="30"
                fill="#4e79a7"
                stroke="white"
                stroke-width="3"
            />

            <text
                x="{x}"
                y="{y + 7}"
                text-anchor="middle"
                font-size="20"
                font-weight="bold"
                fill="white"
            >
                {value}
            </text>

            <text
                x="{x}"
                y="{y + 52}"
                text-anchor="middle"
                font-size="13"
                fill="#777777"
            >
                index {index}
            </text>
            """
        )

    # --------------------------------
    # SVG
    # --------------------------------

    svg = f"""
    <html>

    <head>

        <style>

            body {{
                margin: 0;
                padding: 0;
                background: transparent;
                overflow: hidden;
            }}

            svg {{
                display: block;
                margin: auto;
            }}

        </style>

    </head>

    <body>

        <svg
            width="800"
            height="{100 + (max_level + 1) * 100}"
            viewBox="0 0 800 {100 + (max_level + 1) * 100}"
            xmlns="http://www.w3.org/2000/svg"
        >

            {"".join(svg_elements)}

        </svg>

    </body>

    </html>
    """

    components.html(
        svg,
        height=100 + (max_level + 1) * 100,
        scrolling=False
    )


def show_heap_visualizer():

    st.header("Min Heap Visualizer")

    # --------------------------------
    # Initialize Heap
    # --------------------------------

    if "min_heap" not in st.session_state:

        st.session_state.min_heap = MinHeap()

    heap = st.session_state.min_heap

    # --------------------------------
    # Display Heap
    # --------------------------------

    st.subheader("Heap")

    display_heap(heap)

    st.divider()

    # --------------------------------
    # Heap Array
    # --------------------------------

    st.subheader("Array Representation")

    if heap.heap:

        st.code(
            str(heap.heap)
        )

    else:

        st.info("[]")

    st.divider()

    # --------------------------------
    # Insert
    # --------------------------------

    st.subheader("Insert")

    value = st.number_input(
        "Enter a value",
        value=10,
        step=1,
        key="heap_insert_value"
    )

    if st.button(
        "Insert",
        key="heap_insert_button"
    ):

        heap.insert(value)

        st.success(
            f"Inserted {value}"
        )

        st.rerun()

    # --------------------------------
    # Extract Minimum
    # --------------------------------

    st.subheader("Extract Minimum")

    if st.button(
        "Extract Min",
        key="heap_extract_button"
    ):

        if heap.is_empty():

            st.warning(
                "Heap is empty."
            )

        else:

            minimum = heap.extract_min()

            st.success(
                f"Extracted minimum: {minimum}"
            )

            st.rerun()

    # --------------------------------
    # Peek
    # --------------------------------

    if st.button(
        "Peek Minimum",
        key="heap_peek_button"
    ):

        minimum = heap.peek()

        if minimum is None:

            st.warning(
                "Heap is empty."
            )

        else:

            st.info(
                f"Minimum element: {minimum}"
            )

    # --------------------------------
    # Heap Information
    # --------------------------------

    st.divider()

    st.subheader("Heap Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Size",
            heap.size()
        )

    with col2:

        minimum = heap.peek()

        if minimum is None:
            minimum = "—"

        st.metric(
            "Minimum",
            minimum
        )

    st.divider()

    # --------------------------------
    # Clear
    # --------------------------------

    if st.button(
        "Clear Heap",
        key="heap_clear_button"
    ):

        st.session_state.min_heap = MinHeap()

        st.rerun()