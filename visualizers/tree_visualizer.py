import streamlit as st
from algorithms.tree import BinarySearchTree


# =========================================================
# CREATE TREE HTML
# =========================================================

def build_tree_html(node, highlighted=None):

    if node is None:
        return ""

    # Highlight selected node
    if node.data == highlighted:
        background = "#ffcccc"
        border = "4px solid red"
    else:
        background = "#f5f5f5"
        border = "2px solid #333"

    # Build left subtree
    left_html = build_tree_html(
        node.left,
        highlighted
    )

    # Build right subtree
    right_html = build_tree_html(
        node.right,
        highlighted
    )

    # Children section
    children_html = ""

    if node.left is not None or node.right is not None:

        left_box = (
            f'<div style="flex:1;text-align:center;">'
            f'{left_html}'
            f'</div>'
        )

        right_box = (
            f'<div style="flex:1;text-align:center;">'
            f'{right_html}'
            f'</div>'
        )

        children_html = (
            '<div style="'
            'display:flex;'
            'justify-content:center;'
            'width:100%;'
            'margin-top:20px;'
            '">'
            f'{left_box}'
            f'{right_box}'
            '</div>'
        )

    # Current node
    node_html = (
        '<div style="'
        'display:flex;'
        'flex-direction:column;'
        'align-items:center;'
        'min-width:120px;'
        '">'
        '<div style="'
        f'border:{border};'
        f'background:{background};'
        'color:black;'
        'border-radius:50%;'
        'width:55px;'
        'height:55px;'
        'display:flex;'
        'align-items:center;'
        'justify-content:center;'
        'font-weight:bold;'
        'font-size:18px;'
        '">'
        f'{node.data}'
        '</div>'
        f'{children_html}'
        '</div>'
    )

    return node_html


# =========================================================
# DISPLAY TREE
# =========================================================

def display_tree(tree, highlighted=None):

    if tree.root is None:

        st.info("Tree is empty.")
        return

    tree_html = build_tree_html(
        tree.root,
        highlighted
    )

    st.markdown(
        f'<div style="'
        'width:100%;'
        'overflow-x:auto;'
        'padding:30px;'
        'text-align:center;'
        '">'
        f'{tree_html}'
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# MAIN TREE VISUALIZER
# =========================================================

def show_tree_visualizer():

    st.header("Binary Search Tree Visualizer")

    # =====================================================
    # INITIALIZE TREE
    # =====================================================

    if "binary_tree" not in st.session_state:

        tree = BinarySearchTree()

        initial_values = [
            50,
            30,
            70,
            20,
            40,
            60,
            80
        ]

        for value in initial_values:
            tree.insert(value)

        st.session_state.binary_tree = tree

    tree = st.session_state.binary_tree

    # =====================================================
    # DISPLAY TREE
    # =====================================================

    st.write("### Tree")

    display_tree(tree)

    st.divider()

    # =====================================================
    # INPUT
    # =====================================================

    value = st.number_input(
        "Enter value:",
        value=50,
        step=1,
        key="tree_value"
    )

    # =====================================================
    # INSERT AND SEARCH
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Insert",
            key="tree_insert"
        ):

            if tree.search(value):

                st.warning(
                    f"{value} already exists."
                )

            else:

                tree.insert(value)

                st.success(
                    f"{value} inserted."
                )

            st.rerun()

    with col2:

        if st.button(
            "Search",
            key="tree_search"
        ):

            if tree.search(value):

                st.success(
                    f"{value} found in the tree."
                )

            else:

                st.error(
                    f"{value} not found."
                )

    st.divider()

    # =====================================================
    # TRAVERSALS
    # =====================================================

    st.write("### Traversals")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "Inorder",
            key="tree_inorder"
        ):

            result = tree.inorder()

            st.success(
                " → ".join(
                    map(str, result)
                )
            )

    with col2:

        if st.button(
            "Preorder",
            key="tree_preorder"
        ):

            result = tree.preorder()

            st.success(
                " → ".join(
                    map(str, result)
                )
            )

    with col3:

        if st.button(
            "Postorder",
            key="tree_postorder"
        ):

            result = tree.postorder()

            st.success(
                " → ".join(
                    map(str, result)
                )
            )

    st.divider()

    # =====================================================
    # TREE INFORMATION
    # =====================================================

    st.write("### Tree Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Number of Nodes",
            tree.count_nodes()
        )

    with col2:

        st.metric(
            "Height",
            tree.height()
        )

    st.divider()

    # =====================================================
    # CLEAR TREE
    # =====================================================

    if st.button(
        "Clear Tree",
        key="clear_tree"
    ):

        st.session_state.binary_tree = BinarySearchTree()

        st.rerun()