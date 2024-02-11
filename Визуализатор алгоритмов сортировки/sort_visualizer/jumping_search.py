import matplotlib.pyplot as plt

class JumpingSearch:
    def __init__(self, array):
        self.array = array
        self.fig, self.ax = plt.subplots()
        self.ax.set_title('Поиск прыжками (Jumping Search)')
        self.ax.set_xlabel('Количество элементов в массиве')
        self.ax.set_ylabel('Значения элементов в массиве')

    def update(self, current_index, elementToSearch):
        self.ax.clear()
        self.ax.bar(range(len(self.array)), self.array, color='b', alpha=0.7)
        self.ax.axhline(y=elementToSearch, color='r', linestyle='--', label='Целевой элемент массива')
        if current_index != -1:
            self.ax.bar(current_index, self.array[current_index], color='g', label='Найденный элемент массива', alpha=0.7)
        self.ax.legend()
        plt.pause(0.5)

    def jumping_search(self, elementToSearch):
        arrayLength = len(self.array)
        jumpStep = int(arrayLength ** 0.5)
        previousStep = 0

        while self.array[min(jumpStep, arrayLength) - 1] < elementToSearch:
            previousStep = jumpStep
            jumpStep += int(arrayLength ** 0.5)
            if previousStep >= arrayLength:
                return -1
            self.update(previousStep, elementToSearch)

        while self.array[previousStep] < elementToSearch:
            previousStep += 1
            if previousStep == min(jumpStep, arrayLength):
                return -1
            self.update(previousStep, elementToSearch)

        if self.array[previousStep] == elementToSearch:
            self.update(previousStep, elementToSearch)
            return previousStep

    def visualize_search(self, elementToSearch):
        result = self.jumping_search(elementToSearch)
        plt.show()