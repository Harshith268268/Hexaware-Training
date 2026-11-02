"""
SET 3 - TASK 3: Hub network using an adjacency list, BFS and DFS.
BFS finds a route with the fewest hops in an unweighted graph.
DFS lists every hub reachable from the central depot.
Run: python task3_hub_routes_bfs_dfs.py
"""

from collections import deque

GRAPH = {
    "HUB-A": ["HUB-B", "HUB-C"],
    "HUB-B": ["HUB-A", "HUB-D", "HUB-E"],
    "HUB-C": ["HUB-A", "HUB-F"],
    "HUB-D": ["HUB-B", "HUB-G"],
    "HUB-E": ["HUB-B", "HUB-G", "HUB-H"],
    "HUB-F": ["HUB-C", "HUB-H"],
    "HUB-G": ["HUB-D", "HUB-E", "HUB-I"],
    "HUB-H": ["HUB-E", "HUB-F", "HUB-J"],
    "HUB-I": ["HUB-G", "HUB-J"],
    "HUB-J": ["HUB-H", "HUB-I"],
}


def bfs_shortest_route(graph, start, destination):
    if start not in graph or destination not in graph:
        return None

    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]
        if current == destination:
            return path

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])
    return None


def dfs_reachable(graph, start):
    if start not in graph:
        return []
    visited = set()
    order = []

    def visit(hub):
        visited.add(hub)
        order.append(hub)
        for neighbour in graph[hub]:
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order


def main():
    print("SET 3 - TASK 3: LOGISTICS HUB NETWORK")
    print("\nAdjacency list:")
    for hub, neighbours in GRAPH.items():
        print(f"{hub}: {', '.join(neighbours)}")

    source, destination = "HUB-A", "HUB-J"
    route = bfs_shortest_route(GRAPH, source, destination)
    print(f"\nFewest-hop route from {source} to {destination}:")
    if route:
        print(" -> ".join(route))
        print("Number of hops:", len(route) - 1)
    else:
        print("No route exists.")

    depot = "HUB-A"
    reachable = dfs_reachable(GRAPH, depot)
    print(f"\nHubs reachable from central depot {depot} (DFS):")
    print(", ".join(reachable))
    print("Total reachable hubs:", len(reachable))


if __name__ == "__main__":
    main()
