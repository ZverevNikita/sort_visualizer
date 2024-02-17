from quick_sort import QuickSort
from merge_sort import MergeSort
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from binary_search import BinarySearch
from jumping_search import JumpingSearch
from BFS import BFS
from DFS import DFS
from KMP import KMP
import random
import time

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
            intermediate_results = BFS.BFS(random_graph, start_node)
            BFS.visualize_graph(random_graph, intermediate_results)
            print(' -> '.join(map(str, intermediate_results)))
            end_time = time.time() - start_time
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
            intermediate_results = DFS.DFS(random_graph, start_node)
            DFS.visualize_graph(random_graph, intermediate_results)
            print(' -> '.join(map(str, intermediate_results)))
            end_time = time.time() - start_time
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

