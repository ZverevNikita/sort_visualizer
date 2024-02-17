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
        intermediate_results = []
        while queue:
            node, path = queue.popleft()
            result.append(node)
            intermediate_results.append(list(result))
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)
                    result.append(neighbor)
                    intermediate_results.append(list(result))
        return intermediate_results

    def visualize_graph(graph, intermediate_results):
        G = nx.Graph()
        plt.figure(figsize=(8, 6))

        for node in intermediate_results[0]:
            G.add_node(node)

        for i in range(1, len(intermediate_results)):
            plt.clf()

            for edge in graph.items():
                for n in edge[1]:
                    if edge[0] in intermediate_results[i] and n in intermediate_results[i]:
                        G.add_edge(edge[0], n)

            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='b')
            plt.title(f'Шаг {i}')
            plt.pause(0.5)
            plt.show()