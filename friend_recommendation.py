def suggest_friends(graph, user):
    user_neighbors = set(graph.get_neighbors(user))
    suggestions = {}

    for neighbor in user_neighbors:
        neighbor_neighbors = set(graph.get_neighbors(neighbor))
        potential_friends = neighbor_neighbors - user_neighbors - {user}

        for potential_friend in potential_friends:
            if potential_friend not in suggestions:
                suggestions[potential_friend] = 0
            suggestions[potential_friend] += 1

    # Sort suggestions by the number of mutual friends
    sorted_suggestions = sorted(suggestions.items(), key=lambda item: item[1], reverse=True)
    return [suggestion[0] for suggestion in sorted_suggestions]
