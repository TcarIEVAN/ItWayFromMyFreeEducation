def square_sum(numbers):
    summ = 0
    for i in range(len(numbers)):
        a = numbers[i]
        summ += a*a
    return summ
