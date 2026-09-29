import streamlit as st
from algorithms.tree import BinarySearchTree


# =========================================================
# BUILD TREE HTML
# =========================================================

def build_tree_html(node, highlighted=None):

    if node is None:
        return ""

    if node.data == highlighted:
        background = "#ffcccc"
        border = "4px solid red"
    else:
        background = "#f5f5f5"
        border = "2px solid #333"

    left_html = build_tree_html(
        node.left,
        highlighted
    )

    right_html = build_tree_html(
        node.right,
        highlighted
    )

    if node.left is not None or node.right is not None:

        left_box = (
            '<div style="'
            'flex:1;'
            'text-align:center;'
            '">'
            f'{left_html}'
            '</div>'
        )

        right_box = (
            '<div style="'
            'flex:1;'
            'text-align:center;'
            '">'
            f'{right_html}'
            '</div>'
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

    else:
        children_html = ""

    return (
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
        '<div style="'
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
# MAIN VISUALIZER
# =========================================================

def show_tree_visualizer():

    st.header("Binary Search Tree Visualizer")

    # =====================================================
    # INITIALIZE TREE
    # =====================================================

    if "binary_tree" not in st.session_state:

        tree = BinarySearchTree()

        for value in [
            50,
            30,
            70,
            20,
            40,
            60,
            80
        ]:
            tree.insert(value)

        st.session_state.binary_tree = tree

    tree = st.session_state.binary_tree

    # =====================================================
    # SEARCH STATE
    # =====================================================

    if "tree_search_steps" not in st.session_state:
        st.session_state.tree_search_steps = []

    if "tree_search_index" not in st.session_state:
        st.session_state.tree_search_index = 0

    # =====================================================
    # DISPLAY TREE
    # =====================================================

    st.write("### Tree")

    highlighted = None

    if st.session_state.tree_search_steps:

        current_step = (
            st.session_state.tree_search_steps[
                st.session_state.tree_search_index
            ]
        )

        highlighted = current_step["value"]

    display_tree(
        tree,
        highlighted
    )

    st.divider()

    # =====================================================
    # INPUT
    # =====================================================

    value = st.number_input(
        "Enter value:",
        value=60,
        step=1,
        key="tree_value"
    )

    # =====================================================
    # INSERT / DELETE
    # =====================================================

    st.write("### Tree Operations")

    col1, col2 = st.columns(2)

    # INSERT
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

                st.session_state.tree_search_steps = []

                st.session_state.tree_search_index = 0

                st.success(
                    f"{value} inserted."
                )

            st.rerun()

    # DELETE
    with col2:

        if st.button(
            "Delete",
            key="tree_delete"
        ):

            if not tree.search(value):

                st.warning(
                    f"{value} does not exist in the tree."
                )

            else:

                tree.delete(value)

                st.session_state.tree_search_steps = []

                st.session_state.tree_search_index = 0

                st.success(
                    f"{value} deleted."
                )

            st.rerun()

    st.divider()

    # =====================================================
    # SEARCH
    # =====================================================

    st.write("### Search")

    col1, col2, col3 = st.columns(3)

    # START SEARCH
    with col1:

        if st.button(
            "Start Search",
            key="start_tree_search"
        ):

            st.session_state.tree_search_steps = (
                tree.search_steps(
                    int(value)
                )
            )

            st.session_state.tree_search_index = 0

            st.rerun()

    # NEXT STEP
    with col2:

        steps = st.session_state.tree_search_steps

        index = st.session_state.tree_search_index

        search_finished = (
            len(steps) == 0
            or
            index >= len(steps) - 1
        )

        if st.button(
            "Next Step",
            key="next_tree_search",
            disabled=search_finished
        ):

            st.session_state.tree_search_index += 1

            st.rerun()

    # RESET SEARCH
    with col3:

        if st.button(
            "Reset Search",
            key="reset_tree_search"
        ):

            st.session_state.tree_search_steps = []

            st.session_state.tree_search_index = 0

            st.rerun()

    # =====================================================
    # SEARCH MESSAGE
    # =====================================================

    if st.session_state.tree_search_steps:

        current_step = (
            st.session_state.tree_search_steps[
                st.session_state.tree_search_index
            ]
        )

        st.info(
            current_step["message"]
        )

    st.divider()

    # =====================================================
    # TRAVERSALS
    # =====================================================

    st.write("### Traversals")

    col1, col2, col3 = st.columns(3)

    # INORDER
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

    # PREORDER
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

    # POSTORDER
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

        st.session_state.tree_search_steps = []

        st.session_state.tree_search_index = 0

        st.rerun()