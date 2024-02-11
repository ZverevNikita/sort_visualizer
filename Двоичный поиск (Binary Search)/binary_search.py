import random
import time

def binary_search(array, elementToSearch):
    firstIndex = 0
    lastIndex = len(array) - 1
    while firstIndex <= lastIndex:
        middleIndex = (firstIndex + lastIndex) // 2
        if array[middleIndex] == elementToSearch:
            return middleIndex
        elif array[middleIndex] < elementToSearch:
            firstIndex = middleIndex + 1
        else:
            lastIndex = middleIndex - 1
    return -1

n = int(input('Введите размер массива: '))

start_time = time.time()

array = [random.randint(1, 100) for i in range(n)]
print('Исходный массив: ', array)
array.sort()

elementToSearch = random.randint(0, 100)
print('Отсортированный массив: ', array)
print('Цель: ', elementToSearch)

result = binary_search(array, elementToSearch)
end_time = time.time() - start_time

if result != -1:
    print('Элемент массива найден!', result)
else:
    print('Элемент массива не найден!')

print('Время выполнения программы: ', end_time, 'секунд')




