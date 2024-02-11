import random
import time

def jumping_search(array, elementToSearch):
    arrayLength = len(array)
    jumpStep = int(arrayLength ** 0.5)
    previousStep = 0

    while array[min(jumpStep, arrayLength) - 1] < elementToSearch:
        previousStep = jumpStep
        jumpStep += int(arrayLength ** 0.5)
        if previousStep >= arrayLength:
            return -1

    while array[previousStep] < elementToSearch:
        previousStep += 1
        if previousStep == min(jumpStep, arrayLength):
            return -1

    if array[previousStep] == elementToSearch:
        return previousStep

    return -1

n = int(input('Введите размер массива: '))

start_time = time.time()

array = [random.randint(1, 100) for i in range(n)]
print('Исходный массив: ', array)
array.sort()

elementToSearch = random.randint(0, 100)
print('Отсортированный массив: ', array)
print('Цель: ', elementToSearch)

result = jumping_search(array, elementToSearch)
end_time = time.time() - start_time

if result != -1:
    print('Элемент массива найден!', result)
else:
    print('Элемент массива не найден!')

print('Время выполнения программы: ', end_time, 'секунд')


