import random
import time

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

n = int(input('Введите размер массива: '))

array = [random.randint(0, 100) for i in range(n)]
print('Исходный массив:', array)

start_time = time.time()
sorted_array = quick_sort(array)
end_time = time.time() - start_time

print('Отсортированный массив:', sorted_array)
print('Время выполнения программы:', end_time, 'секунд')


