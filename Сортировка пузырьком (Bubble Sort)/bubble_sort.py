import random
import time

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

n = int(input('Введите размер массива: '))

array = [random.randint(0, 100) for i in range(n)]
print('Исходный массив:', array)

start_time = time.time()
sorted_array = bubble_sort(array)
end_time = time.time() - start_time

print('Отсортированный массив:', array)
print('Время выполнения программы:', end_time, 'секунд')



