import heapq

def dijkstra(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes()}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.get_neighbors(current_node):
            distance = current_distance + 1  # Assuming all edges have equal weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    current = goal
    while previous_nodes[current] is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    if path:
        path.insert(0, start)
    return path
