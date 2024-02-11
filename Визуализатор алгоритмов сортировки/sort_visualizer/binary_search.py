import matplotlib.pyplot as plt

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