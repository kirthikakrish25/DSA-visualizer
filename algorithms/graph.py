class Graph:

    def __init__(self):
        self.adjacency_list = {}

    # ==========================================
    # ADD VERTEX
    # ==========================================

    def add_vertex(self, vertex):

        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # ==========================================
    # ADD EDGE
    # ==========================================

    def add_edge(self, vertex1, vertex2):

        # Make sure both vertices exist
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Undirected graph
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)

        if vertex1 not in self.adjacency_list[vertex2]:
            self.adjacency_list[vertex2].append(vertex1)

    # ==========================================
    # REMOVE VERTEX
    # ==========================================

    def remove_vertex(self, vertex):

        if vertex not in self.adjacency_list:
            return False

        # Remove vertex from neighbors
        for neighbor in self.adjacency_list[vertex]:

            if vertex in self.adjacency_list[neighbor]:
                self.adjacency_list[neighbor].remove(vertex)

        # Remove vertex
        del self.adjacency_list[vertex]

        return True

    # ==========================================
    # REMOVE EDGE
    # ==========================================

    def remove_edge(self, vertex1, vertex2):

        if vertex1 in self.adjacency_list:

            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)

        if vertex2 in self.adjacency_list:

            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    # ==========================================
    # BFS
    # ==========================================

    def bfs(self, start):

        if start not in self.adjacency_list:
            return []

        visited = set()

        queue = [start]

        result = []

        visited.add(start)

        while queue:

            current = queue.pop(0)

            result.append(current)

            for neighbor in self.adjacency_list[current]:

                if neighbor not in visited:

                    visited.add(neighbor)

                    queue.append(neighbor)

        return result

    # ==========================================
    # DFS
    # ==========================================

    def dfs(self, start):

        if start not in self.adjacency_list:
            return []

        visited = set()

        result = []

        def traverse(vertex):

            visited.add(vertex)

            result.append(vertex)

            for neighbor in self.adjacency_list[vertex]:

                if neighbor not in visited:
                    traverse(neighbor)

        traverse(start)

        return result

    # ==========================================
    # BFS STEPS
    # ==========================================

    def bfs_steps(self, start):

        if start not in self.adjacency_list:
            return []

        visited = set()

        queue = [start]

        steps = []

        visited.add(start)

        while queue:

            current = queue.pop(0)

            steps.append({
                "vertex": current,
                "message": f"Visiting {current}"
            })

            for neighbor in self.adjacency_list[current]:

                if neighbor not in visited:

                    visited.add(neighbor)

                    queue.append(neighbor)

        return steps

    # ==========================================
    # DFS STEPS
    # ==========================================

    def dfs_steps(self, start):

        if start not in self.adjacency_list:
            return []

        visited = set()

        steps = []

        def traverse(vertex):

            visited.add(vertex)

            steps.append({
                "vertex": vertex,
                "message": f"Visiting {vertex}"
            })

            for neighbor in self.adjacency_list[vertex]:

                if neighbor not in visited:
                    traverse(neighbor)

        traverse(start)

        return steps

    # ==========================================
    # DISPLAY
    # ==========================================

    def display(self):

        return {
            vertex: neighbors.copy()
            for vertex, neighbors
            in self.adjacency_list.items()
        }


# =================================================
# TESTING
# =================================================

if __name__ == "__main__":

    graph = Graph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    # Add edges
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")

    print("Graph:")
    print(graph.display())

    print("\nBFS:")
    print(graph.bfs("A"))

    print("\nDFS:")
    print(graph.dfs("A"))

    print("\nBFS Steps:")

    for step in graph.bfs_steps("A"):
        print(step["message"])

    print("\nDFS Steps:")

    for step in graph.dfs_steps("A"):
        print(step["message"])