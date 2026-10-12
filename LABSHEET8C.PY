# Lab Sheet 8 - Question 3
# Shortest Path from Node 1 to Node N
# Path can use at most K edges

INF = float('inf')


def shortest_path(n, m, k, edges):

    # dp[v] = minimum cost to reach vertex v
    # using at most the currently processed number of edges

    dp = [INF] * (n + 1)
    dp[1] = 0

    # Allow paths containing at most K edges
    for _ in range(k):

        # Make a copy so that one iteration represents
        # exactly one additional edge.
        new_dp = dp.copy()

        for u, v, weight in edges:

            # u -> v
            if dp[u] != INF:
                new_dp[v] = min(
                    new_dp[v],
                    dp[u] + weight
                )

            # v -> u because graph is undirected
            if dp[v] != INF:
                new_dp[u] = min(
                    new_dp[u],
                    dp[v] + weight
                )

        dp = new_dp

    # If node N is unreachable
    if dp[n] == INF:
        return -1

    return dp[n]


# Input
n, m, k = map(int, input("Enter N, M and K: ").split())

edges = []

print("Enter each edge as: u v weight")

for _ in range(m):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))


# Find shortest path
answer = shortest_path(n, m, k, edges)

print("Minimum path weight:", answer)