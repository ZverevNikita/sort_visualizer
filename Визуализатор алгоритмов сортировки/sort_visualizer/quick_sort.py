import matplotlib.pyplot as plt

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