import streamlit as st
from algorithms.linked_list import LinkedList


def display_linked_list(linked_list):
    values = linked_list.display()

    if not values:
        st.info("Linked List is empty.")
        return

    st.write("### Linked List")

    st.markdown("**HEAD ↓**")

    node_text = ""

    for value in values:
        node_text += (
            '<div style="'
            'display:inline-block;'
            'border:2px solid #333;'
            'border-radius:8px;'
            'padding:12px 20px;'
            'margin:5px;'
            'text-align:center;'
            'background-color:#f5f5f5;'
            'color:black;'
            '">'
            f'<strong>{value}</strong>'
            '</div>'
            '<span style="font-size:25px; margin:5px;">→</span>'
        )

    node_text += (
        '<span style="font-weight:bold; font-size:18px; margin-left:5px;">'
        'NULL'
        '</span>'
    )

    st.markdown(node_text, unsafe_allow_html=True)

def show_linked_list_visualizer():

    st.header("Linked List Visualizer")

    # Initialize linked list
    if "linked_list" not in st.session_state:
        linked_list = LinkedList()

        linked_list.insert_at_end(10)
        linked_list.insert_at_end(20)
        linked_list.insert_at_end(30)

        st.session_state.linked_list = linked_list

    linked_list = st.session_state.linked_list

    # Display current list
    display_linked_list(linked_list)

    st.divider()

    # Input
    value = st.number_input(
        "Enter value:",
        value=40,
        step=1,
        key="linked_list_value"
    )

    # Operations
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Insert at Beginning", key="insert_beginning"):
            linked_list.insert_at_beginning(value)
            st.rerun()

    with col2:
        if st.button("Insert at End", key="insert_end"):
            linked_list.insert_at_end(value)
            st.rerun()

    with col3:
        if st.button("Delete from Beginning", key="delete_beginning"):

            deleted = linked_list.delete_from_beginning()

            if deleted is None:
                st.warning("Linked List is empty.")
            else:
                st.success(f"Deleted: {deleted}")

            st.rerun()

    col4, col5, col6 = st.columns(3)

    with col4:
        if st.button("Delete from End", key="delete_end"):

            deleted = linked_list.delete_from_end()

            if deleted is None:
                st.warning("Linked List is empty.")
            else:
                st.success(f"Deleted: {deleted}")

            st.rerun()

    with col5:
        if st.button("Search", key="search_linked_list"):

            found = linked_list.search(value)

            if found:
                st.success(f"{value} found in the Linked List.")
            else:
                st.error(f"{value} not found.")

    with col6:
        if st.button("Clear List", key="clear_linked_list"):

            st.session_state.linked_list = LinkedList()
            st.rerun()

    st.divider()

    # Information
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Size", linked_list.size())

    with col2:
        if linked_list.head is not None:
            st.metric("Head", linked_list.head.data)
        else:
            st.metric("Head", "NULL")

    with col3:
        if linked_list.head is not None:
            current = linked_list.head

            while current.next is not None:
                current = current.next

            st.metric("Tail", current.data)
        else:
            st.metric("Tail", "NULL")