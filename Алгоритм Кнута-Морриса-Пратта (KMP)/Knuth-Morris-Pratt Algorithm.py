import time

def compilePatternArray(self, pattern):
    patternLength = len(pattern)
    compliedPatternArray = [0] * patternLength
    k = 0
    for i in range(1, patternLength):
        while k > 0 and pattern[k] != pattern[i]:
            k = compliedPatternArray[k - 1]
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

string = input('Введите текст: ')
pattern = input('Введите что искать: ')
text = ' '.join(map(str, string))
pattern = ' '.join(map(str, pattern))
start_time = time.time()
end_time = time.time() - start_time
print('Массив: ', text)
print('Подстрока: ', pattern)
print('Время выполнения программы:', end_time, 'секунд')