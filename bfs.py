from collections import deque


def is_seller(person):
    return person[-1] == 'm'


def bfs(graph, start, desired):
    search_queue = deque()
    search_queue += graph[start]
    searched = set()
    while search_queue:
        next_switch = search_queue.popleft()
        if next_switch not in searched:
            if desired(next_switch):
                return True
            else:
                search_queue += graph[next_switch]
                searched.add(next_switch)


graph = {}
graph.update({'you': ["alice", "bob", "claire"]})
graph.update({'alice': ['peggy']})
graph.update({'bob': ['anuj', 'peggy']})
graph.update({'claire': ['thom', 'jonny']})
graph.update({'anuj': []})
graph.update({'peggy': []})
graph.update({'thom': []})
graph.update({'jonny': []})

print(bfs(graph, 'you', is_seller))
