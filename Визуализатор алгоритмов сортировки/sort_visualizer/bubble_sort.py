import matplotlib.pyplot as plt

class BubbleSort:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Сортировка пузырьком (Bubble Sort)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')
        self.bar = self.ax.bar(range(len(array)), array, color='b')

    def update(self):
        for rect, height in zip(self.bar, self.array):
            rect.set_height(height)
        plt.pause(0.01)

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.update()

    def visualize_sorting(self):
        plt.show()