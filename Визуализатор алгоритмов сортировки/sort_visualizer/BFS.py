import random
import networkx as nx
from matplotlib import pyplot as plt
from collections import deque

class BFS:
    def generate_random_graph(n):
        graph = {}
        nodes = [str(i) for i in range(n)]

        for node in nodes:
            graph[node] = []

        for i, node in enumerate(nodes):
            for other_node in random.sample(nodes[:i] + nodes[i + 1:], k=random.randint(0, n - 1)):
                graph[node].append(other_node)

        return graph

    def BFS(graph, start):
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        result = []

        while queue:
            node, path = queue.popleft()
            result.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
                    result.append(neighbor)

        return result

    def visualize_graph(graph):
        G = nx.Graph(graph)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='b')
        plt.show()