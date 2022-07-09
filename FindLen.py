# Поиск длины строки, 1 способ
str = "Найди меня"
print(len(str))
# способ 2, через счётчик
def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter
print(findLen(str))
