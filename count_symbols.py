# Задача: посчитать каждый символ в строке
def count_symbols(str):
    check = {}
    for i in str:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1
    return check
print(count_symbols("poehali poehali"))
