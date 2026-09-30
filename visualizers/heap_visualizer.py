import streamlit as st
import streamlit.components.v1 as components

from algorithms.heap import MinHeap, MaxHeap


def display_heap(heap):

    values = heap.heap

    if not values:
        st.info("Heap is empty. Insert some values.")
        return

    positions = {}

    # --------------------------------
    # Calculate node positions
    # --------------------------------

    for index in range(len(values)):

        level = index.bit_length()

        position_in_level = (
            index - (2 ** level - 1)
        )

        nodes_in_level = 2 ** level

        x_spacing = 800 / (nodes_in_level + 1)

        x = x_spacing * (position_in_level + 1)

        y = 70 + level * 100

        positions[index] = (x, y)

    max_level = max(
        index.bit_length()
        for index in range(len(values))
    )

    # --------------------------------
    # SVG elements
    # --------------------------------

    svg_elements = []

    # --------------------------------
    # Draw edges
    # --------------------------------

    for index in range(len(values)):

        x1, y1 = positions[index]

        left = 2 * index + 1
        right = 2 * index + 2

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

    svg_height = 120 + (max_level * 100)

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
            height="{svg_height}"
            viewBox="0 0 800 {svg_height}"
            xmlns="http://www.w3.org/2000/svg"
        >

            {"".join(svg_elements)}

        </svg>

    </body>

    </html>
    """

    components.html(
        svg,
        height=svg_height + 20,
        scrolling=False
    )


def show_heap_visualizer():

    st.header("Heap Visualizer")

    # --------------------------------
    # Heap Type
    # --------------------------------

    heap_type = st.radio(
        "Choose Heap Type:",
        ["Min Heap", "Max Heap"],
        horizontal=True,
        key="heap_type_selector"
    )

    # --------------------------------
    # Initialize heap
    # --------------------------------

    if "active_heap" not in st.session_state:

        if heap_type == "Min Heap":
            st.session_state.active_heap = MinHeap()
        else:
            st.session_state.active_heap = MaxHeap()

        st.session_state.active_heap_type = heap_type

    # --------------------------------
    # Switch heap type
    # --------------------------------

    if (
        "active_heap_type" not in st.session_state
        or st.session_state.active_heap_type != heap_type
    ):

        if heap_type == "Min Heap":
            st.session_state.active_heap = MinHeap()
        else:
            st.session_state.active_heap = MaxHeap()

        st.session_state.active_heap_type = heap_type

    heap = st.session_state.active_heap

    # --------------------------------
    # Display Heap
    # --------------------------------

    st.subheader(
        f"{heap_type}"
    )

    display_heap(heap)

    st.divider()

    # --------------------------------
    # Array Representation
    # --------------------------------

    st.subheader("Array Representation")

    if heap.heap:

        st.code(
            str(heap.heap)
        )

    else:

        st.code("[]")

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
    # Extract
    # --------------------------------

    st.subheader("Extract")

    if st.button(
        "Extract Root",
        key="heap_extract_button"
    ):

        if heap.is_empty():

            st.warning(
                "Heap is empty."
            )

        else:

            if heap_type == "Min Heap":

                removed = heap.extract_min()

                st.success(
                    f"Extracted minimum: {removed}"
                )

            else:

                removed = heap.extract_max()

                st.success(
                    f"Extracted maximum: {removed}"
                )

            st.rerun()

    # --------------------------------
    # Peek
    # --------------------------------

    if st.button(
        "Peek Root",
        key="heap_peek_button"
    ):

        root = heap.peek()

        if root is None:

            st.warning(
                "Heap is empty."
            )

        else:

            if heap_type == "Min Heap":

                st.info(
                    f"Minimum element: {root}"
                )

            else:

                st.info(
                    f"Maximum element: {root}"
                )

    st.divider()

    # --------------------------------
    # Heap Information
    # --------------------------------

    st.subheader("Heap Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Size",
            heap.size()
        )

    with col2:

        root = heap.peek()

        if root is None:
            root = "—"

        if heap_type == "Min Heap":

            st.metric(
                "Minimum",
                root
            )

        else:

            st.metric(
                "Maximum",
                root
            )

    st.divider()

    # --------------------------------
    # Clear
    # --------------------------------

    if st.button(
        "Clear Heap",
        key="heap_clear_button"
    ):

        if heap_type == "Min Heap":

            st.session_state.active_heap = MinHeap()

        else:

            st.session_state.active_heap = MaxHeap()

        st.rerun()