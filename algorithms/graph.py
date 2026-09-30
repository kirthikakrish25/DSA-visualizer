class Graph:

    def __init__(self):
        self.adjacency_list = {}

    # --------------------------------
    # Add Vertex
    # --------------------------------

    def add_vertex(self, vertex):

        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    # --------------------------------
    # Add Weighted Edge
    # --------------------------------

    def add_edge(self, vertex1, vertex2, weight=1):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.adjacency_list[vertex1][vertex2] = weight
        self.adjacency_list[vertex2][vertex1] = weight

    # --------------------------------
    # Remove Vertex
    # --------------------------------

    def remove_vertex(self, vertex):

        if vertex not in self.adjacency_list:
            return False

        for neighbor in list(
            self.adjacency_list[vertex].keys()
        ):

            if vertex in self.adjacency_list[neighbor]:
                del self.adjacency_list[neighbor][vertex]

        del self.adjacency_list[vertex]

        return True

    # --------------------------------
    # Remove Edge
    # --------------------------------

    def remove_edge(self, vertex1, vertex2):

        if vertex1 in self.adjacency_list:
            self.adjacency_list[vertex1].pop(
                vertex2,
                None
            )

        if vertex2 in self.adjacency_list:
            self.adjacency_list[vertex2].pop(
                vertex1,
                None
            )

    # --------------------------------
    # BFS
    # --------------------------------

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

    # --------------------------------
    # DFS
    # --------------------------------

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

    # --------------------------------
    # BFS Steps
    # --------------------------------

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

    # --------------------------------
    # DFS Steps
    # --------------------------------

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

    # --------------------------------
    # Dijkstra
    # --------------------------------

    def dijkstra(self, start):

        if start not in self.adjacency_list:
            return {}, {}

        distances = {
            vertex: float("inf")
            for vertex in self.adjacency_list
        }

        previous = {
            vertex: None
            for vertex in self.adjacency_list
        }

        distances[start] = 0

        visited = set()

        while len(visited) < len(self.adjacency_list):

            current = None
            current_distance = float("inf")

            for vertex in self.adjacency_list:

                if (
                    vertex not in visited
                    and distances[vertex] < current_distance
                ):
                    current = vertex
                    current_distance = distances[vertex]

            if current is None:
                break

            visited.add(current)

            for neighbor, weight in (
                self.adjacency_list[current].items()
            ):

                if neighbor in visited:
                    continue

                new_distance = (
                    distances[current] + weight
                )

                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance
                    previous[neighbor] = current

        return distances, previous

    # --------------------------------
    # Dijkstra Steps
    # --------------------------------

    def dijkstra_steps(self, start):

        if start not in self.adjacency_list:
            return []

        distances = {
            vertex: float("inf")
            for vertex in self.adjacency_list
        }

        previous = {
            vertex: None
            for vertex in self.adjacency_list
        }

        visited = set()

        distances[start] = 0

        steps = []

        while len(visited) < len(self.adjacency_list):

            current = None
            current_distance = float("inf")

            for vertex in self.adjacency_list:

                if (
                    vertex not in visited
                    and distances[vertex] < current_distance
                ):
                    current = vertex
                    current_distance = distances[vertex]

            if current is None:
                break

            visited.add(current)

            steps.append({
                "vertex": current,
                "message": (
                    f"Selected {current} "
                    f"with distance {distances[current]}"
                ),
                "distances": distances.copy(),
                "previous": previous.copy()
            })

            for neighbor, weight in (
                self.adjacency_list[current].items()
            ):

                if neighbor in visited:
                    continue

                new_distance = (
                    distances[current] + weight
                )

                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance
                    previous[neighbor] = current

                    steps.append({
                        "vertex": neighbor,
                        "message": (
                            f"Updated distance of {neighbor} "
                            f"to {new_distance} "
                            f"through {current}"
                        ),
                        "distances": distances.copy(),
                        "previous": previous.copy()
                    })

        steps.append({
            "vertex": None,
            "message": "Dijkstra completed.",
            "distances": distances.copy(),
            "previous": previous.copy()
        })

        return steps

    # --------------------------------
    # Shortest Path
    # --------------------------------

    def shortest_path(self, start, target):

        distances, previous = self.dijkstra(start)

        if target not in distances:
            return [], float("inf")

        if distances[target] == float("inf"):
            return [], float("inf")

        path = []

        current = target

        while current is not None:

            path.append(current)

            current = previous[current]

        path.reverse()

        return path, distances[target]

    # --------------------------------
    # Display
    # --------------------------------

    def display(self):

        return {
            vertex: neighbors.copy()
            for vertex, neighbors
            in self.adjacency_list.items()
        }


# --------------------------------
# Test Graph + Dijkstra
# --------------------------------

if __name__ == "__main__":

    graph = Graph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)
    graph.add_edge("D", "E", 3)

    distances, previous = graph.dijkstra("A")

    print("Distances:")
    print(distances)

    print()

    print("Previous:")
    print(previous)

    print()

    path, cost = graph.shortest_path("A", "E")

    print("Shortest Path:")
    print(path)

    print("Cost:")
    print(cost)