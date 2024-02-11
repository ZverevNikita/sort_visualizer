import matplotlib.pyplot as plt

class MergeSort:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()

    def update(self):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b')
        self.ax.set_title('Сортировка слиянием (Merge Sort)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')
        plt.pause(0.01)

    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

            self.update()

    def visualize_sorting(self):
        plt.show()