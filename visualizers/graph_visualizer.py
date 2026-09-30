import streamlit as st
import streamlit.components.v1 as components

from algorithms.graph import Graph


def display_graph(
    graph,
    highlighted=None,
    shortest_path=None
):

    vertices = list(graph.adjacency_list.keys())

    if not vertices:
        st.info("Graph is empty. Add some vertices and edges.")
        return

    # --------------------------------
    # Node positions
    # --------------------------------

    positions = {
        "A": (400, 80),
        "B": (200, 200),
        "C": (600, 200),
        "D": (200, 350),
        "E": (600, 350),
        "F": (400, 470),
    }

    extra_vertices = [
        vertex
        for vertex in vertices
        if vertex not in positions
    ]

    for i, vertex in enumerate(extra_vertices):

        x = 100 + (i % 5) * 150
        y = 100 + (i // 5) * 120

        positions[vertex] = (x, y)

    svg_elements = []

    # --------------------------------
    # Shortest path edges
    # --------------------------------

    path_edges = set()

    if shortest_path:

        for i in range(len(shortest_path) - 1):

            edge = tuple(
                sorted(
                    [
                        shortest_path[i],
                        shortest_path[i + 1]
                    ]
                )
            )

            path_edges.add(edge)

    # --------------------------------
    # Draw edges
    # --------------------------------

    drawn_edges = set()

    for vertex in vertices:

        x1, y1 = positions[vertex]

        for neighbor, weight in (
            graph.adjacency_list[vertex].items()
        ):

            edge = tuple(
                sorted(
                    [vertex, neighbor]
                )
            )

            if edge in drawn_edges:
                continue

            drawn_edges.add(edge)

            x2, y2 = positions[neighbor]

            # Highlight shortest path edge
            if edge in path_edges:

                stroke = "#ff4b4b"
                stroke_width = 7

            else:

                stroke = "#888888"
                stroke_width = 4

            svg_elements.append(
                f"""
                <line
                    x1="{x1}"
                    y1="{y1}"
                    x2="{x2}"
                    y2="{y2}"
                    stroke="{stroke}"
                    stroke-width="{stroke_width}"
                />
                """
            )

            # --------------------------------
            # Weight background
            # --------------------------------

            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2

            svg_elements.append(
                f"""
                <circle
                    cx="{mid_x}"
                    cy="{mid_y}"
                    r="17"
                    fill="white"
                    stroke="#888888"
                    stroke-width="2"
                />
                """
            )

            # --------------------------------
            # Weight text
            # --------------------------------

            svg_elements.append(
                f"""
                <text
                    x="{mid_x}"
                    y="{mid_y + 6}"
                    text-anchor="middle"
                    font-size="16"
                    font-weight="bold"
                    fill="#222222"
                >
                    {weight}
                </text>
                """
            )

    # --------------------------------
    # Draw nodes
    # --------------------------------

    for vertex in vertices:

        x, y = positions[vertex]

        # Node is part of shortest path
        if shortest_path and vertex in shortest_path:

            fill = "#ff4b4b"

        # Current algorithm node
        elif vertex == highlighted:

            fill = "#ffa500"

        else:

            fill = "#4e79a7"

        svg_elements.append(
            f"""
            <circle
                cx="{x}"
                cy="{y}"
                r="32"
                fill="{fill}"
                stroke="white"
                stroke-width="4"
            />

            <text
                x="{x}"
                y="{y + 8}"
                text-anchor="middle"
                font-size="22"
                font-weight="bold"
                fill="white"
            >
                {vertex}
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
            height="540"
            viewBox="0 0 800 540"
            xmlns="http://www.w3.org/2000/svg"
        >

            {"".join(svg_elements)}

        </svg>

    </body>

    </html>
    """

    components.html(
        svg,
        height=560,
        scrolling=False
    )


def show_graph_visualizer():

    st.header("Graph Visualizer")

    # --------------------------------
    # Initialize graph
    # --------------------------------

    if "graph" not in st.session_state:

        graph = Graph()

        graph.add_edge("A", "B", 4)
        graph.add_edge("A", "C", 2)
        graph.add_edge("B", "D", 5)
        graph.add_edge("C", "D", 1)
        graph.add_edge("D", "E", 3)

        st.session_state.graph = graph

    graph = st.session_state.graph

    # --------------------------------
    # Traversal state
    # --------------------------------

    if "graph_steps" not in st.session_state:
        st.session_state.graph_steps = []

    if "graph_step_index" not in st.session_state:
        st.session_state.graph_step_index = -1

    if "graph_highlighted" not in st.session_state:
        st.session_state.graph_highlighted = None

    # --------------------------------
    # Dijkstra state
    # --------------------------------

    if "dijkstra_steps" not in st.session_state:
        st.session_state.dijkstra_steps = []

    if "dijkstra_step_index" not in st.session_state:
        st.session_state.dijkstra_step_index = -1

    if "dijkstra_highlighted" not in st.session_state:
        st.session_state.dijkstra_highlighted = None

    if "shortest_path" not in st.session_state:
        st.session_state.shortest_path = []

    if "shortest_cost" not in st.session_state:
        st.session_state.shortest_cost = None

    # --------------------------------
    # Display graph
    # --------------------------------

    st.subheader("Weighted Graph")

    display_graph(
        graph,
        highlighted=st.session_state.dijkstra_highlighted
        if st.session_state.dijkstra_steps
        else st.session_state.graph_highlighted,
        shortest_path=st.session_state.shortest_path
    )

    # --------------------------------
    # Graph information
    # --------------------------------

    vertices = len(graph.adjacency_list)

    edges = sum(
        len(neighbors)
        for neighbors in graph.adjacency_list.values()
    ) // 2

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Vertices", vertices)

    with col2:
        st.metric("Edges", edges)

    st.divider()

    # --------------------------------
    # Add Vertex
    # --------------------------------

    st.subheader("Add Vertex")

    vertex = st.text_input(
        "Enter vertex",
        max_chars=1,
        key="graph_vertex_input"
    )

    if st.button(
        "Add Vertex",
        key="add_vertex_button"
    ):

        vertex = vertex.upper()

        if vertex:

            if vertex not in graph.adjacency_list:

                graph.add_vertex(vertex)

                st.success(
                    f"Vertex {vertex} added."
                )

            else:

                st.warning(
                    f"Vertex {vertex} already exists."
                )

            st.rerun()

    # --------------------------------
    # Add Weighted Edge
    # --------------------------------

    st.subheader("Add Weighted Edge")

    col1, col2, col3 = st.columns(3)

    with col1:

        vertex1 = st.text_input(
            "Vertex 1",
            max_chars=1,
            key="graph_edge_vertex1"
        )

    with col2:

        vertex2 = st.text_input(
            "Vertex 2",
            max_chars=1,
            key="graph_edge_vertex2"
        )

    with col3:

        weight = st.number_input(
            "Weight",
            min_value=1,
            value=1,
            step=1,
            key="graph_edge_weight"
        )

    if st.button(
        "Add Weighted Edge",
        key="add_edge_button"
    ):

        vertex1 = vertex1.upper()
        vertex2 = vertex2.upper()

        if vertex1 and vertex2:

            graph.add_edge(
                vertex1,
                vertex2,
                weight
            )

            st.success(
                f"Edge added: {vertex1} ↔ {vertex2} "
                f"(weight = {weight})"
            )

            st.rerun()

    st.divider()

    # --------------------------------
    # BFS / DFS
    # --------------------------------

    st.subheader("Graph Traversal")

    start_vertex = st.text_input(
        "Starting Vertex",
        value="A",
        max_chars=1,
        key="graph_start_vertex"
    ).upper()

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "Start BFS",
            key="start_bfs_button"
        ):

            if start_vertex in graph.adjacency_list:

                st.session_state.graph_steps = (
                    graph.bfs_steps(start_vertex)
                )

                st.session_state.graph_step_index = -1
                st.session_state.graph_highlighted = None

                st.session_state.dijkstra_steps = []
                st.session_state.dijkstra_step_index = -1
                st.session_state.dijkstra_highlighted = None
                st.session_state.shortest_path = []
                st.session_state.shortest_cost = None

                st.rerun()

            else:

                st.error(
                    "Starting vertex does not exist."
                )

    with col2:

        if st.button(
            "Start DFS",
            key="start_dfs_button"
        ):

            if start_vertex in graph.adjacency_list:

                st.session_state.graph_steps = (
                    graph.dfs_steps(start_vertex)
                )

                st.session_state.graph_step_index = -1
                st.session_state.graph_highlighted = None

                st.session_state.dijkstra_steps = []
                st.session_state.dijkstra_step_index = -1
                st.session_state.dijkstra_highlighted = None
                st.session_state.shortest_path = []
                st.session_state.shortest_cost = None

                st.rerun()

            else:

                st.error(
                    "Starting vertex does not exist."
                )

    with col3:

        if st.button(
            "Next Step",
            key="graph_next_step_button"
        ):

            steps = st.session_state.graph_steps

            if steps:

                next_index = (
                    st.session_state.graph_step_index + 1
                )

                if next_index < len(steps):

                    st.session_state.graph_step_index = (
                        next_index
                    )

                    current_step = steps[next_index]

                    st.session_state.graph_highlighted = (
                        current_step["vertex"]
                    )

                    st.rerun()

    # --------------------------------
    # BFS / DFS information
    # --------------------------------

    if st.session_state.graph_steps:

        index = st.session_state.graph_step_index

        if (
            index >= 0
            and index < len(st.session_state.graph_steps)
        ):

            current_step = (
                st.session_state.graph_steps[index]
            )

            st.info(
                current_step["message"]
            )

            visited = [
                step["vertex"]
                for step in
                st.session_state.graph_steps[
                    :index + 1
                ]
            ]

            st.write(
                "**Visited:**",
                " → ".join(visited)
            )

    st.divider()

    # =================================
    # DIJKSTRA
    # =================================

    st.subheader("Dijkstra's Shortest Path")

    col1, col2 = st.columns(2)

    with col1:

        dijkstra_start = st.text_input(
            "Start Vertex",
            value="A",
            max_chars=1,
            key="dijkstra_start"
        ).upper()

    with col2:

        dijkstra_target = st.text_input(
            "Target Vertex",
            value="E",
            max_chars=1,
            key="dijkstra_target"
        ).upper()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Find Shortest Path",
            key="dijkstra_start_button"
        ):

            if (
                dijkstra_start in graph.adjacency_list
                and dijkstra_target in graph.adjacency_list
            ):

                path, cost = graph.shortest_path(
                    dijkstra_start,
                    dijkstra_target
                )

                st.session_state.shortest_path = path
                st.session_state.shortest_cost = cost

                st.session_state.dijkstra_steps = (
                    graph.dijkstra_steps(dijkstra_start)
                )

                st.session_state.dijkstra_step_index = -1
                st.session_state.dijkstra_highlighted = None

                st.session_state.graph_steps = []
                st.session_state.graph_step_index = -1
                st.session_state.graph_highlighted = None

                st.rerun()

            else:

                st.error(
                    "Both vertices must exist."
                )

    with col2:

        if st.button(
            "Next Dijkstra Step",
            key="dijkstra_next_button"
        ):

            steps = st.session_state.dijkstra_steps

            if steps:

                next_index = (
                    st.session_state.dijkstra_step_index + 1
                )

                if next_index < len(steps):

                    st.session_state.dijkstra_step_index = (
                        next_index
                    )

                    current_step = steps[next_index]

                    st.session_state.dijkstra_highlighted = (
                        current_step["vertex"]
                    )

                    st.rerun()

    # --------------------------------
    # Dijkstra information
    # --------------------------------

    if st.session_state.dijkstra_steps:

        index = st.session_state.dijkstra_step_index

        if (
            index >= 0
            and index < len(
                st.session_state.dijkstra_steps
            )
        ):

            current_step = (
                st.session_state.dijkstra_steps[index]
            )

            st.info(
                current_step["message"]
            )

            distances = current_step["distances"]

            st.write("### Current Distances")

            distance_display = {}

            for vertex, distance in distances.items():

                if distance == float("inf"):
                    distance_display[vertex] = "∞"
                else:
                    distance_display[vertex] = distance

            st.write(distance_display)

    # --------------------------------
    # Final shortest path
    # --------------------------------

    if st.session_state.shortest_path:

        st.success(
            "Shortest Path: "
            + " → ".join(
                st.session_state.shortest_path
            )
        )

        st.success(
            f"Total Cost: "
            f"{st.session_state.shortest_cost}"
        )

    st.divider()

    # --------------------------------
    # Reset
    # --------------------------------

    if st.button(
        "Reset Graph Algorithms",
        key="reset_graph_button"
    ):

        st.session_state.graph_steps = []
        st.session_state.graph_step_index = -1
        st.session_state.graph_highlighted = None

        st.session_state.dijkstra_steps = []
        st.session_state.dijkstra_step_index = -1
        st.session_state.dijkstra_highlighted = None

        st.session_state.shortest_path = []
        st.session_state.shortest_cost = None

        st.rerun()

    # --------------------------------
    # Clear Graph
    # --------------------------------

    if st.button(
        "Clear Graph",
        key="clear_graph_button"
    ):

        st.session_state.graph = Graph()

        st.session_state.graph_steps = []
        st.session_state.graph_step_index = -1
        st.session_state.graph_highlighted = None

        st.session_state.dijkstra_steps = []
        st.session_state.dijkstra_step_index = -1
        st.session_state.dijkstra_highlighted = None

        st.session_state.shortest_path = []
        st.session_state.shortest_cost = None

        st.rerun()

    st.divider()

    # --------------------------------
    # Algorithm Information
    # --------------------------------

    st.subheader("Algorithm Information")

    algorithm = st.selectbox(
        "Choose an algorithm to learn about:",
        [
            "BFS",
            "DFS",
            "Dijkstra's Algorithm"
        ],
        key="graph_algorithm_info"
    )

    if algorithm == "BFS":

        st.markdown(
            """
            ### Breadth-First Search (BFS)

            BFS explores a graph **level by level**.

            It uses a **queue** to keep track of vertices
            that need to be visited.

            **Basic idea:**

            1. Start from a vertex.
            2. Mark it as visited.
            3. Add its neighbors to the queue.
            4. Remove the first vertex from the queue.
            5. Visit its unvisited neighbors.
            6. Continue until the queue is empty.

            **Time Complexity:** `O(V + E)`

            **Space Complexity:** `O(V)`

            **Common Applications:**

            - Shortest path in an unweighted graph
            - Level-order exploration
            - Network traversal
            - Finding connected components
            """
        )

    elif algorithm == "DFS":

        st.markdown(
            """
            ### Depth-First Search (DFS)

            DFS explores a graph by going **as deep as possible**
            before backtracking.

            It can be implemented using:

            - Recursion
            - Stack

            **Basic idea:**

            1. Start from a vertex.
            2. Mark it as visited.
            3. Visit an unvisited neighbor.
            4. Continue going deeper.
            5. Backtrack when no unvisited neighbor remains.

            **Time Complexity:** `O(V + E)`

            **Space Complexity:** `O(V)`

            **Common Applications:**

            - Cycle detection
            - Connected components
            - Path finding
            - Topological sorting
            - Maze solving
            """
        )

    else:

        st.markdown(
            """
            ### Dijkstra's Algorithm

            Dijkstra's algorithm finds the **shortest path**
            from a starting vertex to other vertices in a
            weighted graph.

            It works with **non-negative edge weights**.

            **Basic idea:**

            1. Set the starting vertex distance to `0`.
            2. Set all other distances to infinity.
            3. Select the unvisited vertex with the smallest
               distance.
            4. Update the distances of its neighbors.
            5. Mark the current vertex as visited.
            6. Repeat until all reachable vertices are processed.

            **Time Complexity:**

            `O(V²)` with the implementation used in this project.

            **Space Complexity:** `O(V)`

            **Important:**

            Dijkstra's algorithm should not be used with
            negative edge weights.

            **Common Applications:**

            - GPS navigation
            - Network routing
            - Shortest path problems
            - Transportation systems
            - Network optimization
            """
        )