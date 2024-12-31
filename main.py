from graph import Graph
from dijkstra import dijkstra
from louvain import louvain_community_detection
from friend_recommendation import suggest_friends

def main():
    # Example usage of the tool
    # Create a graph instance
    g = Graph()

    # Add edges (example user connections)
    edges = [
        ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "Charlie"),
        ("Bob", "David"), ("Charlie", "David"), ("David", "Eve"),
        ("Eve", "Frank"), ("Frank", "Grace"), ("Grace", "Heidi"),
        ("Heidi", "Alice"), ("Alice", "Eve")
    ]

    for u, v in edges:
        g.add_edge(u, v)

    # Find the shortest path between Alice and Grace
    shortest_path = dijkstra(g, "Alice", "Grace")
    print(f"Shortest path from Alice to Grace: {shortest_path}")

    # Detect communities in the graph
    communities = louvain_community_detection(g)
    print(f"Detected communities: {communities}")

    # Suggest friends for Alice
    friend_suggestions = suggest_friends(g, "Alice")
    print(f"Friend suggestions for Alice: {friend_suggestions}")
    print("Check")
if __name__ == "__main__":
    main()
