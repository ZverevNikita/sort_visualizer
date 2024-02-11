import random
import time

def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

n = int(input('Введите размер массива: '))

array = [random.randint(1, 100) for i in range(n)]
print('Исходный массив:', array)

start_time = time.time()
sorted_array = merge_sort(array)
end_time = time.time() - start_time

print('Отсортированный массив:', sorted_array)
print('Время выполнения программы:', end_time, 'секунд')


