import matplotlib.pyplot as plt

class InsertionSort:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()

    def update(self):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b')
        self.ax.set_title('Сортировка вставкой (Insertion Sort)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')
        plt.pause(0.0001)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.update()
            self.array[j + 1] = key
            self.update()

    def visualize_sorting(self):
        plt.show()