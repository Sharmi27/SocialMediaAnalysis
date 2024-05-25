def louvain_community_detection(graph):
    import community as community_louvain
    import networkx as nx

    # Convert our Graph to a NetworkX graph
    nx_graph = nx.Graph()
    for node in graph.nodes():
        nx_graph.add_node(node)
    for node in graph.nodes():
        for neighbor in graph.get_neighbors(node):
            nx_graph.add_edge(node, neighbor)

    # Use Louvain method from the python-louvain library
    partition = community_louvain.best_partition(nx_graph)

    # Transform the partition into a community structure
    communities = {}
    for node, community_id in partition.items():
        if community_id not in communities:
            communities[community_id] = []
        communities[community_id].append(node)

    return list(communities.values())
