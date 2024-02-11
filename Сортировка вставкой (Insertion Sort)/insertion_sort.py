import random
import time

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

n = int(input('Введите размер массива: '))

array = [random.randint(1, 100) for i in range(n)]
print('Исходный массив:', array)

start_time = time.time()
insertion_sort(array)
end_time = time.time() - start_time

print('Отсортированный массив:', array)
print('Время выполнения программы:', end_time, 'секунд')

