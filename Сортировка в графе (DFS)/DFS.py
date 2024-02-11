import time
import random
import networkx as nx
from collections import deque

def DFS(graph, start):
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    result = []

    while queue:
        node, path = queue.pop()
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
                result.append(neighbor)

    return result


def generate_random_graph(n):
    graph = {}
    nodes = [str(i) for i in range(n)]

    for node in nodes:
        graph[node] = []

    for i, node in enumerate(nodes):
        for other_node in random.sample(nodes[:i] + nodes[i + 1:], k=random.randint(0, n - 1)):
            graph[node].append(other_node)

    return graph


def visualize_graph(graph):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='b')
    plt.show()

n = int(input('Введите размер графа: '))
start_node = input('Введите начальную вершину графа: ')
start_time = time.time()
random_graph = generate_random_graph(n)
print('Сгенерированный граф:')
for node, neighbors in random_graph.items():
    print(f'{node}: {neighbors}')
print('Обход сгенерированного графа, начиная с вершины', start_node)
result = DFS(random_graph, start_node)
print(' -> '.join(result))
end_time = time.time() - start_time
print('Время выполнения программы:', end_time, 'секунд')