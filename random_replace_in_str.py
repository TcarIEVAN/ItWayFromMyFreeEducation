# Напишите скрипт,
# который заменяет произвольный
# символ/букву в строке на «$»
text_str = "Напишите скрипт, который позволяет инвертировать последовательность элементов в строке."
import random
counter = 0
while len(text_str) != text_str.count("$"):
    a = random.choice(text_str)
    text_str = text_str.replace(a,"$")
    print(text_str)
    counter += 1
print(f"{counter} попыток зашифровать строку")
