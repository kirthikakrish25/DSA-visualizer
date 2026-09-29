import streamlit as st
from algorithms.linked_list import LinkedList


# =========================================================
# DISPLAY LINKED LIST
# =========================================================

def display_linked_list(linked_list, highlighted_index=-1):
    values = linked_list.display()

    if not values:
        st.info("Linked List is empty.")
        return

    st.write("### Linked List")

    st.markdown("**HEAD ↓**")

    node_text = ""

    for index, value in enumerate(values):

        # Highlight current node during traversal
        if index == highlighted_index:
            border = "4px solid red"
            background = "#ffe6e6"
        else:
            border = "2px solid #333"
            background = "#f5f5f5"

        node_text += (
            f'<div style="'
            f'display:inline-block;'
            f'border:{border};'
            f'border-radius:8px;'
            f'padding:12px 20px;'
            f'margin:5px;'
            f'text-align:center;'
            f'background-color:{background};'
            f'color:black;'
            f'min-width:50px;'
            f'">'
            f'<strong>{value}</strong>'
            f'</div>'
            '<span style="'
            'font-size:25px;'
            'margin:5px;'
            '">'
            '→'
            '</span>'
        )

    node_text += (
        '<span style="'
        'font-weight:bold;'
        'font-size:18px;'
        'margin-left:5px;'
        '">'
        'NULL'
        '</span>'
    )

    st.markdown(
        node_text,
        unsafe_allow_html=True
    )


# =========================================================
# DISPLAY TRAVERSAL
# =========================================================

def display_traversal(linked_list, current_index):
    values = linked_list.display()

    if not values:
        st.info("Linked List is empty.")
        return

    st.write("### Traversal")

    st.markdown("**HEAD ↓**")

    node_text = ""

    for index, value in enumerate(values):

        if index == current_index:
            border = "4px solid red"
            background = "#ffe6e6"
        else:
            border = "2px solid #333"
            background = "#f5f5f5"

        node_text += (
            f'<div style="'
            f'display:inline-block;'
            f'border:{border};'
            f'border-radius:8px;'
            f'padding:12px 20px;'
            f'margin:5px;'
            f'text-align:center;'
            f'background-color:{background};'
            f'color:black;'
            f'min-width:50px;'
            f'">'
            f'<strong>{value}</strong>'
            f'</div>'
            '<span style="'
            'font-size:25px;'
            'margin:5px;'
            '">'
            '→'
            '</span>'
        )

    node_text += (
        '<span style="'
        'font-weight:bold;'
        'font-size:18px;'
        '">'
        'NULL'
        '</span>'
    )

    st.markdown(
        node_text,
        unsafe_allow_html=True
    )


# =========================================================
# MAIN VISUALIZER
# =========================================================

def show_linked_list_visualizer():

    st.header("Linked List Visualizer")

    # =====================================================
    # INITIALIZE LINKED LIST
    # =====================================================

    if "linked_list" not in st.session_state:

        linked_list = LinkedList()

        linked_list.insert_at_end(10)
        linked_list.insert_at_end(20)
        linked_list.insert_at_end(30)

        st.session_state.linked_list = linked_list

    linked_list = st.session_state.linked_list

    # =====================================================
    # INITIALIZE TRAVERSAL STATE
    # =====================================================

    if "traversal_steps" not in st.session_state:
        st.session_state.traversal_steps = []

    if "traversal_index" not in st.session_state:
        st.session_state.traversal_index = 0

    # =====================================================
    # DISPLAY CURRENT LINKED LIST
    # =====================================================

    display_linked_list(linked_list)

    st.divider()

    # =====================================================
    # INPUTS
    # =====================================================

    st.write("### Input")

    col1, col2 = st.columns(2)

    with col1:

        value = st.number_input(
            "Enter value:",
            value=40,
            step=1,
            key="linked_list_value"
        )

    with col2:

        position = st.number_input(
            "Enter position:",
            min_value=0,
            value=0,
            step=1,
            key="linked_list_position"
        )

    # =====================================================
    # INSERTION OPERATIONS
    # =====================================================

    st.write("### Insertion Operations")

    col1, col2, col3 = st.columns(3)

    # Insert at Beginning
    with col1:

        if st.button(
            "Insert at Beginning",
            key="insert_beginning"
        ):

            linked_list.insert_at_beginning(value)

            # Reset traversal
            st.session_state.traversal_steps = []
            st.session_state.traversal_index = 0

            st.rerun()

    # Insert at End
    with col2:

        if st.button(
            "Insert at End",
            key="insert_end"
        ):

            linked_list.insert_at_end(value)

            # Reset traversal
            st.session_state.traversal_steps = []
            st.session_state.traversal_index = 0

            st.rerun()

    # Insert at Position
    with col3:

        if st.button(
            "Insert at Position",
            key="insert_position"
        ):

            success = linked_list.insert_at_position(
                value,
                int(position)
            )

            if success:

                st.session_state.traversal_steps = []
                st.session_state.traversal_index = 0

                st.success(
                    f"{value} inserted at position "
                    f"{int(position)}."
                )

                st.rerun()

            else:

                st.error(
                    "Invalid position."
                )

    st.divider()

    # =====================================================
    # DELETION OPERATIONS
    # =====================================================

    st.write("### Deletion Operations")

    col1, col2, col3 = st.columns(3)

    # Delete from Beginning
    with col1:

        if st.button(
            "Delete from Beginning",
            key="delete_beginning"
        ):

            deleted = linked_list.delete_from_beginning()

            if deleted is None:

                st.warning(
                    "Linked List is empty."
                )

            else:

                st.session_state.traversal_steps = []
                st.session_state.traversal_index = 0

                st.success(
                    f"Deleted: {deleted}"
                )

            st.rerun()

    # Delete from End
    with col2:

        if st.button(
            "Delete from End",
            key="delete_end"
        ):

            deleted = linked_list.delete_from_end()

            if deleted is None:

                st.warning(
                    "Linked List is empty."
                )

            else:

                st.session_state.traversal_steps = []
                st.session_state.traversal_index = 0

                st.success(
                    f"Deleted: {deleted}"
                )

            st.rerun()

    # Delete at Position
    with col3:

        if st.button(
            "Delete at Position",
            key="delete_position"
        ):

            deleted = linked_list.delete_at_position(
                int(position)
            )

            if deleted is None:

                st.warning(
                    "Invalid position or empty list."
                )

            else:

                st.session_state.traversal_steps = []
                st.session_state.traversal_index = 0

                st.success(
                    f"Deleted {deleted} from position "
                    f"{int(position)}."
                )

            st.rerun()

    st.divider()

    # =====================================================
    # SEARCH AND CLEAR
    # =====================================================

    st.write("### Other Operations")

    col1, col2 = st.columns(2)

    # Search
    with col1:

        if st.button(
            "Search",
            key="search_linked_list"
        ):

            found = linked_list.search(value)

            if found:

                st.success(
                    f"{value} found in the Linked List."
                )

            else:

                st.error(
                    f"{value} not found in the Linked List."
                )

    # Clear
    with col2:

        if st.button(
            "Clear List",
            key="clear_linked_list"
        ):

            st.session_state.linked_list = LinkedList()

            st.session_state.traversal_steps = []

            st.session_state.traversal_index = 0

            st.rerun()

    st.divider()

    # =====================================================
    # TRAVERSAL
    # =====================================================

    st.write("### Traversal")

    col1, col2, col3 = st.columns(3)

    # Start Traversal
    with col1:

        if st.button(
            "Start Traversal",
            key="start_traversal"
        ):

            if linked_list.head is None:

                st.warning(
                    "Linked List is empty."
                )

            else:

                st.session_state.traversal_steps = (
                    linked_list.traversal_steps()
                )

                st.session_state.traversal_index = 0

                st.rerun()

    # Next Node
    with col2:

        traversal_steps = (
            st.session_state.traversal_steps
        )

        traversal_index = (
            st.session_state.traversal_index
        )

        traversal_finished = (
            len(traversal_steps) == 0
            or
            traversal_index >= len(traversal_steps) - 1
        )

        if st.button(
            "Next Node",
            key="next_node",
            disabled=traversal_finished
        ):

            st.session_state.traversal_index += 1

            st.rerun()

    # Reset Traversal
    with col3:

        if st.button(
            "Reset Traversal",
            key="reset_traversal"
        ):

            st.session_state.traversal_steps = []

            st.session_state.traversal_index = 0

            st.rerun()

    # =====================================================
    # SHOW CURRENT TRAVERSAL STEP
    # =====================================================

    if st.session_state.traversal_steps:

        current_step = (
            st.session_state.traversal_steps[
                st.session_state.traversal_index
            ]
        )

        current_index = current_step["index"]

        display_traversal(
            linked_list,
            current_index
        )

        st.info(
            current_step["message"]
        )

    # =====================================================
    # LINKED LIST INFORMATION
    # =====================================================

    st.divider()

    st.write("### Linked List Information")

    col1, col2, col3 = st.columns(3)

    # Size
    with col1:

        st.metric(
            "Size",
            linked_list.size()
        )

    # Head
    with col2:

        if linked_list.head is not None:

            st.metric(
                "Head",
                linked_list.head.data
            )

        else:

            st.metric(
                "Head",
                "NULL"
            )

    # Tail
    with col3:

        if linked_list.head is not None:

            current = linked_list.head

            while current.next is not None:
                current = current.next

            st.metric(
                "Tail",
                current.data
            )

        else:

            st.metric(
                "Tail",
                "NULL"
            )