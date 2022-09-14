graph = dict()
parents = dict()
costs = dict()

# fill graph
graph["start"] = dict()
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = dict()
graph["a"]["fin"] = 1

graph["b"] = dict()
graph["b"]["fin"] = 5
graph["b"]["a"] = 3

graph["fin"] = dict()

# fill costs
infinity = float("inf")

costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# fill parents
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, parents, costs):
    processed = set()
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs, processed)


dijkstra(graph, parents, costs)
print(costs)
