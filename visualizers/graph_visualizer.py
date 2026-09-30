import streamlit as st
from algorithms.graph import Graph


# =========================================================
# DISPLAY GRAPH
# =========================================================

def display_graph(graph, highlighted=None):

    if not graph.adjacency_list:
        st.info("Graph is empty.")
        return

    st.write("### Graph")

    # Display each vertex and its connections
    for vertex, neighbors in graph.adjacency_list.items():

        if vertex == highlighted:
            background = "#ffcccc"
            border = "4px solid red"
        else:
            background = "#f5f5f5"
            border = "2px solid #333"

        vertex_html = (
            '<div style="'
            'display:inline-flex;'
            'align-items:center;'
            'justify-content:center;'
            f'border:{border};'
            f'background:{background};'
            'color:black;'
            'border-radius:50%;'
            'width:50px;'
            'height:50px;'
            'font-weight:bold;'
            'margin:5px;'
            '">'
            f'{vertex}'
            '</div>'
        )

        connections = ""

        for neighbor in neighbors:

            connections += (
                '<span style="'
                'margin:5px;'
                'font-size:18px;'
                '">'
                f'→ {neighbor}'
                '</span>'
            )

        st.markdown(
            f'{vertex_html}{connections}',
            unsafe_allow_html=True
        )


# =========================================================
# MAIN GRAPH VISUALIZER
# =========================================================

def show_graph_visualizer():

    st.header("Graph Visualizer")

    # =====================================================
    # INITIALIZE GRAPH
    # =====================================================

    if "graph" not in st.session_state:

        graph = Graph()

        # Initial vertices
        for vertex in ["A", "B", "C", "D", "E"]:
            graph.add_vertex(vertex)

        # Initial edges
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "D")
        graph.add_edge("C", "E")
        graph.add_edge("D", "E")

        st.session_state.graph = graph

    graph = st.session_state.graph

    # =====================================================
    # TRAVERSAL STATE
    # =====================================================

    if "graph_steps" not in st.session_state:
        st.session_state.graph_steps = []

    if "graph_step_index" not in st.session_state:
        st.session_state.graph_step_index = 0

    # =====================================================
    # CURRENT HIGHLIGHT
    # =====================================================

    highlighted = None

    if st.session_state.graph_steps:

        current_step = (
            st.session_state.graph_steps[
                st.session_state.graph_step_index
            ]
        )

        highlighted = current_step["vertex"]

    # =====================================================
    # DISPLAY GRAPH
    # =====================================================

    display_graph(
        graph,
        highlighted
    )

    st.divider()

    # =====================================================
    # VERTEX INPUT
    # =====================================================

    st.write("### Add Vertex")

    vertex = st.text_input(
        "Enter vertex:",
        value="F",
        max_chars=1,
        key="graph_vertex"
    )

    if st.button(
        "Add Vertex",
        key="add_vertex"
    ):

        vertex = vertex.upper()

        if vertex in graph.adjacency_list:

            st.warning(
                f"Vertex {vertex} already exists."
            )

        else:

            graph.add_vertex(vertex)

            st.success(
                f"Vertex {vertex} added."
            )

        st.rerun()

    st.divider()

    # =====================================================
    # EDGE INPUT
    # =====================================================

    st.write("### Add Edge")

    col1, col2 = st.columns(2)

    with col1:

        vertex1 = st.text_input(
            "First vertex:",
            value="A",
            max_chars=1,
            key="edge_vertex1"
        )

    with col2:

        vertex2 = st.text_input(
            "Second vertex:",
            value="B",
            max_chars=1,
            key="edge_vertex2"
        )

    if st.button(
        "Add Edge",
        key="add_edge"
    ):

        vertex1 = vertex1.upper()
        vertex2 = vertex2.upper()

        graph.add_edge(
            vertex1,
            vertex2
        )

        st.success(
            f"Edge added: {vertex1} ↔ {vertex2}"
        )

        st.rerun()

    st.divider()

    # =====================================================
    # TRAVERSAL INPUT
    # =====================================================

    st.write("### Graph Traversal")

    start_vertex = st.text_input(
        "Starting vertex:",
        value="A",
        max_chars=1,
        key="graph_start"
    )

    start_vertex = start_vertex.upper()

    col1, col2, col3 = st.columns(3)

    # -----------------------------------------------------
    # BFS
    # -----------------------------------------------------

    with col1:

        if st.button(
            "Start BFS",
            key="start_bfs"
        ):

            if start_vertex not in graph.adjacency_list:

                st.error(
                    "Starting vertex does not exist."
                )

            else:

                st.session_state.graph_steps = (
                    graph.bfs_steps(
                        start_vertex
                    )
                )

                st.session_state.graph_step_index = 0

                st.session_state.graph_algorithm = "BFS"

                st.rerun()

    # -----------------------------------------------------
    # DFS
    # -----------------------------------------------------

    with col2:

        if st.button(
            "Start DFS",
            key="start_dfs"
        ):

            if start_vertex not in graph.adjacency_list:

                st.error(
                    "Starting vertex does not exist."
                )

            else:

                st.session_state.graph_steps = (
                    graph.dfs_steps(
                        start_vertex
                    )
                )

                st.session_state.graph_step_index = 0

                st.session_state.graph_algorithm = "DFS"

                st.rerun()

    # -----------------------------------------------------
    # NEXT STEP
    # -----------------------------------------------------

    with col3:

        steps = st.session_state.graph_steps

        index = st.session_state.graph_step_index

        finished = (
            len(steps) == 0
            or index >= len(steps) - 1
        )

        if st.button(
            "Next Step",
            key="next_graph_step",
            disabled=finished
        ):

            st.session_state.graph_step_index += 1

            st.rerun()

    # =====================================================
    # TRAVERSAL RESULT
    # =====================================================

    if st.session_state.graph_steps:

        current_step = (
            st.session_state.graph_steps[
                st.session_state.graph_step_index
            ]
        )

        st.info(
            current_step["message"]
        )

        # Show visited vertices
        visited = []

        for step in st.session_state.graph_steps[
            :st.session_state.graph_step_index + 1
        ]:

            visited.append(
                step["vertex"]
            )

        st.write(
            "**Visited:**",
            " → ".join(visited)
        )

    st.divider()

    # =====================================================
    # RESET TRAVERSAL
    # =====================================================

    if st.button(
        "Reset Traversal",
        key="reset_graph"
    ):

        st.session_state.graph_steps = []

        st.session_state.graph_step_index = 0

        st.rerun()

    st.divider()

    # =====================================================
    # CLEAR GRAPH
    # =====================================================

    if st.button(
        "Clear Graph",
        key="clear_graph"
    ):

        st.session_state.graph = Graph()

        st.session_state.graph_steps = []

        st.session_state.graph_step_index = 0

        st.rerun()

    # =====================================================
    # GRAPH INFORMATION
    # =====================================================

    st.divider()

    st.write("### Graph Information")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Vertices",
            len(graph.adjacency_list)
        )

    with col2:

        edge_count = 0

        for neighbors in graph.adjacency_list.values():
            edge_count += len(neighbors)

        # Undirected graph stores each edge twice
        edge_count = edge_count // 2

        st.metric(
            "Edges",
            edge_count
        )