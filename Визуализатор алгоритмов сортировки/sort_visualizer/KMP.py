from matplotlib import pyplot as plt

class KMP:
    def compilePatternArray(self, pattern):
        patternLength = len(pattern)
        compliedPatternArray = [0] * patternLength
        k = 0
        for i in range(1, patternLength):
            while k > 0 and pattern[k] != pattern[i]:
                k = compliedPatternArray[k-1]
            if pattern[k] == pattern[i]:
                k += 1
            compliedPatternArray[i] = k
        return compliedPatternArray

    def performKMPSearch(self, text, pattern):
        n = len(text)
        m = len(pattern)
        compliedPatternArray = self.compilePatternArray(pattern)
        foundIndexes = []
        patternIndex = 0
        for i in range(n):
            while patternIndex > 0 and pattern[patternIndex] != text[i]:
                patternIndex = compliedPatternArray[patternIndex - 1]
            if pattern[patternIndex] == text[i]:
                patternIndex += 1
            if patternIndex == m:
                foundIndexes.append(i - m + 1)
                patternIndex = compliedPatternArray[patternIndex - 1]
        return foundIndexes

    def visualize(indexes):
        if indexes:
            print('Подстрока найдена в позициях:', ', '.join(map(str, indexes)))
            x = indexes
            y = [0] * len(indexes)
            plt.scatter(x, y)
            plt.title('Алгоритм Кнута-Морриса-Пратта (KMP)')
            plt.xlabel('Позиции')
            plt.ylabel('Значения')
            plt.show()
        else:
            print('Подстрока не найдена!')