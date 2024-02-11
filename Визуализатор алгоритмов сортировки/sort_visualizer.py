import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class QuickSort:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()

    def update(self):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b')
        self.ax.set_title('Быстрая сортировка (Quick Sort)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')
        plt.pause(0.1)

    def quick_sort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot)
            self.quick_sort(pivot + 1, high)

    def partition(self, low, high):
        pivot = self.array[low]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while self.array[i] < pivot:
                i += 1
            j -= 1
            while self.array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            self.array[i], self.array[j] = self.array[j], self.array[i]
            self.update()

    def visualize_sorting(self):
        plt.show()

class MergeSort:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()

    def update(self):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b')
        self.ax.set_title('Сортировка слиянием (Merge Sort)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')
        plt.pause(0.01)

    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

            self.update()

    def visualize_sorting(self):
        plt.show()

class BubbleSort:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Сортировка пузырьком (Bubble Sort)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')
        self.bar = self.ax.bar(range(len(array)), array, color='b')

    def update(self):
        for rect, height in zip(self.bar, self.array):
            rect.set_height(height)
        plt.pause(0.01)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.update()

    def visualize_sorting(self):
        plt.show()

class InsertionSort:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()

    def update(self):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b')
        self.ax.set_title('Сортировка вставкой (Insertion Sort)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')
        plt.pause(0.0001)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.update()
            self.array[j + 1] = key
            self.update()

    def visualize_sorting(self):
        plt.show()

class BinarySearch:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Бинарный поиск (Binary Search)')
        self.ax.set_xlabel('Индексы элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')

    def update(self, left, right, mid, elementToSearch):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b', alpha=0.7)
        self.ax.axhline(y=elementToSearch, color='r', linestyle='--', label='Целевой элемент массива')
        if left <= right:
            self.ax.bar(mid, self.array[mid], color='g', label='Сравниваемый элемент', alpha=0.7)
        self.ax.legend()
        plt.pause(0.5)

    def binary_search(self, elementToSearch):
        left = 0
        right = len(self.array) - 1
        while left <= right:
            middle = (left + right) // 2
            self.update(left, right, middle, elementToSearch)
            if self.array[middle] == elementToSearch:
                return middle
            elif self.array[middle] < elementToSearch:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    def visualize_search(self, elementToSearch):
        result = self.binary_search(elementToSearch)
        plt.show()

class JumpingSearch:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Поиск прыжками (Jumping Search)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')

    def update(self, current_index, elementToSearch):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b', alpha=0.7)
        self.ax.axhline(y=elementToSearch, color='r', linestyle='--', label='Целевой элемент массива')
        if current_index != -1:
            self.ax.bar(current_index, self.array[current_index], color='g', label='Найденный элемент массива', alpha=0.7)
        self.ax.legend()
        plt.pause(0.5)

    def jumping_search(self, elementToSearch):
        arrayLength = len(self.array)
        jumpStep = int(arrayLength ** 0.5)
        previousStep = 0

        while self.array[min(jumpStep, arrayLength) - 1] < elementToSearch:
            previousStep = jumpStep
            jumpStep += int(arrayLength ** 0.5)
            if previousStep >= arrayLength:
                return -1
            self.update(previousStep, elementToSearch)

        while self.array[previousStep] < elementToSearch:
            previousStep += 1
            if previousStep == min(jumpStep, arrayLength):
                return -1
            self.update(previousStep, elementToSearch)

        if self.array[previousStep] == elementToSearch:
            self.update(previousStep, elementToSearch)
            return previousStep

    def visualize_search(self, elementToSearch):
        result = self.jumping_search(elementToSearch)
        plt.show()

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

class DFS:
    def generate_random_graph(n):
        graph = {}
        nodes = [str(i) for i in range(n)]

        for node in nodes:
            graph[node] = []

        for i, node in enumerate(nodes):
            for other_node in random.sample(nodes[:i] + nodes[i + 1:], k=random.randint(0, n - 1)):
                graph[node].append(other_node)

        return graph

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

    def visualize_graph(graph):
        G = nx.Graph(graph)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='b')
        plt.show()

class KMP:
    def compilePatternArray(self, pattern):
        patternLength = len(pattern)
        compliedPatternArray = [0] * patternLength
        k = 0
        for i in range(1, patternLength):
            while k > 0 and pattern[k] != pattern[i]:
                k = compliedPatternArray[k-1]
            if pattern[k] == pattern[i]:
                k += 1
            compliedPatternArray[i] = k
        return compliedPatternArray

    def performKMPSearch(self, text, pattern):
        n = len(text)
        m = len(pattern)
        compliedPatternArray = self.compilePatternArray(pattern)
        foundIndexes = []
        patternIndex = 0
        for i in range(n):
            while patternIndex > 0 and pattern[patternIndex] != text[i]:
                patternIndex = compliedPatternArray[patternIndex - 1]
            if pattern[patternIndex] == text[i]:
                patternIndex += 1
            if patternIndex == m:
                foundIndexes.append(i - m + 1)
                patternIndex = compliedPatternArray[patternIndex - 1]
        return foundIndexes

    def visualize(indexes):
        if indexes:
            print('Подстрока найдена в позициях:', ', '.join(map(str, indexes)))
            x = indexes
            y = [0] * len(indexes)
            plt.scatter(x, y)
            plt.title('Алгоритм Кнута-Морриса-Пратта (KMP)')
            plt.xlabel('Позиции')
            plt.ylabel('Значения')
            plt.show()
        else:
            print('Подстрока не найдена!')

if __name__ == '__main__':
    while True:
        print('Выберите алгоритм сортировки:')
        print('1. Быстрая сортировка (Quick Sort)')
        print('2. Сортировка слиянием (Merge Sort)')
        print('3. Сортировка пузырьком (Bubble Sort)')
        print('4. Сортировка вставкой (Insertion Sort)')
        print('5. Двоичный поиск (Binary Search)')
        print('6. Поиск прыжками (Jumping Search)')
        print('7. Сортировка в графе (BFS)')
        print('8. Сортировка в графе (DFS)')
        print('9. Алгоритм Кнута-Морриса-Пратта (KMP)')
        print('0. Выход')
        print('')
        choice = int(input('Введите номер алгоритма сортировки: '))
        if choice == 0:
            break
        elif choice == 1:
            print('Быстрая сортировка (Quick Sort)')
            n = int(input('Введите размер массива: '))
            array = [random.randint(1, 100) for _ in range(n)]
            print('Исходный массив:', array)
            quick_sort = QuickSort(array)
            start_time = time.time()
            quick_sort.quick_sort(0, len(array) - 1)
            end_time = time.time() - start_time
            print('Отсортированный массив:', quick_sort.array)
            print('Время выполнения программы:', end_time, 'секунд')
            quick_sort.visualize_sorting()
            print('')
            if input("Желаете продолжить работу? (да/нет): ").lower() != 'да':
                break
        elif choice == 2:
            print('Сортировка слиянием (Merge Sort)')
            n = int(input('Введите размер массива: '))
            array = [random.randint(1, 100) for _ in range(n)]
            print('Исходный массив:', array)
            merge_sort = MergeSort(array)
            start_time = time.time()
            merge_sort.merge_sort(merge_sort.array)
            end_time = time.time() - start_time
            print('Отсортированный массив:', merge_sort.array)
            print('Время выполнения программы:', end_time, 'секунд')
            merge_sort.visualize_sorting()
            print('')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break
        elif choice == 3:
            print('Сортировка пузырьком (Bubble Sort)')
            n = int(input('Введите размер массива: '))
            array = [random.randint(0, 100) for _ in range(n)]
            print('Исходный массив:', array)
            bubble_sort = BubbleSort(array)
            start_time = time.time()
            bubble_sort.bubble_sort()
            end_time = time.time() - start_time
            print('Отсортированный массив:', bubble_sort.array)
            print('Время выполнения программы:', end_time, 'секунд')
            bubble_sort.visualize_sorting()
            print('')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break
        elif choice == 4:
            print('Сортировка вставкой (Insertion Sort)')
            n = int(input('Введите размер массива: '))
            array = [random.randint(1, 100) for _ in range(n)]
            print('Исходный массив:', array)
            insertion_sort = InsertionSort(array)
            start_time = time.time()
            insertion_sort.insertion_sort()
            end_time = time.time() - start_time
            print('Отсортированный массив:', insertion_sort.array)
            print('Время выполнения программы:', end_time, 'секунд')
            insertion_sort.visualize_sorting()
            print('')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break
        elif choice == 5:
            print('Двоичный поиск (Binary Search)')
            n = int(input('Введите размер массива: '))
            array = [random.randint(1, 100) for _ in range(n)]
            print('Исходный массив:', array)
            array.sort()
            binary_search = BinarySearch(array)
            start_time = time.time()
            elementToSearch = random.randint(0, 100)
            print('Отсортированный массив:', array)
            print('Цель:', elementToSearch)
            result = binary_search.visualize_search(elementToSearch)
            if result != -1:
                print('Элемент массива найден!')
            else:
                print('Элемент массива не найден!')
            end_time = time.time() - start_time
            print('Время выполнения программы:', end_time, 'секунд')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break
        elif choice == 6:
            print('Поиск прыжками (Jumping Search)')
            n = int(input('Введите размер массива: '))
            start_time = time.time()
            array = [random.randint(1, 100) for i in range(n)]
            print('Исходный массив:', array)
            array.sort()
            jumping_search = JumpingSearch(array)
            elementToSearch = random.randint(0, 100)
            print('Отсортированный массив:', array)
            print('Цель:', elementToSearch)
            result = jumping_search.visualize_search(elementToSearch)
            end_time = time.time() - start_time
            if result != -1:
                print('Элемент массива найден!')
            else:
                print('Элемент массива не найден!')
            print('Время выполнения программы:', end_time, 'секунд')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break
        elif choice == 7:
            print('Сортировка в графе (BFS)')
            n = int(input('Введите размер графа: '))
            start_node = input('Введите начальную вершину графа: ')
            start_time = time.time()
            random_graph = BFS.generate_random_graph(n)
            print('Сгенерированный граф:')
            for node, neighbors in random_graph.items():
                print(f'{node}: {neighbors}')
            print('Обход сгенерированного графа, начиная с вершины', start_node)
            result = BFS.BFS(random_graph, start_node)
            print(' -> '.join(result))
            end_time = time.time() - start_time
            BFS.visualize_graph(random_graph)
            print('Время выполнения программы:', end_time, 'секунд')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break
        elif choice == 8:
            print('Сортировка в графе (DFS)')
            n = int(input('Введите размер графа: '))
            start_node = input('Введите начальную вершину графа: ')
            start_time = time.time()
            random_graph = DFS.generate_random_graph(n)
            print('Сгенерированный граф:')
            for node, neighbors in random_graph.items():
                print(f'{node}: {neighbors}')
            print('Обход сгенерированного графа, начиная с вершины', start_node)
            result = DFS.DFS(random_graph, start_node)
            print(' -> '.join(result))
            end_time = time.time() - start_time
            DFS.visualize_graph(random_graph)
            print('Время выполнения программы:', end_time, 'секунд')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break
        elif choice == 9:
            print('Алгоритм Кнута-Морриса-Пратта (KMP)')
            kmp = KMP()
            string = input('Введите текст: ')
            pattern = input('Введите что искать: ')
            text = ' '.join(map(str, string))
            pattern = ' '.join(map(str, pattern))
            start_time = time.time()
            indexes = kmp.performKMPSearch(text, pattern)
            end_time = time.time() - start_time
            KMP.visualize(indexes)
            print('Массив: ', text)
            print('Подстрока: ', pattern)
            print('Время выполнения программы:', end_time, 'секунд')
            if input('Желаете продолжить работу? (да/нет): ').lower() != 'да':
                break