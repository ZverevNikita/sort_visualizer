# Проверка, что имя программы - 'main'
if name == 'main':
    # Цикл для вывода меню выбора алгоритма сортировки
    while True:
        # Вывод списка алгоритмов
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
        # Ввод выбора пользователя
        choice = int(input('Введите номер алгоритма сортировки: '))
        if choice == 0:
            break
        # Обработка выбранного алгоритма
        elif choice == 1:
            # Выбрана быстрая сортировка
            print('Быстрая сортировка (Quick Sort)')
            # Генерация массива случайных чисел
            n = int(input('Введите размер массива: '))
            array = [random.randint(1, 100) for _ in range(n)]
            print('Исходный массив:', array)
            # Создание объекта QuickSort и запуск сортировки
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
        # Обработка других алгоритмов сортировки аналогичным образом